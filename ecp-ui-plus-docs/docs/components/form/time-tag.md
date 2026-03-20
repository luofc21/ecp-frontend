<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/form/time-tag.html -->

# <ecp-time-tag> 时间标签筛选器

> 时间标签筛选器

## 基础用法

创建一个时间标签筛选器

注意：

1. key 值约定(见参数说明)；
2. 需要拓展时间项时需要定义isExpand 和 logicFns，其中 isExpand 为 true，默认是false, logicFns 是拓展项对应的时间值计算逻辑。

## Attributes

| 属性名 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| label | 当前标签组的 label | string |  | -- |
| list | 时间日期标签列表；数组数据项见 [listItem 的结构](#listitem-的结构) | Array<listItem> |  | -- |
| format | 需要回传的日期格式 | string |  | -- |
| v-model | 传入当前标签值value，使用vue原生指令v-model。 | string |  | -- |
| pickerOptions | 自定义时间开启时，时间日期选择器支持的其它选项，见 [ElementPlus - DatePicker 属性](https://element-plus.gitee.io/zh-CN/component/date-picker.html#%E5%B1%9E%E6%80%A7) | Object |  | {} |

### listItem 的结构

| 属性名 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| label | 当前标签项的label | string | -- | -- |
| key | 当前标签项的key，当传入label值为类似‘近3天‘时，key**必须**要命名为 `${number}days`(例如：3days，15days)，才能正确计算时间 | string | 'today(今天)/yesterday(昨天)/before-yesterday(前天)/this-week(本周)/this-month(本月)/this-year(本年)/custom(自定义) | -- |
| isExpand | 是否拓展项，为true时使用logicFns生成时间，扩展项使用方法见示例 | boolean | -- | -- |
| logicFns | 用于生成拓展项的时间，使用方法见示例 | function | -- | -- |

## Events

| 方法名 | 说明 | 返回值 |
| --- | --- | --- |
| change | 时间变化时触发，初始化时也会触发 |  |

## Exposes

| 方法/属性 | 说明 | 入参 | 返回值 |
| --- | --- | --- | --- |
| getTimeArray | 获取当前日期时间值，通过 $refs.getTimeArray 访问获取 | - | [startTime, endTime] |
