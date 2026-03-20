<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/micro-frontends/project-portal.html -->

# 主应用处理

> - `应用名` 默认取 `package.json 的 name`；
> - 这里示例代码片段以模板工程 `template-vue-plus` 为例。

## 需要调整的文件

### vite.config.js

将 `usePortal` 设为 `true`。

- vite server 会校验页面上下文，所以仅 dev 环境下开启主应用时将上下文设为 `/`；
  - 这时候访问还是通过 `/应用名/` 访问，经过 server 代理将 `/应用名/` 重写为 `/`。
- 项目工程打包时，为方便后续适配复杂网络环境拓展多层代理，无论是否启用 uni 模式，上下文都固定 `/应用名/`。

查看代码片段

```js
// ...

/**
 * 是否需要作为主应用
 */
const usePortal = true; // 如果不需要作为主应用，请设为false

export default ({ command, mode }) => {
    const proxy = getProxy(mode);
    const useUniMode = mode === 'uni' || mode === 'previewUni';

    // 生成主入口 html
    const htmlIndex = resolve(__dirname, useUniMode && usePortal ? 'template-portal.html' : 'template-index.html');
    fs.copyFileSync(htmlIndex, resolve(__dirname, 'index.html'));

    // 生成子入口 html
    const htmlSub = resolve(__dirname, 'template-index.html');
    fs.copyFileSync(htmlSub, resolve(__dirname, 'sub.html'));

    const pages = {
        index: resolve(__dirname, 'index.html'),
        sub: resolve(__dirname, 'sub.html')
    };

    return defineConfig({
        base: command === 'serve' && usePortal ? '/' : '/template-vue-plus/',

        // ...
        
    });
};
```

### vite.proxy.config.js

添加本地环境当前应用与子应用代理。

查看代码片段

```js
const API_URL = '网关IP:网关端口';

const defaultProxy = {
    '^/(api|sso|sysmanager)': {
        target: `http://${API_URL}`
    },

    // 当前应用上下文代理
    '^/template-vue-plus': {
        target: 'http://localhost:当前应用端口',
        changeOrigin: true,
        rewrite: (string) => string.replace('/template-vue-plus', '')
    },

    // 公服代理
    '^/common-frontend': {
        target: 'http://公服IP:30922'
    },

    // 第三方应用代理，没有 sub.html 的需要重写
    '^/setting-pcitech-online': {
        target: 'http://setting.pcitech.online',
        changeOrigin: true,
        rewrite: (string) => 
        string.replace('/setting-pcitech-online/sub.html', '/index.html')
                .replace('/setting-pcitech-online', '')
    }
};

const getProxy = (mode) => mode === 'uni'
    ? {
        ...defaultProxy
    }
    : mode === 'previewUni'
        ? {
            ...defaultProxy
        }
        : {
            ...defaultProxy
        };

export default getProxy;
```

### portal.js

路由式加载在 `portal.js` 中初始化与启动。

查看代码片段

```js
import App from './portal.vue';

import ElementPlus, { useGlobalConfig, ElMessage } from 'element-plus';

import EcpUIPlus, { ElementDefaultConfig, MicroUtils, useHistoryApp, useTheme } from '@ecp/ecp-ui-plus';

import CommonPart from '@common';

import router from '@router';

import store from '@store';
import useGlobalStore from '@store/global-config';

import '@styles/index';

import * as InitialUtils from '@common/utils/initial-utils';

import { Menu } from './menu.config.js';

// 必须在调用 ElementPlus 指令类组件（如 ElMessage）之前配置
const ElGlobalConfig = useGlobalConfig();
ElGlobalConfig.value = ElementDefaultConfig;

// 主题初始化渲染
useTheme();

// 主应用菜单配置关键参数
const appConfig = {
    startsWith: '/s-',
    menuProps: {
        id: 'id',
        label: 'Text',
        route: 'Target', // 'Value.Target',
        url: 'url',
        symbol: 'symbol',
        children: 'ChildNodes'
    },
    menu: []
};

