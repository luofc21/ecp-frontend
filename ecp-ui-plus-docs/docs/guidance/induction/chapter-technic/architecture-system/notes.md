<!-- source: http://frontend.pcitech.online/docs/guidance/induction/chapter-technic/architecture-system/notes.html -->

# 实际应用注意事项

1. 网关默认端口 9081，实际环境中网关 IP、端口在 Nacos 配置 applications > api.gateway.ip、api.gateway.proxy.port 这两个参数上配置；
2. Nacos 默认端口 30848，前端应用调用 Nacos 服务，使用域名 nacos-center.v-base（不直接配置IP），域名在应用部署服务器 /etc/hosts 中添加映射。
