<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/instruction/quickstart.html -->

# 快速上手

## 介绍

通过本章节你可以了解到 Ecp-ui-plus 的安装方法和基本使用姿势。

## 安装

### 配置源

#### 方法一 推荐

在前端工程 .npmrc 文件中配置源：

```ini
# .npmrc
registry=http://172.25.20.65:4873/
```

#### 方法二

直接配置源

```sh
npm set registry http://172.25.20.65:4873
```

### 安装依赖

NodeJS 项目中使用 Ecp-ui-plus 时，可以通过 `pnpm` 进行安装：

```sh
# 通过 pnpm 安装
pnpm add @ecp/ecp-ui-plus
```

当然，你也可以通过 `npm` 或 `yarn` 进行安装：

```sh
# 通过 npm 安装
npm add @ecp/ecp-ui-plus

# 通过 yarn 安装
yarn add @ecp/ecp-ui-plus
```

## 引入

### 完整引入 推荐

```js
import { createApp } from 'vue'
import EcpUIPlus from '@ecp/ecp-ui-plus';
import '@ecp/ecp-ui-plus/theme-chalk/index.css';

import App from './App.vue'

const app = createApp(App)

app.use(EcpUIPlus);
app.mount('#app')
```

```vue
<template>
    <ecp-button text="按钮" @click="handleClick" />
</template>

<script setup>
const handleClick = () => { }
</script>
```

### 按需导入

```vue
<!-- path/to/vue-component.vue -->
<template>
    <ecp-button text="按钮" @click="handleClick" />
</template>

<script setup>
import { EcpButton } from '@ecp/ecp-ui-plus';
import '@ecp/ecp-ui-plus/theme-chalk/ecp-button.css';
const handleClick = () => {
}
</script>
```
