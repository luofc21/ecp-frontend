<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/data/card.html -->

# <ecp-card> 卡片

## Ecp-card 卡片

### 基础用法

创建一个卡片内容水平排列的卡片

> 创建一个卡片模版，里面的插槽 content（默认插槽，无需填具名）部分（即文本内容）可以配套组件 ecp-label-item 使用（ecp-label-item 的使用方法左边目录对应组件的详情说明）。另外，图片的宽、高可以通过使用 imgUrlWidth，imgUrlHeight 传入需要设置的宽、高，其中默认值是：112px。

### 图片重新加载

创建一个卡片图片可以重新加载的卡片

### 支持两个图片的卡片

创建一个含有两张图片的卡片

> 创建一个含有两张图片的卡片,如果需要传入两张图片，左边图片为默认的 imgUrl（同只有一张图片的使用方法相同），位于右边的图片通过使用 imgRightUrl 传入。右边的图片的宽高默认使用左边的图片的宽高，如需修改可以通过传入 imgRightUrlWidth，imgRightUrlHeight 需要设置的宽高。

### 支持三张图片的卡片

创建一个含有三张图片的卡片

> 创建一个含有三张图片的卡片,如果需要传入三张图片，左边图片为默认的 imgUrl（同只有一张图片的使用方法相同），位于中间的图片通过使用 imgCenterUrl 传入，位于右边的图片通过使用 imgRightUrl 传入。中间的图片的宽高默认使用右边的图片的宽高，如需修改可以通过传入 imgCenterUrlWidth，imgCenterUrlHeight 需要设置的宽高。右边的图片的宽高默认使用左边的图片的宽高，如需修改可以通过传入 imgRightUrlWidth，imgRightUrlHeight 需要设置的宽高。

### left 插槽

创建使用 left 插槽的卡片

> - 不使用默认提供的图片区域，提供图片区域自定义。
> - 如果图片区域内容现有的场景不能满足实际场景，可以通过使用 left 插槽进行自定义。

### right-top 插槽

创建一个有右上角操作按钮的卡片

> - right-top 插槽的内容完全是自定义，主要是使用定位在右上角实现，是可选的。
> - 下面举一个例子：创建一个有按钮的卡片。

### footer 插槽

创建一个有脚步操作按钮的卡片

> footer 插槽的内容完全是自定义，是可选的。下面举一个例子：创建一个有按钮的卡片，按钮组可以通过使用全局定义的类名 app-card-buttons 实现下面的按钮。footer 插槽的布局默认水平向右, 如需水平居中(向左)可以添加 footer-align='center'('left')。

### 带 checkbox 复选框的卡片

创建一个有复选框的卡片。

> - 需要使用富选框的卡片，可以通过设置添加 showChecked 属性，需要将 checked 值保存在当前卡片的话可以通过添加 checked 属性。
> - 如果是卡片列表的需要使用 含有 `checkbox` 复选框的卡片的话，推荐使用的卡片组组件。

### 竖向排列的卡片

创建一个竖向排列的卡片

> - 创建一个竖向排列卡片模版，默认是水平排列。
> - 若需将内容竖向排列，添加 type = 'column' 即可，type 默认值是 row。

### 竖向排列两张图片的卡片

创建一个竖向排列两张图片的卡片

### 竖向排列三张图片的卡片

创建一个竖向排列三张图片的卡片

### 含有相似度值的卡片

创建一个含有相似度值的卡片

### 紧凑布局的卡片

创建一个紧凑布局的卡片

> 设置 compact 属性为 true 即可。

## Ecp-card-group 卡片组

### 卡片组基础用法

创建卡片组。

> - 卡片组内对卡片的布局排版做了处理：每个卡片宽度根据屏幕分辨率和列数进行计算。
> - ecp-card-group 元素能把多个 ecp-card 管理为一组并且对布局排版做了处理。
> - 每一行展示几个卡片可以通过 options 进行设置，默认值是 UI 规范提供的不同分辨率区间对应不同的列数。
> - 每一行展示几个卡片可以通过 options 进行设置，默认值是 UI 规范提供的不同分辨率区间对应不同的列数。
> - 具体的 options 设置可文档下面的说明。在分页请求卡片时，可以通过 getCol 获取 列数(col) 进行计算每一页的 pageSize。

注意：

