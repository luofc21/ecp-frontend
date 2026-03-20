<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/data/table-v2.html -->

# Virtualized Table 虚拟化表格 beta

> - 在 `ElTableV2` 的基础上作样式重置。
> - `ElTableV2` 只做了行优化，未做列优化。
> - **请勿**将 `scroll-behavior: smooth;` 添加至 `.#{$namespace}-table-v2` 和 `.#{$namespace}-vl__wrapper`。
> - 在 SSR 场景下，您需要将组件包裹在 `<client-only></client-only>` 之中 (如: [Nuxt](https://nuxt.com/v3)) 和 SSG (例如: [VitePress](https://vitepress.vuejs.org/)).

## 基础用法

让我们演示虚拟化表的性能，用10列和1000行渲染一个基本示例。

## 自动调整大小

如果不想手动向表格传递 `width` 和 `height` 属性，可以使用 AutoResizer 对表格组件进行封装。 这会自动为你更新宽度和高度。

尝试调整您的浏览器大小来看看它是如何工作的。

TIP

由于 `AutoResizer` 组件的默认高度是 100%，所以请确保该组件的父元素**拥有固定的高度值**。 或者，您可以通过将 `style` 属性传递到 `AutoResizer` 来定义它。

## 固定列表格

如果您想要有列粘贴左侧或右侧的某种原因。 您可以通过向表中添加特殊属性来实现这一点。

您可以设置该行的 `fixed` 属性为 `true` （代表 `FixedDir.LEFT`）、`FixedDir.LEFT` 或 `FixedDir.RIGHT` 。

## 更多

> 详见 [ElementPlus - Virtualized Table 虚拟化表格](https://element-plus.gitee.io/zh-CN/component/table-v2.html)
