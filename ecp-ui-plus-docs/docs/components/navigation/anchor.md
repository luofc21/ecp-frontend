<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/navigation/anchor.html -->

# <ecp-anchor> 锚点

> - 锚点组件的构成：导航栏 + 滚动内容体（自定义）；
>   - 两者是解耦的，导航栏通过 `parent` 属性传入滚动内容体的类名（className）或者 id 进行关联锚点定位。

## 基础用法

默认使用小圆点的锚点组件示例

`parent` 属性如果使用的类名要带上 '.'（如果是 id，则要带上 '#'）。提示：对应的类名或 id 样式中要有 overflow: auto 属性（即：内容体是可滚动的）。

## 使用滑块样式锚点

设置 `use-slide` 属性为 `true` 来使用滑块高亮。

## 导航列表内容自定义

通过 data 访问传进去的 menus-item 的数据。

## Attributes

| 参数 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| parent | 内容体的类名或 id（记得前面添加 '.'（'#'）） | string | -- | — |
| menus | 导航栏列表数据（跟内容体一一对应）[{label: '', value: ''}] | array | -- | — |
| activeMenu | 默认选中的导航数据，值为选中的数据项的value，如'.item-23' | string | -- |  |
| useSlide | 高亮使用滑块的样式（默认使用小圆点） | boolean | -- | false |
| offsetTop | 距离滚动区域顶部达到指定偏移量后触发 | boolean | -- | false |
| offsetBottom | 距离滚动区域底部达到指定偏移量后触发 | boolean | -- | false |
