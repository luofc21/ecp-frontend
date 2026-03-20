<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/micro-frontends/scheme-design.html -->

# 方案设计

## 设计背景

Wujie 提供了 3 种运行模式，保活模式、单例模式、重建模式。引入 Wujie 之后，我们主要要解决这几大问题：

- 应用保活模式添加路由同步支持；
- 路由同步 url 拼接方式修改；
- 添加路由式加载方式，无需主应用提供各路由承载页面；
- 保活模式添加支持门户多页签。

再结合实际应用场景看：

- 使用保活模式，主要是避免路由式加载的子应用重复初始化；
- 组件式加载的子应用，更多是作为路由式加载的拓展、用于系统 “临时操作” （如弹窗等）场景下的，应区别于路由式加载的同名子应用、独享另外的子应用实例；
- 组件式加载的子应用，通常是基于定制化需求开发的，一般都需要修改子应用，因此这种加载模式下，子应用必然是有适配新微前端框架改造的；
- 组件式加载也不仅仅局限于应用加载其它应用，也应该适用于应用加载本应用，为便于实际应用开发，通信方式改用组件传参与组件事件通信更为合适；
- 现存项目中，大部分是使用 Qiankun 框架的 Vue2 项目，其中部分项目由于应用过广或历史过于悠久不便于改造，且部分项目使用 UniPlugin 将 vue、vue-router、vuex、lodash 设为 external 并通过主应用加载；
- 主应用与加载的所有子应用都是独立的 Vue 实例，所引用的弹出层层级各自管理，需要统一管理，以保证后弹出来的弹窗层一定是在最前面的。

因此，Ecp-ui-plus 实际要解决的问题是：

1. 重新包装，仅直接提供 `路由式加载调用` 与 `组件式加载组件` ；
2. 利用保活模式与重建模式，提供路由加载方式，并重构路由同步；
3. 利用单例模式，提供组件式加载组件，并支持加载 挂载到子应用router上的子应用页面/组件 与 挂载到主应用router上的主应用页面/组件；
4. 基于第 3 点，组件式加载组件的应用通信应从双向广播，调整为 父组件 通过组件 Props 单向传递，与组件通过 $emit 单向抛出自定义事件；
5. 基于第 3 点，组件式加载组件的子应用生命周期应跟随组件，销毁组件同时销毁子应用；
6. 适配使用了 UniPlugin 的项目，并为这些子应用插入缺失依赖；
7. 添加 `门户多页签组件` ；
8. 添加 `全局弹出层层级管理` 。

## 路由式加载

路由式加载多见于集成业务系统，主要用于实现内容区域业务代码实现与多系统模块整合展示。

### 实现思路

实现思路与 Ecp-ui 的 Qiankun 类似：

1. 需要重写主应用的 history.pushState、history.replaceState，以实现后续主应用路由监听；
2. 需要实现路由监听，匹配识别子应用页面或主应用route页面；
3. 需要指定子应用入口为 `http(s)://主应用IP:主应用端口/子应用唯一标识/sub.html`；
4. 需要根据子应用是否完成 Wujie 兼容改造，来切换 Wujie 运行模式：已改造的使用保活模式，未改造的使用重建模式；
5. 需要根据子应用是否使用 UniPlugin 的 Vue2 项目，来判断是否插入缺失 external；
6. 子应用挂载前，劫持子应用 iframe 的 history.pushState、 history.replaceState、 history.go、 history.back、 history.forward 方法，并添加调用主应用的对应方法，同步主应用与子应用的路由；
7. 需要按调用顺序依次加载子应用，以应对频繁切换的情况。

### 使用路由式加载

> 路由式加载已在 HistroyApp 中实现，具体使用方法见 [UseHistoryApp 路由式加载](/ecp-ui-plus/docs/micro-frontends/use-history-app.html) 。

## 组件式加载

基于 Wujie 与 vue-router 封装：

1. 需要根据传入组件的 url 找到匹配该 url 的页面组件；
2. 当传入的 url 是子应用路由时，新建 Wujie 实例，重写实例的子应用 history 相关方法，注册子应用通信监听，并调用 `$emit` 转换为对应组件事件；
3. 需要根据子应用是否完成 Wujie 兼容改造，来切换 Wujie 运行模式：已改造的使用单例模式，未改造的使用重建模式；
4. 组件销毁时，调用 Wujie destroyApp 方法销毁子应用，并注销对应子应用通信监听。
5. 当传入的 url 非子应用路由时，调用当前应用 $router.resolve 方法，解析出对应 query、params 和 匹配的 component；
6. 将 query、params、组件props、添加到组件上的事件 全部作为页面组件传参，与 component 一并组成 Vnode 来渲染。

### 使用组件式加载

> 组件式加载已在 Micro-component 中实现，具体使用方法见 [Micro-component 组件式加载](/ecp-ui-plus/docs/micro-frontends/micro-component.html) 。

## 页面缓存

页面缓存通常搭配页面多页签使用，多用于多对比项页面的业务系统。

1. 应用级缓存由路由式加载实现；
2. 应用内页缓存，由主应用、各子应用使用 Vue 的 <keep-alive> 组件实现；
3. 门户多页签组件已加载的页面切换功能。

### 使用门户多页签

> 门户多页签已在 Portal-tabs 中实现，具体使用方法见 [Portal-tabs 门户多页签](/ecp-ui-plus/docs/micro-frontends/portal-tabs.html) 。

## 全局弹出层层级管理

主应用与所有子应用的弹出层 z-index 统一维护。

> - `路由式加载` 与 `组件式加载` 均已添加全局弹出层层级维护，一般无需额外配置；
> - 为方便后续拓展应用，已提供相关方法，具体见 [UsePopupZIndex 弹出层级管理](/ecp-ui-plus/docs/micro-frontends/use-popup-z-index.html) 。
