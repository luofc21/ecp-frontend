<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/design/standard.html -->

# Standard 标准样式

## 规范要求

为统一项目中的样式，主色、功能色、字体颜色、边框颜色、阴影、间距等请使用样式变量设置。

> **注意：**
>
> - 组件库、业务代码内的间隔、颜色、字体大小、行高等样式属性 **`不可直接写死数值`**，应使用预定义的 `css 变量`，以便主题定制换肤处理；
> - `css 变量` 直接应用于浏览器端，不可用于 scss 计算，不参与 scss 编译！！！
> - 如需计算，请使用 css 函数处理。

## 颜色

### 基础色板

![](../../../assets/ecp-ui-plus/images/web-ui.jpg)

### 主题色

| 变量名 | 说明 |
| --- | --- |
| --color-primary | 主色。 color 值：#1890FF 。 |
| --color-primary-assist-1 | 主色-辅色 1。 `--color-primary-assist-1: var(--color-primary-opacity-1)` color 值：#1890FF + 0.1 透明度。 场景：下拉框内容悬浮背景色 |
| --color-primary-assist-2 | 主色-辅色 2。 `--color-primary-assist-2: var(--color-primary-light-1-5)` color 值：mix($--color-white, --color-primary, 15%)； 表示：白色 15% + 主色 85% 混合色； 场景：按钮悬浮色 |
| --color-primary-assist-3 | 主色-辅色 3。 `--color-primary-assist-3: var(--color-primary-dark-2-5)` color 值：mix($--color-black, --color-primary, 25%)； 表示：黑色 25% + 主色 75% 混合色； 场景：按钮点击色 |
| --color-primary-assist-4 | 主色-辅色 4。 `--color-primary-assist-4: var(--color-primary-light-4-5)` color 值：mix($--color-white, --color-primary, 45%)； 表示：白色 45% + 主色 55% 混合色； 场景：主按钮失效色 |
| --color-white | 白色。 color 值：#ffffff |
| --color-black | 黑色。 color 值：#000000 |

### 功能色

| 变量名 | 说明 |
| --- | --- |
| --color-success | 成功。#52c41a |
| --color-warning | 警告。#faad14 |
| --color-danger | 错误。#f5222d |
| --color-success-light-1 | 成功-辅色。 |
| --color-warning-light-1 | 警告-辅色。 |
| --color-danger-light-1 | 错误-辅色； |

### 背景色

页面默认底色

组件控件背景色、通用背景色

高亮背景色、表格背景色

常态组件背景色、卡片背景色

弹窗背景色

loading 加载背景色

填充色：强调

填充色：默认

填充色：次要

填充色：不可用

| 变量名 | 说明 |
| --- | --- |
| --background-color-page | #F0F3F7； 页面默认底色 |
| --background-color-base | rgba(0, 0, 0, 0.04)； 组件控件背景色、通用背景色 |
| --background-color-light | rgba(0, 0, 0, 0.02)； 高亮背景色、表格背景色 |
| --background-color-primary | rgba(255, 255, 255, 1)； 常态组件背景色、卡片背景色 |
| --background-color-dialog | rgba(255, 255, 255, 1)； 弹窗背景色：下拉框、日历、气泡、弹窗、抽屉 |
| --background-color-loading | rgba(255, 255, 255, 0.07)；  loading 加载背景色 |
| --fill-color-light | 填充色：强调 |
| --fill-color-primary | 填充色：默认 |
| --fill-color-secondary | 填充色：次要 |
| --fill-color-placeholder | 填充色：不可用 |

## 字体样式

### 字体

