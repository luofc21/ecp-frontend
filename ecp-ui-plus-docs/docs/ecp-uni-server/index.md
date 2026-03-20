<!-- source: http://frontend.pcitech.online/docs/ecp-uni-server/index.html -->

# ECP-UNI-SERVER

基于 nodejs 的应用服务，主要用于应用部署。

> 想知道服务如何工作的？看看 [详解 ◁](./detail.html)

## 接入说明

在项目中添加两个目录：config、server，其中必须的文件如下：

```bash
|-- config
      |-- config.ini （前端配置模板）
      |-- proxy.ini （服务代理模板）
      |-- var.ini （config.ini、proxy.ini用到的变量，同nacos）
      |-- server-config.js （前端服务的配置文件）
|-- server
      |-- main.js （前端服务的入口文件）
      |-- server.js （通过脚本启动的入口）
|-- dist （项目构建产物）
      |-- config.js （非必须）
      |-- config.json （非必须）
      |-- index.html
...
```

> \*\*config/\*\*说明：config.ini、proxy.ini 都为模板文件，模板中的变量根据 **var.ini**（本地）或 NACOS\_CONFIG.items（server-config.js，启用 nacos 时）定义的变量解析。

下面做详细的说明：

### config/server-config.js

node 服务的配置文件，必须包含 SERVER\_CONFIG、NACOS\_CONFIG，具体配置如下说明：

1. SERVER\_CONFIG: 配置**必须**修改，请按实际项目调整
2. NACOS\_CONFIG: nacos 相关配置
3. NACOS\_CONFIG.serviceList: 获取 nacos 上注册的前端服务列表并生成代理，一般情况下，没有使用其他子应用不需要启用；如果启用，需要同时暴露变量**APPS\_ENTRY**（见下例）
4. NACOS\_CONFIG.registerService: 将当前应用注册到 nacos 的服务列表
5. NACOS\_CONFIG.ipRules: 应用注册到 nacos 时获取 ip 的规则，请在 config.ini 或者 nacos 上配置
6. NACOS\_CONFIG.items: 需要获取的 nacos 配置列表，**注意**只有启动时才会获取一次，如果 nacos 配置有更新，需要重启服务

以多维为例，

- 普通应用

```js
const SERVER_CONFIG = {
    APP_PORT: 30010, // 端口
    APP_NAME: "multi-info-frontend", // 应用名
    APP_ALIAS: "multi", // 别名，网关访问路径
    KEEP_ALIVE: 10, // 服务保活，监听时间默认10s（最小值为10），设为false、null、0、空字符则不开启
    APP_REG_IP: "127.*.*.*", //如需用虚拟IP注册服务时配置，用真实IP则不需配置
};

// nacos配置项
const NACOS_CONFIG = {
    enabled: true,
    // serviceList: true, // 是否获取所有前端服务列表
    registerService: true, // 注册当前应用
    address: "nacos-center.v-base:30848", // 服务域名:端口
    namespace: "a85a37ef-5bec-478c-a60f-0b11f10b3da4",
    items: [
        // 前端应用配置，frontend: true 表示为前端应用模板/配置，已废弃
        // {
        //     dataId: 'uni-multi-frontend',
        //     group: 'frontend',
        //     frontend: true
        // },
        // 前端公共配置
        {
            dataId: "settings-frontend",
            group: "prophet",
        },
        // 公共配置
        {
            dataId: "applications",
            group: "prophet",
        },
    ],
    // 服务注册到nacos时，获取ip的规则，请在config.ini或者nacos上配置
    ipRules: {
        preferredNetworks: [], // 首选
    },
};

module.exports = {
    SERVER_CONFIG,
    NACOS_CONFIG,
};
```

- 门户应用（主应用）

