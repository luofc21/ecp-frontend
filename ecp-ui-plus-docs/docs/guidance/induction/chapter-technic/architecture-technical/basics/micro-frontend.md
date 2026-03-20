<!-- source: http://frontend.pcitech.online/docs/guidance/induction/chapter-technic/architecture-technical/basics/micro-frontend.html -->

# 微前端架构

微前端架构是应用于浏览器端的前端架构，即将多个单页面应用由独立的单体应用，转变成把多个小型前端应用合一的聚合应用。聚合应用内的各个前端应用独立开发、独立部署、独立运行。

## 设计背景

传统Web应用架构多数为前后端分离架构。随着前端工程不断改善，系统变得越来越复杂，前端应用也从原始的 Html+Js+Css 一把梭模式进化成了组件化+MV\*的单页面应用模式。技术更新支撑了业务的扩张，而业务扩张到一定程度之后，又给我们带来了新的问题：

- 业务模块越来越多；
- 组件越来越多；
- 文件越来越多，定位文件越来越慢，打包上线速度越来越慢；
- 即使是一个小改动也需要全量打包；
- 开发启动速度越来越慢；

到这时候，组件化+MV\*模式也无法应对大型的前端应用了。同时，受后端微服务理念的影响，微前端架构概念就提了出来。

## 名词定义与术语解释

| 名词、术语 | 描述 |
| --- | --- |
| 基座 | 微前端中心化模式（基座模式）的基础与技术核心，负责管理其他应用，包括从应用的生命周期管理到应用间的通信机制。 |
| 主应用 | 系统的统一入口应用，可以只带有基座功能，也可以带有业务功能，但它所处理的业务功能指的是核心部分的业务功能，如：登录注册、用户鉴权、导航菜单管理、路由管理、数据管理、通信代理等等。 |
| 子应用 | 负责各个子模块业务实现的应用。 |

## 架构设计

微前端既然是在微服务的基础上提出来的，那就需要满足微服务的要求：

- 业务应用划分设计高内聚，避免应用过大或太小；
- 各应用独立开发，避免业务应用互相依赖；
- 各应用独立部署，可实现增量升级；
- 各应用独立运行，某个应用出问题，不影响系统整体的可用性；
- 风格标准化，不应因为应用独立而产生展示或操作上的巨大差异；
- 需要应用监控，可观察可分析诊断问题。

![微前端架构设计](../../../assets/images/guidance/induction/micro-frontend-design.png)

## 技术实现

### Vue3 实现

