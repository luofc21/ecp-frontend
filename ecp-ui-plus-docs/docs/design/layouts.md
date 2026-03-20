<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/design/layouts.html -->

# Layouts 布局类名

> 一些常用的布局样式类名（均以 app- 为前缀）

## 表单相关

| 类名 | 说明 | 注意事项 |
| --- | --- | --- |
| app-form | 单列表单 | -- |
| app-form-inline | 两列表单 | 需要同时配合 app-form 使用 |
| app-form-three-column | 三列表单 | 需要同时配合 app-form 使用 |
| app-form-vertical | 效果：文本 与 输入框 垂直展示 | 需要同时配合 app-form 使用 |
| app-search-form | 用于检索表单 | 比 app-form 更紧凑，会在 label 后添加冒号 |
| interval | 在 app-search-form 上加内边距 | 需要同时配合 app-search-form 使用 |
| app-submit-form | 用于提交表单 | 比 app-form 更紧凑，会在 label 后添加冒号 |

## 图片容器相关

| 类名 | 说明 | 注意事项 |
| --- | --- | --- |
| app-sized-image | 以指定比例展示图片容器 | -- |
| app-sized-image--16-9 | (横向) 宽高比 16:9 | 需要同时配合 app-sized-image 使用 |
| app-sized-image--3-2 | (横向) 宽高比 3:2 | 需要同时配合 app-sized-image 使用 |
| app-sized-image--4-3 | (横向) 宽高比 4:3 | 需要同时配合 app-sized-image 使用 |
| app-sized-image--9-16 | (纵向) 宽高比 9:16 | 需要同时配合 app-sized-image 使用 |
| app-sized-image--2-3 | (纵向) 宽高比 2:3 | 需要同时配合 app-sized-image 使用 |
| app-sized-image--3-4 | (纵向) 宽高比 3:4 | 需要同时配合 app-sized-image 使用 |
| app-sized-image--1-1 | 宽高比 1:1 | 需要同时配合 app-sized-image 使用 |

## 卡片相关

| 类名 | 说明 | 注意事项 |
| --- | --- | --- |
| app-card-buttons | 卡片 footer 插槽使用操作按钮组时的样式 | -- |

## 文本布局相关

> ecp-label-item 组件

| 类名 | 说明 | 注意事项 |
| --- | --- | --- |
| app-inline-card-item | 文本两列布局样式 | -- |

## 步骤条相关

> el-steps 组件

element-ui 的 steps 步骤条组件只有现有设计规范中的小号步骤条，如需使用中等步骤条只需通过添加下面的全局类名即可。

| 类名 | 说明 | 注意事项 |
| --- | --- | --- |
| app-steps-medium | 中等步骤条 | -- |