- 主体文本 font-family 固定设置为 `"SourceHansSans SC", "Microsoft YaHei", "微软雅黑", "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", Arial, sans-serif'`；
- 如业务系统需要使用 `SourceHanSansSC（思源黑体）`，请前往 [前端资源中心 - 字体](http://frontend.pcitech.online/#resources) 下载字体文件，并在业务系统公共样式中添加 `@font-face` 字体文件引用，如：

```css
@font-face {
    font-family: 'SourceHanSansSC';
    src: url('path/to/SourceHanSansSC.otf') format('truetype');
}
```

### 字阶

8px

12px

14px

16px

20px

24px

30px

38px

| 变量名 | 说明 |
| --- | --- |
| --font-size-extra-small | 字号：8px |
| --font-size-small | 字号：12px |
| --font-size-base | 字号：14px，页面默认字号 |
| --font-size-medium | 字号：16px |
| --font-size-large | 字号： 20px |
| --font-size-larger-1 | 字号： 24px |
| --font-size-larger-2 | 字号： 30px |
| --font-size-larger-3 | 字号： 38px |

### 行高

> - 关于文字的行高，css 属性当中的 line-height，在国际无障碍网页使用标准中给出了明确的指引 line-height = font-size \* 1.5；
> - 在验证过程中发现，固定 1.5 倍的行高比例，在当字号越大的时候，行高就会越大，在大号文字的展示上信息的连贯明显得出现割裂，尤其在多种字号及元素混排的场景中；
> - 行高是为了让上一行的文字和下一行的文字之间有呼吸的空间，基于呼吸空间一致，让不同字号之间的间距都保持相同，通过逻辑得到这样一个公式：「 行高 = 字号 + n 」，8 作为变量正好同时满足与 1.5 倍的「 14px & 16px 」常用字号行高保持一致，总体文字间隙稳定呼吸，行高空间较一致得出计算公式：「line-height = font-size + 8px」

行高: 16px

行高: 20px

行高: 22px

行高: 24px

行高: 28px

行高: 32px

行高: 38px

行高: 46px

| 变量名 | 说明 |
| --- | --- |
| --line-height-gap | 行高计算变量：8px |
| --font-line-height-extra-small | 行高：16px |
| --font-line-height-secondary | 同 --font-line-height-extra-small |
| --font-line-height-small | 行高：20px |
| --font-line-height-primary | 行高：22px，页面默认行高 |
| --font-line-height-medium | 行高：24px |
| --font-line-height-large | 行高：28px |
| --font-line-height-larger-1 | 行高：32px |
| --font-line-height-larger-2 | 行高：38px |
| --font-line-height-larger-3 | 行高：46px |

### 字重

400

700

bolder

| 变量名 | 说明 |
| --- | --- |
| --font-weight-primary | 字重： 400 |
| --font-weight-bold | 字重：700，即 bold |
| --font-weight-bolder | 字重：bolder |

### 字体颜色

强调

标题

正文

次要

不可用、说明

水印

深底背景文字强调色

| 变量名 | 说明 |
| --- | --- |
| --color-text-light | 字体色：强调；rgba(0, 0, 0, 1) |
| --color-text-primary | 字体色：标题；rgba(0, 0, 0, 0.85) |
| --color-text-regular | 字体色：正文；rgba(0, 0, 0, 0.65) |
| --color-text-secondary | 字体色：次要；rgba(0, 0, 0, 0.45) |
| --color-text-placeholder | 字体色：不可用、说明；rgba(0, 0, 0, 0.25) |
| --color-text-mark | 字体色：水印；rgba(0, 0, 0, 0.15) |
| --color-text-light-darken | 字体色：深底背景文字强调色；rgba(255,255,255,1) |
| ... | 字体色：链接；color 值为：$--color-primary(主色) ，请直接使用 <ecp-button> 组件 |

## 边框

### 边框样式

描边

分割线

高亮描边

透明边框

虚线分割线

失效状态边框

表单边框悬浮

| 变量名 | 说明 |
| --- | --- |
| --border-color-base | 描边；rgba(0, 0, 0, 0.15) |
| --border-color-light | 分割线；rgba(0, 0, 0, 0.09) |
| --border-color-white | 高亮描边；rgba(255, 255, 255, 0.25) |
| --border-color-none | 透明边框：用于重置弹出框、确认框的边框样式；rgba(255, 255, 255, 0) |
| --border-color-dash | 虚线分割线；rgba(0, 0, 0, 0.15) |
| --border-color-disabled | 失效状态边框： rgba(0, 0, 0, 0.09) |
| --border-color-hover | 边框悬浮色：主色 |
| --border-width-base | 宽度：1px |
| --border-style-base | 描边样式：solid |
| --border-base | 基础边框样式：$--border-width-base --border-style-base --border-color-base; |
| --border-dash | 虚线边框：$--border-width-base dashed --border-color-base; |
| --border-hover | 边框悬浮样式： --border-width-base --border-style-base --border-color-hover ; |

### 圆角

4px

2px

0

circle

capsule

| 变量名 | 说明 |
| --- | --- |
| --border-radius-base | 圆角： 4px |
| --border-radius-second | 圆角： 2px |
| --border-radius-zero | 圆角： 0 |
| --border-radius-circle | 圆角： 100% |
| --border-radius-capsule | 圆角： 99999px，等宽高时效果与circle一致 |

## 阴影

> 提供 6 种阴影样式，具体呈现的效果请查看 [Elevations 阴影](/ecp-ui-plus/docs/design/elevations.html) 。

| 变量名 | 说明 |
| --- | --- |
| --box-shadow-base | box-shadow: 0px 0px 8px 0px rgba(0, 0, 0, 0.15); |
| --box-shadow-bottom-select | box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, 0.15); |
| --box-shadow-bottom | box-shadow: 0px 4px 12px 0px rgba(0, 0, 0, 0.15); |
| --box-shadow-left | box-shadow: -2px 0px 8px 0px rgba(0, 0, 0, 0.15); |
| --box-shadow-right | box-shadow: 2px 0px 8px 0px rgba(0, 0, 0, 0.15); |
| --box-shadow-top | box-shadow: 0px -2px 8px 0px rgba(0, 0, 0, 0.15); |

## 间距

> 间距辅助器对于修改元素的填充（padding）和边距（margin）都非常有用，详见 [Spacer 间距类名](/ecp-ui-plus/docs/design/spacer.html)。

| 变量名 | 说明 |
| --- | --- |
| --spacer | 8px |
| --spacer-extra-small | spacer \* 0.25 = 2px |
| --spacer-small | spacer \* 0.5 = 4px |
| --spacer-medium | spacer \* 1.25 = 10px |
| --spacer-medium-2 | spacer \* 1.5 = 12px |
| --spacer-medium-3 | spacer \* 1.75 = 14px |
| --spacer-large | spacer \* 2 = 16px |
| --spacer-large-2 | spacer \* 2.5 = 20px |
| --spacer-large-3 | spacer \* 3 = 24px |
| --spacer-large-4 | spacer \* 4 = 32px |
| --spacer-extra-large | spacer \* 5 = 40px |
| --spacer-extra-large-2 | spacer \* 6 = 48px |
