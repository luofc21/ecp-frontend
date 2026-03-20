<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/form/num-area.html -->

# <ecp-num-area> 数值范围输入框

> 提供一个数值范围组合式输入框。

## 基础用法

使用标签ecp-num-area进行创建,传入一个数组类型的变量进行回显数据。

说明：

1. 左右两侧必须是一个合理的数值范围：如果左侧输入10，右侧输入1，会自动变成左侧为1，右侧为10
2. input框内显示的值不会超过设置的最大最小值（maxNumber和minNumber）
3. 会去除所有空格符号
4. 必须输入数字，否则返回空串

## Attributes

| 参数 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| value/v-model | 传入当前标签值 value,v-model使用 vue 原生指令 v-model。 | Array | -- | [] |
| separator | 最大最小值之间的连接标识符 | String | -- | '至' |
| placeholder1 | 左侧最小值的占位描述值 | String | -- | '最小值' |
| placeholder2 | 右侧最大值的占位描述值 | String | -- | '最大值' |
| disabled | 是否禁用 | Boolean | -- | false |
| label | input框内左侧占位描述文案 | String | -- | '得分范围：' |
| minNumber | 最小值默认值, String类型仅支持数值格式的字符串 | Number/String | -- | Number.MIN\_SAFE\_INTEGER |
| maxNumber | 最大值默认值, String类型仅支持数值格式的字符串 | Number/String | -- | Number.MAX\_SAFE\_INTEGER |
| needParseInt | 是否需要取整 | Boolean | -- | false |

## Events

| 事件名称 | 说明 | 回调参数 |
| --- | --- | --- |
| change | 选中项变化时触发 | 变化后的选中项 |
