<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/data/empty.html -->

# <ecp-empty> 空状态

> 当没有数据的时候页面填充的空状态图标和文案。

## 基础用法

## 带标题

## 自定义尺寸

## 颜色自定义

## 使用插槽

## Attributes

| 参数 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| empty-title | 显示的文本标题 | string |  |  |
| empty-text Global | 显示的文本内容 | string |  | '暂无数据' |
| color Global | 图标与文本颜色 | string |  | var(--ecpp-empty-color)，默认 `#C3CBD6` |
| fillColor Global | 图标填充颜色 | string |  | var(--ecpp-empty-fill-color)，默认 `#FFFFFF` |
| fillOpacity Global | 图标填充透明度 | string |  | var(--ecpp-empty-fill-opacity)，默认 `0.1` |
| size Global | 显示的图标大小，  也可传入自定义 px，  选 small 时会相应缩小字体 | string | small / medium / large | medium |

## Slots

| 插槽名 | 说明 |
| --- | --- |
| icon | 图标插槽 |
| title | 文本标题插槽 |
| text | 文本内容插槽 |
| footer | 脚注插槽 |