详见 [Ecp-ui-plus - 微前端](http://frontend.pcitech.online/ecp-ui-plus/docs/micro-frontends/introduction.html) 。

### Vue2 实现

采用 [Qiankun](https://qiankun.umijs.org/zh) 微前端实现库（已集成于PC端基础组件库 Ecp-ui 中），应用加载流程如下：

![微前端加载流程](../../../assets/images/guidance/induction/micro-frontend-load-flow.png)

#### 工程中微前端相关目录

查看相关工程目录

```bash
|-- config （部署服务的配置）
    |-- server-config.js （部署服务的配置文件）
    ...
|-- public
      |-- index.html （普通应用或子应用入口）
      |-- portal.html （主应用入口）
      |-- portal-iframe.html （主应用下的iframe入口）
|-- src
      |-- app （普通应用或子应用）
      |-- portal （主应用）
        |-- portal.js （主应用入口）
        |-- portal.vue （主应用入口组件）
      |-- App.vue （普通应用或子应用的入口组件）
      |-- main.js （普通应用或子应用的入口）
      ...
|-- vue.config.js
|-- package.json
...
```

#### 具体实现步骤

##### 主应用处理

- 在 vue.config.js 启用门户

```js
// ...
const usePortal = true;
// ...
```

设置 output（指定为umd），设置 externals，设置 pages（使用 /public/portal.html 代替 /public/index.html 作为主应用入口 html，并使用 /src/portal/portal.js 代替/src/ main.js 作为主应用入口、使用 /src/portal/portal.vue 代替 /src/App.vue 作为主应用入口组件）。

查看代码片段

```js
// ...
if (useMicroApp) {
    output = {
        library: packageName,
        libraryTarget: 'umd',
        jsonpFunction: `webpackJsonp_${packageName}`
    };
    externals = {
        loadsh: {
            commonjs: 'lodash',
            amd: 'lodash',
            root: '_' // 指向全局变量
        }
    };
    if (usePortal) {
        pages.sub = {
            entry: 'src/main.js',
            template: 'public/index.html',
            filename: 'sub.html'
        };
        pages.index = {
            entry: 'src/portal/portal.js',
            template: 'public/portal.html',
            filename: 'index.html'
        };
    }

    if (process.env.NODE_ENV === 'production' || !usePortal) {
        // 本地调试时，不修改publicPath，通过代理的方式重写当前应用的sub入口
        publicPath = `/${packageName}/`;
    }
}
// ...
```

设置 devServer 与 UniPlugin：

查看代码片段

```js
// ...
module.exports = {
    devServer: {
        port: DEV_SERVER_PORT,
        host: '0.0.0.0',
        https: false,
        publicPath: publicPath,
        proxy: proxyConfig,
        before (app) {
            if (usePortal) {
                app.get(`/${packageName}/sub.html`, function (req, res) {
                    res.redirect('/sub.html');
                });
            }
        }
    },
    configureWebpack: config => {
        return {
            output: output,
            resolve: {
                alias: {
                    // ...
                }
            },
            externals: externals,
            plugins: [
                new webpack.ProvidePlugin({
                    _: 'lodash',
                    Axios: 'axios',
                    Utils: path.resolve(__dirname, 'src/common/utils')
                }),
                new webpack.DefinePlugin({
                    PACKAGE_NAME: JSON.stringify(packageName)
                }),
                new UniPlugin({
                    enabled: !!useMicroApp,
                    replaceIndex: !usePortal,
                    externals: Object.keys(externals).map(item =>
                        item === 'loadsh' ? 'lodash' : item
                    )
                }),
                new EcpVersionWebpackPlugin()
            ]
        };
    },    
// ...
};
```

- 主应用入口处理

设置菜单映射属性，创建微前端构建实例：

查看代码片段

```js
/* portal.js */
import { Utils as EcpUtils } from 'ecp-ui';
import { LoginUtils } from 'ecp-login-component';
import * as InitialUtils from '@/common/utils/initial-utils';
import store from '@/app/store';

const MicroApp = EcpUtils.MicroApp;
const MicroUtils = EcpUtils.MicroUtils;

// 菜单的属性
const menuProps = {
    id: 'Id',
    label: 'Text',
    route: 'Target',
    url: 'Url',
    symbol: 'symbol',
    children: 'ChildNodes'
};

const mountErrHandler = err => {
    if (err.reason === 'cancel' || err.type === 'unhandledrejection') return;
    window.eventBus.emit('PORTAL_APP_MOUNT_ERROR', err);
};

const microApp = new MicroApp({
    // vue: Vue,
    rootEntry: App,
    mainContainer: '#container',
    subContainer: '#sub-wrapper'
});

// ...
```

处理主应用初始化相关部分，如获取用户基本信息、权限树处理等。获取权限树之后，将权限树处理成微前端可识别的形式。

查看代码片段

```js
/* portal.js */

// ...

(async function () {
    // 初始化应用
    try {
        await InitialUtils.systemInitial({});
    } catch (error) {
        console.log(
            '%c [PORTAL] systemInitial Caught Error',
            'font-size:18px;color:red;font-weight:700;',
            error
        );
    }

    const appConfig = {
        startsWith: '/s-',
        menu: store.state.permission['navMenu'],
        systemMenu: store.state.permission['systemMenu'] // 导航菜单和系统管理菜单有需要可以拆开来
    }; 

    appConfig.menuProps = menuProps;
    appConfig.menu = InitialUtils.formatMenu({
        menu: appConfig.menu,
        menuProps,
        symbol: appConfig.startsWith
    });
    appConfig.systemMenu = InitialUtils.formatMenu({
        menu: appConfig.systemMenu,
        menuProps,
        symbol: appConfig.startsWith
    });

// ...
```

权限树关键处理：

查看代码片段

```js
/* utils 应用初始化处理相关方法 */
import { Utils as EcpUtils } from 'ecp-ui';
const MicroUtils = EcpUtils.MicroUtils;

/**
 * @method formatMenu 菜单处理
 * @param {Object} params
 *** @property {Array} menu 菜单树
 *** @property {Array} menuProps 菜单键映射
 *** @property {String} symbol 链接前缀匹配规则
 *** @property {Number} level 层级
 */
export const formatMenu = ({ menu, menuProps, symbol = '/s-', level = 0 }) => {
    if (!menuProps) {
        menuProps = _.cloneDeep(defaultMenuProps);
    }
    return menu.map(d => {
        let children = d[menuProps['children']];
        const indexSymbol = symbol;
        if (children && children.length) {
            // if (level === 1) {
            //     indexSymbol = `/s${padStart(++index, 3)}-`;
            // }
            children = formatMenu({
                menu: children,
                menuProps,
                symbol: indexSymbol,
                level: level + 1
            });
        }
        const menuRoute = menuProps['route'];
        let route = d[menuRoute];
        // if (+d?.Value?.Funtype === 1) {
        route = MicroUtils.formatRoute(d[menuRoute], indexSymbol);
        // }
        const result = {
            ...d,
            symbol: indexSymbol,
            [menuProps['route']]: route
        };
        if (children && children.length) {
            result[menuProps['children']] = children;
        } else {
            delete result[menuProps['children']];
        }
        return result;
    });
};
```

设置子应用相关启动参数：

查看代码片段

```js
/* portal.js */
// ...
    const appConfig = {
        startsWith: '/s-',
        menu: store.state.permission['navMenu'],
        systemMenu: store.state.permission['systemMenu'] // 导航菜单和系统管理菜单有需要可以拆开来
    };    
// ...
```

设置子应用加载完成后跳转的的首个路径：

查看代码片段

```js
/* portal.js */

// ...

    const locations = window.location;
    let href = locations.pathname + (locations?.hash || '');
    const hrefMatcher =
        locations.pathname + (locations?.hash?.replace(/\?.*/, '') || '');
    const rootPath = '/';

    const isGetFirstMenu =
        hrefMatcher === `${rootPath}s-` || hrefMatcher === rootPath || hrefMatcher === '/#/';

    // 没有路径时，使用配置的默认路径
    // isGetFirstMenu && (href = MicroUtils.getFirstMenuRoute(appConfig.menu, menuProps));
    // // const menuNode = MicroUtils.findTree(appConfig.menu, (d) => d[menuProps.route] === href, menuProps);
    if (isGetFirstMenu) {
        const firstPath = MicroUtils.getFirstMenuRoute(
            appConfig.menu,
            menuProps
        );
        firstPath && (href = firstPath);
    }
    const symbol =
        (MicroUtils.constants.SYMBOL_REG.exec(href) || [])[0] ||
        appConfig.startsWith;

    appConfig.defaultPath = href;
    appConfig.defaultRoute = href;
    appConfig.startsWith = symbol;

// ...
```

将配置放到全局状态：

查看代码片段

```js
/* portal.js */

// ...

    // 初始化 state
    const state = {
        config: appConfig
    };

    // 将配置放到全局状态
    const actions = MicroUtils.initGlobalState(state);
    actions.setGlobalState(state);
    actions.offGlobalStateChange();

// ...
```

加载子应用，设置 Qiankun 子应用注册生命周期处理（含配置子应用加载动画）：

查看代码片段

```js
/* portal.js */

// ...

    // 动画的类名
    const enterName = 'fade-transform-enter';
    const enterActiveName = 'fade-transform-enter-active';
    const leaveName = 'fade-transform-leave-to';
    const leaveActiveName = 'fade-transform-leave-active';

    const loadingWrapper = '#portal-layout-content'; // 这里要替换为实际的包裹子应用容器的id
    nprogress.configure({ parent: loadingWrapper }); // 子应用加载进度条配置

    // 初始化完成后跳转的的首个路径
    MicroUtils.runAfterFirstMounted(() => {
        if (href !== location.href.replace(location.origin, '')) {
            window.history.pushState({}, '', href);
        }
    });
    /**
     * 子应用加载
     */
    let initComp = false;
    const subWrapperName = '#sub-wrapper'; // 这里要替换为实际的子应用容器id
    microApp.start([...appConfig.menu, ...appConfig.systemMenu], {
        config: appConfig,
        defaultRoute: appConfig.defaultRoute,
        symbol,
        menuProps,
        beforeLoad: app => {
            /**
             * // 如确定主应用没有使用 loadMicroApp 手动加载子应用，则可保留 externals，并需要嵌入公服或其它未剔除 externals 的应用，请放开这段
             * // 否则主应用与子应用应移除 vue、vuex、vue-router 等 externals 处理
             * // 剔除了 externals 的主应用，可使用代理+匹配上下文标识替换，并使用 iframe 嵌入未剔除 externals 的应用
            const otherUnuseExternalsSystems = [
                'omof-frontend',
                'common-frontend',
                'template-vue'
            ];
            if (otherUnuseExternalsSystems.includes(app.name)) {
                if (!window.Vue) {
                    window.Vue2 && (window.Vue = window.Vue2);
                }
            } else if (window.Vue) {
                // 单独的实例应用
                window.Vue2 = window.Vue;
                delete window.Vue;
            }
            */
        },
        beforeMount: () => {
            return new Promise(resolve => {
                nprogress.start();
                let subContainer = document.querySelector(subWrapperName);
                if (subContainer) {
                    subContainer.classList.add(enterActiveName);
                    subContainer.classList.add(enterName);
                }
                setTimeout(
                    () => {
                        resolve();
                    },
                    initComp ? 100 : 0
                );
                if (!initComp) {
                    initComp = true;
                }
            });
        },
        afterMount: app => {
            return new Promise(resolve => {
                InitialUtils.reformatSubSystem(app.name);
                let subContainer = document.querySelector(subWrapperName);
                if (subContainer) {
                    nprogress.done();
                    subContainer.classList.remove(enterActiveName);
                    subContainer.classList.remove(enterName);
                }
                resolve();
            });
        },
        beforeUnmount: () => {
            return new Promise(resolve => {
                nprogress.start();
                let subContainer = document.querySelector(subWrapperName);
                if (subContainer) {
                    subContainer.classList.add(leaveActiveName);
                    subContainer.classList.add(leaveName);
                }
                setTimeout(() => {
                    resolve();
                }, 150);
            });
        },
        afterUnmount: () => {
            return new Promise(resolve => {
                let subContainer = document.querySelector(subWrapperName);
                if (subContainer) {
                    subContainer.classList.remove(leaveActiveName);
                    subContainer.classList.remove(leaveName);
                }
                resolve();
            });
        }
    });
})();
```

处理微应用发送的sso登录消息：

查看代码片段

```js
/* portal.js */

// ...

// 处理微应用发送的sso登录消息
window.eventBus.on('loginStatus', (data) => {
    const param = {
        isPrimaryApp: true,
        response: data.response,
        loginUrl: '/multi/login',
    };
    LoginUtils.loginInterceptors(param);
});
```

- portal.vue 添加包裹子应用容器

查看代码片段

```vue
<template>
    <div class="portal" id="container">
        <portal-layout :name="title" :showNav="!isFreeNav" @select="goto" @goBack="goBack" :menu="menu" :props="menuProps" :defaultPath="config.defaultPath">
            <template #content>
                <!-- ↓↓↓↓↓ 关键 ↓↓↓↓↓ -->
                <div id="sub-wrapper"></div>
            </template>
        </portal-layout>
    </div>
</template>

<script>
import { Utils as EcpUtils } from 'ecp-ui';
import PortalLayout from './portal-layout.vue';

import store from '@/app/store';

const MicroUtils = EcpUtils.MicroUtils;

export default {
    name: 'container',
    components: {
        PortalLayout
    },
    props: {
        config: {
            type: Object,
            default: () => ({})
        },
        menuProps: {
            type: Object,
            default: () => ({})
        }
    },
    data () {
        return {
            isFreeNav: true
        };
    },
    computed: {
        title () {
            return this.globalConfigs?.IMPORT_CONFIGS?.title || 'template-vue';
        },
        menu () {
            return this.config.menu;
        }
    },    methods: {
        goto (data) {
            let href = '';
            if (data.type === 'iframe') {
                href = MicroUtils.getIframeUrl(
                    data,
                    this.menuProps,
                    this.config.startsWith
                );
            } else if (data.type === 'open') {
                if (this.opener && !this.opener.closed) {
                    this.opener.close();
                }
                this.opener = window.open(data[this.menuProps.url]);
                return;
            } else if (data.type === 'reload') {
                // 刷掉当前页面
                window.location.href = data[this.menuProps.url];
                return;
            } else {
                href = data[this.menuProps.route];
            }

            window.history.pushState({}, '', href);
        },
        goBack () {
            window.location.href = '/';
        },
        caughtError () {
            window.eventBus.on('PORTAL_APP_MOUNT_ERROR', err => {
                if (
                    err.reason === 'cancel' ||
                    err.type === 'unhandledrejection'
                ) { return; }
                
                // Some Other Actions, Such As MsgBox...
            });
        }
    }
};
</script>
```

- 在 server-config.js 配置需要使用的子模块，应用启动时会将 APPS\_ENTRY 配置的子模块添加到前端服务代理去：

查看代码片段

```js
const SERVER_CONFIG = {
    // APP_IP: '', // IP，不需要配IP
    APP_PORT: 8080, // 端口
    APP_NAME: 'template-vue', // 应用名
    APP_ALIAS: 'template-vue' // 别名，网关访问路径
};

// nacos配置项
const NACOS_CONFIG = {
    enabled: true, // 是否关联nacos
    serviceList: true, // 是否获取所有前端服务列表
    registerService: true, // 注册当前应用
    address: 'nacos-center.v-base:30848', // nacos服务域名:端口
    namespace: 'a85a37ef-5bec-478c-a60f-0b11f10b3da4', // nacos PROD namespace, 固定值
    items: [
        // 前端配置
        {
            dataId: 'settings-frontend',
            group: 'frontend',
            frontend: true
        },
        // 系统公共配置        {
            dataId: 'applications',
            group: 'prophet'
        }
    ]
};

// 门户需要使用的子模块，在前端服务订阅和子模块监控中，根据此列表获取
const APPS_ENTRY = [
    {
        name: SERVER_CONFIG.APP_NAME,
        alias: SERVER_CONFIG.APP_ALIAS
    },
    {
        // 公服
        name: 'common-frontend',
        alias: 'common-frontend'
    }
    // {
    //     name: 'data-govern-frontend',
    //     alias: 'dgs'
    // }
];

module.exports = {
    SERVER_CONFIG,
    NACOS_CONFIG,
    APPS_ENTRY
};
```

##### 子应用处理

- main.js 暴露子应用加载调用函数

查看代码片段

```js
/* main.js */
// ...
export async function bootstrap () {
    // console.log('template-vue bootstraped');
}

export async function mount (props) {
    // console.log('template-vue props from main framework', props);
    Vue.use({ ...EcpUI });
    Vue.use({ ...CommonPart });

    initApp(props.componentName && props.container).then(() => {
        instance = new Vue({
            router,
            store,
            el: props.container
                ? props.container.querySelector('#app')
                : '#app',
            render: h =>
                h(App, {
                    props: {
                        componentName: props.componentName,
                        componentProps: props.componentProps
                    }
                })
        });
    });
}

export async function unmount () {
    // 必须确保 有实例 且 有 $destroy 才能调用销毁, 否则会把主子应用整个qiankun拉宕掉
    if (instance) {
        instance?.$destroy && instance.$destroy();
        instance = null;
    }
}
```
