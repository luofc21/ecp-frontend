<!-- source: http://frontend.pcitech.online/docs/guidance/induction/chapter-technic/architecture-technical/design/mobile.html -->

# 移动端

移动端包括 H5、小程序与 App三部分。

## H5

### 技术架构及技术栈

  
  

![移动端 H5 技术架构及技术栈](../../../assets/images/guidance/induction/h5.png)

### 工程基础

工程仓库：<http://git.pcitech.com/frontend/template-vue-h5>。

基于 Vue3 全家桶搭建的 移动端 H5 模板工程。

关键依赖：[Vue 3](https://cn.vuejs.org/)、[Vite 3](https://cn.vitejs.dev/)、[Rollup](https://cn.rollupjs.org/)、[Vue-router](https://router.vuejs.org/zh/)、[Pinia](https://pinia.vuejs.org/zh/)、[Axios](https://axios-http.com/zh/docs/intro)、[Vant 4](https://vant.pro/vant/#/zh-CN)、[Emv-ui](http://frontend.pcitech.online/emv-ui/)、[Emv-JSBridge](http://frontend.pcitech.online/emv-jsbridge/)。

具体使用指南及注意事项见 [H5 模板工程](/docs/template-emv/)。

### 应用场景

面向G端、B端的 H5 应用一般是与 PC 端配套使用的，业务量一般也是 PC 端的缩减版，业务量并不会太大，采用单体前端应用架构即可。

对应开放环境有以下几种情况：

- 普通内网移动端 H5

这种情况下，在网络层面就限制了用户访问。无需过多考虑负载等情况，部署同 PC 端，采用 uni-server即可。

- 开放互联网 H5（含微信公众号）

这种情况下，前端不可直连网关调用服务（否则网关所有接口都会暴露出互联网），需要经过后端过滤服务，请求第三方服务如无系统后端支撑需求可直连。

开放互联网使用的 H5 一般通过域名访问，可考虑使用 uni-server + Nginx 或直接用Nginx 代替 uni-server（直接替换成 Nginx 不会启用 Nacos 配置，应修改为使用对应环境下的本地配置）。

- 混合模式 App H5

这种情况是指：H5 打包输出静态资源，再与 App 一起打包输出 App 安装包，这时候前端请求都由 App 代转发。 如无特殊需求，一般不考虑采用这种模式。

## 小程序
