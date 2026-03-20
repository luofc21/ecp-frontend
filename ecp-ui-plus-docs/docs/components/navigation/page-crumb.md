<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/navigation/page-crumb.html -->

# <ecp-page-crumb> 页头面包屑

> 页头面包屑：用于子页面显示当前页面路径，可以调整到任意层级

## 基础用法

通过 callback 回调执行页面调整

当所有子页面均使用遮罩的方式显示时，通过callback关闭子页面。

## Attributes

| 参数 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| crumbData | 面包屑的对象数组 | Array<[crumbDataItem](#crumbdataitem-的结构)> | -- | -- |
| crumbProps | 自定义crumbData的属性key映射，可选属性key见[crumbDataItem 的结构](#crumbdataitem-的结构) | Object<String, String> | -- | -- |
| triggerOnly | 是否只执行当前回调，默认会链式执行回调 | Boolean | -- | -- |

### crumbDataItem 的结构

| key | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| key | 唯一标识 | String/Number | -- | -- |
| label | 显示文本 | String | -- | -- |
| only | 仅触发当前回调 | Boolean | -- | -- |
| disabled | 禁止触发 | Boolean | -- | -- |
| route | route 对象，router.push 的参数 | Object | -- | -- |
| callback | 点击执行的回调，推荐使用callback进行页面跳转，执行返回 Promise.reject 时会停止后续回调执行 | Async Function | -- | -- |

## Events

| 事件名称 | 说明 | 回调参数 |
| --- | --- | --- |
| close | 返回按钮的点击事件 | -- |
