<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/layout/query-row.html -->

# <ecp-query-row> 基础检索条件容器

> 针对列表中常见的基础检索业务，根据当前组件宽度动态展示对应数量的检索条件、支持更多/收起筛选检索条件。

## 基础用法

默认配置

## Attributes

| 参数 | 说明 | 默认值 | 类型 |
| --- | --- | --- | --- |
| showCollapse | 是否需要`更多/收起筛选` 按钮 | true | Boolean |
| baseLine | 默认展示几行基础检索 | 2 | Number |
| baseItemWidth | 检索容器每列的宽度 | 500 | Number |
| columns | [4,3,2,1] - 不同尺寸下显示几列（尺寸对应baseItemWidth的宽度乘以4、3、2、1，比如baseItemWidth为500时，此时 `>2000px=4列`，`>1500px=3列`，`>1000px=2列`，`<1000=1列`） | `[4,3,2,1]` | Array |

## Slots

| 插槽名 | 说明 |
| --- | --- |
| default | 默认插槽 |
| btns | 按钮组插槽，符合情况的条件下会自动补全 `更多/收起筛选` 按钮 |
