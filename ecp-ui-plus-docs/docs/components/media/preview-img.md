<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/media/preview-img.html -->

# Preview-img 图片预览弹窗

## 基础用法

下面列举现有图片组件支持的布局，示例中有图片标注的简单使用。

- 图片布局组件主要由三部分组成：
  - 图片区域
  - 轮播图（可选），可与任意一组比例进行搭配
  - 文本（可选）。
- 图片布局由 type 属性决定，支持由：16:9、3:4、1:1组合构成的布局。

## Attributes

| 参数 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| show / v-model:show | 用于控制弹窗展示关闭 | String |  |  |
| title | 标题 | String |  |  |
| append-to-body | Dialog 自身是否插入至 body 元素上 | Boolean |  | false |
| modal | 是否展示需要遮罩层 | Boolean |  | true |
| modal-append-to-body | 遮罩层是否插入至 body 元素上 | Boolean |  | true |
| close-on-click-modal | 是否可以通过点击 modal 关闭 Dialog | Boolean |  | true |
| ... | 其它支持参数，见 [Preview-img-content 多图预览 - Attributes](/ecp-ui-plus/docs/components/media/preview-img-content.html#attributes) | ... |  |  |

## Events

| 事件名称 | 说明 | 回调参数 |
| --- | --- | --- |
| open | 弹窗打开事件 |  |
| opened | 弹窗打开动画完成事件 |  |
| close | 弹窗关闭事件，用于自主控制弹窗关闭 |  |
| closed | 弹窗关闭动画完成事件 |  |
| ... | 其它支持事件，见 [Preview-img-content 多图预览 - Events](/ecp-ui-plus/docs/components/media/preview-img-content.html#events) | ... |

## Slots

| 插槽名称 | 说明 |
| --- | --- |
| content | 同 `default`，底部内容区域插槽，回传当前数据项：imgData，该信息是用户传入的 |
| ... | 其他插槽同 [<ecp-preview-img-content> 多图预览 - Slots](/ecp-ui-plus/docs/components/media/preview-img-content.html#slots) |
