<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/navigation/pagination.html -->

# <ecp-pagination> 分页器

> - 基于 `ElPagination` 封装的分页器；
> - 只需关注传入数据和页码发生变化及相关回调，不用关注页数变化时需要调用的处理方法。

## 基础用法

列举现有规范的分页器。

## Attributes

| 参数 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| layout Global | 组件布局，子组件名用逗号分隔。由于产品规范，注意不要传 total！ | String | sizes, prev, pager, next, jumper, slot | 'prev, pager, next, jumper' |
| small Global | 是否使用小型分页样式 | Boolean | -- | false |
| total | 总记录数量，类型是 String 时需支持 parseInt | Number / String | -- | 0 |
| current-page Global / v-model:current-page | 当前页数 | Number | -- | 0 |
| page-size Global / v-model:page-size | 每页显示条目个数 | Number | -- | 10 |
| page-sizes Global | 每页显示个数选择器的选项设置 | number[] | -- | [10, 20, 30, 40, 50, 100] |
| pager-count Global | 页码按钮的数量，当总页数超过该值时会折叠 | Number | 大于等于 5 且小于等于 21 的奇数 | 5 |
| justify Global | 总记录数和分页器的布局 | String | 为样式 justify-content 的值。 | space-between |

## Events

| 事件名称 | 说明 | 回调参数 |
| --- | --- | --- |
| query | 页数更新时触发的查询方法 | -- |
| current-change | currentPage 改变时会触发 | 当前页 |

## Slots

| 插槽名 | 说明 |
| --- | --- |
| total | 总记录数量插槽 |
| custom | 自定义内容插槽，需要在 layout 中列出 slot |
