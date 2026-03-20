<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/instruction/development.html -->

# 开发指南

## 介绍

通过本章节你可以了解到 Ecp-ui-plus 组件库开发、维护的基本姿势。

## 项目脚本

### 安装依赖

```sh
pnpm i
```

### 打包构建

```sh
pnpm build:gl
```

## 文档编辑

### 文档调试

```sh
pnpm docs:dev
```

### 文档打包

```sh
pnpm docs:build
```

### 文档预览

```sh
pnpm docs:preview
```

## 组件库工程

### 生成目录树

使用命令

```sh
pnpm md:tree
```

输出文件在工程根目录的 tree.md

### 组件库工程目录结构

```md
. ecp-ui-plus
├── .vscode
│   ├── extensions.json
│   └── settings.json
├── docs
│   ├── .vitepress
│   ├── code-snippets
│   │   └── ...code-snippets
│   ├── docs
│   │   └── ...documents
│   ├── examples
│   │   └── ...examples
│   ├── public
│   │   └── ...document-resources
│   ├── CHANGELOG.md
│   ├── README.md
│   └── package.json
├── internal
│   ├── build
│   ├── plugins-for-doc
│   └── release
├── packages
│   ├── components
│   │   ├── ...components
│   │   ├── index.ts
│   │   └── package.json
│   ├── constants
│   │   ├── ...constants
│   │   ├── index.ts
│   │   ├── key.ts
│   │   └── package.json
│   ├── directives
│   │   └── index.js
│   ├── ecp-ui-plus
│   │   ├── component.ts
│   │   ├── defaults.ts
│   │   ├── index.ts
│   │   ├── make-installer.ts
│   │   ├── package.json
│   │   └── plugin.ts
│   ├── micro-app
│   │   ├── micro-components
│   │   ├── micro-composables
│   │   ├── micro-utils
│   │   ├── portal-tabs
│   │   ├── index.js
│   │   └── package.json
│   ├── theme-chalk
│   │   ├── src
│   │   │   └── ...styles/style-vars
│   │   ├── gulpfile.ts
│   │   └── package.jsonsrc
│   └── utils
│       ├── ...utils
│       ├── index.js
│       └── package.json
├── play
│   └── ...
├── CONTRIBUTING.md
├── README.md
├── auto-imports.d.ts
├── package.json
├── pnpm-lock.yaml
├── pnpm-workspace.yaml
├── tsconfig.base.json
├── tsconfig.json
├── tsconfig.node.json
├── tsconfig.web.json
└── turbo.json
```
