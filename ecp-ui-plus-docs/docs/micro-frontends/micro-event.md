<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/micro-frontends/micro-event.html -->

# MicroEvent 应用通信

温馨提示

**应用通信请使用 MicroEvent**，不要直接使用 Wujie 提供的通信方式。

- Wujie 本身提供了 3 种通信方式：props 通信、window 通信、eventBus 通信。
- 为便于统一管理和跟进 Wujie 后续版本更新，Ecp-ui-plus 在这基础上封装了 MicroEvent 应用通信实现类，并规范 iframe 嵌套第三方应用的通信方式与消息格式。

## MicroEvent 实现类

> MicroEvent 事件实例既可用于跨应用（主子应用、iframe嵌套应用）通信，也可以手动实例化用于同一应用内的跨组件通信。

警告

对于手动创建的 MicroEvent 实例，如果确定不再用到实例 (如组件销毁时)，必须手动调用实例的 [destroy](#destroy) 方法销毁实例，否则可能会导致内存泄露。

```js
import { MicroEvent } from '@ecp/ecp-ui-plus';
const microEventInstance = new MicroEvent(options);
```

### 构造函数入参的结构

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| channel | String |  | 是 | 事件频道，实例自动创建时的格式见 [示例代码](#示例代码) 中不同的使用场景 |
| targetWindow | Window | window |  | 目标窗口 |

### 其它可用属性

#### on

`Function` 添加事件监听

注意

如需要发送跨层请求（仅限于普通 iframe 嵌套，如从子应用的内嵌 iframe 发送请求消息到主应用这种），需要在 iframe 外层应用调用 [on](#on) 方法添加监听，以避免消息传递断连。

```js
const listener = microEventInstance.on(options<Object>);
```

入参 options 的结构：

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | String | 是 | 监听的事件类型 |
| key | String |  | 事件处理唯一标识, 未设置会自动生成随机 UUID |
| registerOnly | Boolean |  | 是否仅注册事件，不处理监听（主要用于跨层应用通信中转） |
| callback | Function | registerOnly 为 `falsy` 时必填 | 事件处理函数 |

返参 listener 的结构：

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | String | 是 | 监听的事件类型 |
| key | String |  | 事件处理唯一标识, 未设置会自动生成随机 UUID |
| channel | String |  | 监听的频道 |

##### callback 返参的结构

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| detail | Object |  | 完整消息体，包括 type, data, messageType, target |
| data | Any |  | 即 detail.data, 消息传递的数据 |

#### off

`Function` 取消事件监听

```js
microEventInstance.off(options<Object>);
```

入参 options 的结构：

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | String | 是 | 监听的事件类型 |
| key | String |  | 事件处理唯一标识, 未设置会取消对应事件类型的所有监听事件 |
| channelRestrict | Boolean |  | 是否仅取消监听当前实例对应频道的对应事件，当 key 未设置且 channelRestrict 为 true 时，仅取消对应频道的所有监听事件 |

#### dispatch

`Function` 分发事件

```js
microEventInstance.dispatch(options<Object>);
```

入参 options 的结构：

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | String | 是 | 事件类型 |
| messageType | String |  | 分发类型，为空时默认为 BROADCAST |
| target | String / Array |  | 接收频道/事件处理标识。 多个接收对象可使用英文逗号隔开的 String 或者直接传入 Array。 messageType 为 SINGLE 时必填； messageType 为 CHANNEL 时默认当前实例的频道，传入 target 会覆盖。 |
| data | Object |  | 传输数据 |

messageType 的可选值：

| 值 | 说明 |
| --- | --- |
| BROADCAST | 广播 |
| CHANNEL | 特定频道多播，未指定 target 时，默认为实例所在频道 |
| SINGLE | 指定对象单播 |

#### request

`Function` 发送组合请求消息，类似握手。

- 可用于获取某些数据。
- 这种情境下，请求方通常需要触发一次发送与添加一次性监听，用这个方法可以简化发送与监听处理，当普通异步接口使用即可。

```js
try {
    const result = await microEventInstance.request(options<Object>);
    const resultData = result?.data?.data;
} catch (error) {
    console.log('microEventInstance.request Caught Error', error);
}
```

入参 options 的结构：

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | String | 是 | 事件类型 |
| params | Object |  | 请求的数据 |
| timeout | Number |  | 请求的超时时间 |
| successCode | Number |  | 约定的成功响应状态码，默认 0 成功 |

返回 `Promise` 。

##### request 回调的结构

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| detail | Object |  | 完整消息体，包括 type, data, messageType, target |
| data | Any |  | 即 detail.data, 响应消息体：`{ code: 自编响应状态码, data: 响应的数据 }` |

#### response

`Function` 发送响应消息

- 用于响应 microEventInstance.request 请求，可在事件监听回调中调用。

```js
microEventInstance.on({
    type: 'some-request-listener',
    callback: (res) => {
        const requestId = res?.data?.requestId;
        const requestParams = res?.data?.params;

        // some logic

        microEventInstance.response(options<Object>);
    }
})
```

入参 options 的结构：

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | String | 是 | 事件类型 |
| requestId | Number |  | 请求唯一标识，由 request 发送 |
| code | Number |  | 自编响应状态码 |
| data | Object |  | 响应的数据 |

#### destroy

`Function` 销毁实例

- 销毁实例会清空这个实例所对应的事件频道的所有事件监听；
- 如果有未响应的 request 请求，会全部清空并响应失败；

```js
microEventInstance.destroy();
```

#### isActive

`Function` 是否已激活

- MicroEvent 完成实例化后，状态会变更为激活状态；
- 实例只有在激活状态时，才能调用以上方法。

```js
const isActive = microEventInstance.isActive();
```

返回 `Boolean` 。

#### isDestroyed

`Function` 是否已销毁

```js
const isDestroyed = microEventInstance.isDestroyed();
```

## 示例代码

### 配合 UseHistoryApp 使用

> - 在 HistoryApp 实例化时会自动创建一个 MicroEvent 实例，并挂载到 HistoryApp 实例上；
>   - 在使用 useHistoryApp 时，这个 MicroEvent 实例会单独提取出来，可直接在 useHistoryApp 返参中获取。
> - 对于子应用，会在初始化子应用的时候创建一个子应用自己用的 MicroEvent 实例，并挂载到子应用 window 中，子应用通过 `window.$microEvent` 调用
>   - 也可以引入 MicroEvent 自行实例化，再调用。

自动创建的 MicroEvent 实例

- 主应用 MicroEvent 实例 - `microEvent`：
  - 实例化参数：
    - channel: `主应用容器名称`；
    - targetWindow: 主应用所在窗口对象；
- 各子应用 MicroEvent 实例 - `子应用window.$microEvent`：
  - 实例化参数：
    - channel: `各子应用上下文名称`；
    - targetWindow: 各子应用对应窗口对象。

查看代码片段

```js
// Portal App

import { useHistoryApp } from '@ecp/ecp-ui-plus';

const { microEvent } = useHistoryApp({
    // ... UseHistoryApp Options
});

// 事件监听
microEvent.on({
    type: 'init-sub-app',
    callback: (result) => {
        // do something
    }
});

// 事件请求监听
microEvent.on({
    type: 'getUserInfo',
    callback: (result) => {
        const { data, detail } = result || {};
        const { params, requestId } = data || {};

        if (!requestId) {
            // 注意主应用也会接收到该事件，所以要做判空处理
            return;
        }

        // do something

        // 响应事件请求
        microEvent.response({
            type: 'getUserInfo',
            requestId,
            code: 0,
            data: {
                // ... userInfo
            }
        });
    }
});

window.beforeLogout = () => {
    // do something

    // 事件派发
    microEvent.dispatch({
        type: 'abort-request',
        messageType: 'broadcast',
        data: {
            all: true
        }
    });
};
```

```js
// Sub App

// 事件监听
window?.$microEvent?.on?.({
    type: 'abort-request',
    callback: () => {
        console.log('%c [SUB] Received abort-request', 'font-size:18px;color:red;font-weight:700;');
        // do something
    }
});

const getUserInfo = async () => {
    try {
        let responseData = null;
        if (window?.$microEvent) {
            // 事件请求
            const res = await window.$microEvent.request({
                type: 'getUserInfo',
                params: {
                // params
                }
            });
            const { data, detail } = res || {};
            responseData = data;
        } else {
            // eslint-disable-next-line no-undef
            const res = await doSomething();
            responseData = res.Data;
        }
        console.log('%c [SUB] getUserInfo Result', 'font-size:18px;color:blue;font-weight:700;', responseData);
    } catch (error) {
        console.log('%c [SUB] getUserInfo Caught Error', 'font-size:18px;color:red;font-weight:700;', error);
    }
};

const doSthToInitSubApp = async () => {
    try {
        await getUserInfo();

        if (window?.$microEvent) {
            // 事件派发
            window.$microEvent.dispatch({
                type: 'init-sub-app',
                params: {
                // params
                }
            });
        }
    } catch (error) {
        console.log('%c doSthToInitSubApp Caught Error', 'font-size:18px;color:red;font-weight:700;', error);
    }
};
```

### 配合 Micro-component 使用

> - 在使用 `<ecp-micro-component />` 时，会在内部引用的 `<ecp-route-app-component />` 创建一个 MicroEvent 实例，可通过`<ecp-micro-component />` 组件实例获取；
>   - 注意：这个通信实例是给组件创建的通信实例，不是挂载到子应用 window 中的实例；
>   - 在组件销毁后，会自动销毁这个通信实例。
> - 对于子应用，会在初始化子应用的时候创建一个子应用自己用的 MicroEvent 实例，并挂载到子应用 window 中，子应用通过 `window.$microEvent` 调用
>   - 也可以引入 MicroEvent 自行实例化，再调用。

自动创建的 MicroEvent 实例

- 组件的 MicroEvent 实例 - `microEvent`：
  - 实例化参数：
    - channel: `wrapper-micro-component-子应用上下文名称-参数更新时间戳`；
    - targetWindow: 主应用所在窗口对象；
  - 自动监听：
    - 在组件上添加的所有自定义事件，**同时支持** `kebab-case` 和 `camelCase` 格式。
- 被加载子应用的 MicroEvent 实例 - `子应用window.$microEvent`：
  - 实例化参数：
    - channel: `micro-component-子应用上下文名称-参数更新时间戳`；
    - targetWindow: 各子应用对应窗口对象。
  - 自动监听：
    - 无，需要手动监听，监听的 type 需要与引用组件 dispatch 的 type 完全一致。

查看代码片段

```vue
<template>
    <app-business-panel class="load-app-in-dialog" title="Load App In Dialog">

        <ecp-button text="手动加载微应用页面" @click="loadMicroAppPage(true)" />

        <el-dialog class="load-app-in-dialog--overlay" :title="dialog.title" v-model="dialogVisible" width="80%"
            append-to-body modal-append-to-body :before-close="onClose">
            <ecp-micro-component show-loading :url="dialog.url" :props="dialog.props" @toggle-maximum="onToggleMaximum"
                ref="microComponentRef" :key="dialog.url" v-if="dialogVisible">
            </ecp-micro-component>

            <template #footer>
                <ecp-button :text="maximumModule ? '缩小' : '放大'" @click="triggerMaximum" />
            </template>
        </el-dialog>
    </app-business-panel>
</template>

<script>
import { EcpMicroComponent } from '@ecp/ecp-ui-plus';

export default {
    name: 'load-app-in-dialog',
    components: {
        EcpMicroComponent
    },
    data: function () {
        return {
            dialog: {},
            dialogVisible: false,

            maximumModule: null
        };
    },
    beforeRouteLeave (to, from, next) {
        if (this.dialogVisible) {
            this.onClose();
        }
        next();
    },
    methods: {
        loadMicroAppPage () {
            this.dialog = {
                title: 'Load Micro App',
                url: '/some-micro-app-frontend/sub.html#/path/to/component-app',
                props: {}
            };
            this.$nextTick(() => {
                this.dialogVisible = true;
            });
        },

        onClose () {
            this.dialogVisible = false;
        },

        // 向子应用发送消息
        triggerMaximum () {
            this.$refs.microComponentRef.microEvent.dispatch({
                type: 'trigger-maximum'
            });
        },

        // 接收子应用消息
        onToggleMaximum (result) {
            console.log('onToggleMaximum', result);
            this.maximumModule = !!result?.data?.maximumModule;
        }
    }
};
</script>
```

```vue
<template>
    <app-business-panel class="component-app" title="Component App">
        <div class="component-app-maximum" v-if="maximum"></div>
        <div class="component-app-normal" v-else></div>
    </app-business-panel>
</template>

<script>
export default {
    name: 'component-app',
    data: function () {
        return {
            maximum: false
        };
    },
    mounted () {
        this.startListener();
    },
    unmounted () {
        this.stopListener();
    },
    methods: {
        startListener () {
            if (window.$microEvent) {
                // 监听主应用发送的消息
                this.listener = window.$microEvent.on({
                    type: 'trigger-maximum',
                    callback: (...args) => {
                        console.log('Event - trigger-maximum', ...args);
                        this.toggleMaximumModule();
                    }
                });
            }
        },
        stopListener () {
            if (window.$microEvent && this.listener) {
                // 取消监听
                window.$microEvent.off(this.listener);
            }
        },
        toggleMaximumModule () {
            this.maximum = !this.maximum;
            // 向主应用发送消息
            window?.$microEvent?.dispatch?.({
                type: 'toggle-maximum',
                data: {
                    maximum: this.maximum
                }
            });
        }
    }
};
</script>
```

### 嵌套 Iframe 使用

相关 MicroEvent 实例

- 主应用、子应用的 MicroEvent 实例见上文；
- 嵌套的 iframe 使用的 MicroEvent 实例需要引入后，手动实例化；
- 嵌套的第三方应用，可以按照消息格式发送、监听处理：
  - 使用 `window.parent.postMessage(FormattedMessage, '*')` 发送消息；
  - 使用 `window.addEventListener('message', (event) => {/* do something */})` 监听消息。

查看代码片段

```vue
<template>
    <div class="portal-content" ref="portalContentRef">
        <!-- 主应用嵌套 iframe -->
        <iframe class="sub-wrapper" src="//ip:port/path/to/nested-third-party-iframe" frameborder="0"></iframe>

        <!-- 子应用容器 -->
        <div class="sub-wrapper" id="sub-wrapper"></div>

        <ecp-button class="portal-content-button" text="发送消息" @click="sendMessage"></ecp-button>
    </div>
</template>

<script setup>
import { useHistoryApp } from '@ecp/ecp-ui-plus';

// MicroEvent 实例化
const { microEvent } = useHistoryApp();

// 事件监听
microEvent.on({
    type: 'test',
    callback: (...args) => {
        console.log('Event - Portal: ', ...args);
    }
});

const sendMessage = () => {
    // 发送消息
    microEvent.dispatch({
        type: 'test',
        data: {
            message: 'Message from Portal',
            timestamp: Date.now()
        }
    });
};
</script>

<style lang="scss" scoped>
.portal-content {
    width: 100%;
    height: 100%;
    display: flex;

    &-button {
        position: fixed;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        margin: var(--spacer-large-3);
    }
}

.sub-wrapper {
    width: 50%;
    height: 100%;
    flex: 1 1 auto;
    display: flex;
    flex-direction: column;
    position: relative;
    z-index: 1;

    :deep {
        &>wujie-app {
            width: 100%;
            height: 100%;
            flex: 1 1 auto;
            display: flex;
            flex-direction: column;
        }
    }
}
</style>
```

```vue
<template>
    <div class="sub-content">
        <!-- 子应用嵌套 iframe -->
        <iframe class="sub-wrapper" src="//ip:port/path/to/nested-app-sub-iframe" frameborder="0"></iframe>

        <ecp-button class="sub-button" text="发送消息" @click="sendMessage"></ecp-button>
    </div>
</template>

<script setup>
// 事件监听
window.$microEvent.on({
    type: 'test',
    callback: (...args) => {
        console.log('Event - Sub: ', ...args);
    }
});

const sendMessage = () => {
    // 发送消息
    window.$microEvent.dispatch({
        type: 'test',
        data: {
            message: 'Message from Sub',
            timestamp: Date.now()
        }
    });
};
</script>

<style lang="scss" scoped>
.sub-content {
    width: 100%;
    height: 100%;
    display: flex;

    &-button {
        position: fixed;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        margin: var(--spacer-large-3);
    }
}

.sub-wrapper {
    width: 100%;
    height: 100%;
    flex: 1 1 auto;
    display: flex;
    flex-direction: column;
    position: relative;
    z-index: 1;
}
</style>
```

```vue
<template>
    <div class="nested-sub-iframe">
        <ecp-button class="nested-sub-iframe-button" text="发送消息" @click="sendMessage"></ecp-button>
    </div>
</template>

<script setup>
import { MicroEvent } from '@ecp/ecp-ui-plus';

// MicroEvent 实例化
const microEvent = new MicroEvent({
    channel: 'nested-sub-iframe'
});

// 事件监听
microEvent.on({
    type: 'test',
    callback: (...args) => {
        console.log('Event - Sub Nested Iframe: ', ...args);
    }
});

const sendMessage = () => {
    // 发送消息
    microEvent.dispatch({
        type: 'test',
        data: {
            message: 'Message from Sub Nested Iframe',
            timestamp: Date.now()
        }
    });
};
</script>

<style lang="scss" scoped>
.nested-sub-iframe {
    width: 100%;
    height: 100%;
    display: flex;
}
</style>
```

```vue
<template>
    <div class="nested-third-party-iframe">
        <button class="nested-third-party-iframe-button" @click="sendMessage">发送消息</button>
    </div>
</template>

<script setup>
// 固定值
const EVENT_SYMBOL = '__ECP_MICRO_EVENT_SYMBOL__';

// 自定义常量
const MESSAGE_WINDOW = 'NESTED_THIRD_PARTY_IFRAME';
const CHANNEL = 'nested-third-party-iframe';

// 事件类型队列 Map
let eventQueueMap = {};

/**
 * @constant MESSAGE_TYPE 分发类型枚举
 * @property { String } BROADCAST 广播
 * @property { String } CHANNEL 特定频道多播
 * @property { String } SINGLE 指定对象单播
 */
const MESSAGE_TYPE = {
    BROADCAST: 'BROADCAST',
    CHANNEL: 'CHANNEL',
    SINGLE: 'SINGLE'
};

/**
 * @constant MESSAGE_TYPE_KEY 分发类型关键字
 * @property { String } BROADCAST 广播不需要指定频道或唯一标识
 * @property { String } CHANNEL 多播需要指定频道 'channel'
 * @property { String } SINGLE 单播需要指定唯一标识 'key'
 */
const MESSAGE_TYPE_KEY = {
    // 广播不需要指定频道或唯一标识
    [MESSAGE_TYPE.BROADCAST]: '',

    // 多播需要指定频道
    [MESSAGE_TYPE.CHANNEL]: 'channel',

    // 单播需要指定唯一标识
    [MESSAGE_TYPE.SINGLE]: 'key'
};

// 添加 test 事件监听
const listenTest = () => {
    if (!eventQueueMap.test) {
        eventQueueMap.test = [];
    }
    const key = `${CHANNEL}-test-${Date.now()}`;
    eventQueueMap.test.push({
        channel: CHANNEL,
        key,
        callback: (...args) => {
            console.log('Event Test - Nested Third-party Iframe: ', ...args);
        }
    });
};

// 添加 test2 事件监听
const listenTest2 = () => {
    if (!eventQueueMap.test2) {
        eventQueueMap.test2 = [];
    }
    const key = `${CHANNEL}-test2-${Date.now()}`;
    eventQueueMap.test2.push({
        channel: CHANNEL,
        key,
        callback: (...args) => {
            console.log('Event Test2 - Nested Third-party Iframe: ', ...args);
        }
    });
};

// 发送消息
const sendMessage = () => {
    window.parent.postMessage({
        messageFrom: EVENT_SYMBOL,
        messageWindow: MESSAGE_WINDOW,
        detail: {
            type: 'test',
            messageType: MESSAGE_TYPE.BROADCAST,
            // target: 'xxx,yyy', // 非广播消息需要指定一个或多个接收对象
            data: {
                message: 'Message from Third-party Iframe',
                timestamp: Date.now()
            }
        }
    }, '*');
};

// message 事件回调函数
const messageEventCallback = (event) => {
    // 解构 event 对象
    const { data: eventData, origin, ...otherArgs } = event || {};
    const { messageFrom, detail } = eventData || {};

    if (messageFrom !== EVENT_SYMBOL) {
        return;
    }

    const { type, data, messageType, target } = detail || {};

    // 拆解监听目标
    const targetList = typeof target === 'string' ? (target || '').split(',').map(item => (item || '').trim()).filter(val => val) : Array.isArray(target) ? target : [];

    // 事件类型的队列
    let eventQueue = eventQueueMap[type] || [];

    // 按照分发类型过滤事件队列
    const messageTypeKey = MESSAGE_TYPE_KEY[messageType];
    if (messageTypeKey) {
        eventQueue = eventQueue?.filter?.((item) => targetList.includes(item[messageTypeKey]));
    }

    if (eventQueue?.length) {
        // 执行事件回调
        eventQueue.forEach((item) => {
            try {
                typeof item?.callback === 'function' && item.callback({
                    data,
                    detail
                });
            } catch (error) {
                console.error('%c [MicroEvent] eventQueue callback Caught Error', 'font-size:18px;color:red;font-weight:700;', error, item);
            }
        });

        // 单次监听事件处理
        eventQueueMap[type] = eventQueueMap[type].filter(item => !item.once || !messageTypeKey || !targetList.includes(item[messageTypeKey]));
    }
};

onMounted(() => {
    // 监听 message 事件
    window.addEventListener('message', messageEventCallback);

    // 添加 test 事件监听
    listenTest();

    // 添加 test2 事件监听
    listenTest2();
});

onUnmounted(() => {
    // 移除 message 事件监听
    window.removeEventListener('message', messageEventCallback);

    // 清空事件队列
    eventQueueMap = {};
});
</script>

<style lang="scss" scoped>
.nested-third-party-iframe {
    width: 100%;
    height: 100%;
    display: flex;
}
</style>
```

### 跨组件通信

> 类似 EventBus，需要手动实例化。

查看代码片段

```vue
<template>
    <div class="component-messaging-alice">
        <ecp-button class="component-messaging-alice-button" text="发送消息" @click="sendMessage"></ecp-button>
    </div>
</template>

<script setup>
import { MicroEvent } from '@ecp/ecp-ui-plus';

// MicroEvent 实例化
const microEvent = new MicroEvent({
    channel: 'custom-component-message-channel'
});

// 事件监听
microEvent.on({
    type: 'custom-component-message-type',
    callback: (event) => {
        console.log('Event - Component Alice: ', event);

        if (event?.data?.from === 'Bob') {
            // do something
        }
    }
});

const sendMessage = () => {
    // 发送消息
    microEvent.dispatch({
        type: 'custom-component-message-type',
        messageType: 'CHANNEL',
        target: 'custom-component-message-channel',
        data: {
            from: 'Alice',
            message: 'Message from Component Alice',
            timestamp: Date.now()
        }
    });
};
</script>

<style lang="scss" scoped>
.component-messaging-alice {
    width: 100%;
    height: 100%;
    display: flex;
}
</style>
```

```vue
<template>
    <div class="component-messaging-bob">
        <ecp-button class="component-messaging-bob-button" text="发送消息" @click="sendMessage"></ecp-button>
    </div>
</template>

<script setup>
import { MicroEvent } from '@ecp/ecp-ui-plus';

// MicroEvent 实例化
const microEvent = new MicroEvent({
    channel: 'custom-component-message-channel'
});

// 事件监听
microEvent.on({
    type: 'custom-component-message-type',
    callback: (event) => {
        console.log('Event - Component Bob: ', event);

        if (event?.data?.from === 'Alice') {
            // do something
        }
    }
});

const sendMessage = () => {
    // 发送消息
    microEvent.dispatch({
        type: 'custom-component-message-type',
        messageType: 'CHANNEL',
        target: 'custom-component-message-channel',
        data: {
            from: 'Bob',
            message: 'Message from Component Bob',
            timestamp: Date.now()
        }
    });
};
</script>

<style lang="scss" scoped>
.component-messaging-bob {
    width: 100%;
    height: 100%;
    display: flex;
}
</style>
```
