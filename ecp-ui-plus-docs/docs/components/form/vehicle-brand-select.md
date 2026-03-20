<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/form/vehicle-brand-select.html -->

# <ecp-vehicle-brand-select> 车辆品牌选择器

> 车辆品牌选择器

## 基础用法

创建一个车辆品牌选择器，目前组件数据为静态数据

可结合多标签展示器组件使用

## Attributes

| 参数 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| multiple | 是否多选 | Boolean |  | true |
| showOperationBtns | 是否需要操作按钮，需要操作按钮时选中的品牌只有在点击确定时才会触发brands-change事件 | Boolean |  | true |

## Events

| 事件名称 | 说明 | 回调参数 |
| --- | --- | --- |
| brands-change | 品牌变化事件，有操作按钮时选中的品牌只有在点击确定时才会触发brands-change事件，无操作按钮时会实时触发 | 选中的品牌数组，每一项都是{ platename: 车辆品牌名, platecode: 车辆品牌编码 }的格式 |

## Exposes

| 方法/属性 | 说明 | 入参 |
| --- | --- | --- |
| removeAllBrands | 移除所有已选中的品牌 |  |
| removeBrand | 移除所有单个选中的品牌 | 品牌编码 |
| selectBrands | 预选中某个品牌列表，全量地，多选时全部选中，单选时只会选中数组中第一项 | 品牌编码数组 |