async function getMenu (config) {
    try {
        config.menu = Menu;

        // 初始化应用
        const locations = window.location;

        let href = locations.pathname + locations.hash.replace(/\?.*/, '');
        const rootPath = '/template-vue-plus/';

        // 获取第一个页面路径
        const isGetFirstMenu = href === `${rootPath}` || href === '/' || href === '/#/';

        // 菜单格式化
        config.menu = InitialUtils.formatMenu({
            menu: config.menu,
            menuProps: config.menuProps,
            symbol: config.startsWith
        });

        // 没有路径时，使用配置的默认路径
        if (isGetFirstMenu) {
            href = MicroUtils.getFirstMenuRoute(config.menu, config.menuProps);
            if (href) {
                window.location.replace(href);
            }
        }

        // 将第一个路径/默认路径加到配置中
        appConfig.defaultPath = href;

        return {
            ...config
        };
    } catch (error) {
        ElMessage.error(error);
        console.log(
            '%c getMenu Caught error',
            'font-size:18px;color:red;font-weight:700;',
            error
        );
    }
}

const initApp = async (container) => {
    try {
        // 如果还有其它渲染前置处理，请在 src、common、utils、initial-utils、index.js 的 systemInitial 里面添加
        await InitialUtils.systemInitial({
            // loadingTarget: (container || document).querySelector('#container')
        });

        await getMenu(appConfig);

        const globalStore = useGlobalStore();
        const globalConfigs = globalStore?.globalConfigs || {};

        appConfig.IMPORT_CONFIGS = globalConfigs?.IMPORT_CONFIGS;
        document.title = globalConfigs.IMPORT_CONFIGS.title;
    } catch (error) {
        console.log(
            '%c systemInitial Caught Error',
            'font-size:18px;color:red;font-weight:700;',
            error
        );
    }
    return Promise.resolve();
};

let microApp = null;

const renderApp = async (props = {}) => {
    try {
        const VueApp = createApp(App, {
            ...props,
            menu: props?.config?.menu,
            menuProps: props?.config?.menuProps
        });
        VueApp.use(router);
        VueApp.use(store);
        VueApp.use(ElementPlus);
        VueApp.use(EcpUIPlus);
        VueApp.use(CommonPart);

        await initApp(props.componentName && props.container);

        // Vue3 在 createApp 之后、mount 之前，只能通过这样修改传入的属性值
        // VueApp._context.app._props.menuProps = appConfig.menuProps; // 一般不需要再修改菜单项关键字映射配置
        VueApp._context.app._props.menu = appConfig.menu;

        // 路由式加载初始化
        const historyApp = useHistoryApp({
            initOptions: {
                portalName: PACKAGE_NAME,
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
                        useUniPlugin: true // 公服使用了 UniPlugin 的 external，需要将 useUniPlugin 设为 true
                    },
                    // 其它可通过当前应用代理访问的第三方应用
                    'setting-pcitech-online': {
                        raw: true
                    }
                }
            },
            keepAlive: false // 是否缓存页面，默认不缓存
        });

        // 路由式加载实例
        microApp = historyApp.microApp;

        // 启动路由式加载
        const startInst = await microApp.start({
            firstRoute: props?.config?.defaultPath || ''
        });

        // 跳转第一个页面
        if (startInst?.replaceUri) {
            // 获取初始化需要跳转的链接
            const replaceUri = startInst.replaceUri;

            // 先替换地址栏链接
            requestAnimationFrame(() => {
                window.history.replaceState({}, '', replaceUri);
            });

            // 第一个页面是当前应用的页面时，用 router 跳转
            if (replaceUri.match(PACKAGE_NAME)) {
                const fullPath = MicroUtils.getAppFullPath(replaceUri);
                const matchedRoute = router.resolve(fullPath);
                const matchedRouteQuery = matchedRoute?.query || {};
                router.replace({
                    path: matchedRoute.path,
                    query: matchedRouteQuery,
                    force: true
                });
            }
        }

        return VueApp;
    } catch (error) {
        console.log(
            '%c renderApp Caught error',
            'font-size:18px;color:red;font-weight:700;',
            error
        );
        return null;
    }
};

