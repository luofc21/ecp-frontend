<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/data/label-item.html -->

# <ecp-label-item> 文本组件

基于现有设计的文本快速布局结构

> 结构类似于 `label(文本 | icon) + value` 的文本，只需传如 label 和 value 即可，根据实际需求选择文本的布局和样式。

## 基础用法

创建通用的文本

> - 文本左右两边的值支持自定义。
> - 对齐: label 和 value 默认两边对齐，可以通过设置 justify 属性进行对齐方式的设置。
> - 分割线: 默认使用虚线分割，如需使用实线分割，需要设置 solid 属性。
> - 复用类名: 两列布局使用提供的全局样式类名：app-inline-card-item。

## Attributes

| 参数 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| icon | 卡片的文本内容区域，使用图标（内部使用的是 ecp-icon 的组件） | string |  |  |
| label | 卡片的文本内容区域 | string |  |  |
| text | 文本右边的值 | string |  |  |
| justify（后面会废弃） | 决定使用自定以的 label 和 text 的布局，使用的是 justify-content 属性（后面会废弃） | string |  | space-between |
| labelWidth | 文本左边的 label 内容的宽度（默认单位是 px） | string |  |  |
| align | 决定 text 的布局，使用的是 text-align 的属性 | string |  | right |
| title | 设置为标题样式 | string |  | right |

## Slots

| 插槽名 | 说明 | 注意事项 |
| --- | --- | --- |
| default | 文本内容 | -- |

## Style Class

| 类名 | 说明 |
| --- | --- |
| app-inline-card-item | 卡片两列布局的样式类名 |
