<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/layout/layout-pagination.html -->

# <ecp-layout-pagination> 翻页查询

> - 基于 `EcpPagination` 翻页组件封装的带翻页布局组件。
> - 组件结构：head + content(main + pagination)。

## 基础用法

## 展示头部分页

## 表体滚动，底部页脚固定

## 可搜索

创建可搜索的卡片列表

## 手动更新搜索关键词

调用组件实例的 updateSearch 方法，可以手动更新搜索关键词

## 列表总 total=0 时不展示分页器

## Attributes

| 参数 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| loading | 是否加载中 | Boolean | -- | false |
| top-pagination | 头部分页器是否展示 | Boolean | -- | true |
| footer-pagination | 底部分页器是否展示 | Boolean | -- | true |
| search | 可搜索，每次搜索，默认会将页码重设为 1 | Boolean | -- | false |
| search-keywords | search 为 true 有效，搜索框的关键词 | String | -- | '' |
| search-placeholder | search 为 true 有效，搜索框的默认显示文本 | String | -- | '请输入关键字查询' |
| clearable | 检索是否支持可清空 | Boolean | -- | true |
| content-scroll | 用于设置内容体滚动，底部页脚固定的样式布局 | Boolean | -- | false |
| loadingText | loading时需要展示的文案，默认不展示 | String | -- | -- |
| loadingCount | loading时读秒，默认不开启，如果设置了loadingText也不会开启 | Boolean | -- | false |
| ... | 其它支持参数，见 [<ecp-pagination> 分页器](/ecp-ui-plus/docs/components/navigation/pagination.html) | ... | ... | ... |

## Events

| 事件名称 | 说明 | 回调参数 |
| --- | --- | --- |
| query | 页数更新时触发的查询方法 | -- |
| current-change | currentPage 改变时会触发 | 当前页 |
| search-change | searchKeywords 改变时会触发 | 当前搜索词 |

## Slots

| 插槽名 | 说明 |
| --- | --- |
| default | 默认插槽 |
| content | 主体插槽，可以用表格或卡片等形式，同 default |
| head | 头部插槽，翻页按钮左侧的内容，如按钮、查询框等 |
| total | 总记录数量插槽 |
| custom | 自定义内容插槽，需要在 layout 中列出 slot |

## Exposes

| 方法/属性 | 说明 | 入参 |
| --- | --- | --- |
| updateSearch | 在 search 为 true 时可用，需要手动更新搜索的输入值时，可以调用此方法更新 | keyword 需要更新的输入值； query 是否查询更新，默认为 false，不查询 |
