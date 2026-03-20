<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/api/directives/v-zoomable.html -->

# v-zoomable 元素缩放

> 可以让元素在父级元素中任意缩放。

```vue
<div v-zoomable:[arg]="value"></div>
```

## 基础用法

## Arg

`String`

- 可选值：
  - disable 是否禁用缩放

## Value 的结构

| key | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| scale | `Array` | [1, Infinity] | 缩放范围 |
| cb | `Function` |  | 缩放回调 |