(async function () {
    renderApp({
        config: appConfig
    });
})();
```

### portal.vue

主应用入口 Vue 组件，子应用内容承载 DOM 在这里面。

查看代码片段

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

## 启用页面缓存的处理

### 路由式加载初始化

初始化参数 `keepAlive` 设为 `true`

查看代码片段

```js
/* portal.js */
import EcpUIPlus, { ElementDefaultConfig, MicroUtils, useHistoryApp, useTheme } from '@ecp/ecp-ui-plus';

// ...

// 路由式加载初始化
const historyApp = useHistoryApp({
    initOptions: {
        portalName: PACKAGE_NAME,
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
                useUniPlugin: true // 公服使用了 UniPlugin 的 external，需要将 useUniPlugin 设为 true
            },
            // 其它可通过当前应用代理访问的第三方应用
            'setting-pcitech-online': {
                raw: true
            }
        }
    },
    keepAlive: true // 是否缓存页面，开启缓存
});

// ...
```

### store 添加缓存

相关逻辑已内置于 `src/app/store/permission/index.js`，此处仅提取关键代码展示。

命名规范

- Vue 的 `<keep-alive>` 组件的 `include` 和 `exclude` 是根据 `组件的 name 选项` 进行匹配的；
- 但动态加载的页面组件是拿不到 name 的，因此，我们将获取 `vue-router` 的 `routes 中声明的 name` 传入 `<keep-alive>` 的 `include` 和 `exclude`，请确保 `routes 中声明的 name` 与 `页面组件中显示声明的 name` 相同；
- 当前模板工程 Vue 版本中，使用 `<script setup>` 的单文件组件时，Vue 会自动根据文件名生成对应的 `大驼峰 name 选项`，无需再手动声明，但请确保 `routes 中声明的 name` 与该自动生成的 `组件 name` 保持一致。

查看代码片段

```js
/* src/app/store/permission/index.js */

const usePermissionStore = defineStore('permission-store', {
    state: () => {
        return {
            // ...

            // 缓存视图
            cachedViews: []

            //...
        };
    },
    actions: {
        addCachedView (view) {
            return new Promise(resolve => {
                if (!Array.isArray(this.cachedViews)) {
                    return resolve();
                }
                if (this.cachedViews.some(
                    (cachedView) => cachedView.name === view.name
                )) {
                    return resolve();
                };
                if (view && !view.meta?.noCache) {
                    // 将需要缓存的视图添加到缓存视图中
                    this.cachedViews.push(view);

                    // 将驼峰命名转换为短横线命名也加到缓存视图中，以做兼容处理
                    this.cachedViews.push({
                        ...view,
                        name: view.name.replace(/([A-Z])/g, '-$1').replace(/^-/, '').toLowerCase()
                    });
                }
                resolve();
            });
        },
        delCachedView (view) {
            return new Promise(resolve => {
                if (!Array.isArray(this.cachedViews)) {
                    return resolve();
                }

                // 将指定页面从缓存视图中删除
                const index = this.cachedViews.findIndex(
                    (cachedView) => cachedView.name === view.name
                );
                index > -1 && this.cachedViews.splice(index, 1);

                // 将驼峰命名转换为短横线命名的页面也从缓存视图中删除
                const kababName = view.name.replace(/([A-Z])/g, '-$1').replace(/^-/, '').toLowerCase();
                const kababIndex = this.cachedViews.findIndex((cachedView) => cachedView.name === kababName);
                kababIndex > -1 && this.cachedViews.splice(kababIndex, 1);
                resolve();
            });
        }
    }
});

export default usePermissionStore;
```

### portal.vue 处理

此处仅提取关键代码展示。

查看代码片段

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
            </app-layout>
        </div>
    </el-config-provider>
</template>

<script setup>
// ...

import usePermissionStore from '../app/store/permission';

// ...

const permissionStore = usePermissionStore();
// 获取缓存页面组件 name
const cachedViews = computed(() => (permissionStore.cachedViews || []).map((view) => view.name));

// ...

</script>
```

## 启用门户多页签

### 使用多页签组件

在启用页面缓存后，如需使用门户多页签，请根据 UI 设计稿在合适位置添加 `Portal-tabs 门户多页签组件`。

> 示例代码见 [Portal-tabs 门户多页签 - 示例](/ecp-ui-plus/docs/micro-frontends/portal-tabs.html#示例) 。
