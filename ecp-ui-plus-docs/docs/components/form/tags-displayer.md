<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/form/tags-displayer.html -->

# <ecp-tags-displayer> 标签展示器

> 标签展示器

## 基础用法

创建一个标签展示器，在给定宽度内展示给定标签列表，若给定宽度不能将标签完全展示，超出的部分使用+n形式展示，同时提供移除标签功能

## 彩色标签

> - 创建一个基础标签展示器，可全局配置标签项字体大小，可配置标签项颜色，包括标签文字颜色（color），标签背景色（background-color）和边框颜色（border-color）。可使用内置的颜色类名设置标签颜色，也可传入自定义颜色值。
> - **类名颜色样式权重更大。同时传入类名和自定义颜色值时，会取类名颜色展示。**
> - 建议使用类名，颜色类名见 [Colors 色彩表](/ecp-ui-plus/docs/design/colors.html)。

## 使用slot装饰你的标签展示器

标签展示器提供prefix、suffix插槽供用户自定义展示其想在展示器头部、尾部插入的内容

## Attributes

| 参数 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| value/v-model | 传入当前标签值 value,v-model使用 vue 原生指令 v-model。 | Array<String>或Array<Object> | -- | [] |
| width | 展示器组件宽度，将会被传入style，所以可接受一切css中width属性接受的值 | String | -- | '100%' |
| showBorder | 是否显示边框 | boolean | -- | true |
| props | 当v-model传入对象数组时的配置选项，具体看下表 | Object | -- | -- |
| deleteAvailable | 标签是否可移除 | boolean | -- | true |
| deleteAllSymbol | 移除全部时delete事件传入回调的值，在标签项的值可能与预设值有冲突时使用 | String | -- | 'ALL' |
| placeholder | 无标签时显示的文本 | String | -- | -- |
| fontSize | 配置标签字体大小，将会被传入style，所以可接受一切css中font-size属性接受的值 | String | -- | '12px' |
| disabled | 设为true时背景色会变灰，且将不能移除标签,但是仍能触发click相关事件 | Boolean | -- | false |
| highlightWhenHover | 设为true时鼠标悬停会高亮边框 | Boolean | -- | false |
| active | 设为true时将高亮边框 | Boolean | -- | false |

## Props

| 参数 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| value | 指定标签项展示的值为标签对象的某个属性值 | String | -- | 'value' |
| color | 指定标签项文字颜色为标签对象的某个属性值 | String | -- | 'color' |
| backgroundColor | 指定标签项背景色为标签对象的某个属性值 | String | -- | 'backgroundColor' |
| borderColor | 指定标签项边框色为标签对象的某个属性值 | String | -- | 'borderColor' |
| colorClass | 指定标签项字体颜色类名为标签对象的某个属性值 | String | -- | 'colorClass' |
| bgColorClass | 指定标签项背景颜色类名为标签对象的某个属性值 | String | -- | 'bgColorClass' |
| borderColorClass | 指定标签项边框颜色类名为标签对象的某个属性值 | String | -- | 'borderColorClass' |

## Events

| 事件名称 | 说明 | 回调参数 |
| --- | --- | --- |
| delete | 移除标签时触发 | 单个移除时传入标签对象，全部移除时传入设置的或默认的deleteAllSymbol |
| click | 点击标签展示器时触发，注意：slot中的内容不会触发这个事件,点击标签项不会触发这个事件 | -- |
| itemClick | 点击某标签时触发 | 点击的标签对象 |
| resetClick | 点击+n标识时触发 | 当前展示的标签数量 |

## Slot

| 插槽名称 | 说明 |
| --- | --- |
| prefix | 展示器头部插槽，点击该区域不会触发click事件 |
| suffix | 展示器尾部插槽，点击该区域不会触发click事件 |
