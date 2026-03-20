<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/design/utilities.html -->

# Utilities 辅助类名

> 一些常用的样式辅助类

## 文本内容相关

| 样式类名/属性 | 说明 | 注意事项 |
| --- | --- | --- |
| empty-cell | 空数据占位符，默认展示 `--` | `ElTable` 与 `ElTableV2` 单元格已添加占位符处理， 一般无需再添加 `empty-cell`。 |
| --empty-cell-content | 空数据占位符展示文本 | 配合 `empty-cell` 使用 |
| app-ellipsis-text | 文本省略样式，默认展示 1 行 |  |
| --app-ellipsis-line | 文本展示行数 | 配合 `app-ellipsis-text` 使用 |

## 浮动相关

浮动、清除浮动

| 类名 | 说明 | 注意事项 |
| --- | --- | --- |
| fl | 左浮动 | -- |
| fr | 右浮动 | -- |
| clearfix | 清除浮动和margin溢出的影响 | -- |

## 颜色相关

使用主题变量生成的颜色类名

| 类名 | 说明 | 注意事项 |
| --- | --- | --- |
| link | color为 $--color-primary，链接的样式 | -- |
| success | color为 $--color-success | -- |
| warning | color为 $--color-warning | -- |
| danger | color为 $--color-danger | -- |
| success-bg | 背景为 $--color-success | -- |
| warning-bg | 背景为 $--color-warning | -- |
| danger-bg | 背景为 $--color-danger | -- |

## 显示隐藏

显示隐藏，注意hide、invisible的区别

| 类名 | 说明 | 注意事项 |
| --- | --- | --- |
| show | display: block | -- |
| hide | display: none | 不占文档空间 |
| invisible | visibility: hidden | 仍占据文档空间 |

## 块级、行内

display: inline/block/inline-block

| 类名 | 说明 | 注意事项 |
| --- | --- | --- |
| inline | 行内 | -- |
| block | 块级 | -- |
| inline-block | 行内块 | -- |

## 字体相关

font-weight、text-overflow

| 类名 | 说明 | 注意事项 |
| --- | --- | --- |
| fwn | 字体普通 | -- |
| fwb | 字体加粗 | -- |
| text-overflow | 单行文本溢出，显示省略号 | -- |

## 溢出处理

overflow: hidden/auto/visible

| 类名 | 说明 | 注意事项 |
| --- | --- | --- |
| oh | overflow: hidden | -- |
| oa | overflow: auto | -- |
| ov | overflow: visible | -- |
