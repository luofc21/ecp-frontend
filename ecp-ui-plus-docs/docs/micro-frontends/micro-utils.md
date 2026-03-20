<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/micro-frontends/micro-utils.html -->

# MicroUtils 辅助工具

> - 可能会用到的辅助方法；
> - 注意 [formatRoute](#formatroute) 与 Ecp-ui 的用法有一点区别。

```js
import { MicroUtils } from '@ecp/ecp-ui-plus';
```

## constants

见 [MicroConstants 辅助常量](/ecp-ui-plus/docs/micro-frontends/micro-constants.html) 。

## HistoryApp

见 [UseHistoryApp 路由式加载 - HistoryApp 实现类](/ecp-ui-plus/docs/micro-frontends/use-history-app.html#historyapp-实现类) 。

## getAppWindowMap

获取所有通过路由式加载的已加载子应用的 window

```js
const appWindowMap = MicroUtils.getAppWindowMap();
```

- **入参**

  - 无
- **返回**

  - `Object` appWindowMap: 所有已加载子应用的 `子应用名称-子应用window` 集合，即：

```js
appWindowMap = {
    appNameXxx: appWindowXxx,
    appNameYyy: appWindowYyy,
    appNameZzz: appWindowZzz,
    // ...
};
```

## getAppWindow

根据子应用 name 获取通过路由式加载的子应用的 window

```js
const appWindow = MicroUtils.getAppWindow(appName);
```

- **入参**

  - `String` appName: 子应用
- **返回**

  - `Window` appWindow: 子应用的 window

## PortalTabsActions

见 [Portal-tabs 门户多页签 - PortalTabsActions 实现类](/ecp-ui-plus/docs/micro-frontends/portal-tabs.html#portaltabsactions-实现类) 。

## getPortalTabsCallbackSymbol

获取 PortalTabs 所有监听器回调队列集合的 key

```js
const PortalTabsCallbackSymbol = MicroUtils.getPortalTabsCallbackSymbol();
```

- **入参**

  - 无
- **返回**

  - `Symbol` PortalTabsCallbackSymbol: 主应用可通过 window[PortalTabsCallbackSymbol] 获取不同类型的监听器队列：

```js
window[PortalTabsCallbackSymbol] = {
    // 添加操作前的回调函数集合
    beforeAdd: [],
    // 移除操作前的回调函数集合
    beforeRemove: [],
    // 添加操作完成时的回调函数集合
    add: [],
    // 移除操作完成时的回调函数集合
    remove: [],
    // 更新操作完成时的回调函数集合
    update: [],
    // 跳转操作相关的回调函数集合
    goto: []
};
```

## getSymbolMatcher

获取匹配前缀正则

```js
const symbolMatcher = MicroUtils.getSymbolMatcher(symbol);
```

- **入参**

  - `String` symbol: 路由标记字符串
- **返回**

  - `RegExp` symbolMatcher: 匹配前缀正则

## getUri

获取链接 Uri

```js
const uri = MicroUtils.getUri(href, symbol);
```

- **入参**

  - `String` href: 链接地址
  - `String` origin: 页面的域名
- **返回**

  - `String` uri: 链接 Uri（即去除了 origin 的 url）

## getAppNameFromHref

从链接获取子应用名称

```js
const appName = MicroUtils.getAppNameFromHref(href, symbol);
```

- **入参**

  - `String` href: 链接地址
  - `String` symbol: 路由标记字符串
- **返回**

  - `String` appName: 子应用名称

## getAppOriginHref

获取完整的子应用链接地址

```js
const originHref = MicroUtils.getAppOriginHref(uri, symbol);
```

- **入参**

  - `String` uri: 链接 Uri
  - `String` symbol: 路由标记字符串
- **返回**

  - `String` originHref: 完整的子应用链接地址（带 origin）

## getAppFullPath

获取可用于 vue-router 的 fullPath

```js
const fullPath = MicroUtils.getAppFullPath(href);
```

- **入参**

  - `String` href: 链接地址
- **返回**

  - `String` 可用于: vue-router 的 fullPath

## getFirstMenuRoute

获取第一个权限路由

```js
const firstMenuRoute = MicroUtils.getFirstMenuRoute(menus, menuProps, pathname);
```

- **入参**

  - `Array` menus: 菜单树
  - `Object` menuProps: 菜单项关键映射
  - `String` pathname: 应用上下文
- **返回**

  - `String` firstMenuRoute: 第一个有效权限路由

## findTree

查找指定菜单项

```js
const menuItem = MicroUtils.findTree(menus, matcher, menuProps);
```

- **入参**

  - `Array` menus: 菜单树
  - `Function` matcher: 菜单项匹配操作
  - `Object` menuProps: 菜单项关键映射
- **返回**

  - `Object` menuItem: 匹配菜单项

## getIframeUrl

获取 portal-iframe 链接

```js
const iframeHtmlSrc = MicroUtils.getIframeUrl(menuItem, menuProps, symbol);
```

- **入参**

  - `Array` menus: 菜单树
  - `Object` menuProps: 菜单项关键映射
  - `String` symbol: 路由标记字符串
- **返回**

  - `String` iframeHtmlSrc: portal-iframe 链接

## getIframePath

获取 iframe 路由路径

```js
const iframePath = MicroUtils.getIframePath(menuItem, menuProps, pathname);
```

- **入参**

  - `Array` menus: 菜单树
  - `Object` menuProps: 菜单项关键映射
  - `String` pathname: 应用上下文
- **返回**

  - `String` iframePath: iframe 路由 path

## formatRoute

处理路由，加入路由标记

```js
const uri = MicroUtils.formatRoute(uri, symbol, portalName);
```

- **入参**

  - `String` uri: 路由链接
  - `String` symbol: 路由标记字符串
  - `String` portalName: 主应用名称，主应用页面通过router加载，不需要添加 symbol
- **返回**

  - `String` uri: 加入路由标记的路由链接

## recoverRoute

去除路由标记

```js
const uri = MicroUtils.recoverRoute(uri);
```

- **入参**

  - `String` uri: 路由链接
- **返回**

  - `String` uri: 去除路由标记的路由链接

## getUrlParams

获取链接地址 search 参数

```js
const query = MicroUtils.getUrlParams(url);
```

- **入参**

  - `String` url: 路由链接，url、uri、location.search 都可以
- **返回**

  - `Object` query: 链接参数 `key-value` 对象