```js
const SERVER_CONFIG = {
    APP_PORT: 30010, // 端口
    APP_NAME: "multi-info-frontend", // 应用名
    APP_ALIAS: "multi", // 别名，网关访问路径
};

// nacos配置项
const NACOS_CONFIG = {
    enabled: true,
    serviceList: true, // 是否获取所有前端服务列表
    registerService: true, // 注册当前应用
    address: "nacos-center.v-base:30848", // 服务域名:端口
    namespace: "a85a37ef-5bec-478c-a60f-0b11f10b3da4",
    items: [
        // 前端公共配置
        {
            dataId: "settings-frontend",
            group: "prophet",
        },
        // 公共配置
        {
            dataId: "applications",
            group: "prophet",
        },
    ],
    // 服务注册到nacos时，获取ip的规则，请在config.ini或者nacos上配置
    ipRules: {
        preferredNetworks: [], // 首选
    },
};

// 门户需要使用的子模块，在前端服务订阅和子模块监控中，根据此列表获取
const APPS_ENTRY = [
    // 除了name，其余配置都会按 local代理配置、nacos代理配置、nacos服务订阅 的顺序更新
    /**
     * 如果ip、端口、需要修改，请在var.ini中配置变量，不要直接修改此文件，如：
     * metadata-frontend.ip=172.25.21.205
     * metadata-frontend.port=30013
     */
    {
        name: "metadata-frontend",
        alias: "metadata",
        port: "30013",
        ip: "",
    },
    {
        name: "data-integrate-frontend",
        alias: "dts",
        port: "30016",
        ip: "",
    },
    {
        name: "data-govern-frontend",
        alias: "dgs",
        port: "30017",
        ip: "",
    },
];

module.exports = {
    SERVER_CONFIG,
    NACOS_CONFIG,
    APPS_ENTRY,
};
```

### config/config.ini

前端配置模板，会解析成对象，给前端调用。（同 nacos 上的配置）

> 注意：请不要以 ['proxy', 'SERVER\_CONFIG', 'NACOS\_CONFIG', 'APPS\_ENTRY'] 开头，推荐使用 IMPORT\_CONFIGS 开头

```bash
########### 以下是需要注入的变量 ###########

# CAS服务地址
IMPORT_CONFIGS.CAS_HOST=http:\/\/${psc.cas.ip}:${psc.cas.port}
# 大屏服务地址
IMPORT_CONFIGS.MAP_URL=http:\/\/${mapserver.ip}:${mapserver.port}/public/maps/21
```

### config/proxy.ini

node 代理使用的变量（nacos 不再配置代理）

