<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/micro-frontends/use-history-app.html -->

# UseHistoryApp 路由式加载

> - 路由式加载多见于集成业务系统，主要用于实现内容区域业务代码实现与多系统模块整合展示；
> - 主应用通过 window.history 相关方法拦截加载对应子应用；
> - 每一个子应用对应一个子应用实例；
> - `由 Wujie 处理` 每一个子应用在属于各自的 iframe 中执行 js。

```js
import { useHistoryApp } from '@ecp/ecp-ui-plus';
const { keyOptions, keepAlive, microApp, microEvent } = useHistoryApp(Options);
```

## 入参 Options 的结构

| 参数 | 类型 | 默认值 | 可选值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
| initOptions | Object |  |  | 使用 UseHistoryApp 初始化时必填 | HistoryApp 初始化参数，详见[HistoryApp - 构造函数入参的结构](#构造函数入参的结构) |
| microApp | HistoryApp |  |  |  | 不通过 initOptions 初始化 HistoryApp 时传入 |
| keepAlive | Boolean | false |  |  | 是否开启缓存 |

## 返参

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| keyOptions | Reactive<Object> | 当前激活子应用关键参数: name 和 url |
| keepAlive | Ref<Boolean> | 是否开启缓存，可搭配 [Portal-tabs 门户多页签](/ecp-ui-plus/docs/micro-frontends/portal-tabs.html) 使用 |
| microApp | HistoryApp | 全局唯一 HistoryApp 实例 |
| microEvent | MicroEvent | MicroEvent 应用通信实例 |

## HistoryApp 实现类

> - 调用 useHistoryApp 初始化时会创建一个 HistoryApp 实例；
> - 不建议项目工程内直接使用 HistoryApp 创建实例。

```js
import { MicroUtils } from '@ecp/ecp-ui-plus';

const { HistoryApp } = MicroUtils;

const historyAppInst = new HistoryApp(options);
```

### 构造函数入参的结构

| 参数 | 类型 | 默认值 | 可选值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
| portalName | String |  |  |  | 全局唯一主应用标识 |
| portalContainer | String / HTMLElement |  |  | 是 | 主应用加载容器 |
| subContainer | String / HTMLElement |  |  | 是 | 子应用加载容器 |
| transitionName | String |  |  |  | 切换子应用过渡效果 name |
| transitionDuration | Number / String |  |  |  | 过渡效果时间 |
| keepAlive | Boolean |  |  |  | 是否开启页面缓存，需要结合子应用 `<keep-alive>` 组件使用 |
| app | VueInstance |  |  | 是 | 主应用 Vue 实例 |
| symbol | String |  |  | 是 | 子应用匹配前缀，模板工程默认'/s-' |
| showLoading | Boolean | true |  |  | 是否展示子应用初始化加载 loading |
| loadingText | String |  |  |  | 初始化加载 loading 展示文本 |
| props | Object |  |  |  | 同 Wujie.startApp 的参数 [props](https://wujie-micro.github.io/doc/api/startApp.html#props) |
| fetch | Function |  |  |  | 同 Wujie.startApp 的参数 [fetch](https://wujie-micro.github.io/doc/api/startApp.html#fetch) |
| plugins | Array |  |  |  | 同 Wujie.startApp 的参数 [plugins](https://wujie-micro.github.io/doc/api/startApp.html#plugins) |
| polyfill | Object<String, Object> |  |  |  | 需要兼容的子应用, key是子应用唯一标识，value是需要添加的适配配置项，value 的结构见 [PolyfillValue 的结构](#polyfillvalue-的结构) |
| lifeCycle | Object |  |  |  | 见 [LifeCycle 的结构](#lifecycle-的结构) |

#### PolyfillValue 的结构

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| raw | Boolean | 子应用是否完成适配改造 |
| useUniPlugin | Boolean | 子应用是否使用了uniPlugin的external |

#### LifeCycle 的结构

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| replace | Function | 同 Wujie.startApp 的参数 [replace](https://wujie-micro.github.io/doc/api/startApp.html#replace) |
| beforeLoad | Function | 同 Wujie.startApp 的参数 [beforeLoad](https://wujie-micro.github.io/doc/api/startApp.html#beforeLoad) |
| beforeUnload | Function | 针对未完成适配改造的子应用，重建前的处理 |
| beforeMount | Function | 同 Wujie.startApp 的参数 [beforeMount](https://wujie-micro.github.io/doc/api/startApp.html#beforeMount) |
| afterMount | Function | 同 Wujie.startApp 的参数 [afterMount](https://wujie-micro.github.io/doc/api/startApp.html#afterMount) |
| beforeUnmount | Function | 同 Wujie.startApp 的参数 [beforeUnmount](https://wujie-micro.github.io/doc/api/startApp.html#beforeUnmount) |
| afterUnmount | Function | 同 Wujie.startApp 的参数 [afterUnmount](https://wujie-micro.github.io/doc/api/startApp.html#afterUnmount) |
| activated | Function | 同 Wujie.startApp 的参数 [activated](https://wujie-micro.github.io/doc/api/startApp.html#activated) |
| deactivated | Function | 同 Wujie.startApp 的参数 [deactivated](https://wujie-micro.github.io/doc/api/startApp.html#deactivated) |
| loadError | Function | 同 Wujie.startApp 的参数 [loadError](https://wujie-micro.github.io/doc/api/startApp.html#loadError) |
| urlChange | Function | url 变更回调 |
| routeUnmatch | Function | 更新url不符合子应用匹配规则的回调：name 命中的子应用唯一标识, url 更新的 url, matchedSymbol 命中的匹配前缀 |

### 其它可用属性

#### start

`Function` 挂载主应用 Vue 实例，启动路由式加载

```js
historyAppInst.start(options<Object>);
```

入参 options 的结构：

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| firstRoute | String | 加载的首个路由，传入时如与当前地址不符，将调用 replaceState 替换为传入路由 |

#### destroy

`Function` 销毁子应用 Wujie 实例，appName 不传时销毁全部子应用实例，不建议调用

```js
historyAppInst.destroy(appName<String>);
```

#### uniPluginPolyfillPlugins

`Function` 获取当前激活子应用需要插入的 uniPlugin external

```js
historyAppInst.uniPluginPolyfillPlugins();
```

调用返回 Array<String>，polyfill.useUniPlugin 为 false 时返回空数组。

#### microEvent

`MicroEvent` 应用通信 MicroEvent 实例，详见 [MicroEvent 应用通信](/ecp-ui-plus/docs/micro-frontends/micro-event.html) 。

## 伪代码示例

主要在 `portal.js` 与 `portal.vue` 中使用。

查看代码片段

```js
// portal.js

import { useHistoryApp } from '@ecp/ecp-ui-plus';

const props = {
    config: {
        startsWith: '/s-'
    },
    // container: HTMLElement
};

const { keyOptions, keepAlive, microApp } = useHistoryApp({
    initOptions: {
        portalName: PACKAGE_NAME, // 主应用名称，vite.config 中注入
        portalContainer: props.container
            ? props.container.querySelector('#container')
            : '#container',
        subContainer: '#sub-wrapper',
        app: VueApp,
        symbol: props?.config?.startsWith,
        transitionName: 'fade-transform',
        polyfill: {
            // 未做适配改造的公服
            'common-frontend': {
                raw: true,
                useUniPlugin: true
            },
            // 其它第三方应用
            'setting-pcitech-online': {
                raw: true
            }
        }
    },
    keepAlive: true
});
```

```vue
<template>
    <el-config-provider v-bind="ElementDefaultConfig">
        <div class="portal-content" ref="portalContentRef">
            <app-layout :name="title" @select="goto" :menu="menu" :props="menuProps" :defaultPath="config.defaultPath">
                <template #content>
                    <transition name="fade-transform" mode="out-in">
                        <keep-alive :include="['RouterView', 'router-view', ...cachedViews]">
                            <div class="sub-wrapper" id="sub-wrapper" v-if="isSubApp"></div>

                            <router-view v-slot="{ Component }" v-else-if="initComplete">
                                <div class="sub-wrapper">
                                    <transition name="fade-transform" mode="out-in">
                                        <keep-alive :include="cachedViews">
                                            <component :is="Component" :key="routeKey" />
                                        </keep-alive>
                                    </transition>
                                </div>
                            </router-view>
                        </keep-alive>
                    </transition>
                </template>
                <template #tools>
                    <el-icon size="var(--font-size-large)" @click="switchTheme" style="cursor: pointer">
                        <Brush />
                    </el-icon>
                </template>
            </app-layout>
        </div>
    </el-config-provider>
</template>

<script setup>
import { nextTick, ref, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';

import { useTheme, ElementDefaultConfig, useHistoryApp, MicroUtils } from '@ecp/ecp-ui-plus';
import { Brush } from '@element-plus/icons-vue';

import useGlobalStore from '@store/global-config';
import usePermissionStore from '@store/permission';

// 主应用组件参数
const props = defineProps({
    config: {
        type: Object,
        require: true
    },
    menu: {
        type: Array
    },
    menuProps: {
        type: Object,
        default: () => ({
            id: 'id',
            label: 'Text',
            route: 'Target', // 'Value.Target',
            url: 'url',
            symbol: 'symbol',
            children: 'ChildNodes'
        })
    }
});

const globalStore = useGlobalStore();
const title = computed(() => {
    return globalStore?.globalConfigs?.IMPORT_CONFIGS?.title || PACKAGE_NAME;
});

const { isDark, theme, setTheme } = useTheme();
const switchTheme = () => {
    setTheme(theme.value === 'default' ? 'dark' : 'default');
};

const route = useRoute();
const router = useRouter();

// 微前端参数
const { keyOptions, microApp } = useHistoryApp();
const isSubApp = computed(() => {
    return !!(keyOptions?.name && keyOptions?.url);
});

const permissionStore = usePermissionStore();
// 获取缓存页面组件 name
const cachedViews = computed(() => (permissionStore.cachedViews || []).map((view) => view.name));

// 用 fullPath 做页面组件缓存标识
const routeKey = computed(() => {
    return route.fullPath;
});

let opener = null;
const goto = (data) => {
    const force = data?.force === true;
    let href = data?.[props.menuProps?.route || 'route'] || data?.[props.menuProps?.url || 'url'];
    const startsWith = props.config?.startsWith || '/s-';
    if (data.type === 'open') {
        if (opener && !opener.closed) {
            opener.close();
        }

        opener = window.open(href);
        return;
    } else if (data.type === 'reload') {
        // 刷掉当前页面
        window.location.href = href;
        return;
    }

    if (href.match(PACKAGE_NAME)) { // 当前应用通过 router 跳转
        href = MicroUtils.getUri(MicroUtils.getAppOriginHref(href, startsWith));

        // 目标路径上下文
        const targetName = MicroUtils.getAppNameFromHref(href, startsWith);
        // 当前链接上下文
        const currentName = MicroUtils.getAppNameFromHref(location.href, startsWith);

        // 可用于 router 解析的全路径
        const fullPath = MicroUtils.getAppFullPath(href);

        if (targetName !== currentName) {
            // url 上下文更改了，用 pushState 调整为 router 的上下文
            window.history.pushState({}, '', href);

            // 可能 vue-router 有点 bug，push/replace 带 query 的全路径会丢掉 query 参数并重定向，所以要用 router 把参数解析出来先
            const matchedRoute = router.resolve(fullPath);
            const matchedRouteQuery = matchedRoute?.query || {};

            // 因为已经调用过 pushState 了，页面组件用 replace 渲染就好了
            router.replace({
                path: matchedRoute.path,
                query: matchedRouteQuery,
                force: true
            });
        } else {
            // url 上下文没更改的，直接 push 就行
            router.push(force ? `/redirect${fullPath}` : fullPath);
        }
    } else { // 子应用通过 history 跳转
        window.history[force ? 'replaceState' : 'pushState']({
            force
        }, '', href);
    }
};

// 路由式加载是否加载完成，加载完成后才能添加 router-view，否则可能会进主应用 router 的 404 页
const initComplete = ref(false);
watch(
    () => microApp,
    (newVal) => {
        nextTick(() => {
            if (!initComplete.value) {
                initComplete.value = !!newVal;
            }
        });
    },
    {
        immediate: true,
        flush: 'post'
    }
);
</script>

<style lang="scss" scoped>
.portal-content {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;

    &-tabs {
        flex: 0 0 auto;
    }
}

.sub-wrapper {
    width: 100%;
    height: 100%;
    flex: 1 1 auto;
    display: flex;
    flex-direction: column;
    transition-duration: var(--custom-transition-duration, 150ms);
    position: relative;

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
