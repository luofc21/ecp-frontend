<!-- source: http://frontend.pcitech.online/docs/ecp-uni-server/detail.html -->

# UNI-SERVER 工作详解

## 启动流程

uni-server 源码的目录如下：

> 注意区分源码与项目的入口

```bash
|-- bin
      |-- healthcheck.sh （前端配置模板）
      |-- run.sh （服务代理模板）
|-- example （示例/测试样例）
      |-- 项目中使用的配置，参考README.md即可
      |-- server
         |-- main.js （项目中的pm2执行入口，项目的入口）
         |-- server.js （项目中的run.sh启动入口，项目的入口）
|-- src （源码）
      |-- config
         |-- path.js （路径变量）
      |-- constants （常量）
      |-- template （模板文件）
         |-- main.js （项目中使用的前端服务入口）
         |-- pm2.config.js （pm2启动模板）
      |-- utils （工具函数）
      |-- entry.js （run.sh脚本启动入口，源码的入口）
      |-- index.js （插件入口，源码的入口）
      |-- proxy.js （前端服务，源码的入口）
      |-- server.js （pm2启动入口，源码的入口）
...
```

1. 部署启动时，执行 sh bin/run.sh 启动服务
2. run.sh 会调用 entry.js 进行启动前的初始化，并在项目中生成 config/pm2.config.js
3. pm2.conig.js 指定 src/server.js 为入口
4. server.js 先根据本地的 config.ini、proxy.ini、var.ini 生成 local-config.js 本地配置，同时进行 nacos 配置订阅、注册当前服务到 nacos、nacos 服务列表轮询
5. 然后 server.js 会通过 proxy.js 启动前端 express 服务，proxy.js 先根据 local-config.js 提供前端静态资源和 api 代理的访问能力
6. 当订阅到 nacos 配置或者 nacos 服务列表有更新，就会生成或更新 nacos-config.js，同时更新 proxy.js 启动的服务，改为读取最新的 nacos-config.js

## 本地调试

> windows 环境下，run.sh 不可用，所以本地调试可以直接用 node 启动

- 通过 pm2 调试：

```bash
node example/server/server.js
```

注意：执行前请确保安装了 pm2。执行命令后会在 pm2 里面添加应用，如果调试完了需要手动停止服务：

```bash
node example/server/server.js stop
# or
pm2 delete ${APP_NAME} # 替换为应用名
```

- 直接启动前端服务：

```bash
node example/server/main.js
```

直接在终端中运行一个前台的 node 进程，如果有文件修改，都需要 Ctrl+C 停掉服务，然后重新运行。

## 项目中调试

需要在项目的 server 目录下安装 uni-server 插件

```bash
npm i @ecp/uni-server --registry http://172.25.20.65:4873/
```

然后和 `本地调试` 一致

## 问题汇总

### 1. 将 server-config.js 下的 address 改了，但是获取不到对应的配置？

A：nacos 客户端有一个问题：当同一台服务器上，启动了多个 nacos 配置订阅，只有第一个连接的 nacos 配置订阅是正确的，后面连接即使配置了不同的 address 都会无效，依然会指向第一个连接的 address。

解决方法：

- 如果是本地调试，将所有的 uni-server 服务都关掉，然后再启动要调试的服务即可；
- 如果是现场或测试环境出现此问题，需要根据 `pm2 ls` 里面的前端应用列表检查每一个应用的 address 配置，确保都使用域名 `nacos-center.v-base:30848` ，然后执行 `pm2 restart all` 重启所有前端即可。

### 2. 将 server-config.js 下的 address 都使用域名了，但是获取不到对应的配置？

A: 首先检查 hosts 配置是否正确，可以在服务器上 `cat /etc/hosts` 查看配置，或者通过接口 `http://前端应用 ip+端口/hosts` 查看域名配置是否正确。修改域名后，使用 `pm2 restart all` 重启即可。

### 3. 所有配置都正确了，但是通过/config 查看的配置却有问题？

A: 一般是 nacos 的线上配置出现了没有考虑到的情况，如果无法一眼看出就需要本地调试了。一般情况下调试 src/server.js 下的 generateConfigFile 函数即可定位到问题。

### 4. multi-info-frontend、data-govern-frontend 等前端代理是怎么来的？

A: 前端代理的生成规则：

(1) proxy.ini 如果有 context 为前端的代理项，会生成前端代理

(2) server-config.js 的 APPS\_ENTRY 会生成前端代理

(3) 如果有 server-config.js 的 APPS\_ENTRY，则前端代理的 ip 等信息优先级为：nacos 服务注册列表 → nacos 配置 → 本地 var.ini 配置
