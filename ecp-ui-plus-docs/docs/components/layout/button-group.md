<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/layout/button-group.html -->

# <ecp-button-group> 按钮组

> 基于UI规范 封装表格中行的按钮组。
>
> - 表格中的按钮数超过3时（在表格头部的按钮数超过4时），通过“更多”展示剩余按钮。

警告：

- 按钮组中的按钮，请**使用 `ecp-button`** ，**不要使用 `el-button`** ！
- 组件会对 button 的 type、text、icon、plain 等属性和 click 事件，有一定的侵入，以强制适配UI规范。

## 基础用法

## 配合卡片使用

## 自定义 ui

## Attributes

| 参数 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| limit | 显示的数量 | number | -- | 3 |
| type | 使用场景类型 | string | button/text/card | text |
| size | 统一管理按钮组中按钮的大小 | string | default / large / small （同 el-button 的 size） | --（默认根据type自动设置） |
| primary-first | 第一个按钮是否设置"primary"，仅type="button"有效 | boolean | true/false | false |
| icon-strict | 严格按照UI规范显示按钮图标（type=button第一个有图标后面没有图标、type=text清除所有icon） | boolean | true/false | true |
| ui-strict | 严格按照UI规范控制按钮样式，设为false时组件将不做属性侵入（包括icon） | boolean | true/false | true |
| hide-after-click | 点击按钮后隐藏更多的弹出层 | boolean | true/false | true |
| trigger | “更多”按钮触发方式 | Number | 见 [Popover Attributes](https://element-plus.gitee.io/zh-CN/component/popover.html#attributes) | hover |
| placement | 出现位置 | String | 见 [Popover Attributes](https://element-plus.gitee.io/zh-CN/component/popover.html#attributes) | bottom-start |
| visible-arrow | 是否显示 Tooltip 箭头 | Boolean | -- | false |
| ... | 更多下拉参数见 [ElementPlus - Popover Attributes](https://element-plus.gitee.io/zh-CN/component/popover.html#attributes) | -- | -- | -- |

## Slots

| 插槽名 | 说明 |
| --- | --- |
| more-button | “更多”按钮，替换默认的“更多”按钮 |