- 目前存在一个问题是在渲染卡片组是需要先判断卡片列表数据list长度是否大于0才能计算宽度正确渲染。
- 另外如果有翻页，需要在每次请求前将列表数据list的设置为空数组,或在nextTick中手动调用setEcpCardWidth方法

### 带 checkbox 的卡片组

创建带 checkbox 的卡片组。

> 如需要使用复选框，在 ecp-card 中设置 showChecked 后并且同时绑定 id 属性， 只需要在 Group 中使用 v-model 绑定 Array 类型的变量即可获取被选中的卡片 id 列表。

## Ecp-card Attributes

| 参数 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| type | 卡片使用的排列方式（水平、竖向） | string | row(水平)，column(竖向) | row |
| compact | 是否使用紧凑的布局模式 | boolean | -- | false |
| showChecked | 是否展示复选框 | boolean | -- | false |
| isReloadImg | 是否重新加载图片 | boolean | -- | false |
| checked | 复选框的值 | boolean | -- | false |
| sizedImage | 以指定比例展示图片 | string | `16-9`, `3-2`, `4-3`, `1-1`, `3-4`, `2-3`, `9-16` | -- |
| imgUrl | 图片的 url | string | -- | -- |
| imgUrlWidth | 图片的宽 | string | -- | 112px |
| imgUrlHeight | 图片的高 | string | -- | 112px |
| imgRightUrl | 两张图片的情况下，右边图片的 url | string | -- | -- |
| imgRightUrlWidth | 右边图片的宽 | string | -- | 默认值为第一张图的 imgUrlWidth |
| imgRightUrlHeight | 右边图片的高 | string | -- |  |
| imgCenterUrl | 三张图片的情况下，中间图片的 url | string | -- | -- |
| imgCenterUrlWidth | 中间图片的宽 | string | -- | 默认值为右边图片的 imgUrlWidth |
| imgCenterUrlHeight | 中间图片的高 | string | -- | 默认值为右边图片的 imgUrlHeight |
| imgTotal | 图片的张数 | string / number | -- | -- |
| similarity | 相似度 | string | -- | -- |
| footerAlign | 脚部插槽的对齐方式 | string | right，left， center | center |
| fit | 确定图片如何适应容器框，同原生 object-fit | string | fill / contain / cover / none / scale-down | -- |
| rightFit | 确定第二张图片如何适应容器框，同原生 object-fit，不传值时默认使用第一张图片的适应方式 | string | fill / contain / cover / none / scale-down | -- |

## Ecp-card Event

| 事件名称 | 说明 | 回调参数 |
| --- | --- | --- |
| change | 卡片复选框改变时触发 | 当前复选框的值 |
| clickImg | 图片点击事件 | 图片的 url |

## Ecp-card Slots

| 插槽名 | 说明 | 注意事项 |
| --- | --- | --- |
| default | 卡片的文本内容 | -- |
| footer | 卡片的脚部区域，可选 | 如果使用操作按钮，推荐使用提供的全局的类名（class）：app-card-buttons |
| right-top | 卡片的右上角区域，可选 | -- |

## Ecp-card-group Attributes

| 参数 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| v-model | 选中的卡片列表 id | array | -- | -- |
| options | 设置不同分辨率下设置的列数。每个对象的参数说明见下面。 | array<object> | -- | [{ min: 0, max: 1280, col: 4 },{ min: 1281, max: 1440, col: 5 },{ min: 1441, max: 100000, col: 6 }] |

### options 的结构

| 参数 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| min | 最小分辨率 | number | -- | -- |
| max | 最大分辨率 | number | -- | -- |
| col | 列数 | number | -- | -- |

## Ecp-card-group Event

| 事件名称 | 说明 | 回调参数 |
| --- | --- | --- |
| getCol | 卡片在当前分辨率下的列数，配合分页请求数据时可用于设置 pageSize | 列数 (col) |
| change | 卡片复选框改变时触发 | 当前被选中的卡片 id 列表的值 |

## Ecp-card-group Slots

| 插槽名 | 说明 | 注意事项 |
| --- | --- | --- |
| default | 卡片组默认插槽 | -- |

## Ecp-card-group Exposes

| 方法/属性 | 说明 | 参数 |
| --- | --- | --- |
| setEcpCardWidth | 设置组中卡片宽度，一般在卡片列表数据改变时调用 | -- |
