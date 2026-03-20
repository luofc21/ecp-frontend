<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/micro-frontends/project.html -->

# 项目模板工程

> - 项目模板工程支持 主应用 与 子应用；
> - 如需启用主应用，详见 [主应用处理](/ecp-ui-plus/docs/micro-frontends/project-portal.html) 与 [子应用处理](/ecp-ui-plus/docs/micro-frontends/project-sub.html)；
> - 如需兼容 Vue2 主应用，详见 [兼容乾坤](/ecp-ui-plus/docs/micro-frontends/qiankun-polyfill.html)。

## 工程目录结构

查看目录结构

```bash
.
├── .vscode                         # VS Code 的配置目录
│   ├── extensions.json             # 插件配置文件
│   └── settings.json               # 设置配置文件
├── config                          # uni-server 配置目录
│   ├── config.ini                  # 配置模板文件
│   ├── proxy.ini                   # 代理配置文件
│   ├── server-config.js            # uni-server 服务配置文件
│   └── var.ini                     # 默认变量配置文件
├── login                           # 登录模块目录
│   ├── login.html
│   ├── login.js                    # 登录页面 入口文件
│   └── login.vue                   # 登录页面入口 Vue 组件
├── public                          # 公共资源目录
├── server                          # uni-server 服务目录
│   ├── main.js                     # uni-server 服务实例文件
│   └── server.js                   # uni-server 服务启动文件
├── src
│   ├── app                         # 应用主体目录
│   │   ├── api                     # API 接口目录
│   │   ├── router                  # 路由目录
│   │   ├── store                   # Pinia 状态管理目录
│   │   │   ├── dictionary          # 字典数据
│   │   │   ├── global-config       # 全局配置
│   │   │   ├── permission          # 权限管理
│   │   │   └── user                # 用户信息
│   │   └── views                   # 页面组件目录
│   │       ├── example             # 示例页面目录
│   │       ├── exception           # 异常页面目录
│   │       │   ├── coming-soon.vue         # 404 页面
│   │       │   └── redirect.jsx            # 重定向页面，可用于跳转重复路径中转，和清除指定页面keep-alive缓存
│   │       ├── iframe              # 内嵌页面目录
│   │       │   └── inner-iframe.vue        # 承载 iframe 页面组件
│   │       └── view-route.js       # 视图路由文件
│   ├── assets                      # 静态资源目录
│   ├── common                      # 工程内公共模块目录
│   │   ├── components              # 公共组件目录
│   │   ├── directives              # Vue 指令目录
│   │   └── utils                   # 工具函数目录
│   ├── constants                   # 常量定义目录
│   ├── portal                      # 门户页面目录
│   │   ├── portal.js               # 门户页面入口文件
│   │   └── portal.vue              # 门户页面入口 Vue 组件
│   ├── styles                      # 公共样式目录
│   │   ├── index.js                # 样式入口文件
│   │   ├── global                  # Scss 全局混入目录
│   │   │   ├── element.scss        # Element Plus 样式命名空间混入
│   │   │   ├── index.scss          # 全局混入入口文件
│   │   │   ├── mixin.scss          # Scss 混入文件
│   │   │   └── variable.scss       # Scss 变量文件
│   │   ├── styles                  # 项目公共样式目录
│   │   │   ├── common.scss         # 通用样式文件
│   │   │   ├── index.scss          # 项目样式入口文件
│   │   │   ├── reset.scss          # 样式重置文件
│   │   │   └── transition.scss         # 过渡效果样式文件
│   │   └── theme                   # 主题样式目录
│   │       ├── dark                # 暗色主题目录
│   │       │   ├── index.scss          # 暗色主题入口文件
│   │       │   ├── mapper.scss         # 暗色主题映射文件
│   │       │   └── var.scss            # 暗色主题变量文件
│   │       └── default             # 默认主题目录
│   │           ├── index.scss          # 默认主题入口文件
│   │           ├── mapper.scss         # 默认主题映射文件
│   │           └── var.scss            # 默认主题变量文件
│   ├── App.vue                     # 主入口 Vue 组件
│   └── main.js                     # 项目入口文件
├── .eslintrc.cjs                   # ESLint 配置文件
├── .gitignore
├── .npmrc                          # npm 配置文件
├── .prettierrc.json                # Prettier 配置文件
├── .yarnrc                         # Yarn 配置文件
├── jsconfig.json                   # JS 配置文件
├── package.json
├── pnpm-lock.yaml                  # pnpm 锁文件
├── README.md                       # 项目说明文件
├── template-index.html             # 主页模板文件，用于生成 sub.html 与非 portal 模式的 index.html
├── template-portal.html            # 门户页面模板文件，用于生成 portal 模式的 index.html
├── tsconfig.json                   # TypeScript 配置文件
├── vite.config.js                  # Vite 配置文件
└── vite.proxy.config.js            # Vite 代理配置文件
```