proxy 开头的为服务代理配置，根据配置自动生成，[配置参考](https://github.com/chimurai/http-proxy-middleware#options)

```ini
########### proxy开头为代理配置 ###########

proxy.api.ip=${api.gateway.ip}
proxy.api.port=${api.gateway.proxy.port}
proxy.api.context=["^/sso","^/api","^/sysmanager"]
```

或者

```ini
########### proxy开头为代理配置 ###########

proxy.api.ip=${api.ip}
proxy.api.port=${api.port}
proxy.api.context=^/api

proxy.sso.ip=${sso.ip}
proxy.sso.port=${sso.port}
proxy.sso.context=^/sso
```

### config/var.ini

config/config.ini、config/proxy.ini 使用的变量（同 nacos 上的基础变量）

preferred-networks 为前端应用注册的 ip 获取规则

```ini
########### 基础变量 ###########

api.ip=172.25.22.160
api.port=8000

sso.ip=172.25.21.205
sso.port=9011

psc.cas.ip=
psc.cas.port=

mapserver.ip=
mapserver.port=

# 如果订阅的服务不健康或者不启用nacos时，会根据APPS_ENTRY使用此变量生成代理
multi-info-frontend.ip=172.25.21.205
multi-info-frontend.port=30010

# 特殊变量，前端应用注册时，使用的ip匹配规则
preferred-networks=172.25
```

### server/server.js

通过 bin/run.sh 启动时的入口，一般情况下直接拷贝下面内容到 server.js 即可。

```js
const path = require("path");
const config = require("../config/server-config");
const UniServer = require("@ecp/uni-server");

UniServer.init(path.resolve(__dirname, "./"), config);
```

### server/main.js

node 服务的主入口，server.js 会执行此脚本；如果使用容器部署，请使用此文件作为入口启动

1. 普通应用：如果只需要简单部署前端，并且无特殊情况需要处理，可直接用此模板

```js
const path = require("path");
const config = require("../config/server-config");
const UniServer = require("@ecp/uni-server");

const MainServer = UniServer.server;

const server = new MainServer({
    context: path.resolve(__dirname, "./"),
    config,
    middleware(app, config) {},
});
```

2. 微前端的门户应用：如果需要控制子应用的接入，使用此模板

> 以多维门户举例：

```js
const path = require("path");
const config = require("../config/server-config");
const UniServer = require("@ecp/uni-server");
const { monitor } = require("@ecp/uni-monitor");

const MainServer = UniServer.server;

const server = new MainServer({
    context: path.resolve(__dirname, "./"),
    config,
    useDefaultStatic: false, // 根路径重定向时，需要禁用默认的资源路径
    middleware(app, config) {
        // 允许使用头'x-requested-with'，解决firefox跨域问题
        app.all("*", function (req, res, next) {
            res.header("Access-Control-Allow-Headers", "X-Requested-With");
            next();
        });

        const renderIndex = (req, res) => {
            res.sendFile(path.resolve(__dirname, "../dist/index.html"));
        };

        // 自定义的路由都指向首页
        app.get("/", renderIndex);
        app.get("/s-*", renderIndex);

        // 子模块监控
        app.use("/monitor", monitor(app, config, { title: "多维模块监控" }));
    },
});
```

3. 自定义模板：如果需要更高的自由度，可以使用提供的钩子函数，自定义服务

```js
const path = require("path");
const config = require("../config/server-config");
const UniServer = require("@ecp/uni-server");

const MainServer = UniServer.server;

const server = new MainServer({
    context: path.resolve(__dirname, "./"),
    config,
    // 代理的响应设置
    onProxyRes(proxyRes, req, res) {},
    // 代理的请求设置
    onProxyReq(proxyReq, req, res) {},
    // 服务的自定义
    middleware(app, config) {
        // App为express实例，config为应用配置
    },
});
```

- 插件内置了一些模块，可以按情况使用：
  - @ecp/uni-monitor (前端模块监控)
  - body-parser
  - connect-history-api-fallback (history 推荐插件)
  - [express 文档](https://www.expressjs.com.cn/4x/api.html)

> 如果有配置需要通过 nodejs 服务传递给页面，可以使用 public/config.json 或 public/config.js（config.js 即将废弃）

### public/config.json （非必须）

在项目中，请在 public 目录下添加 config.json 文件，部署后会根据 config.ini 生成并覆盖原有的 config.json，然后通过异步请求 config.json 的方式使用

- config.json

```json
{
    "IMPORT_CONFIGS": {
        "CAS_HOST": "http://172.25.21.205:8989"
    }
}
```

然后，在项目中异步调用获取 config.json

```js
Axios(`${__webpack_public_path__}config.json`).then(res => {
    // 推荐将配置放到vuex，不推荐放到window下
    console.log(res.data);
});
```

### public/config.js （非必须）

在项目中，请在 public 目录下添加 config.js 文件，部署后会根据 config.ini 生成并覆盖原有的 config.js，然后通过 window.IMPORT\_CONFIGS 的方式使用

```js
window.IMPORT_CONFIGS = {
    CAS_HOST: "http://172.25.21.205:8989",
};
```

然后，在 public/index.html 使用 config.js

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width,initial-scale=1.0" />
        <link rel="icon" href="<%= BASE_URL %>favicon.ico" />
        <title>元数据</title>
        <script src="./config.js"></script>
    </head>
    <body>
        <div id="app"></div>
        <!-- built files will be auto injected -->
    </body>
</html>
```

## 镜像构建

uni-server 支持构建为镜像，直接将根目录下的 **Dockerfile** 拷贝到项目根目录即可

> - image-builder: [前端镜像构建插件](./../image-builder/)，package.json 需要按照文档改造;
> - Jenkins 需要支持 docker 才能构建镜像。

- Dockerfile

```bash
FROM node:10.15.0-alpine

RUN mkdir /app

COPY ./server /app/server
COPY ./dist /app/dist
COPY ./config /app/config

WORKDIR /app/server

RUN npm init --yes
RUN npm install -S @ecp/uni-server --production --registry=http://172.25.20.65:4873/

CMD node main.js
```

Jenkins 的构建任务需要调整下

```bash
yarn
yarn build:uni

npm i -g image-builder --registry http://172.25.20.65:4873/

imbuilder --path ./ -l disable
```
