<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/micro-frontends/qiankun-polyfill.html -->

# 兼容乾坤

> - 基于 Ecp-ui-plus 开发的 Vue3 微前端主应用，一定是使用 Wujie 的；
> - 主应用支持加载 Vue2 或 Vue3 子应用；
> - 子应用也支持被 Wujie 或 Qiankun 加载；
> - 参考文档 [Qiankun 微前端框架](https://qiankun.umijs.org/zh)

## 主应用加载 Vue2 子应用

见 [主应用处理-路由式加载初始化](/ecp-ui-plus/docs/micro-frontends/project-portal.html#路由式加载初始化) 。

## Vue3 子应用兼容 Qiankun

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

## Vue2 子应用兼容 Wujie

查看代码片段

```js
/* main.js */

import Vue from 'vue';
import App from './App.vue';
import router from './app/router';
import store from '@store';

// ...

const initApp = async (cb) => {
    // ...

    cb();
};

let instance = null;

export async function bootstrap () {
    console.log('%c [template-vue bootstrap]', 'font-size:18px;color:purple;font-weight:700;');
}

export async function mount (props) {
    console.log(
        '%c [template-vue mount]: template-vue props from main framework',
        'font-size:18px;color:purple;font-weight:700;',
        props
    );
    Vue.use({ ...EcpUI });

    // ...

    Vue.use(Table); // 用 ElTable 重新覆盖，以修复 EcpUI 重写的 Table 组件报 Error 的问题
    Vue.use(TableColumn); // 用 ElTableColumn 重新覆盖，以修复 EcpUI 重写的 Table 组件报 Error 的问题

    Dialog.props.closeOnClickModal.default = false;
    Dialog.props.appendToBody.default = true;

    initApp(() => {
        instance = new Vue({
            router,
            store,
            el: props?.container
                ? props?.container?.querySelector?.('#app')
                : '#app',
            render: (h) =>
                h(App, {
                    props: {
                        componentName: props?.componentName,
                        componentProps: props?.componentProps
                    }
                })
        });
    });
}

export async function unmount () {
    console.log('%c [template-vue unmount]', 'font-size:18px;color:purple;font-weight:700;');
    if (instance) {
        instance?.$destroy && instance.$destroy();
        instance = null;
    }
}

if (window.__POWERED_BY_WUJIE__) { // 兼容无界处理
    window.__MICRO_APP_ROUTER__ = router;
    window.__WUJIE_MOUNT = () => mount?.();
    window.__WUJIE_UNMOUNT = () => unmount?.();
} else {
    // ...
}
```
