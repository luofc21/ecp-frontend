<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/form/sort-group.html -->

# <ecp-sort-group> 排序组件

> 排序组件

## 基础用法

创建一个排序组件

排序组件每个按钮默认有三种状态（空`''`，升 `ASC`，降 `DESC`），如果不需要使用‘空’状态则可以通过设置 `use-empty` 为 `false`。设置默认排序可以通过使用 `default` 进行设置 `sortType` 和 `sortOrder` 来分别指定要使用的排序按钮和排序的状态。

## Attributes

| 参数 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| list | 排序按钮组（格式严格按照 [{type: '', name: ''}]传入） | Array | -- |
| default | 设置需要初始化时默认选中的排序按钮和方式（格式严格按照 [{sortType: '', sortOrder: ''}]传入） | Object | -- |
| use-empty | 关闭使用‘空’状态。（默认状态：空`''`，升 `ASC`，降 `DESC`） | Boolean | true |

## Events

| 事件名称 | 说明 | 回调参数 |
| --- | --- | --- |
| change | 排序按钮改变或者排序方式改变时触发 | 当前排序按钮传入的 type 和 排序方式({sortType, sortOrder} ) |

## Exposes

| 方法/属性 | 说明 | 入参 |
| --- | --- | --- |
| clearSort | 清空排序选中状态 |  |
| setSortType | 设置当前排序方法，传入两个参数：(排序的类型(type)，排序的方式（升、降、空）) |  |
| setDisabledSorts | 设置排序按钮为不可用，需要使用`list`中的`type`属性 | (types) 接收需要设置为不可用的按钮数组 |
