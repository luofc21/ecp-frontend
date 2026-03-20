<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/media/cropper.html -->

# <ecp-cropper> 图片裁剪

WARNING

- 图片跨域时无法进行裁剪

## 基础用法

1. 传入 imgUrl，配置 options（与 [cropperjs](https://github.com/fengyuanchen/cropperjs) 一致的配置）后可进行图片裁剪。
2. 可通过 preview 指定显示预览效果的目标元素。
3. v-model 绑定裁剪框区域列表，可传入供用户点选、编辑的裁剪框。
4. 可自行选择需要的组件自带操作按钮，通过 operations，可指定组件自带操作按钮的显示与隐藏；且可以通过 button 插槽添加自定义的操作按钮。当 operations 传入空字符串且不添加插槽时不显示操作按钮区域。
5. 可绘制多个裁剪框区域，裁剪区域改变时会触发 change 事件和 cropImage 事件，更多特性请看文末详细文档。

TIP

- 若预览图未正确显示，请尝试设置指定元素的样式为 overflow: hidden 。

## Attributes

| 参数 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| v-model | 供选择的预置裁剪框的位置大小信息数组 | Object[] ({ x:'', y:'', w:'', h:'' }) | [] |
| imgUrl | 待裁剪图片源 | String | -- |
| options | cropperjs 的配置项，详见 [options 配置项的部分默认值](#options-配置项的部分默认值) | Object | {} |
| preview | 显示预览图的元素或其集合。 应为一个元素、元素数组、节点列表对象或 querySelectorAll 的有效选择器。 这个是 options 中的一项，单独提出来是为了强调该配置项。 | Element, Array<Element>, NodeList, String<CssSelector> | -- |
| showDefaultCropper | 是否初始显示默认裁剪框 | Boolean | true |
| ~~operations~~ | ~~需要显示的操作按钮~~ `后续版本将废弃，请使用layout` | ~~String~~ |  |
| layout Global | 需要显示的操作按钮 | String/Array | zoomout, zoomin, mirror, counterclockwise, clockwise |
| ... | 其它操作栏相关属性见 [Image-toolbar 图片操作栏 - Attributes](/ecp-ui-plus/docs/components/layout/image-toolbar.html#attributes) | ... | ... |

### options 配置项的部分默认值

组件中 options 某些配置项非 cropperjs 的默认值 （如下所列），其它详见 [cropperjs - options](https://github.com/fengyuanchen/cropperjs/blob/main/README.md#options)。

| 配置项 | 含义 | 默认值 |
| --- | --- | --- |
| initialAspectRatio | 定义裁剪框的初始纵横比，该值为 1 则裁剪框初始为正方形 | 1 |
| modal | 是否在图像上方和裁剪框下方显示遮罩层 | false |
| background | 是否显示容器的网格背景 | false |
| autoCropArea | 定义初始裁剪区域大小（百分比），应为一个介于 0 和 1 之间的数字 | 1 |
| zoomOnWheel | 是否启用通过鼠标滚轮缩放图像 | false |
| viewMode | 显示模式，详情参见 cropperjs 文档 | 2 |

## Events

| 事件名称 | 说明 | 回调参数 |
| --- | --- | --- |
| update:modelValue | 裁剪区域改变触发 | 改变后的 cropList |
| cropImage | modelValue 改变时触发，在图片改变时也会触发 | 改变后的裁剪图片列表，列表项见 [CropListItem 的结构](#croplistitem-的结构) |
| ready | 同 cropperjs，当待裁剪图片已加载且裁剪器实例准备好运行时触发，详见 [ready](https://github.com/fengyuanchen/cropperjs/blob/main/README.md#ready-1)。 | Event |
| cropstart | 同 cropperjs，当底图或裁剪框开始改变时触发，详见 [cropperjs - cropstart](https://github.com/fengyuanchen/cropperjs/blob/main/README.md#cropstart-1)。 | Event |
| cropmove | 同 cropperjs，当底图或裁剪框正在改变时触发，详见 [cropperjs - cropstmove](https://github.com/fengyuanchen/cropperjs/blob/main/README.md#cropstmove-1)。 | Event |
| cropend | 同 cropperjs，当底图或裁剪框停止改变时触发，详见 [cropperjs - cropend](https://github.com/fengyuanchen/cropperjs/blob/main/README.md#cropend-1)。 | Event |
| crop | 同 cropperjs，当底图或裁剪框改变后触发，详见 [cropperjs - crop](https://github.com/fengyuanchen/cropperjs/blob/main/README.md#crop-1)。 | Event |
| zoom | 同 cropperjs，当开始缩放底图时触发，详见 [cropperjs - zoom](https://github.com/fengyuanchen/cropperjs/blob/main/README.md#zoom-1)。 | Event |
| transform | 底图旋转或镜像时触发 | 见 [TransformEvent 的结构](#transformevent-的结构) |

### TransformEvent 的结构

| 参数名 | 说明 |
| --- | --- |
| scaleX | 水平方向镜像参数，1 为正常，-1 为镜像 |
| scaleY | 垂直方向镜像参数，1 为正常，-1 为镜像 |
| rotate | 旋转角度 |

### CropListItem 的结构

| 参数名 | 说明 |
| --- | --- |
| w | 图片宽度 |
| h | 图片高度 |
| url | 图片 url，base64 格式 |

## Slots

| name | 说明 |
| --- | --- |
| buttons-prepend | 按钮前缀插槽 |
| buttons | 按钮后缀插槽 |

## Exposes

不建议！

- 可通过 ref 访问本组件的 cropInstance，其为 cropperjs 的实例，通过它可以调用 cropperjs 提供的方法，例如手动获取剪裁结果等；
- 具体方法请查看 [cropperjs - methods](https://github.com/fengyuanchen/cropperjs/blob/main/README.md#methods) 。
