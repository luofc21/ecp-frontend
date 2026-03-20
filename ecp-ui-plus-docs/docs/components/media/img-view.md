<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/media/img-view.html -->

# <ecp-img-view> 图片预览

> 提供图片预览、鼠标滚轮缩放、旋转、拖拽等功能。

## 基础用法

## 展示图片标注

使用插槽img-tips可以在图片上展示内容，提供 imgInfo 图片信息，同时会抛出 img-info 事件。

## 自由搭配

> - `zoomOut`、`zoomIn`、`reset`、`counterclockwise`、`clockwise`、`download` 等按钮已内置处理，不会再抛出按钮点击事件；
> - 自定义图标按钮的点击事件，在 <ecp-image-toolbar> 的基础上添加 imgInfo 图片信息；
> - 具体使用，见 [Image-toolbar 图片操作栏 - 自由搭配](/ecp-ui-plus/docs/components/layout/image-toolbar.html#自由搭配)。

## 使用按钮插槽

> - 按钮插槽在 <ecp-image-toolbar> 的基础上添加 imgInfo 图片信息。

## 开启悬停显示图片操作栏

使用 `icon-show-by-hover` 可以开启鼠标悬停显示图片操作栏功能。

## Attributes

| 参数 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| imgUrl | 图片片链接 | String |  |
| download-method | 下载方法，参数为图片url，不传时默认使用 Blob 下载 | Function |  |
| zoom-rate | 缩放速率 | Number | 0.2 |
| move-rate | 移动速率 | Number | 1.5 |
| icon-show-by-hover | 是否开启鼠标悬停显示工具按钮 | Boolean | false |
| ... | 操作栏相关属性见 [Image-toolbar 图片操作栏 - Attributes](/ecp-ui-plus/docs/components/layout/image-toolbar.html#attributes) | ... | ... |

## Events

| 事件名称 | 说明 | 回调参数 |
| --- | --- | --- |
| change | 图片切换的回调事件，返回 | index, imgObject |
| img-info | 图片信息回传 | 图片信息 imgInfo |
| click-icon | 图片操作按钮点击事件 | 图片信息 imgInfo，其它回调参数见 [Image-toolbar 图片操作栏 - Events](/ecp-ui-plus/docs/components/layout/image-toolbar.html#events) |

## Slots

| 插槽名称 | 说明 |
| --- | --- |
| img-tips | 图片 tips 插槽，回传当前图片大小的信息：imgInfo。 |
| buttons-prepend | 按钮前缀插槽，回传当前图片大小的信息：imgInfo。 |
| buttons | 按钮后缀插槽，回传当前图片大小的信息：imgInfo。 |
