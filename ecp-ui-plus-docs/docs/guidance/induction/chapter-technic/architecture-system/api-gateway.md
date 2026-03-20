<!-- source: http://frontend.pcitech.online/docs/guidance/induction/chapter-technic/architecture-system/api-gateway.html -->

# API 网关

在微服务集成之前：

- 所有服务都是单点，服务间交互复杂；
- 所有服务配置、代理配置写在配置中心，公共配置项膨胀；
- 服务间互操作艰难，鉴权复杂。

为解决以上痛点，引入了Api网关。

![Api 网关](../../../assets/images/guidance/induction/api-gateway.png)

对于前端应用来说，Api 网关最主要实现了以下功能：

- 引入 SSO鉴权，实现单点登录；
- 依赖 Nacos 集群，引入服务注册、发现、同步；
- 请求统一转发处理，精简大量服务IP、Port的代理配置（通过上下文匹配，不再需要对各个服务单独配置IP端口了），简化服务间交互，有效减少运维操作。
