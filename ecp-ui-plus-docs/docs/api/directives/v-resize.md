<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/api/directives/v-resize.html -->

# v-resize 尺寸监听

> 元素尺寸变化监听，参考 [ResizeObserver](https://developer.mozilla.org/zh-CN/docs/Web/API/ResizeObserver) 。

```vue
<div v-resize="onResize"></div>
```

## 基础用法

## Value

`Function` 回调函数，回调参数 `<ResizeObserverEntry>` 结构如下：

| key | 类型 | 说明 |
| --- | --- | --- |
| borderBoxSize | `Array<ResizeObserverSize>` | CSS 中定义的边框区域的大小 |
| contentBoxSize | `Array<ResizeObserverSize>` | CSS 中定义的内容区域的大小 |
| contentRect | `DOMRectReadOnly` | 变化后的内容区域尺寸息 |
| devicePixelContentBoxSize | `Array<ResizeObserverSize>` | 在对元素或其祖先应用任何 CSS 转换之前，CSS 中定义的内容区域的大小，以设备像素为单位 |
| target | `HTMLElement` / `SVGElement` | 监听的元素 |