## 关键目录或文件说明

### .vscode

VS Code 的配置目录，已添加推荐插件与 ESLint 代码格式化相关配置，**`请勿添加至 .gitignore`** 。

### config/server-config.js

uni-server 服务配置文件，已适配 物理机部署 与 容器化部署。

### @store

Pinia 全局状态管理。

> Vue3 不再使用 Vuex，改用 [Pinia 状态管理库](https://pinia.vuejs.org/zh/)。

### @views/exception/redirect.jsx

重定向页面，可用于跳转重复路径中转，和清除指定页面 keep-alive 缓存。

### @views/iframe/inner-iframe.vue

承载 iframe 加载的页面，匹配路由 `/inner-iframe/:url`，建议使用 `inner-iframe` 代替 portal-iframe.html 加载内嵌 iframe。

### src/portal

`portal.js` 主应用门户入口文件 与 `portal.vue` 主应用门户入口 Vue 组件存放位置。

### src/styles

- `global` Scss 全局混入目录，这个目录的文件只放混入，不放普通样式定义；
- `styles` 样式放在这个目录下，
  - 全局样式写在 `src/styles/styles/common.scss` 内，注意样式作用域，详见对应文件内注释；
- `theme` 主题换肤相关，主题变量与样式存放目录，已内置 `默认主题` 与 `暗色主题` 模板；
  - 如需使用主题换肤，请参考 [Theme 主题定义](/ecp-ui-plus/docs/design/theme.html) 文档开发。

### template-index.html

主页模板文件，用于生成 `sub.html` 与 `非 portal 模式的 index.html`。

> - 由于 vite 工具链目录限制，不再使用固定 `sub.html` 与 `非 portal 模式的 index.html`，改为在执行 vite 命令时生成。

### template-portal.html

门户页面模板文件，用于生成 `portal 模式的 index.html`。

> - 由于 vite 工具链目录限制，不再使用固定 `portal 模式的 index.html`，改为在执行 vite 命令时生成。

## 其它注意事项

### Vite 插件

警告！！！

- 请勿使用 vite-plugin-html 插件 ！！！！！

### Filter

`src/common` 已移除 filter 目录，详见 [Vue 3 迁移指南 - 过滤器](https://v3-migration.vuejs.org/zh/breaking-changes/filters.html) 。

### ElementPlus 全局命名空间

为避免与 Vue2 ElementUI 产生样式冲突，请添加 ElementPlus 全局命名空间。

> 命名空间 [ElementDefaultConfig](/ecp-ui-plus/docs/api/constants/element-default-config.html) 已提供，其它默认配置项与 ElementPlus 支持配置项参考 [ElementDefaultConfig - 全局配置](/ecp-ui-plus/docs/api/constants/element-default-config.html)。

```js
import { useGlobalConfig } from 'element-plus';
import { ElementDefaultConfig } from '@ecp/ecp-ui-plus';

// 必须在调用 ElementPlus 指令类组件（如 ElMessage）之前配置
const ElGlobalConfig = useGlobalConfig();
ElGlobalConfig.value = ElementDefaultConfig;
```

```vue
<template>
    <el-config-provider v-bind="ElementDefaultConfig">
        <!-- ... -->
    </el-config-provider>
</template>
<script setup>
import { ElementDefaultConfig } from '@ecp/ecp-ui-plus';
</script>
```
