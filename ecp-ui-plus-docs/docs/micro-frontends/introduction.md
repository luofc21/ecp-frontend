<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/micro-frontends/introduction.html -->

# 微前端介绍

## 微前端架构

🥳 哦哟~

- 这一小节内容是通过微前端加载的，原文见 [前端资源中心 - 微前端架构](http://frontend.pcitech.online/docs/guidance/induction/chapter-technic/architecture-technical/basics/micro-frontend.html)。

## 技术选型

现流行的微前端框架中，主要有 3 个方案：

1. Single-spa 方案：
   - 来源于现代框架组件生命周期，将多个单页面应用聚合为一个整体应用，典型案例：[乾坤](#乾坤)；
2. 完全 iframe 方案：
   - 即在采用传统 iframe 嵌套的基础上，进行路由同步改造与数据共享改造；
3. 半 iframe 方案：
   - 即仅利用 iframe 天然沙箱实现 js 隔离，并在此基础上，使用其它技术手段进行 HTML 元素 与 CSS 隔离改造、路由同步改造与数据共享改造，典型案例：[无界](#无界)。

### 乾坤

[乾坤 Qiankun](https://qiankun.umijs.org/zh) 是 阿里 基于 [Single-spa 方案](https://zh-hans.single-spa.js.org/docs/getting-started-overview) 实现的微前端框架，主要实现思路：

1. 子应用预注册；
2. 子应用资源预加载；
3. 路由监听：匹配到了激活的路由则加载子应用资源，顺序调用生命周期函数并最终渲染到容器；
4. 通过 Proxy 代理与指定代码执行上下文，实现 js 沙箱；
5. 通过 ShadowDOM 或 添加 CSS 指定上下文，实现 css 沙箱。

- 优点：
  - 基于路由监听自动加载、卸载对应子应用；
  - 沙箱方案完备，基本实现应用隔离；
  - 路由同步，同时作用于主应用于子应用；
  - 应用间通信简单，全局注入；
- 缺点：
  - **不支持 vite 等 ESM 脚本运行**；
  - 不支持子应用动态注册；
  - 不支持子应用保活；
  - js 沙箱无法绝对隔离：
    - 主、子应用和子应用间 Vue 实例会互相覆盖，子应用卸载清理不干净；
    - 在主应用开启 vue.js external 的情况下，主、子应用和子应用间同名全局注册的组件会互相覆盖；
    - $router 不允许重定义，需要主、子应用同时开启或关闭 vue.js external；
    - 主应用不可在 Vue 实例上挂载 $router、$store...；
    - 同名依赖会重复加载，且易与主应用的产生冲突；
  - css 沙箱无法绝对隔离：
    - 主、子应用和子应用间全局样式会互相覆盖，子应用卸载清理不干净；
    - 因为主、子应用和子应用间 Vue 实例会互相覆盖，scoped 样式无法匹配对应组件元素；
    - 不同版本的同名依赖样式互相覆盖，导致样式异常。

在 Ecp-ui(Vue2) 中，我们采用乾坤实现微前端，并通过 Hack 的方式解决部分框架缺陷。

对于 Vue3 + vite，虽然有民间方案可以解决 ESM 脚本运行问题，但反过来，由于 ESM 加载机制与传统 JS 脚本加载机制不同，无法加载不使用 ESM 的应用。

进一步地，在经过 Hack 之后，Qiankun 仍遗留一些问题无法解决。这些问题更多是 Qiankun 或 Single-spa 框架设计问题导致的，并不是民间方案或者 Hack 就可以处理的。

因此，我们不希望在已存在这堆问题的基础上再改造，应该要寻求更合适的微前端解决方案。

### 无界

[无界 Wujie](https://wujie-micro.github.io/doc/) 是 腾讯 参考乾坤的 issue 中一个 [议题](https://github.com/umijs/qiankun/issues/286)、基于 [WebComponent](https://developer.mozilla.org/zh-CN/docs/Web/API/Web_components) 容器和 iframe 沙箱实现的微前端框架，主要实现思路：

1. 子应用的实例在主应用同域的 iframe 内运行；
2. Dom 在主应用容器下的 WebComponent 内；
3. 通过代理 iframe 的 document 到 WebComponent，实现两者的互联；
4. 通过劫持 iframe 的 history.pushState 和 history.replaceState，将子应用的 url 同步到主应用的 query 参数上；
5. 通过数据注入、window.parent、EventBus 等实现数据共享与应用通信。

- 优点：
  - **支持同时运行 普通脚本 与 ESM 脚本**；
  - 利用 iframe 搭建天然的 js 沙箱；
  - 利用 WebComponent 搭建天然的 css 沙箱；
  - 隔离样式，但不隔离 CSS 变量，便于实现主题换肤；
  - 基于 iframe，可实现应用级保活；
  - 支持多应用同时激活；
  - 应用间通信简单，全局注入；
  - 组件式加载方式，跟随组件装载、卸载；
- 缺点：
  - ShadowDom 内加载子应用节点，有一定局限性；
  - 应用保活模式不支持路由同步；
  - 路由同步 url 拼接太难看，能明显看出来是内嵌应用；
  - 组件式加载方式，需要主应用为每个子应用提供路由页面承载；
  - 同步脚本与异步脚本在不同的闭包中执行，未显式挂载到 window 上的全局变量拿不到。

与 乾坤 相比，无界 的应用隔离做得更彻底，并且在这基础上添加 ESM 脚本支持、应用级保活等，而且加载方式、应用通信等等更加自由。

无界 的缺点也很明显，但这些都是可以通过包装来解决的，而且 无界 还提供比较完备的插件系统，方便在不改动子应用仓库代码的前提下，修改子应用代码。

因此，无界 是更适合 Vue3 + vite 的微前端框架，具体方案设计与实现思路见下一章节。
