<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/micro-frontends/project-sub.html -->

# 子应用处理

> - 这里的 `子应用` 指的是通过 `template-vue-plus` 创建的 `Vue3 + vite 子应用`，Vue2 子应用请查看 [兼容乾坤](/ecp-ui-plus/docs/micro-frontends/qiankun-polyfill.html)；
> - `应用名` 默认取 `package.json 的 name`；
> - 这里示例代码片段以模板工程 `template-vue-plus` 为例。

## 需要调整的文件

### vite.config.js

与主应用处理类似，仅需将 `usePortal` 设为 `false`。

查看代码片段

```js
// ...

/**
 * 是否需要作为主应用
 */
const usePortal = false; // 如果不需要作为主应用，请设为false

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

### main.js

查看代码片段

```js
/* main.js */

import App from './App.vue';

import { createLifecyle, getMicroApp } from 'vite-plugin-legacy-qiankun';

import ElementPlus, { useGlobalConfig } from 'element-plus';
import EcpUIPlus, { ElementDefaultConfig } from '@ecp/ecp-ui-plus';

import CommonPart from '@common';

import router from '@/app/router';
import store from '@store';

import '@styles/index';
import 'virtual:svg-icons-register';

import * as InitialUtils from '@/common/utils/initial-utils';

// 必须在调用 ElementPlus 指令类组件（如 ElMessage）之前配置
const ElGlobalConfig = useGlobalConfig();
ElGlobalConfig.value = ElementDefaultConfig;

// vite-plugin-legacy-qiankun 插件 bug，无法支持破折号 注意！！！
const packageNameQiankun = PACKAGE_NAME.replace(/-/g, '_');
const microApp = getMicroApp(packageNameQiankun);

const initApp = async (container) => {
    try {
    // 如果还有其它渲染前置处理，请在 src、common、utils、initial-utils、index.js 的 systemInitial 里面添加
        await InitialUtils.systemInitial({
            loadingTarget: (container || document).querySelector('#app')
        });
    } catch (error) {
        console.log(
            '%c systemInitial Caught Error',
            'font-size:18px;color:red;font-weight:700;',
            error
        );
    }
    return Promise.resolve();
};

const renderApp = async (props = {}) => {
    const VueApp = createApp(App, {
        ...props
    });
    VueApp.use(router);
    VueApp.use(store);
    VueApp.use(ElementPlus);
    VueApp.use(EcpUIPlus);
    VueApp.use(CommonPart);

    await initApp(props.componentName && props.container);    

    // 单应用需要更新文档title
    if (!microApp.__POWERED_BY_QIANKUN__ && !window.__POWERED_BY_WUJIE__) {
        const globalStore = useGlobalStore();
        const globalConfigs = globalStore?.globalConfigs || {};

        appConfig.IMPORT_CONFIGS = globalConfigs?.IMPORT_CONFIGS;
        document.title = globalConfigs.IMPORT_CONFIGS.title;
    }

    VueApp.mount(props.container
        ? props.container.querySelector('#app')
        : '#app');
    return VueApp;
};

let instance = null;

const lifeCycle = {
    bootstrap() {
        console.log('%c [lifeCycle bootstrap]', 'font-size:18px;color:purple;font-weight:700;', PACKAGE_NAME);
    },
    async mount(props) {
        instance = await renderApp(props);
        console.log('%c [lifeCycle mount]: props from main framework', 'font-size:18px;color:purple;font-weight:700;', PACKAGE_NAME, props);
    },
    unmount() {
        console.log('%c [lifeCycle unmount]', 'font-size:18px;color:purple;font-weight:700;', PACKAGE_NAME);
        instance?.unmount?.();
    }
};

