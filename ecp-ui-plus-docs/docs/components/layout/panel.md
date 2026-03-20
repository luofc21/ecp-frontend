<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/layout/panel.html -->

# <ecp-panel> 上下布局组件

> 基于 UI 规范定制的布局容器组件，上下布局（标题 + 内容）。

## 基础用法

> - 标题: 标题通过 title 属性传入。
> - 内容: 设置 slot="content" 来存放主体内容。
> - 底部: 设置 slot="footer" 来存放底部内容。

## 默认背景色

## 头部/底部插槽

> 复用类名: app-panel-content-wrapper, 多内容项并列排列时，各内容项容器用。注意不要与 border-white 一起用。

## 头部/底部吸附

## Attributes

| 参数 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| title | 头部区域标题 | string | -- | -- |
| interval | 是否添加内容区域边距 | boolean | -- | false |
| border-white | 用于设置背景色为白色的布局。高度默认： 内容体高度撑开的高度。 | string | -- | -- |
| full-height | 搭配 border-white 属性使用，用于固定内容高度为 100%。 | string | -- | -- |
| align | 底部区域布局 | string | right,left,center,start,end | right |

## Slots

| 插槽名 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| default | 默认插槽（内容区域） | string | -- | -- |
| content | 内容区域插槽名称（与默认插槽） | string | -- | -- |
| header | 头部区域插槽名称 | string | -- | -- |
| footer | 底部区域插槽名称 | string | -- | -- |

## Style Class

| 类名 | 说明 |
| --- | --- |
| app-panel-content-wrapper | 多内容项并列排列时，各内容项容器用 |
