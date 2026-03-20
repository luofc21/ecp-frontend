<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/layout/left-right-panel.html -->

# <ecp-left-right-panel> 左右分栏布局

> 左右分栏布局，可自由控制左右分栏的宽度。

## 基础用法

- 搭配el-menu使用, 响应展开与收起事件；
- width 属性可设置左右分栏宽度，默认值为 `auto` ，可传入 具体数值/像素/百分比。

## 可拖拽调整宽度

## 搭配上下布局组件使用

## 自由内容高度

## Attributes

| 参数 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| width | 左分栏区域宽度（单位 px） | number / string | -- | 'auto' |
| containerId | 左右分栏组件容器id，可用于区别同时存在多个左右分栏的情况 | string | -- | 'panelContainer' |
| dragAvailable | 左栏是否允许拖拽改变宽度 | boolean | -- | false |
| rightMinWidth | 左栏允许改变宽度时右栏的最小宽度 | number / string | -- | 200 |

## Slots

| 插槽名 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| left | 左分栏区域插槽 | string | -- | -- |
| default | 默认插槽（右分栏内容区域插槽） | string | -- | -- |