if (microApp.__POWERED_BY_QIANKUN__) { // 当前应用是乾坤子应用
    createLifecyle(packageNameQiankun, lifeCycle);
} else if (window.__POWERED_BY_WUJIE__) { // 当前应用是无界子应用
    // 需要将 router 挂载到 window 上，以便 HistoryApp 代处理切换子应用但子应用内页面没更新的问题
    window.__MICRO_APP_ROUTER__ = router;

    window.__WUJIE_MOUNT = () => lifeCycle.mount();
    window.__WUJIE_UNMOUNT = () => lifeCycle.unmount();

    requestAnimationKeyFrame(() => {
        console.log('%c [lifeCycle mount manual]', 'font-size:18px;color:indianred;font-weight:700;', window.__WUJIE);
        window.__WUJIE.mount();
    });
} else { // 单应用
    renderApp();
}
```

### App.vue

查看代码片段

```vue
<template>
    <el-config-provider v-bind="ElementDefaultConfig">
        <div class="app" ref="appRef">
            <template v-if="!componentName">
                <app-layout name="template-vue" :menu="menu" v-if="showNav" @select="goto">
                    <template #content>
                        <router-view v-slot="{ Component }">
                            <transition name="fade-transform" mode="out-in">
                                <keep-alive :include="cachedViews">
                                    <component :is="Component" :key="$route.fullPath" />
                                </keep-alive>
                            </transition>
                        </router-view>
                    </template>
                    <template #tools>
                        <el-icon size="var(--font-size-large)" @click="switchTheme">
                            <Brush />
                        </el-icon>
                    </template>
                </app-layout>
                <template v-else>
                    <router-view v-slot="{ Component }">
                        <transition name="fade-transform" mode="out-in">
                            <keep-alive :include="cachedViews">
                                <component :is="Component" :key="$route.fullPath" />
                            </keep-alive>
                        </transition>
                    </router-view>
                </template>
            </template>
            <template v-else>
                <transition name="fade-transform" mode="out-in">
                    <ecp-micro-component is-route :url="componentName" :props="componentProps" v-if="isRoute" />
                    <template v-else>
                        <component :is="componentName" v-bind="componentProps" />
                    </template>
                </transition>
            </template>
        </div>
    </el-config-provider>
</template>

<script setup>
import { useTheme, ElementDefaultConfig, MicroUtils } from '@ecp/ecp-ui-plus';

import usePermissionStore from '@store/permission';
import { Brush } from '@element-plus/icons-vue';

const { isDark, theme, setTheme } = useTheme();

const switchTheme = () => {
    setTheme(theme.value === 'light' ? 'dark' : 'light');
};

const props = defineProps({
    config: {
        type: Object
    },
    componentName: {
        type: String,
        default: ''
    },
    componentProps: {
        type: Object,
        default: () => ({})
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

const permissionStore = usePermissionStore();
const router = useRouter();

const menu = computed(() => {
    return permissionStore.navMenu;
});
// 获取缓存页面组件 name
const cachedViews = computed(() => (permissionStore.cachedViews || []).map((view) => view.name));

const isRoute = computed(() => typeof props?.componentName === 'string' && props?.componentName && !!props.componentName.match('/'));

const isSubMode = window.__POWERED_BY_QIANKUN__ || window.__POWERED_BY_WUJIE__;
const showNav = computed(() => {
    return !isSubMode;
});

let opener = null;

const goto = (data) => {
    let href = '';
    if (data.type === 'iframe') {
        // 拼接 iframe 承载页路径
        href = MicroUtils.getIframePath(
            data,
            props.menuProps,
            PACKAGE_NAME
        );
    } else if (data.type === 'open') {
        // 新窗口打开

        if (opener && !opener.closed) {
            opener.close();
        }
        opener = window.open(data[props.menuProps.url]);
        return;
    } else if (data.type === 'reload') {
        // 刷掉当前页面
        if (window.__POWERED_BY_WUJIE__) {
            // vite 子应用所有的 location 操作都必须采用 window.$wujie.location
            window.$wujie.location.href = data[props.menuProps.url];
        } else {
            window.location.href = data[props.menuProps.url];
        }
        return;
    } else {
        href = data[props.menuProps.route];
    }
    if (window.__POWERED_BY_QIANKUN__) {
        window.history.pushState({}, '', href);
    } else {
        const matchedRoute = router.resolve(href.replace(/.*#/, ''));
        const matchedRouteQuery = matchedRoute?.query || {};
        router.push({
            path: matchedRoute.path,
            query: matchedRouteQuery
        });
    }
};
</script>

<style lang="scss" scoped>
.app {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
}
</style>
```

## 启用缓存的处理

与主应用处理类似，参考 [主应用页面缓存 - store 添加缓存](/ecp-ui-plus/docs/micro-frontends/project-portal.html#store-添加缓存) 和 [主应用页面缓存 - portal.vue 处理](/ecp-ui-plus/docs/micro-frontends/project-portal.html#portal-vue-处理) 。

### 适配门户多页签

见 [Portal-tabs 门户多页签 - 子应用添加页签](/ecp-ui-plus/docs/micro-frontends/portal-tabs.html#子应用添加页签) 。
