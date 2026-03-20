<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/form/tag.html -->

# <ecp-tag> 标签型选择器

> 多用于简单数据筛选。

## 基础用法

## Attributes

| 参数 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| label | 当前标签的 title | String | -- |
| v-model | 传入当前标签值 value,使用 vue 原生指令 v-model。 | String/Number/Array | -- |
| multiple | 多选模式。 | Boolean | false |
| options | 标签列表数组，数据格式严格要求为：[{label: String/Number, value: String/Number, disabled: Boolean}], disabled为可选项，表示该标签不可点击 | Array | -- |

## Events

| 事件名称 | 说明 | 回调参数 |
| --- | --- | --- |
| change | 标签改变时触发 | 当前标签v-model的值和点击的标签对象 |
