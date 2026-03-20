<!-- source: http://frontend.pcitech.online/ecp-ui-plus/CHANGELOG.html -->

# Changelog

> All notable changes to `ecp-ui-plus` will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

## (2025-09-23)

### 🐛 Bug Fixes | Bug 修复

- `theme-chalk` 修复 ecp-icon 尺寸对齐等有误的 bug ([ca04f25](http://172.25.21.141/frontend/ecp-ui-plus/commit/ca04f255f9ac40d9661c0bd3ffdd4f779e022ac6))

### 📝 Documentation Changes | 文档更新

- 文档样式更新 ([8d4f480](http://172.25.21.141/frontend/ecp-ui-plus/commit/8d4f480d263e8d1228ef975bcee613e83fd0314e))

## (2025-09-19)

### 🐛 Bug Fixes | Bug 修复

- `components` `theme-chalk` 修复 ecp-button 使用文字类型且二字汉字文本使用slot嵌入时会自动添加空格的 bug，plain 展示样式优化 ([a2b329d](http://172.25.21.141/frontend/ecp-ui-plus/commit/a2b329dfff4b72bac4ffb829e644aa39d83ec610))
- `components` `theme-chalk` 修复 ecp-button 组件胶囊形状与圆形展示样式有误的 bug ([12a7907](http://172.25.21.141/frontend/ecp-ui-plus/commit/12a7907a9ed5f870e5c82ed3457809a2f45c07b4))
- `components` `theme-chalk` 修复 ecp-preview-img-content、ecp-preview-img 展示比例有误的 bug，修复当图片链接为空时 ecp-preview-img-content、ecp-preview-img 展示有误的 bug，样式优化，其他细节优化 ([709e4ea](http://172.25.21.141/frontend/ecp-ui-plus/commit/709e4ea8f09b80b4e01b31fe28753279a3d6d277))
- `components` `theme-chalk` ecp-card 样式修正，去除行内样式与使用了important的样式 ([809a8b2](http://172.25.21.141/frontend/ecp-ui-plus/commit/809a8b27cae92304b6cb95ed6469ce183ca6aafa))
- `components` `theme-chalk` ecp-layout-pagination 样式修正 ([d63f55c](http://172.25.21.141/frontend/ecp-ui-plus/commit/d63f55c6ab591d9d2a4eb7a182255a55ef6d3d76))
- `components` 修复 ecp-preview-img-content、ecp-preview-img 图片列表图片展示有误的 bug ([d257918](http://172.25.21.141/frontend/ecp-ui-plus/commit/d2579187855cd9bd7d6c33a1abd85d220bcd1e66))
- `components` 修复 ecp-query-row 未根据VNode类型进行特殊处理的 bug ([edf5db0](http://172.25.21.141/frontend/ecp-ui-plus/commit/edf5db0f96ac7f8fb97b14eee901fb08b74f24f4))
- `theme-chalk` ecp-icon、ecp-license-place、element日期时间选择等组件样式修正 ([cf368ed](http://172.25.21.141/frontend/ecp-ui-plus/commit/cf368edc6566d90abce630d1a84317265cffbc88))

### ✨ Features | 新功能

- `components` `theme-chalk` `micro-app` ecp-preview-img 插槽兼容处理，app-sized-image 优化，app-search-form、app-submit-form 优化，注释补充 ([66abc3c](http://172.25.21.141/frontend/ecp-ui-plus/commit/66abc3cef60fade9d41827e2df62c57fb1ad35b1))
- `components` `theme-chalk` ecp-button-group 添加支持反向排列 ([cc18a12](http://172.25.21.141/frontend/ecp-ui-plus/commit/cc18a12f695ab0d9edcfb6850cf97c68560aec8b))
- `components` `theme-chalk` ecp-button-group 文字型展示优化，ElTag、ElTabs、ElImage、ElDatePicker 等 ElementPlus 组件重置样式优化 ([bb23c15](http://172.25.21.141/frontend/ecp-ui-plus/commit/bb23c1553002d844b1cf3a53ed6af1656c1ba3d2))
- `components` `theme-chalk` ecp-card、ecp-card-group、ecp-label-item 等组件优化，添加全局样式 app-sized-image 以支持以指定比例展示图片 ([eefe0c0](http://172.25.21.141/frontend/ecp-ui-plus/commit/eefe0c0bc01ec635ecbc7eb8ce218e20ba801d45))
- `components` `theme-chalk` ecp-panel 添加支持顶部、底部吸附，修复顶部无内容时顶部区域未隐藏的 bug ([6db371b](http://172.25.21.141/frontend/ecp-ui-plus/commit/6db371b4d90d8fd0881183e70c0b752b51762367))
- `micro-app` PortalTabsActions 实例允许在当前激活Tab项后新增Tab、允许在指定索引位置新增Tab ([69901ee](http://172.25.21.141/frontend/ecp-ui-plus/commit/69901ee31c73c44304bd14ea59313dc0a00d5db1))
- `theme-chalk` 表单布局样式优化 ([4c7894b](http://172.25.21.141/frontend/ecp-ui-plus/commit/4c7894baaf2d7e4804a123a8bb390dc628c8af67))
- `theme-chalk` ecp-empty、ecp-icon、ecp-label-item 等组件样式优化 ([9f9365c](http://172.25.21.141/frontend/ecp-ui-plus/commit/9f9365c3e8a0bc185dbbd066ad39761caa28ebf8))

### 📝 Documentation Changes | 文档更新

- `DSL` 描述文件初始化 ([800b4f5](http://172.25.21.141/frontend/ecp-ui-plus/commit/800b4f59bc602a96d55bbbf66004225fcbb8217d))
- `DSL` 描述文件更新 ([70e15b0](http://172.25.21.141/frontend/ecp-ui-plus/commit/70e15b034cc2c74f654ff716462de5103720c457))
- 文档、文档示例代码更新，配置格式化处理 ([5be8839](http://172.25.21.141/frontend/ecp-ui-plus/commit/5be88390f9928f146a0b473fdb3e24a60645ce23))
- 文档示例更新，添加 ecp-panel 吸附示例 ([5ad89fd](http://172.25.21.141/frontend/ecp-ui-plus/commit/5ad89fd6cfe7dc22f415da7c307fbe7332cba247))
- 许可协议修正 ([41dbac7](http://172.25.21.141/frontend/ecp-ui-plus/commit/41dbac76ff3c2027b73e32e0705f474414cd61d5))
- ecp-card文档更新 ([cd51797](http://172.25.21.141/frontend/ecp-ui-plus/commit/cd517971c5ea7b650f4e7ef3fd9eee7b292379c0))
- tabs 文档示例更新 ([0968be7](http://172.25.21.141/frontend/ecp-ui-plus/commit/0968be72cb9a6116e3ca08259dbd0320f399429a))

## (2025-04-10)

### 🐛 Bug Fixes | Bug 修复

- `components` 修复 ecp-button-group hideAfterClick 参数未生效的 bug ([fd0208b](http://172.25.21.141/frontend/ecp-ui-plus/commit/fd0208b92bd134942266d12ced17493d0eb767ff))

## (2025-03-29)

### 🚀 Performance Improvements | 性能优化

- `components` transfer-tree 优化 ([d7a3510](http://172.25.21.141/frontend/ecp-ui-plus/commit/d7a351051ebd9d7fd9d9127f41ac31ad8f6ecf41))

## (2025-03-28)

### 🚀 Performance Improvements | 性能优化

- 去除不必要的打印，数据处理减少cloneDeep使用 ([6e03694](http://172.25.21.141/frontend/ecp-ui-plus/commit/6e03694f86c17360e2897e38608878d60ed7a4cc))

### 🐛 Bug Fixes | Bug 修复

- `components` 修复 layout-pagination small参数未生效的 bug，修复 pagination 自定义插槽未生效的 bug ([8e08536](http://172.25.21.141/frontend/ecp-ui-plus/commit/8e08536b3367460b1bf1f8af71402d3df8f8f92f))

### 📝 Documentation Changes | 文档更新

- pagination、layout-pagination 文档修正 ([087af09](http://172.25.21.141/frontend/ecp-ui-plus/commit/087af09a06b7b725da2cdff0733a0f32009615ae))

## (2025-02-23)

### ✨ Features | 新功能

- `components` `composables` `constants` `utils` ecp-import-dialog 默认上传方法修改为使用原生xhr，文件处理相关方法补充 ([da2c87f](http://172.25.21.141/frontend/ecp-ui-plus/commit/da2c87f17f6b55da99fb05431df73fdd38ad65a5))
- `components` `theme-chalk` `composables` `constants` `utils` 添加 ecp-import-dialog 导入弹窗组件与相关全局配置，添加文件相关常量与处理方法 ([112805e](http://172.25.21.141/frontend/ecp-ui-plus/commit/112805ed916b8a2954f70c71467e569c450a5dd2))
- `utils` Helper 常用辅助方法添加fillTemplate、getDeepValue等方法 ([0b267bd](http://172.25.21.141/frontend/ecp-ui-plus/commit/0b267bd6ac4df2eae5323162d715d8e713660433))

### 🐛 Bug Fixes | Bug 修复

- `micro-app` 修复子应用 popper 位置有误的bug ([4abd866](http://172.25.21.141/frontend/ecp-ui-plus/commit/4abd866fcde30a860329a6bf3e5e78dac749171a))
- `micro-app` 修复子应用路由链接更新后浏览器地址栏未更新的bug，wujie-polyfill升级并添加部分可用插件 ([ab8b091](http://172.25.21.141/frontend/ecp-ui-plus/commit/ab8b091a37de4cd22965490066f8c9e220db2d8c))

### 📝 Documentation Changes | 文档更新

- 添加 Mime 文档类型、FileUtils 常用文件处理方法等，更新 UseConfig 全局配置、Helper 常用辅助方法等 ([29718bf](http://172.25.21.141/frontend/ecp-ui-plus/commit/29718bf72cf5b3b706b4c26fd12d9dfbb33cdc23))
- FileUtils 文档展示优化 ([1baefec](http://172.25.21.141/frontend/ecp-ui-plus/commit/1baefeca7a0bdad0dfde7f9182802daa60cb5f20))
- Helper 示例更新，添加 ecp-import-dialog 导入弹窗组件文档 ([8ee1ceb](http://172.25.21.141/frontend/ecp-ui-plus/commit/8ee1ceb46d07ad0a1da189edcbaee543a1a71751))

## (2025-01-16)

### 🐛 Bug Fixes | Bug 修复

- `components` button-group 去除二字按钮加空格处理 ([c277352](http://172.25.21.141/frontend/ecp-ui-plus/commit/c277352cfeadd5eb34ff0919bad0fed9b6d1d144))

### ✨ Features | 新功能

- `components` `theme-chalk` 树形穿梭选择组件拆分为 EcpTransferTree 本体选择组件与 EcpTransferTreeDialog 弹窗选择组件 ([a303ea9](http://172.25.21.141/frontend/ecp-ui-plus/commit/a303ea9ac052f891832f180cfecf5535de351400))
- `components` `theme-chalk` 添加 ecp-mark-text 文本标记组件 ([4e80044](http://172.25.21.141/frontend/ecp-ui-plus/commit/4e80044c8eaf6bc2ca6efc0055b57d36a7b13be0))
- `components` `theme-chalk` 增加树形穿梭选择弹窗EcpTransferTreeDialog ([044619e](http://172.25.21.141/frontend/ecp-ui-plus/commit/044619e32de80f4d2e3b78359a4088da13d7d32a))
- `directives` 点击波纹指令优化 ([e00de3b](http://172.25.21.141/frontend/ecp-ui-plus/commit/e00de3b23c7207bd230b9d605ef1dc7b93c4f8de))
- `theme-chalk` element-plus 版本升级至 ^2.9.0, sass 版本升级至 ^1.70.0, sass:color 使用调整 ([a194eb1](http://172.25.21.141/frontend/ecp-ui-plus/commit/a194eb1c2a633076ad46cbc24b9b2d8db01d8c01))
- `theme-chalk` sass:color、sass:map、sass:list 使用调整 ([8a4659b](http://172.25.21.141/frontend/ecp-ui-plus/commit/8a4659b06e3021b0d44b63e35179e6c54c3d2d52))
- `utils` Helper 常用辅助方法更新 ([900025c](http://172.25.21.141/frontend/ecp-ui-plus/commit/900025cb0b8dc9fec3313b09b41b804099e24e21))

### 📝 Documentation Changes | 文档更新

- 文档主题更新，树形穿梭选择组件文档更新 ([8390888](http://172.25.21.141/frontend/ecp-ui-plus/commit/8390888f52b4a522173f017e7eaf75f008f418d6))
- v-ripple、Helper等示例更新，添加 ecp-mark-text 文本标记组件文档 ([c9e0817](http://172.25.21.141/frontend/ecp-ui-plus/commit/c9e081753ef69296ad0718783d89d215c6b396b6))

## (2024-12-03)

### 🐛 Bug Fixes | Bug 修复

- `micro-app` 去除 debugger ([2c7d188](http://172.25.21.141/frontend/ecp-ui-plus/commit/2c7d1886898c373f75a89c636bfa6a0fa3e9ac10))

### ✨ Features | 新功能

- `components` `theme-chalk` 添加悬浮按钮组件 ([580fa49](http://172.25.21.141/frontend/ecp-ui-plus/commit/580fa498fccb21e89d4c7a0b7412513802452e50))
- `theme-chalk` 样式目录结构调整，ecp-layout-pagination 去除样式单独引入组件 ([1a713de](http://172.25.21.141/frontend/ecp-ui-plus/commit/1a713def9e9d8eb96d3e13e5aa5316224ed7b0a6))
- `theme-chalk` 主题变量 WebComponent 嵌入优化，Tabs 样式优化 ([4268d70](http://172.25.21.141/frontend/ecp-ui-plus/commit/4268d70c97b779939e4851fbf27e0791d27bee93))

### 📝 Documentation Changes | 文档更新

- 历史版本更新日志剥离 ([2f3b492](http://172.25.21.141/frontend/ecp-ui-plus/commit/2f3b49208f03af5ae6eef3ff1009f1c95c7aff84))
- 添加悬浮按钮组件文档 ([745accc](http://172.25.21.141/frontend/ecp-ui-plus/commit/745acccdba6cf0661991f7b1e17b743059caadca))

## (2024-11-27)

### ✨ Features | 新功能

- `components` `composables` `theme-chalk` 抽离图片操作栏组件，图片预览、图片裁剪等组件统一使用图片操作栏组件，并对齐操作栏属性 ([2ff4869](http://172.25.21.141/frontend/ecp-ui-plus/commit/2ff48695f776b5d3e0e62555ca8cc9037ee7680b))
- `components` `theme-chalk` ecp-img-view 基础图片预览组件传参进行显隐默认的工具，并支持鼠标悬停显隐工具栏功能 ([5c699b5](http://172.25.21.141/frontend/ecp-ui-plus/commit/5c699b55b913912843c97d9c716631fa92feabf9))
- `micro-app` 添加 MicroEvent 应用通信方法与相关常量枚举，HistoryApp、route-app-component等通信改造 ([b38c184](http://172.25.21.141/frontend/ecp-ui-plus/commit/b38c184ad8634321ba77d2bf72dee1e091674b42))
- `micro-app` PortalTabsActions 实例添加 getPresetLists 获取当前预设列表方法 ([6ed9edb](http://172.25.21.141/frontend/ecp-ui-plus/commit/6ed9edb8315803e330466b315e1b09a20d2c38f6))
- `utils` Helper 常用辅助方法优化 ([5a3cc0e](http://172.25.21.141/frontend/ecp-ui-plus/commit/5a3cc0eb7ef4de195a0da76883a9f94fe570dfee))

### 🐛 Bug Fixes | Bug 修复

- `components` 修复 ecp-icon 使用 ElementIcon 不能响应原生事件的 bug ([e5e8ebf](http://172.25.21.141/frontend/ecp-ui-plus/commit/e5e8ebf7f4efab8fddf0f6652e95ad310451676e))
- `components` 修复 EcpPreviewImg 打开弹窗处理有误的bug ([a4c9f66](http://172.25.21.141/frontend/ecp-ui-plus/commit/a4c9f664bfcc6846048ac796513160956e1c6f53))
- `components` 修复 EcpPreviewImg 打开弹窗回调有误的bug ([63b3777](http://172.25.21.141/frontend/ecp-ui-plus/commit/63b3777711a62527bf0b2375b55d06a31c3af53d))

### 📝 Documentation Changes | 文档更新

- 添加 MicroEvent 应用通信方法与相关常量枚举文档，相关微前端文档更新 ([a712ba3](http://172.25.21.141/frontend/ecp-ui-plus/commit/a712ba36588783ea9f9331905e92984f14569b12))
- 添加图片操作栏组件文档，图片预览、图片裁剪等组件文档更新 ([3df0044](http://172.25.21.141/frontend/ecp-ui-plus/commit/3df0044edd6e1205df70930e53de0a4e477430bc))
- 文档修正 ([6a56f75](http://172.25.21.141/frontend/ecp-ui-plus/commit/6a56f75f2e6b18dc9ea4b095a732756ce33a7392))

## (2024-09-30)

### ✨ Features | 新功能

- `micro-app` portal-tabs 抛出 PortalTabsActions 实例，PortalTabsActions.remove 添加移除操作配置 ([53f2ffd](http://172.25.21.141/frontend/ecp-ui-plus/commit/53f2ffdb700b95cb305435df2c17cbee1b71d484))
- `theme-chalk` 样式更新、修正 ([231d169](http://172.25.21.141/frontend/ecp-ui-plus/commit/231d16974e727f4de05e8387436dfb3ee871e1b9))
- `utils` Helper 常用辅助方法 ([e6b37bb](http://172.25.21.141/frontend/ecp-ui-plus/commit/e6b37bb3f4526acf6d95f3aaf992ceaf3c89d3be))

### 📝 Documentation Changes | 文档更新

- 文档更新、修正 ([ba59a70](http://172.25.21.141/frontend/ecp-ui-plus/commit/ba59a70e1c195c62e33e4629b8d1e955d2af0fef))

## (2024-08-19)

### ✨ Features | 新功能

- `components` `theme-chalk` card 展示优化 ([73b0eda](http://172.25.21.141/frontend/ecp-ui-plus/commit/73b0eda873d6ff90699f88ebd9a01d3e6295ed70))
- `components` `theme-chalk` img-view、preview-img-content、preview-img 等组件添加按钮区域插槽，展示优化 ([01de33a](http://172.25.21.141/frontend/ecp-ui-plus/commit/01de33af183afadc9bb401bdef34cb335034f502))
- `theme-chalk` 背景色、投影色变量调整，message、message-box、drawer、dialog、table、table-v2 等样式优化 ([e7d7007](http://172.25.21.141/frontend/ecp-ui-plus/commit/e7d7007bcf4a6fe4e66be8b9bba7be4dc8cd5480))

### 📝 Documentation Changes | 文档更新

- 文档主题调整，组件示例优化，table-v2 添加固定列示例 ([185c40b](http://172.25.21.141/frontend/ecp-ui-plus/commit/185c40b80b4a807ffa4dfc8f4e69eccbc3d0e47e))
- img-view、preview-img-content、preview-img 等添加按钮区域插槽示例 ([d50f4c0](http://172.25.21.141/frontend/ecp-ui-plus/commit/d50f4c0a6b59179f2f3b2f3a321fc51f2f219ecf))

## (2024-08-12)

### ⚠ BREAKING CHANGES

- `components` `composables` `micro-app` `theme-chalk` 组件库前缀修改，由 ecpr 修改为 ecpp

### 🎨 Code Refactoring | 代码重构

- `components` `composables` `micro-app` `theme-chalk` 组件库前缀修改，由 ecpr 修改为 ecpp ([6d90fb5](http://172.25.21.141/frontend/ecp-ui-plus/commit/6d90fb59cd87d63bb088f16b0887e785ab77b656))

### 📝 Documentation Changes | 文档更新

- 文档 ecpr 前缀修改为 ecpp ([80e34bb](http://172.25.21.141/frontend/ecp-ui-plus/commit/80e34bbeeef2d9100cbd63250a6333a6c8d46910))

## 历史版本

> - V1.0.0 以前的版本：[CHANGELOG-0.0.X](/ecp-ui-plus/docs/changelogs/CHANGELOG-0.0.X.html) 。
