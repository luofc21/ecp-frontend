<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/media/preview-img-content.html -->

# Preview-img-content 多图预览

## 基础用法

仅设置宽度，高度根据比例计算。

## 两张图

### 1-1

> - 比例：
>   - 左: 1:1
>   - 右: 1:1

### 16-3

> - 比例：
>   - 左: 16:9
>   - 右: 3:4

### 16-1

> - 比例：
>   - 左: 16:9
>   - 右: 1:1
> - 需同时设置宽度和高度，因为比例不同，图片比例计算出的高度不同；
> - maxShowLength 用于控制轮播列表小图展示个数。

## 三张图

### 16-3-3 + 相似度

> - 比例：
>   - 左: 16:9
>   - 中: 3:4
>   - 右: 3:4
> - 需同时设置宽度和高度，因为比例不同，图片比例计算出的高度不同。

### 3-3-16 + 相似度 + 可镜像

> - 比例：
>   - 左: 3:4
>   - 中: 3:4
>   - 右: 16:9
> - 需同时设置宽度和高度，因为比例不同，图片比例计算出的高度不同。

## 使用按钮插槽

使用插槽buttons-left、buttons-center、buttons-right可以在按钮区域追加按钮，提供 imgInfo 图片信息。

## Attributes

| 参数 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| type | 图片布局，目前支持 `16` (16:9)、`9` (9:16)、`4` (4:3)、`3` (3:4)、`1` (1:1) 5 种比例通过 `-` 组合。 | String | `n`、`n-n`、`n-n-n` |  |
| index | 初始化展示图片列表中的第index项 从0开始。支持 .sync 属性获取当前的index | Number |  | 0 |
| props | 图片 url 的字段映射配置项，配置项见 [Props 的结构](#props-的结构) | Props |  | { leftImgUrl:'leftImgUrl', rightImgUrl:'rightImgUrl', centerImgUrl:'centerImgUrl' } |
| imgList | 图片列表，列表项见 [ImgListItem 的结构](#imglist-的结构) | Array |  |  |
| similarity | 相似度 | String |  |  |
| similarity-top | 相似度自定义距离顶部的距离，相对于图片区域的定位(单位为px) | Number |  |  |
| similarity-left | 相似度自定义距离左边的距离，相对于图片区域的定位(单位为px) | Number |  |  |
| ... | 其它支持参数，见 [Img-view 图片预览 - Attributes](/ecp-ui-plus/docs/components/media/img-view.html#attributes) | ... |  |  |

### Props 的结构

| key | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| leftImgUrl | 左边图片的 url 对应的键名 | String | 'leftImgUrl' |
| rightImgUrl | 右边图片的 url 对应的键名 | String | 'rightImgUrl' |
| centerImgUrl | 中间图片的 url 对应的键名 | String | 'centerImgUrl' |

### ImgList 的结构

| key | 说明 | 类型 |
| --- | --- | --- |
| leftImgUrl | 左边图片的 url，自定义键名可在 Props 中定义 | String |
| rightImgUrl | 右边图片的 url，自定义键名可在 Props 中定义 | String |
| centerImgUrl | 中间图片的 url，自定义键名可在 Props 中定义 | String |

## Events

| 事件名称 | 说明 | 回调参数 |
| --- | --- | --- |
| change | 图片切换的回调事件 | index, imgObject |
| img-info | 图片信息回传 | 在 `ecp-img-view` 基础上，增加一个参数 imgPosition 标识回传的图片位置 |
| click-icon | 图片操作按钮点击事件 | 在 `ecp-img-view` 基础上，增加一个参数 imgPosition 标识回传的图片位置 |

## Slots

| 插槽名称 | 说明 |
| --- | --- |
| default | 底部内容区域插槽，回传当前数据项：imgData，该信息是用户传入的 |
| swiper-item | 轮播图中每张图片的内容插槽，回传当前数据项：imgData，当前轮播图的图片链接：poster |
| img-tips-left | 左侧图片tips插槽，回传当前图片大小的信息：imgInfo, 当前数据项：imgData。 |
| img-tips-center | 中间图片tips插槽，回传当前图片大小的信息：imgInfo, 当前数据项：imgData。 |
| img-tips-right | 右侧图片tips插槽，回传当前图片大小的信息：imgInfo, 当前数据项：imgData。 |
| buttons-left-prepend | 左侧按钮前缀插槽，回传当前图片大小的信息：imgInfo, 当前数据项：imgData。 |
| buttons-left | 左侧按钮后缀插槽，回传当前图片大小的信息：imgInfo, 当前数据项：imgData。 |
| buttons-center-prepend | 中间按钮前缀插槽，回传当前图片大小的信息：imgInfo, 当前数据项：imgData。 |
| buttons-center | 中间按钮后缀插槽，回传当前图片大小的信息：imgInfo, 当前数据项：imgData。 |
| buttons-right-prepend | 右侧按钮前缀插槽，回传当前图片大小的信息：imgInfo, 当前数据项：imgData。 |
| buttons-right | 右侧按钮后缀插槽，回传当前图片大小的信息：imgInfo, 当前数据项：imgData。 |
| empty | 空状态插槽，回传空项信息：emptyInfo, 当前数据项：imgData。 |
| empty-left | 左侧空状态插槽，回传空项信息：emptyInfo, 当前数据项：imgData。 |
| empty-center | 中间空状态插槽，回传空项信息：emptyInfo, 当前数据项：imgData。 |
| empty-right | 右侧空状态插槽，回传空项信息：emptyInfo, 当前数据项：imgData。 |
