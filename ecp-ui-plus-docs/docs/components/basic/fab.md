<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/basic/fab.html -->

# <ecp-fab> 悬浮按钮

## Attributes

| 参数 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| draggable | 是否可拖拽 | Boolean |  |  |
| teleportTo | Teleport 指定目标容器 | String / HTMLElement |  |  |
| bounding | 贴边临界数值，Array 类型的顺序同 CSS padding | Number / String / Array<Number> |  |  |
| absolute | 是否采用 absolute 定位 | Boolean |  |  |
| initPosition | 初始定位位置 | String | `top-left` `top` `top-right` `left` `right` `bottom-left` `bottom` `bottom-right` |  |

## Events

| 事件名称 | 说明 | 回调参数 |
| --- | --- | --- |
| done | 拖拽完成回调 | `String` 当前定位位置描述 |

## Slots

| 插槽名 | 说明 | 参数 |
| --- | --- | --- |
| default | 悬浮按钮内容 | { currentPosition: `String` 同 initPosition 可选值，可用于定制贴边状态样式 } |

## Exposes

| 方法/属性 | 类型 | 说明 | 入参 |
| --- | --- | --- | --- |
| fabWrapperRef | HTMLElementRef | 拖拽范围 |  |
| fabViewRef | HTMLElementRef | 拖拽容器 |  |
| formatBounding | ArrayRef | 格式化后的边界值 |  |
| snapAttrs | ObjectRef | 拖拽容器相关参数 |  |
| updatePositionManual | Function | 手动更新位置 | `String` 同 initPosition 可选值 |
