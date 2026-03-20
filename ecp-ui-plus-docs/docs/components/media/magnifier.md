<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/media/magnifier.html -->

# <ecp-magnifier> 图片放大镜

> 鼠标移入图片的放大效果。

## 基础用法

图片放大镜效果

- magnify 控制开启/关闭放大镜效果；
- scale 指定放大的倍数；
- magnifierWidth、magnifierHeight 指定放大镜效果展示区域的宽高；
  - 若都不指定，则宽度默认为480px，高度通过计算，与本组件的宽高比相同；
  - 当只指定 magnifierWidth 或 magnifierHeight 中其中一个时，其高度或宽度则也通过计算，与本组件的宽高比相同；
- 触发放大镜效果时默认不允许滚动，可设置 allowScroll 允许滚动。

## 自定义图片放大镜展示效果

可动过关闭默认展示效果，通过事件回调处理

- 指定 showMagnifier 为 false ，可关闭默认放大镜展示效果。
- 监听 mouseenter，mousemove，mouseleave 事件及其抛出的回调参数，自行处理展示效果。

## 图片裁切

开启图片裁切效果

- clip 控制开启/关闭裁切效果；
- clipProps 指定裁切范围后，可展示裁切后的效果，clipProps 的格式见下表；
- backupImgUrl 备选展示图，当 clipProps 未传入而无法裁切时默认展示的图片；
- 支持开启裁切的同时，开启图片放大镜功能。

## 指定裁切倍数

可指定裁切的倍数

- clipScale 指定裁切倍数：
  - 当 clipScale 为1时，裁切面积与 clipProps 指定的面积一致；
  - 否则，裁切面积为 clipProps 指定的宽高的 clipScale 倍所得的面积；
- 支持开启裁切的同时，开启图片放大镜功能。

## 结合卡片使用

使用卡片的 left 插槽即可将本组件应用于卡片中。

WARNING

放大镜效果及裁切效果通过 canvas 实现，需注意图片需要支持跨域问题。

## 支持应用 transform:scale

> - 针对可能要在组件或包裹组件的外层元素上应用 transform:scale 的情况作了处理：
>   - 指定transformScale为与transform:scale相同的数值即可。

## Attributes

| 参数 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| magnify | 是否开启放大镜 | Boolean | false |
| scale | 放大倍数 | Number | 3 |
| src | 图片源，同原生 | String | -- |
| showMagnifier | 是否显示放大镜展示区 | Boolean | true |
| allowScroll | 触发放大镜效果时是否允许滚动 | Boolean | false |
| transformScale | 组件或其外层组件应用transform:scale时，设置此值与transform:scale一致，保持正常放大镜效果 | Number | 1 |
| magnifierWidth | 放大镜效果展示区的宽度 | String, Number | -- |
| magnifierHeight | 放大镜效果展示区的高度 | String, Number | -- |
| clip | 是否开启图片裁切 | Boolean | false |
| clipProps | clip为true时有效，指定裁切的起始位置和宽高 | Object({ x: '', y: '', width: '', height: '' }) | null |
| clipScale | clip为true时有效，指定裁切的宽高与clipProps所指定的宽高的比例 | Number | 1 |
| backupImgUrl | clip为true时有效，当未指定clipProps，可以指定该值作为备选的图片源 | String | -- |

## Slot

| name | 说明 |
| --- | --- |
| placeholder | 同el-image，图片未加载的占位内容 |
| error | 同el-image，加载失败的内容 |

## Event

| 事件名称 | 说明 | 回调参数 |
| --- | --- | --- |
| load | 同el-image，图片加载成功触发 | (e: Event) |
| error | 同el-image，图片加载失败触发 | (e: Error) |
| mag-mouseenter | 开启放大镜时，鼠标移入时触发 | (e: Event) |
| mag-mousemove | 开启放大镜时，鼠标在组件区域内移动时触发 | 共两个参数，依次为：event、 包含绘制放大镜效果的CanvasRenderingContext2D.drawImage方法参数的drawParams对象，其值如下 |
| mag-mouseleave | 开启放大镜时，鼠标移出时触发 | (e: Event) |

## drawParams

| key | 说明 |
| --- | --- |
| image | 绘制到上下文的元素，是传入的图片后者经裁切后的生成的canvas |
| sx | 需要绘制到目标上下文中的，image的矩形（裁剪）选择框的左上角 X 轴坐标 |
| sy | 需要绘制到目标上下文中的，image的矩形（裁剪）选择框的左上角 Y 轴坐标 |
| sWidth | 需要绘制到目标上下文中的，image的矩形（裁剪）选择框的宽度 |
| sHeight | 需要绘制到目标上下文中的，image的矩形（裁剪）选择框的高度 |
| dx | image的左上角在目标canvas上 X 轴坐标 |
| dy | image的左上角在目标canvas上 Y 轴坐标 |
| dWidth | image在目标canvas上绘制的宽度。 允许对绘制的image进行缩放 |
| dHeight | image在目标canvas上绘制的高度。 允许对绘制的image进行缩放 |
