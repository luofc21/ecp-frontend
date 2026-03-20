<!-- source: http://frontend.pcitech.online/docs/guidance/induction/chapter-practice/deploy-package-building.html -->

# 手摸手教你构建前端部署包

## 基础部署包结构

```bash
.
├── bin                     # 启动脚本
├── config                  # 前端服务配置
├── dist                    # 打包后的前端页面与静态资源
├── logs                    # 前端服务日志
├── server                  # 前端服务
├── nodejs-plugin.tar.gz    # nodejs、pm2 等环境包
└── node_modules.tar.gz     # 前端服务依赖
```

## 构建部署流程

- 请使用 Jenkins / k8s 流水线 打包、构建；
- 部署支持物理机部署、docker容器部署、k8s部署；
- 支持 AMD64 (x86\_64 / x64)、ARM64 (AArch64) 架构。

> - 物理机、docker容器部署流程，见 wiki 文档 [前端应用部署说明(uni-server 1.5) - 物理机、Docker容器](http://wiki.pcitech.com/books/%E5%BA%94%E7%94%A8%E9%83%A8%E7%BD%B2/page/uni-server-15-docker)；
> - k8s 流水线部署流程，见 wiki 文档 [前端应用部署说明(uni-server 1.5) - k8s流水线](http://wiki.pcitech.com/books/%E5%BA%94%E7%94%A8%E9%83%A8%E7%BD%B2/page/uni-server-15-k8s)。
