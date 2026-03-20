<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/micro-frontends/micro-component.html -->

# Micro-component 组件式加载

> - 组件式加载多用于系统 “临时操作” ，如弹窗、抽屉、通用业务模块等。
> - 加载子应用页面组件时，每加载一个 Micro-component 都会生成一个新的子应用实例，且**不会**与路由式加载的冲突；
> - 卸载 Micro-component 后，如果加载的是子应用页面组件，会将子应用实例也一并销毁了。

## 基础用法

- `<ecp-micro-component />`
  - 通用组件，如果可能需要加载 `route 页面` 或 `子应用页面`，可使用 `<ecp-micro-component />`，通过 `isRoute` 判断；
- `<ecp-route-component />`
  - route 页面组件，在非常明确仅需加载路由组件时，可直接使用 `<ecp-route-component />`；
- `<ecp-route-app-component />`
  - 子应用页面组件，在非常明确仅需加载子应用页面组件时，可直接使用 `<ecp-route-app-component />`。

## Attributes

| 参数 | 类型 | 可选值 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| isRoute | Boolean |  |  | 是否加载当前应用 route 页面组件，仅 `<ecp-micro-component />` 支持 |
| url | String |  |  | `route 页面` 路径链接 或 `子应用页面` 路径链接，可带参数 |
| props | String |  |  | 传入要加载的页面组件的属性，作为 `route 页面组件` 加载时传入组件属性，作为 `子应用页面组件` 加载时传入 Wujie startApp 的 [props](https://wujie-micro.github.io/doc/api/startApp.html#props) |
| showLoading | Boolean |  |  | 是否展示加载态，仅 `子应用页面组件` 生效 |
| plugins | Array |  |  | 传入 Wujie startApp 的 [plugins](https://wujie-micro.github.io/doc/api/startApp.html#plugins) |
| fetch | Array |  |  | 传入 Wujie startApp 的 [fetch](https://wujie-micro.github.io/doc/api/startApp.html#fetch) |
| lifeCycle | Array |  |  | 见 [LifeCycle 的结构](#lifecycle-的结构) |

### LifeCycle 的结构

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| replace | Function | 同 Wujie.startApp 的参数 [replace](https://wujie-micro.github.io/doc/api/startApp.html#replace) |
| beforeLoad | Function | 同 Wujie.startApp 的参数 [beforeLoad](https://wujie-micro.github.io/doc/api/startApp.html#beforeLoad) |
| beforeMount | Function | 同 Wujie.startApp 的参数 [beforeMount](https://wujie-micro.github.io/doc/api/startApp.html#beforeMount) |
| afterMount | Function | 同 Wujie.startApp 的参数 [afterMount](https://wujie-micro.github.io/doc/api/startApp.html#afterMount) |
| beforeUnmount | Function | 同 Wujie.startApp 的参数 [beforeUnmount](https://wujie-micro.github.io/doc/api/startApp.html#beforeUnmount) |
| afterUnmount | Function | 同 Wujie.startApp 的参数 [afterUnmount](https://wujie-micro.github.io/doc/api/startApp.html#afterUnmount) |
| activated | Function | 同 Wujie.startApp 的参数 [activated](https://wujie-micro.github.io/doc/api/startApp.html#activated) |
| deactivated | Function | 同 Wujie.startApp 的参数 [deactivated](https://wujie-micro.github.io/doc/api/startApp.html#deactivated) |
| loadError | Function | 同 Wujie.startApp 的参数 [loadError](https://wujie-micro.github.io/doc/api/startApp.html#loadError) |

## Events

可监听由 `route 页面组件` 或 `子应用页面组件` 抛出的事件。

## Slots

仅 `route 页面组件` 支持组件插槽，与对应 `route 页面组件` 提供的插槽一致。

## Exposes

### EcpMicroComponent Exposes

| 方法/属性 | 说明 |
| --- | --- |
| RouteCompRef | `<ecp-route-component />` 实例 |
| RouteAppCompRef | 子应用页面组件实例，即 `<ecp-route-app-component />` 实例 |
| ActiveRef | 当前激活的实例，为 RouteCompRef 或 RouteAppCompRef其中之一 |
| microEvent | RouteAppCompRef 的 MicroEvent 应用通信实例 |

### EcpRouteComponent Exposes

| 方法/属性 | 说明 |
| --- | --- |
| componentVNode | 解析命中的 route 页面组件 VNode |

### EcpRouteAppComponent Exposes

| 方法/属性 | 说明 |
| --- | --- |
| destroy | 可手动销毁当次手动加载的子应用，但不建议自行调用 |
| microEvent | MicroEvent 应用通信实例， 详见 [MicroEvent 应用通信](/ecp-ui-plus/docs/micro-frontends/micro-event.html) |
| appWindow | 子应用的 window |

## 示例代码

### 加载路由组件

查看代码片段

```vue
<template>
    <app-business-panel class="load-route-in-dialog" title="Load Route In Dialog">
        <el-form>
            <el-form-item label="名称：">
                <el-input v-model="form.name" placeholder="请输入名称" />
            </el-form-item>
        </el-form>

        <ecp-button text="手动加载本应用页面" @click="loadLocalPage()" />

        <el-dialog class="load-route-in-dialog--overlay" :title="dialog.title" v-model="dialogVisible" width="80%"
        append-to-body modal-append-to-body :before-close="onClose">
            <ecp-micro-component show-loading is-route :url="dialog.url" :props="dialog.props" @confirm="onConfirm"
                ref="microComponentRef" :key="dialog.url" v-if="dialogVisible">
                <template #header>
                    <div class="text-slot pa-1 pl-4 pr-4 mt-4 amber white--text">Slot Header: {{
                        version
                    }}</div>
                </template>
                <template #default>
                    <div class="text-slot pa-1 pl-4 pr-4 mt-2 mb-4 amber darken-3 white--text">Slot Default: {{
                        version
                    }}</div>
                </template>
            </ecp-micro-component>
        </el-dialog>
    </app-business-panel>
</template>

<script>
import dayjs from 'dayjs';
import { EcpMicroComponent } from '@ecp/ecp-ui-plus';

export default {
    name: 'load-route-in-dialog',
    components: {
        EcpMicroComponent
    },
    data: function () {
        return {
            dialog: {},
            dialogVisible: false,
            form: {
                name: '',
                status: '',
                time: null
            }
        };
    },
    beforeRouteLeave (to, from, next) {
        if (this.dialogVisible) {
            this.onClose();
        }
        next();
    },
    methods: {
        loadLocalPage () {
            this.dialog = {
                title: 'Load As Route-Component',
                url: `/template-vue-plus/#/component-route?loadAs=Route-Component&detailInfo=${JSON.stringify({
                    name: this.name
                })}`,
                props: {
                    detailInfo: this.form
                }
            };
            this.version = dayjs().format('YYYY-MM-DD HH:mm:ss');
            this.$nextTick(() => {
                this.dialogVisible = true;
            });
        },
        onClose () {
            this.dialogVisible = false;
        },
        onConfirm (type, data) {
            console.log('onConfirm', type, data);
            if (type === 'confirm') {
                this.form = data;
            }
            this.onClose();
        }
    }
};
</script>
```

```vue
<template>
    <app-business-panel class="component-route">
        <template #header>
            <div class="app-business-panel-title">Load As：{{ loadAs }}</div>

            <slot name="header"></slot>
        </template>

        <el-form :model="form" class="app-form app-form-inline filter">
            <el-form-item label="名称：">
                <el-input v-model="form.name" placeholder="请输入名称" clearable />
            </el-form-item>
            <el-form-item label="状态：">
                <el-input v-model="form.status" placeholder="请输入状态" clearable />
            </el-form-item>
            <el-form-item label="时间：">
                <el-date-picker v-model="form.time" type="datetimerange" range-separator="至" start-placeholder="开始日期"
                    end-placeholder="结束日期" value-format="YYYY-MM-DD HH:mm:ss" clearable>
                </el-date-picker>
            </el-form-item>
        </el-form>

        <slot></slot>

        <el-button type="primary" @click="handleConfirm">提 交</el-button>
    </app-business-panel>
</template>

<script>
import { unref } from 'vue';

export default {
    name: 'component-route',
    props: {
        detailInfo: {
            type: Object
        }
    },
    data: function () {
        let detailInfo = this.detailInfo || this.$route.query.detailInfo;
        console.log('detailInfo', detailInfo);
        if (typeof detailInfo === 'string') {
            try {
                detailInfo = JSON.parse(detailInfo);
            } catch (error) {
                detailInfo = {};
            }
        }
        return {
            form: {
                name: detailInfo?.name || '',
                status: detailInfo?.status || '',
                time: detailInfo?.time || null
            }
        };
    },
    computed: {
        loadAs () {
            if (this.$route.path.match(/component-route/i)) {
                return 'Route';
            }
            return this?.$attrs?.query?.loadAs
                ? this.$attrs.query.loadAs
                : 'Component';
        }
    },
    methods: {
        handleConfirm () {
            console.log(JSON.stringify(this.form, null, 4), this.$route?.query);

            this.$emit('confirm', 'confirm', unref(this.form));
        }
    }
};
</script>

<style scoped lang="scss">
.component-route {
    padding: 0 0 var(--spacer-large-3);
}
</style>
```

### 加载子应用页面组件

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
