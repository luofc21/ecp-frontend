<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/design/theme.html -->

# Theme 主题定义

现 Ecp-ui-plus 提供 `默认浅色` 与 `深色` 两套主题，可按需替换 `css 变量` 进行主题定制。

> - 请先阅读文档：
>   - MDN: [CSS 变量](https://developer.mozilla.org/zh-CN/docs/Web/CSS/--*)、[使用 CSS 变量](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Using_CSS_custom_properties)；
>   - CSSWG: [css-variable](https://drafts.csswg.org/css-variables/)。

## 变量命名规则

### 基础色值

- 自定义颜色基准色：`--color-#{颜色标识}`；
- 自定义颜色基准色的变体色：`--color-#{颜色标识}-#{基准色类型}-#{百分制十位数}-#{百分制个位数}`；
  - 基准色类型: `light白混合 / dark黑混合 / opacity透明度`；
  - 百分制个位数为 0 时，命名不添加 `-#{百分制个位数}`；
  - 变体色生成范围（百分制，包括上下限）：
    - light: 5~95 (步长 5, 即 light-0-5 ~ light-9-5)；
    - dark: 5~95 (步长 5, 即 dark-0-5 ~ dark-9-5)；
    - opacity: 0~9 (步长 1, 即 opacity-0 ~ opacity-0-9), 10~95 (步长 5, opacity-1 ~ opacity-9-5)；
- 自定义颜色基准色的 RGB 数值：`--color-#{颜色标识}-rgb`, 可用于 css RGBA 函数；
- 保留变量名：
  - 主色: `--color-primary-#{基准色类型}-#{百分制十位数}-#{百分制个位数}`
  - 功能色 - 成功: `--color-success-#{基准色类型}-#{百分制十位数}-#{百分制个位数}`
  - 功能色 - 警告: `--color-warning-#{基准色类型}-#{百分制十位数}-#{百分制个位数}`
  - 功能色 - 危险: `--color-danger-#{基准色类型}-#{百分制十位数}-#{百分制个位数}`
  - 功能色 - 错误: `--color-error-#{基准色类型}-#{百分制十位数}-#{百分制个位数}`
  - 功能色 - 信息: `--color-info-#{基准色类型}-#{百分制十位数}-#{百分制个位数}`

### 基础样式色值

- 文本颜色：`--color-text-#{类型}`
- 文本颜色反色：`--color-text-#{类型}-reverse`
- 背景颜色：`--background-color-#{类型}`
- 边框颜色：`--border-color-#{类型}`
- 填充颜色：`--fill-color-#{类型}`
- 禁用态颜色：`--disabled-#{类型}`
- 弹框颜色：`--overlay-color-#{类型}`
- 蒙层颜色：`--mask-color-#{类型}`

### 带颜色的属性

- 边框：`--border-#{类型}`
- 滚动条：`--scrollbar-#{类型}`
- 阴影：`--box-shadow-#{类型}`
- 填充颜色：`--fill-color-#{类型}`
- 禁用态颜色：`--disabled-#{类型}`
- 蒙层颜色：`--overlay-color-#{类型}`

### 通用变量

- 字体：`--font-family`
- 字阶：`--font-size-#{类型}`
- 行高：`--font-line-height-#{类型}`
- 字重：`--font-weight-#{类型}`
- 间距：`--spacer-#{类型}`
- 层级：`--index-#{类型}`
- 圆角：`--border-radius-#{类型}`

## 主题定义

### 第一步：变量枚举

#### 通用变量枚举

> 如不需要定制通用变量，可以跳过。

点击查看代码片段

```scss
/* Size Related Variables */
@use "sass:math";
@use "sass:map";

// Typography
$font-family: (
    // default family
    "":
        '"SourceHansSans SC", "Microsoft YaHei", "微软雅黑", "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", Arial, sans-serif'
);
$font-size-base: 14px;
$font-size-gap: 2px;
$font-size: (
    "larger-3": $font-size-base + $font-size-gap * 12,
    "larger-2": $font-size-base + $font-size-gap * 8,
    "larger-1": $font-size-base + $font-size-gap * 5,
    "extra-large": $font-size-base + $font-size-gap * 5,
    "large": $font-size-base + $font-size-gap * 3,
    "medium-1": $font-size-base + $font-size-gap * 2,
    "medium": $font-size-base + $font-size-gap,
    "base": $font-size-base,
    "small": $font-size-base - $font-size-gap,
    "extra-small": $font-size-base - $font-size-gap * 3,
);
$line-height-gap: 8px;
$line-height: (
    "gap": $line-height-gap,
    "larger-3": map.get($font-size, "larger-3") + $line-height-gap, /* 42px */
    "larger-2": map.get($font-size, "larger-2") + $line-height-gap, /* 38px */
    "larger-1": map.get($font-size, "larger-1") + $line-height-gap, /* 32px */
    "extra-large": map.get($font-size, "extra-large") + $line-height-gap, /* 32px */
    "large": map.get($font-size, "large") + $line-height-gap, /* 28px */
    "medium-1": map.get($font-size, "medium-1") + $line-height-gap, /* 26px */
    "medium": map.get($font-size, "medium") + $line-height-gap, /* 24px */
    "primary": map.get($font-size, "base") + $line-height-gap, /* 22px */
    "base": map.get($font-size, "base") + $line-height-gap, /* 22px */
    "small": map.get($font-size, "small") + $line-height-gap, /* 20px */
    "extra-small": map.get($font-size, "extra-small") + $line-height-gap, /* 16px */
);
$font-weight: (
    "primary": 400,
    "bold": 700,
    "bolder": bolder,
);

// spacer
$spacer-base: 8px !default;
$spacer: (
    "": $spacer-base /* 8px */,
    "extra-small": $spacer-base * 0.25 /* 2px */,
    "small": $spacer-base * 0.5 /* 4px */,
    "medium": $spacer-base * 1.25 /* 10px */,
    "medium-2": $spacer-base * 1.5 /* 12px */,
    "medium-3": $spacer-base * 1.75 /* 14px */,
    "large": $spacer-base * 2 /* 16px */,
    "large-2": $spacer-base * 2.5 /* 20px */,
    "large-3": $spacer-base * 3 /* 24px */,
    "large-4": $spacer-base * 4 /* 32px */,
    "extra-large": $spacer-base * 5 /* 40px */,
    "extra-large-2": $spacer-base * 6 /* 48px */,
);

// zIndex
$z-index: (
    "normal": 1,
    "top": 1000,
    "popper": 2000,
);

$border-radius: (
    "base": 4px,
    "small": 2px,
    "round": 20px,
    "circle": 100%,
    "second": 2px,
    "capsule": 99999px,
    "zero": 0,
);

// Loading
$loading: (
    "spinner-size": 32px,
    "fullscreen-spinner-size": 48px,
);
```

#### 主题色变量枚举

> 浅色、深色枚举规则相同，这里以浅色主题（默认主题）为例。

点击查看代码片段

```scss
/* Color Default Variables */
@use "sass:map";

// types
$types: primary, success, warning, danger, error, info;

// Color
$theme-colors: (
    "white": #ffffff,
    "black": #000000,
    "primary": (
        "base": #1890ff,
    ),
    "success": (
        "base": #52c41a,
    ),
    "warning": (
        "base": #faad14,
    ),
    "danger": (
        "base": #f5222d,
    ),
    "error": (
        "base": #f5222d,
    ),
    "info": (
        "base": rgba(#000000, 45%),
    ),
);

$text-color: (
    "light": var(--color-black),
    "primary": var(--color-black-opacity-8-5),
    "regular": var(--color-black-opacity-6-5),
    "secondary": var(--color-black-opacity-4-5),
    "placeholder": var(--color-black-opacity-2-5),
    "mark": var(--color-black-opacity-1-5),
    "shadow": var(--color-black-opacity-0-9),
    "light-darken": var(--color-white),
    "disabled": var(--color-black-opacity-2-5),
);
$text-color-reverse: (
    "light-reverse": var(--color-white),
    "primary-reverse": var(--color-white-opacity-8-5),
    "regular-reverse": var(--color-white-opacity-6-5),
    "secondary-reverse": var(--color-white-opacity-4-5),
    "placeholder-reverse": var(--color-white-opacity-2-5),
    "mark-reverse": var(--color-white-opacity-1-5),
    "shadow-reverse": var(--color-white-opacity-0-9),
    "light-darken-reverse": var(--color-black),
    "disabled-reverse": var(--color-white-opacity-2-5),
);

$border-color: (
    "": var(--color-black-opacity-1-5),
    "base": var(--color-black-opacity-1-5),
    "light": var(--color-black-opacity-0-9),
    "lighter": var(--color-black-opacity-0-4),
    "extra-light": var(--color-black-opacity-0-2),
    "dark": rgba(var(--color-black-rgb), 14%),
    "darker": var(--color-black-opacity-2),
    "none": var(--color-black-opacity-0),
    "dash": var(--color-black-opacity-1-5),
    "disabled": var(--color-black-opacity-0-9),
    "hover": var(--color-primary),
);

$fill-color: (
    "": #f0f2f5,
    "base": var(--color-white),
    "light": #f5f7fa,
    "lighter": #fafafa,
    "extra-light": #fafcff,
    "dark": #ebedf0,
    "darker": #e6e8eb,
    "blank": var(--color-white),
    "primary": var(--color-black-opacity-6-5),
    "secondary": var(--color-black-opacity-4-5),
    "placeholder": var(--color-black-opacity-2-5),
);

$bg-color: (
    "": var(--color-white),
    "page": #f0f3f7,
    "base": var(--color-black-opacity-0-4),
    "light": var(--color-black-opacity-0-2),
    "primary": var(--color-white),
    "dialog": var(--background-color-primary),
    "overlay": var(--background-color-primary),
);

// Border
$border-width: 1px;
$border-style: solid;
$border: (
    "width": $border-width,
    "width-base": $border-width,
    "style": $border-style,
    "style-base": $border-style,
    "": $border-width $border-style var(--border-color-base),
    "base": $border-width $border-style var(--border-color-base),
    "dash": $border-width dashed var(--border-color-base),
    "hover": $border-width $border-style var(--border-color-hover),
);

// Box-shadow
$box-shadow-color-base: var(--color-black-opacity-1-5);
$box-shadow-color-light: rgba(var(--color-black-rgb), 12%);
$box-shadow: (
    "": (
        0px 12px 32px 4px rgba(0, 0, 0, 0.04),
        0px 8px 20px rgba(0, 0, 0, 0.08),
    ),
    "color-base": $box-shadow-color-base,
    "base": 0px 2px 8px 0px $box-shadow-color-base,
    "bottom-select": 0px 2px 8px 0px $box-shadow-color-base,
    "bottom": 0px 4px 12px 0px $box-shadow-color-base,
    "left": -2px 0px 8px 0px $box-shadow-color-base,
    "right": 2px 0px 8px 0px $box-shadow-color-base,
    "top": 0px -2px 8px 0px $box-shadow-color-base,
    "input-focus": 0px 0px 0px 2px var(--color-primary-opacity-2-5),
    "color-light": $box-shadow-color-light,
    "light": 0px 0px 12px $box-shadow-color-light,
    "lighter": 0px 0px 6px $box-shadow-color-light,
    "dark": (
        0px 16px 48px 16px var(--color-black-opacity-0-8),
        0px 12px 32px $box-shadow-color-light,
        0px 8px 16px -8px rgba(var(--color-black-rgb), 16%),
    ),
);

// Disable default
$disabled: (
    "bg-color": var(--background-color-base),
    "text-color": var(--color-text-placeholder),
    "border-color": var(--border-color-light),
    "fill-color": var(--background-color-base),
    "color-base": var(--color-text-placeholder),
);

// overlay
$overlay-color: (
    "": var(--color-black-opacity-8),
    "light": var(--color-black-opacity-7),
    "lighter": var(--color-black-opacity-5),
);

// mask
$mask-color: (
    "": var(--color-white-opacity-9),
    "extra-light": var(--color-white-opacity-3),
);

// Scrollbar
$scrollbar: (
    "opacity": 0,
    "bg-color": map.get($theme-colors, "black"),
    "bg-color-webkit": transparent,
    "color": map.get($theme-colors, "black"),
    "visible-opacity": 0.15,
    "visible-bg-color-webkit": var(--color-black-opacity-1-5),
    "hover-opacity": 0.25,
    "hover-bg-color": map.get($theme-colors, "black"),
    "hover-bg-color-webkit": var(--color-black-opacity-2-5),
    "color-hover": var(--color-black-opacity-2-5),
);

// Table
$table: (
    "header-bg-color": var(--color-primary-light-9),
    "row-hover-bg-color": var(--color-primary-light-9),
    "row-current-bg-color": var(--color-primary-light-8),
    "row-striped": var(--color-primary-light-9-5),
);
```

### 第二步：CSS 变量生成

> 各主题各自引入变量枚举，各自生成 CSS 变量。

#### 变量作用域

- 替换默认主题：作用域使用 `:root` 即可；
- 替换深色主题/新增主题：作用域需要指定 `.custom-theme, html.custom-theme, [data-theme^="custom-theme"]`；
- 适配深色主题需要添加：`color-scheme: dark`。

#### 基础色值生成

使用 scss 指令 `@include set-color-variable` 经编译处理，批量输出 css 色值变量。

点击查看代码片段

```scss
/* path/to/theme/custom-theme/var.scss */
@use "sass:map";

@use "@ecp-ui-plus/theme-chalk/src/tools/theme-config.scss" as *;

@use "./mapper.scss" as *;

xxxxx {
    @each $type in ($types) {
        $color: map.get($theme-colors, $type, "base");
        @include set-color-variable($type, $color, $ignore-type, $reverse);
    }
}
```

##### set-color-variable 参数

| 字段 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| $type | String |  | 是 | 颜色标识 |
| $color | String |  | 是 | 颜色基准色 (固定颜色值) |
| $ignore-type | Boolean/String | false | 否 | 是否忽略指定基准色类型， String 可选值 `light / dark / opacity`， Boolean true 时为 `light` |
| $reverse | Boolean | false | 否 | 是否调转黑白混合值（基准色类型标识不变） |

#### 其它变量生成

使用 scss 指令 `@include set-mapper-variable` 经编译处理，批量输出枚举 css 变量, 用法：

点击查看代码片段

```scss
/* path/to/theme/custom-theme/var.scss */
@use "sass:map";

@use "@ecp-ui-plus/theme-chalk/src/tools/theme-config.scss" as *;

@use "./mapper.scss" as *;

xxxxx {
    @include set-mapper-variable($attribute-name, $attribute-mapper);
}
```

##### set-mapper-variable 参数

| 字段 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| $attribute-name | String |  | 是 | CSS 变量前缀 |
| $attribute-mapper | ScssMap |  | 是 | SCSS 变量枚举 Map |

#### 生成示例

##### 浅色主题变量

点击查看代码片段

```scss
/* path/to/theme/custom-theme/var.scss */
@use "sass:map";

@use "@ecp-ui-plus/theme-chalk/src/tools/theme-config.scss" as *;

@use "./mapper.scss" as *;
@use "./mapper-size.scss" as *;

.custom-theme,
html.custom-theme,
[data-theme^="custom-theme"] {
    @each $type in ($types) {
        $color: map.get($theme-colors, $type, "base");
        @include set-color-variable($type, $color);
    }

    @include set-mapper-variable("background-color", $bg-color);

    @include set-mapper-variable("color-text", $text-color);
    @include set-mapper-variable("color-text", $text-color-reverse);

    @include set-mapper-variable("border-color", $border-color);
    @include set-mapper-variable("border", $border);

    @include set-mapper-variable("scrollbar", $scrollbar);

    @include set-mapper-variable("fill-color", $fill-color);

    @include set-mapper-variable("box-shadow", $box-shadow);

    @include set-mapper-variable("disabled", $disabled);

    @include set-mapper-variable("overlay-color", $overlay-color);

    @include set-mapper-variable("mask-color", $mask-color);
}
.custom-theme,
html.custom-theme,
[data-theme^="custom-theme"] {
    @include set-mapper-variable("font-family", $font-family);
    @include set-mapper-variable("font-size", $font-size);
    @include set-mapper-variable("font-line-height", $line-height);
    @include set-mapper-variable("font-weight", $font-weight);

    @include set-mapper-variable("spacer", $spacer);

    @include set-mapper-variable("index", $z-index);
    @include set-mapper-variable("border-radius", $border-radius);
}
```

##### 深色主题变量

点击查看代码片段

```scss
/* path/to/theme/custom-theme-dark/var.scss */
@use "sass:map";

@use "@ecp-ui-plus/theme-chalk/src/tools/theme-config.scss" as *;

@use "./mapper.scss" as *;
@use "./mapper-size.scss" as *;

.custom-theme-dark,
html.custom-theme-dark,
[data-theme^="custom-theme-dark"] {
    color-scheme: dark;

    @each $type in ($types) {
        $color: map.get($theme-colors, $type, "base");
        @include set-color-variable($type, $color, false, true);
    }

    @include set-mapper-variable("background-color", $bg-color);

    @include set-mapper-variable("color-text", $text-color);
    @include set-mapper-variable("color-text", $text-color-reverse);

    @include set-mapper-variable("border-color", $border-color);
    @include set-mapper-variable("border", $border);

    @include set-mapper-variable("scrollbar", $scrollbar);

    @include set-mapper-variable("fill-color", $fill-color);

    @include set-mapper-variable("box-shadow", $box-shadow);

    @include set-mapper-variable("disabled", $disabled);

    @include set-mapper-variable("overlay-color", $overlay-color);

    @include set-mapper-variable("mask-color", $mask-color);
}
.custom-theme-dark,
html.custom-theme-dark,
[data-theme^="custom-theme-dark"] {
    @include set-mapper-variable("font-family", $font-family);
    @include set-mapper-variable("font-size", $font-size);
    @include set-mapper-variable("font-line-height", $line-height);
    @include set-mapper-variable("font-weight", $font-weight);

    @include set-mapper-variable("spacer", $spacer);

    @include set-mapper-variable("index", $z-index);
    @include set-mapper-variable("border-radius", $border-radius);
}
```

### 第三步：主题统一暴露

直接将所有主题变量文件引入，变量已根据 CSS 作用域区分，无需手动切换主题文件。

```scss
/* path/to/theme/index.scss */
@use "./custom-theme/var.scss" as *;
@use "./custom-theme-dark/var.scss" as *;
```

### 第四步：样式全量引入

> 建议顺序：element-plus → ecp-ui-plus → 自定义主题。

```scss
@use "element-plus/theme-chalk/src/index.scss" as *;
@use '@ecp/ecp-ui-plus/theme-chalk' as *;
@use 'path/to/theme/index.scss' as *;
```

## 动态切换主题

使用 组合式 Api `useTheme` 切换主题。

> 详见 [UseTheme 主题切换](/ecp-ui-plus/docs/api/composables/use-theme.html) 。

## 附：编译后的内置主题变量

### 通用样式变量

点击查看代码片段

```scss
:root {
    --font-family: "SourceHansSans SC", "Microsoft YaHei", "微软雅黑",
        "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", Arial,
        sans-serif;
    --font-size-larger-3: 38px;
    --font-size-larger-2: 30px;
    --font-size-larger-1: 24px;
    --font-size-extra-large: 24px;
    --font-size-large: 20px;
    --font-size-medium: 16px;
    --font-size-base: 14px;
    --font-size-small: 12px;
    --font-size-extra-small: 8px;
    --font-line-height-gap: 8px;
    --font-line-height-larger-3: 46px;
    --font-line-height-larger-2: 38px;
    --font-line-height-larger-1: 32px;
    --font-line-height-extra-large: 32px;
    --font-line-height-large: 28px;
    --font-line-height-medium: 24px;
    --font-line-height-primary: 22px;
    --font-line-height-base: 22px;
    --font-line-height-small: 20px;
    --font-line-height-extra-small: 16px;
    --font-weight-primary: 400;
    --font-weight-bold: 700;
    --font-weight-bolder: bolder;
    --spacer: 8px;
    --spacer-extra-small: 2px;
    --spacer-small: 4px;
    --spacer-medium: 10px;
    --spacer-medium-2: 12px;
    --spacer-medium-3: 14px;
    --spacer-large: 16px;
    --spacer-large-2: 20px;
    --spacer-large-3: 24px;
    --spacer-large-4: 32px;
    --spacer-extra-large: 40px;
    --spacer-extra-large-2: 48px;
    --index-normal: 1;
    --index-top: 1000;
    --index-popper: 2000;
    --border-radius-base: 4px;
    --border-radius-small: 2px;
    --border-radius-round: 20px;
    --border-radius-circle: 100%;
    --border-radius-second: 2px;
    --border-radius-capsule: 99999px;
    --border-radius-zero: 0;
}
```

### 浅色主题

> 也是默认主题

点击查看代码片段

```scss
:root {
    color-scheme: light;

    --color-white: #ffffff;
    --color-white-rgb: 255, 255, 255;
    --color-white-opacity-0: rgba(255, 255, 255, 0);
    --color-white-opacity-0-1: rgba(255, 255, 255, 0.01);
    --color-white-opacity-0-2: rgba(255, 255, 255, 0.02);
    --color-white-opacity-0-3: rgba(255, 255, 255, 0.03);
    --color-white-opacity-0-4: rgba(255, 255, 255, 0.04);
    --color-white-opacity-0-5: rgba(255, 255, 255, 0.05);
    --color-white-opacity-0-6: rgba(255, 255, 255, 0.06);
    --color-white-opacity-0-7: rgba(255, 255, 255, 0.07);
    --color-white-opacity-0-8: rgba(255, 255, 255, 0.08);
    --color-white-opacity-0-9: rgba(255, 255, 255, 0.09);
    --color-white-opacity-1: rgba(255, 255, 255, 0.1);
    --color-white-opacity-2: rgba(255, 255, 255, 0.2);
    --color-white-opacity-3: rgba(255, 255, 255, 0.3);
    --color-white-opacity-4: rgba(255, 255, 255, 0.4);
    --color-white-opacity-5: rgba(255, 255, 255, 0.5);
    --color-white-opacity-6: rgba(255, 255, 255, 0.6);
    --color-white-opacity-7: rgba(255, 255, 255, 0.7);
    --color-white-opacity-8: rgba(255, 255, 255, 0.8);
    --color-white-opacity-9: rgba(255, 255, 255, 0.9);
    --color-white-opacity-1-5: rgba(255, 255, 255, 0.15);
    --color-white-opacity-2-5: rgba(255, 255, 255, 0.25);
    --color-white-opacity-3-5: rgba(255, 255, 255, 0.35);
    --color-white-opacity-4-5: rgba(255, 255, 255, 0.45);
    --color-white-opacity-5-5: rgba(255, 255, 255, 0.55);
    --color-white-opacity-6-5: rgba(255, 255, 255, 0.65);
    --color-white-opacity-7-5: rgba(255, 255, 255, 0.75);
    --color-white-opacity-8-5: rgba(255, 255, 255, 0.85);
    --color-white-opacity-9-5: rgba(255, 255, 255, 0.95);
    --color-white-lighter: var(--color-white-light-9);
    --color-white-assist-1: var(--color-white-opacity-1);
    --color-white-assist-2: var(--color-white-light-1-5);
    --color-white-assist-3: var(--color-white-dark-2);
    --color-white-assist-4: var(--color-white-light-4);
    --color-white-assist-5: var(--color-white-light-5);
    --color-black: #000000;
    --color-black-rgb: 0, 0, 0;
    --color-black-opacity-0: rgba(0, 0, 0, 0);
    --color-black-opacity-0-1: rgba(0, 0, 0, 0.01);
    --color-black-opacity-0-2: rgba(0, 0, 0, 0.02);
    --color-black-opacity-0-3: rgba(0, 0, 0, 0.03);
    --color-black-opacity-0-4: rgba(0, 0, 0, 0.04);
    --color-black-opacity-0-5: rgba(0, 0, 0, 0.05);
    --color-black-opacity-0-6: rgba(0, 0, 0, 0.06);
    --color-black-opacity-0-7: rgba(0, 0, 0, 0.07);
    --color-black-opacity-0-8: rgba(0, 0, 0, 0.08);
    --color-black-opacity-0-9: rgba(0, 0, 0, 0.09);
    --color-black-opacity-1: rgba(0, 0, 0, 0.1);
    --color-black-opacity-2: rgba(0, 0, 0, 0.2);
    --color-black-opacity-3: rgba(0, 0, 0, 0.3);
    --color-black-opacity-4: rgba(0, 0, 0, 0.4);
    --color-black-opacity-5: rgba(0, 0, 0, 0.5);
    --color-black-opacity-6: rgba(0, 0, 0, 0.6);
    --color-black-opacity-7: rgba(0, 0, 0, 0.7);
    --color-black-opacity-8: rgba(0, 0, 0, 0.8);
    --color-black-opacity-9: rgba(0, 0, 0, 0.9);
    --color-black-opacity-1-5: rgba(0, 0, 0, 0.15);
    --color-black-opacity-2-5: rgba(0, 0, 0, 0.25);
    --color-black-opacity-3-5: rgba(0, 0, 0, 0.35);
    --color-black-opacity-4-5: rgba(0, 0, 0, 0.45);
    --color-black-opacity-5-5: rgba(0, 0, 0, 0.55);
    --color-black-opacity-6-5: rgba(0, 0, 0, 0.65);
    --color-black-opacity-7-5: rgba(0, 0, 0, 0.75);
    --color-black-opacity-8-5: rgba(0, 0, 0, 0.85);
    --color-black-opacity-9-5: rgba(0, 0, 0, 0.95);
    --color-black-lighter: var(--color-black-light-9);
    --color-black-assist-1: var(--color-black-opacity-1);
    --color-black-assist-2: var(--color-black-light-1-5);
    --color-black-assist-3: var(--color-black-dark-2);
    --color-black-assist-4: var(--color-black-light-4);
    --color-black-assist-5: var(--color-black-light-5);
    --color-primary: #1890ff;
    --color-primary-rgb: 24, 144, 255;
    --color-primary-light-1: #2f9bff;
    --color-primary-light-2: #46a6ff;
    --color-primary-light-3: #5db1ff;
    --color-primary-light-4: #74bcff;
    --color-primary-light-5: #8cc8ff;
    --color-primary-light-6: #a3d3ff;
    --color-primary-light-7: #badeff;
    --color-primary-light-8: #d1e9ff;
    --color-primary-light-9: #e8f4ff;
    --color-primary-light-0-5: #2496ff;
    --color-primary-light-1-5: #3ba1ff;
    --color-primary-light-2-5: #52acff;
    --color-primary-light-3-5: #69b7ff;
    --color-primary-light-4-5: #80c2ff;
    --color-primary-light-5-5: #97cdff;
    --color-primary-light-6-5: #aed8ff;
    --color-primary-light-7-5: #c5e3ff;
    --color-primary-light-8-5: #dceeff;
    --color-primary-light-9-5: #f3f9ff;
    --color-primary-dark-1: #1682e6;
    --color-primary-dark-2: #1373cc;
    --color-primary-dark-3: #1165b3;
    --color-primary-dark-4: #0e5699;
    --color-primary-dark-5: #0c4880;
    --color-primary-dark-6: #0a3a66;
    --color-primary-dark-7: #072b4d;
    --color-primary-dark-8: #051d33;
    --color-primary-dark-9: #020e1a;
    --color-primary-dark-0-5: #1789f2;
    --color-primary-dark-1-5: #147ad9;
    --color-primary-dark-2-5: #126cbf;
    --color-primary-dark-3-5: #105ea6;
    --color-primary-dark-4-5: #0d4f8c;
    --color-primary-dark-5-5: #0b4173;
    --color-primary-dark-6-5: #083259;
    --color-primary-dark-7-5: #062440;
    --color-primary-dark-8-5: #041626;
    --color-primary-dark-9-5: #01070d;
    --color-primary-opacity-0: rgba(24, 144, 255, 0);
    --color-primary-opacity-0-1: rgba(24, 144, 255, 0.01);
    --color-primary-opacity-0-2: rgba(24, 144, 255, 0.02);
    --color-primary-opacity-0-3: rgba(24, 144, 255, 0.03);
    --color-primary-opacity-0-4: rgba(24, 144, 255, 0.04);
    --color-primary-opacity-0-5: rgba(24, 144, 255, 0.05);
    --color-primary-opacity-0-6: rgba(24, 144, 255, 0.06);
    --color-primary-opacity-0-7: rgba(24, 144, 255, 0.07);
    --color-primary-opacity-0-8: rgba(24, 144, 255, 0.08);
    --color-primary-opacity-0-9: rgba(24, 144, 255, 0.09);
    --color-primary-opacity-1: rgba(24, 144, 255, 0.1);
    --color-primary-opacity-2: rgba(24, 144, 255, 0.2);
    --color-primary-opacity-3: rgba(24, 144, 255, 0.3);
    --color-primary-opacity-4: rgba(24, 144, 255, 0.4);
    --color-primary-opacity-5: rgba(24, 144, 255, 0.5);
    --color-primary-opacity-6: rgba(24, 144, 255, 0.6);
    --color-primary-opacity-7: rgba(24, 144, 255, 0.7);
    --color-primary-opacity-8: rgba(24, 144, 255, 0.8);
    --color-primary-opacity-9: rgba(24, 144, 255, 0.9);
    --color-primary-opacity-1-5: rgba(24, 144, 255, 0.15);
    --color-primary-opacity-2-5: rgba(24, 144, 255, 0.25);
    --color-primary-opacity-3-5: rgba(24, 144, 255, 0.35);
    --color-primary-opacity-4-5: rgba(24, 144, 255, 0.45);
    --color-primary-opacity-5-5: rgba(24, 144, 255, 0.55);
    --color-primary-opacity-6-5: rgba(24, 144, 255, 0.65);
    --color-primary-opacity-7-5: rgba(24, 144, 255, 0.75);
    --color-primary-opacity-8-5: rgba(24, 144, 255, 0.85);
    --color-primary-opacity-9-5: rgba(24, 144, 255, 0.95);
    --color-primary-lighter: var(--color-primary-light-9);
    --color-primary-assist-1: var(--color-primary-opacity-1);
    --color-primary-assist-2: var(--color-primary-light-1-5);
    --color-primary-assist-3: var(--color-primary-dark-2);
    --color-primary-assist-4: var(--color-primary-light-4);
    --color-primary-assist-5: var(--color-primary-light-5);
    --color-success: #52c41a;
    --color-success-rgb: 82, 196, 26;
    --color-success-light-1: #63ca31;
    --color-success-light-2: #75d048;
    --color-success-light-3: #86d65f;
    --color-success-light-4: #97dc76;
    --color-success-light-5: #a9e28d;
    --color-success-light-6: #bae7a3;
    --color-success-light-7: #cbedba;
    --color-success-light-8: #dcf3d1;
    --color-success-light-9: #eef9e8;
    --color-success-light-0-5: #5bc725;
    --color-success-light-1-5: #6ccd3c;
    --color-success-light-2-5: #7dd353;
    --color-success-light-3-5: #8fd96a;
    --color-success-light-4-5: #a0df81;
    --color-success-light-5-5: #b1e498;
    --color-success-light-6-5: #c2eaaf;
    --color-success-light-7-5: #d4f0c6;
    --color-success-light-8-5: #e5f6dd;
    --color-success-light-9-5: #f6fcf4;
    --color-success-dark-1: #4ab017;
    --color-success-dark-2: #429d15;
    --color-success-dark-3: #398912;
    --color-success-dark-4: #317610;
    --color-success-dark-5: #29620d;
    --color-success-dark-6: #214e0a;
    --color-success-dark-7: #193b08;
    --color-success-dark-8: #102705;
    --color-success-dark-9: #081403;
    --color-success-dark-0-5: #4eba19;
    --color-success-dark-1-5: #46a716;
    --color-success-dark-2-5: #3e9314;
    --color-success-dark-3-5: #357f11;
    --color-success-dark-4-5: #2d6c0e;
    --color-success-dark-5-5: #25580c;
    --color-success-dark-6-5: #1d4509;
    --color-success-dark-7-5: #153107;
    --color-success-dark-8-5: #0c1d04;
    --color-success-dark-9-5: #040a01;
    --color-success-opacity-0: rgba(82, 196, 26, 0);
    --color-success-opacity-0-1: rgba(82, 196, 26, 0.01);
    --color-success-opacity-0-2: rgba(82, 196, 26, 0.02);
    --color-success-opacity-0-3: rgba(82, 196, 26, 0.03);
    --color-success-opacity-0-4: rgba(82, 196, 26, 0.04);
    --color-success-opacity-0-5: rgba(82, 196, 26, 0.05);
    --color-success-opacity-0-6: rgba(82, 196, 26, 0.06);
    --color-success-opacity-0-7: rgba(82, 196, 26, 0.07);
    --color-success-opacity-0-8: rgba(82, 196, 26, 0.08);
    --color-success-opacity-0-9: rgba(82, 196, 26, 0.09);
    --color-success-opacity-1: rgba(82, 196, 26, 0.1);
    --color-success-opacity-2: rgba(82, 196, 26, 0.2);
    --color-success-opacity-3: rgba(82, 196, 26, 0.3);
    --color-success-opacity-4: rgba(82, 196, 26, 0.4);
    --color-success-opacity-5: rgba(82, 196, 26, 0.5);
    --color-success-opacity-6: rgba(82, 196, 26, 0.6);
    --color-success-opacity-7: rgba(82, 196, 26, 0.7);
    --color-success-opacity-8: rgba(82, 196, 26, 0.8);
    --color-success-opacity-9: rgba(82, 196, 26, 0.9);
    --color-success-opacity-1-5: rgba(82, 196, 26, 0.15);
    --color-success-opacity-2-5: rgba(82, 196, 26, 0.25);
    --color-success-opacity-3-5: rgba(82, 196, 26, 0.35);
    --color-success-opacity-4-5: rgba(82, 196, 26, 0.45);
    --color-success-opacity-5-5: rgba(82, 196, 26, 0.55);
    --color-success-opacity-6-5: rgba(82, 196, 26, 0.65);
    --color-success-opacity-7-5: rgba(82, 196, 26, 0.75);
    --color-success-opacity-8-5: rgba(82, 196, 26, 0.85);
    --color-success-opacity-9-5: rgba(82, 196, 26, 0.95);
    --color-success-lighter: var(--color-success-light-9);
    --color-success-assist-1: var(--color-success-opacity-1);
    --color-success-assist-2: var(--color-success-light-1-5);
    --color-success-assist-3: var(--color-success-dark-2);
    --color-success-assist-4: var(--color-success-light-4);
    --color-success-assist-5: var(--color-success-light-5);
    --color-warning: #faad14;
    --color-warning-rgb: 250, 173, 20;
    --color-warning-light-1: #fbb52c;
    --color-warning-light-2: #fbbd43;
    --color-warning-light-3: #fcc65b;
    --color-warning-light-4: #fcce72;
    --color-warning-light-5: #fdd68a;
    --color-warning-light-6: #fddea1;
    --color-warning-light-7: #fee6b9;
    --color-warning-light-8: #feefd0;
    --color-warning-light-9: #fff7e8;
    --color-warning-light-0-5: #fab120;
    --color-warning-light-1-5: #fbb937;
    --color-warning-light-2-5: #fbc24f;
    --color-warning-light-3-5: #fcca66;
    --color-warning-light-4-5: #fcd27e;
    --color-warning-light-5-5: #fdda95;
    --color-warning-light-6-5: #fde2ad;
    --color-warning-light-7-5: #feebc4;
    --color-warning-light-8-5: #fef3dc;
    --color-warning-light-9-5: #fffbf3;
    --color-warning-dark-1: #e19c12;
    --color-warning-dark-2: #c88a10;
    --color-warning-dark-3: #af790e;
    --color-warning-dark-4: #96680c;
    --color-warning-dark-5: #7d570a;
    --color-warning-dark-6: #644508;
    --color-warning-dark-7: #4b3406;
    --color-warning-dark-8: #322304;
    --color-warning-dark-9: #191102;
    --color-warning-dark-0-5: #eea413;
    --color-warning-dark-1-5: #d59311;
    --color-warning-dark-2-5: #bc820f;
    --color-warning-dark-3-5: #a3700d;
    --color-warning-dark-4-5: #8a5f0b;
    --color-warning-dark-5-5: #714e09;
    --color-warning-dark-6-5: #583d07;
    --color-warning-dark-7-5: #3f2b05;
    --color-warning-dark-8-5: #261a03;
    --color-warning-dark-9-5: #0d0901;
    --color-warning-opacity-0: rgba(250, 173, 20, 0);
    --color-warning-opacity-0-1: rgba(250, 173, 20, 0.01);
    --color-warning-opacity-0-2: rgba(250, 173, 20, 0.02);
    --color-warning-opacity-0-3: rgba(250, 173, 20, 0.03);
    --color-warning-opacity-0-4: rgba(250, 173, 20, 0.04);
    --color-warning-opacity-0-5: rgba(250, 173, 20, 0.05);
    --color-warning-opacity-0-6: rgba(250, 173, 20, 0.06);
    --color-warning-opacity-0-7: rgba(250, 173, 20, 0.07);
    --color-warning-opacity-0-8: rgba(250, 173, 20, 0.08);
    --color-warning-opacity-0-9: rgba(250, 173, 20, 0.09);
    --color-warning-opacity-1: rgba(250, 173, 20, 0.1);
    --color-warning-opacity-2: rgba(250, 173, 20, 0.2);
    --color-warning-opacity-3: rgba(250, 173, 20, 0.3);
    --color-warning-opacity-4: rgba(250, 173, 20, 0.4);
    --color-warning-opacity-5: rgba(250, 173, 20, 0.5);
    --color-warning-opacity-6: rgba(250, 173, 20, 0.6);
    --color-warning-opacity-7: rgba(250, 173, 20, 0.7);
    --color-warning-opacity-8: rgba(250, 173, 20, 0.8);
    --color-warning-opacity-9: rgba(250, 173, 20, 0.9);
    --color-warning-opacity-1-5: rgba(250, 173, 20, 0.15);
    --color-warning-opacity-2-5: rgba(250, 173, 20, 0.25);
    --color-warning-opacity-3-5: rgba(250, 173, 20, 0.35);
    --color-warning-opacity-4-5: rgba(250, 173, 20, 0.45);
    --color-warning-opacity-5-5: rgba(250, 173, 20, 0.55);
    --color-warning-opacity-6-5: rgba(250, 173, 20, 0.65);
    --color-warning-opacity-7-5: rgba(250, 173, 20, 0.75);
    --color-warning-opacity-8-5: rgba(250, 173, 20, 0.85);
    --color-warning-opacity-9-5: rgba(250, 173, 20, 0.95);
    --color-warning-lighter: var(--color-warning-light-9);
    --color-warning-assist-1: var(--color-warning-opacity-1);
    --color-warning-assist-2: var(--color-warning-light-1-5);
    --color-warning-assist-3: var(--color-warning-dark-2);
    --color-warning-assist-4: var(--color-warning-light-4);
    --color-warning-assist-5: var(--color-warning-light-5);
    --color-danger: #f5222d;
    --color-danger-rgb: 245, 34, 45;
    --color-danger-light-1: #f63842;
    --color-danger-light-2: #f74e57;
    --color-danger-light-3: #f8646c;
    --color-danger-light-4: #f97a81;
    --color-danger-light-5: #fa9196;
    --color-danger-light-6: #fba7ab;
    --color-danger-light-7: #fcbdc0;
    --color-danger-light-8: #fdd3d5;
    --color-danger-light-9: #fee9ea;
    --color-danger-light-0-5: #f62d38;
    --color-danger-light-1-5: #f7434d;
    --color-danger-light-2-5: #f85962;
    --color-danger-light-3-5: #f96f77;
    --color-danger-light-4-5: #fa858c;
    --color-danger-light-5-5: #fb9ca1;
    --color-danger-light-6-5: #fcb2b6;
    --color-danger-light-7-5: #fdc8cb;
    --color-danger-light-8-5: #fedee0;
    --color-danger-light-9-5: #fff4f5;
    --color-danger-dark-1: #dd1f29;
    --color-danger-dark-2: #c41b24;
    --color-danger-dark-3: #ac1820;
    --color-danger-dark-4: #93141b;
    --color-danger-dark-5: #7b1117;
    --color-danger-dark-6: #620e12;
    --color-danger-dark-7: #4a0a0e;
    --color-danger-dark-8: #310709;
    --color-danger-dark-9: #190305;
    --color-danger-dark-0-5: #e9202b;
    --color-danger-dark-1-5: #d01d26;
    --color-danger-dark-2-5: #b81a22;
    --color-danger-dark-3-5: #9f161d;
    --color-danger-dark-4-5: #871319;
    --color-danger-dark-5-5: #6e0f14;
    --color-danger-dark-6-5: #560c10;
    --color-danger-dark-7-5: #3d090b;
    --color-danger-dark-8-5: #250507;
    --color-danger-dark-9-5: #0c0202;
    --color-danger-opacity-0: rgba(245, 34, 45, 0);
    --color-danger-opacity-0-1: rgba(245, 34, 45, 0.01);
    --color-danger-opacity-0-2: rgba(245, 34, 45, 0.02);
    --color-danger-opacity-0-3: rgba(245, 34, 45, 0.03);
    --color-danger-opacity-0-4: rgba(245, 34, 45, 0.04);
    --color-danger-opacity-0-5: rgba(245, 34, 45, 0.05);
    --color-danger-opacity-0-6: rgba(245, 34, 45, 0.06);
    --color-danger-opacity-0-7: rgba(245, 34, 45, 0.07);
    --color-danger-opacity-0-8: rgba(245, 34, 45, 0.08);
    --color-danger-opacity-0-9: rgba(245, 34, 45, 0.09);
    --color-danger-opacity-1: rgba(245, 34, 45, 0.1);
    --color-danger-opacity-2: rgba(245, 34, 45, 0.2);
    --color-danger-opacity-3: rgba(245, 34, 45, 0.3);
    --color-danger-opacity-4: rgba(245, 34, 45, 0.4);
    --color-danger-opacity-5: rgba(245, 34, 45, 0.5);
    --color-danger-opacity-6: rgba(245, 34, 45, 0.6);
    --color-danger-opacity-7: rgba(245, 34, 45, 0.7);
    --color-danger-opacity-8: rgba(245, 34, 45, 0.8);
    --color-danger-opacity-9: rgba(245, 34, 45, 0.9);
    --color-danger-opacity-1-5: rgba(245, 34, 45, 0.15);
    --color-danger-opacity-2-5: rgba(245, 34, 45, 0.25);
    --color-danger-opacity-3-5: rgba(245, 34, 45, 0.35);
    --color-danger-opacity-4-5: rgba(245, 34, 45, 0.45);
    --color-danger-opacity-5-5: rgba(245, 34, 45, 0.55);
    --color-danger-opacity-6-5: rgba(245, 34, 45, 0.65);
    --color-danger-opacity-7-5: rgba(245, 34, 45, 0.75);
    --color-danger-opacity-8-5: rgba(245, 34, 45, 0.85);
    --color-danger-opacity-9-5: rgba(245, 34, 45, 0.95);
    --color-danger-lighter: var(--color-danger-light-9);
    --color-danger-assist-1: var(--color-danger-opacity-1);
    --color-danger-assist-2: var(--color-danger-light-1-5);
    --color-danger-assist-3: var(--color-danger-dark-2);
    --color-danger-assist-4: var(--color-danger-light-4);
    --color-danger-assist-5: var(--color-danger-light-5);
    --color-error: #f5222d;
    --color-error-rgb: 245, 34, 45;
    --color-error-light-1: #f63842;
    --color-error-light-2: #f74e57;
    --color-error-light-3: #f8646c;
    --color-error-light-4: #f97a81;
    --color-error-light-5: #fa9196;
    --color-error-light-6: #fba7ab;
    --color-error-light-7: #fcbdc0;
    --color-error-light-8: #fdd3d5;
    --color-error-light-9: #fee9ea;
    --color-error-light-0-5: #f62d38;
    --color-error-light-1-5: #f7434d;
    --color-error-light-2-5: #f85962;
    --color-error-light-3-5: #f96f77;
    --color-error-light-4-5: #fa858c;
    --color-error-light-5-5: #fb9ca1;
    --color-error-light-6-5: #fcb2b6;
    --color-error-light-7-5: #fdc8cb;
    --color-error-light-8-5: #fedee0;
    --color-error-light-9-5: #fff4f5;
    --color-error-dark-1: #dd1f29;
    --color-error-dark-2: #c41b24;
    --color-error-dark-3: #ac1820;
    --color-error-dark-4: #93141b;
    --color-error-dark-5: #7b1117;
    --color-error-dark-6: #620e12;
    --color-error-dark-7: #4a0a0e;
    --color-error-dark-8: #310709;
    --color-error-dark-9: #190305;
    --color-error-dark-0-5: #e9202b;
    --color-error-dark-1-5: #d01d26;
    --color-error-dark-2-5: #b81a22;
    --color-error-dark-3-5: #9f161d;
    --color-error-dark-4-5: #871319;
    --color-error-dark-5-5: #6e0f14;
    --color-error-dark-6-5: #560c10;
    --color-error-dark-7-5: #3d090b;
    --color-error-dark-8-5: #250507;
    --color-error-dark-9-5: #0c0202;
    --color-error-opacity-0: rgba(245, 34, 45, 0);
    --color-error-opacity-0-1: rgba(245, 34, 45, 0.01);
    --color-error-opacity-0-2: rgba(245, 34, 45, 0.02);
    --color-error-opacity-0-3: rgba(245, 34, 45, 0.03);
    --color-error-opacity-0-4: rgba(245, 34, 45, 0.04);
    --color-error-opacity-0-5: rgba(245, 34, 45, 0.05);
    --color-error-opacity-0-6: rgba(245, 34, 45, 0.06);
    --color-error-opacity-0-7: rgba(245, 34, 45, 0.07);
    --color-error-opacity-0-8: rgba(245, 34, 45, 0.08);
    --color-error-opacity-0-9: rgba(245, 34, 45, 0.09);
    --color-error-opacity-1: rgba(245, 34, 45, 0.1);
    --color-error-opacity-2: rgba(245, 34, 45, 0.2);
    --color-error-opacity-3: rgba(245, 34, 45, 0.3);
    --color-error-opacity-4: rgba(245, 34, 45, 0.4);
    --color-error-opacity-5: rgba(245, 34, 45, 0.5);
    --color-error-opacity-6: rgba(245, 34, 45, 0.6);
    --color-error-opacity-7: rgba(245, 34, 45, 0.7);
    --color-error-opacity-8: rgba(245, 34, 45, 0.8);
    --color-error-opacity-9: rgba(245, 34, 45, 0.9);
    --color-error-opacity-1-5: rgba(245, 34, 45, 0.15);
    --color-error-opacity-2-5: rgba(245, 34, 45, 0.25);
    --color-error-opacity-3-5: rgba(245, 34, 45, 0.35);
    --color-error-opacity-4-5: rgba(245, 34, 45, 0.45);
    --color-error-opacity-5-5: rgba(245, 34, 45, 0.55);
    --color-error-opacity-6-5: rgba(245, 34, 45, 0.65);
    --color-error-opacity-7-5: rgba(245, 34, 45, 0.75);
    --color-error-opacity-8-5: rgba(245, 34, 45, 0.85);
    --color-error-opacity-9-5: rgba(245, 34, 45, 0.95);
    --color-error-lighter: var(--color-error-light-9);
    --color-error-assist-1: var(--color-error-opacity-1);
    --color-error-assist-2: var(--color-error-light-1-5);
    --color-error-assist-3: var(--color-error-dark-2);
    --color-error-assist-4: var(--color-error-light-4);
    --color-error-assist-5: var(--color-error-light-5);
    --color-info: rgba(0, 0, 0, 0.45);
    --color-info-rgb: 0, 0, 0;
    --color-info-light-1: rgba(71, 71, 71, 0.505);
    --color-info-light-2: rgba(118, 118, 118, 0.56);
    --color-info-light-3: rgba(152, 152, 152, 0.615);
    --color-info-light-4: rgba(178, 178, 178, 0.67);
    --color-info-light-5: rgba(198, 198, 198, 0.725);
    --color-info-light-6: rgba(214, 214, 214, 0.78);
    --color-info-light-7: rgba(227, 227, 227, 0.835);
    --color-info-light-8: rgba(238, 238, 238, 0.89);
    --color-info-light-9: rgba(247, 247, 247, 0.945);
    --color-info-light-0-5: rgba(39, 39, 39, 0.4775);
    --color-info-light-1-5: rgba(96, 96, 96, 0.5325);
    --color-info-light-2-5: rgba(136, 136, 136, 0.5875);
    --color-info-light-3-5: rgba(166, 166, 166, 0.6425);
    --color-info-light-4-5: rgba(188, 188, 188, 0.6975);
    --color-info-light-5-5: rgba(206, 206, 206, 0.7525);
    --color-info-light-6-5: rgba(221, 221, 221, 0.8075);
    --color-info-light-7-5: rgba(233, 233, 233, 0.8625);
    --color-info-light-8-5: rgba(243, 243, 243, 0.9175);
    --color-info-light-9-5: rgba(251, 251, 251, 0.9725);
    --color-info-dark-1: rgba(0, 0, 0, 0.505);
    --color-info-dark-2: rgba(0, 0, 0, 0.56);
    --color-info-dark-3: rgba(0, 0, 0, 0.615);
    --color-info-dark-4: rgba(0, 0, 0, 0.67);
    --color-info-dark-5: rgba(0, 0, 0, 0.725);
    --color-info-dark-6: rgba(0, 0, 0, 0.78);
    --color-info-dark-7: rgba(0, 0, 0, 0.835);
    --color-info-dark-8: rgba(0, 0, 0, 0.89);
    --color-info-dark-9: rgba(0, 0, 0, 0.945);
    --color-info-dark-0-5: rgba(0, 0, 0, 0.4775);
    --color-info-dark-1-5: rgba(0, 0, 0, 0.5325);
    --color-info-dark-2-5: rgba(0, 0, 0, 0.5875);
    --color-info-dark-3-5: rgba(0, 0, 0, 0.6425);
    --color-info-dark-4-5: rgba(0, 0, 0, 0.6975);
    --color-info-dark-5-5: rgba(0, 0, 0, 0.7525);
    --color-info-dark-6-5: rgba(0, 0, 0, 0.8075);
    --color-info-dark-7-5: rgba(0, 0, 0, 0.8625);
    --color-info-dark-8-5: rgba(0, 0, 0, 0.9175);
    --color-info-dark-9-5: rgba(0, 0, 0, 0.9725);
    --color-info-opacity-0: rgba(0, 0, 0, 0);
    --color-info-opacity-0-1: rgba(0, 0, 0, 0.01);
    --color-info-opacity-0-2: rgba(0, 0, 0, 0.02);
    --color-info-opacity-0-3: rgba(0, 0, 0, 0.03);
    --color-info-opacity-0-4: rgba(0, 0, 0, 0.04);
    --color-info-opacity-0-5: rgba(0, 0, 0, 0.05);
    --color-info-opacity-0-6: rgba(0, 0, 0, 0.06);
    --color-info-opacity-0-7: rgba(0, 0, 0, 0.07);
    --color-info-opacity-0-8: rgba(0, 0, 0, 0.08);
    --color-info-opacity-0-9: rgba(0, 0, 0, 0.09);
    --color-info-opacity-1: rgba(0, 0, 0, 0.1);
    --color-info-opacity-2: rgba(0, 0, 0, 0.2);
    --color-info-opacity-3: rgba(0, 0, 0, 0.3);
    --color-info-opacity-4: rgba(0, 0, 0, 0.4);
    --color-info-opacity-5: rgba(0, 0, 0, 0.5);
    --color-info-opacity-6: rgba(0, 0, 0, 0.6);
    --color-info-opacity-7: rgba(0, 0, 0, 0.7);
    --color-info-opacity-8: rgba(0, 0, 0, 0.8);
    --color-info-opacity-9: rgba(0, 0, 0, 0.9);
    --color-info-opacity-1-5: rgba(0, 0, 0, 0.15);
    --color-info-opacity-2-5: rgba(0, 0, 0, 0.25);
    --color-info-opacity-3-5: rgba(0, 0, 0, 0.35);
    --color-info-opacity-4-5: rgba(0, 0, 0, 0.45);
    --color-info-opacity-5-5: rgba(0, 0, 0, 0.55);
    --color-info-opacity-6-5: rgba(0, 0, 0, 0.65);
    --color-info-opacity-7-5: rgba(0, 0, 0, 0.75);
    --color-info-opacity-8-5: rgba(0, 0, 0, 0.85);
    --color-info-opacity-9-5: rgba(0, 0, 0, 0.95);
    --color-info-lighter: var(--color-info-light-9);
    --color-info-assist-1: var(--color-info-opacity-1);
    --color-info-assist-2: var(--color-info-light-1-5);
    --color-info-assist-3: var(--color-info-dark-2);
    --color-info-assist-4: var(--color-info-light-4);
    --color-info-assist-5: var(--color-info-light-5);
    --background-color: var(--color-white);
    --background-color-page: #f0f3f7;
    --background-color-base: var(--color-black-opacity-0-4);
    --background-color-light: var(--color-black-opacity-0-2);
    --background-color-primary: var(--color-white);
    --background-color-dialog: var(--background-color-primary);
    --background-color-overlay: var(--background-color-primary);
    --color-text-light: var(--color-black);
    --color-text-primary: var(--color-black-opacity-8-5);
    --color-text-regular: var(--color-black-opacity-6-5);
    --color-text-secondary: var(--color-black-opacity-4-5);
    --color-text-placeholder: var(--color-black-opacity-2-5);
    --color-text-mark: var(--color-black-opacity-1-5);
    --color-text-shadow: var(--color-black-opacity-0-9);
    --color-text-light-darken: var(--color-white);
    --color-text-disabled: var(--color-black-opacity-2-5);
    --color-text-light-reverse: var(--color-white);
    --color-text-primary-reverse: var(--color-white-opacity-8-5);
    --color-text-regular-reverse: var(--color-white-opacity-6-5);
    --color-text-secondary-reverse: var(--color-white-opacity-4-5);
    --color-text-placeholder-reverse: var(--color-white-opacity-2-5);
    --color-text-mark-reverse: var(--color-white-opacity-1-5);
    --color-text-shadow-reverse: var(--color-white-opacity-0-9);
    --color-text-light-darken-reverse: var(--color-black);
    --color-text-disabled-reverse: var(--color-white-opacity-2-5);
    --border-color: var(--color-black-opacity-1-5);
    --border-color-base: var(--color-black-opacity-1-5);
    --border-color-light: var(--color-black-opacity-0-9);
    --border-color-lighter: var(--color-black-opacity-0-4);
    --border-color-extra-light: var(--color-black-opacity-0-2);
    --border-color-dark: rgba(var(--color-black-rgb), 14%);
    --border-color-darker: var(--color-black-opacity-2);
    --border-color-none: var(--color-black-opacity-0);
    --border-color-dash: var(--color-black-opacity-1-5);
    --border-color-disabled: var(--color-black-opacity-0-9);
    --border-color-hover: var(--color-primary);
    --border-width: 1px;
    --border-width-base: 1px;
    --border-style: solid;
    --border-style-base: solid;
    --border: 1px solid var(--border-color-base);
    --border-base: 1px solid var(--border-color-base);
    --border-dash: 1px dashed var(--border-color-base);
    --border-hover: 1px solid var(--border-color-hover);
    --scrollbar-opacity: 0;
    --scrollbar-bg-color: #000000;
    --scrollbar-bg-color-webkit: transparent;
    --scrollbar-color: #000000;
    --scrollbar-visible-opacity: 0.15;
    --scrollbar-visible-bg-color-webkit: var(--color-black-opacity-1-5);
    --scrollbar-hover-opacity: 0.25;
    --scrollbar-hover-bg-color: #000000;
    --scrollbar-hover-bg-color-webkit: var(--color-black-opacity-2-5);
    --scrollbar-color-hover: var(--color-black-opacity-2-5);
    --fill-color: #f0f2f5;
    --fill-color-base: var(--color-white);
    --fill-color-light: #f5f7fa;
    --fill-color-lighter: #fafafa;
    --fill-color-extra-light: #fafcff;
    --fill-color-dark: #ebedf0;
    --fill-color-darker: #e6e8eb;
    --fill-color-blank: var(--color-white);
    --fill-color-primary: var(--color-black-opacity-6-5);
    --fill-color-secondary: var(--color-black-opacity-4-5);
    --fill-color-placeholder: var(--color-black-opacity-2-5);
    --box-shadow: 0px 12px 32px 4px rgba(0, 0, 0, 0.04), 0px 8px 20px rgba(0, 0, 0, 0.08);
    --box-shadow-base: 0px 2px 8px 0px var(--color-black-opacity-1-5);
    --box-shadow-bottom-select: 0px 2px 8px 0px var(--box-shadow-color-base);
    --box-shadow-bottom: 0px 4px 12px 0px var(--box-shadow-color-base);
    --box-shadow-left: -2px 0px 8px 0px var(--box-shadow-color-base);
    --box-shadow-right: 2px 0px 8px 0px var(--box-shadow-color-base);
    --box-shadow-top: 0px -2px 8px 0px var(--box-shadow-color-base);
    --box-shadow-input-focus: 0px 0px 0px 2px var(--color-primary-opacity-2-5);
    --box-shadow-light: 0px 0px 12px rgba(var(--color-black-rgb), 12%);
    --box-shadow-lighter: 0px 0px 6px rgba(var(--color-black-rgb), 12%);
    --box-shadow-dark: 0px 16px 48px 16px var(--color-black-opacity-0-8), 0px 12px 32px rgba(var(--color-black-rgb), 12%), 0px 8px 16px -8px rgba(var(--color-black-rgb), 16%);
    --disabled-bg-color: var(--background-color-base);
    --disabled-text-color: var(--color-text-placeholder);
    --disabled-border-color: var(--border-color-light);
    --disabled-fill-color: var(--background-color-base);
    --disabled-color-base: var(--color-text-placeholder);
    --overlay-color: var(--color-black-opacity-8);
    --overlay-color-light: var(--color-black-opacity-7);
    --overlay-color-lighter: var(--color-black-opacity-5);
    --mask-color: var(--color-white-opacity-9);
    --mask-color-extra-light: var(--color-white-opacity-3);
    --table-header-bg-color: var(--color-primary-light-9);
    --table-row-hover-bg-color: var(--color-primary-light-9);
    --table-row-striped: var(--color-primary-light-9-5);
}
```

### 深色主题

点击查看代码片段

```scss
.dark,
html.dark,
[data-theme^="dark"] {
    color-scheme: dark;

    --color-primary: #1890ff;
    --color-primary-rgb: 24, 144, 255;
    --color-primary-light-1: #2f9bff;
    --color-primary-light-2: #46a6ff;
    --color-primary-light-3: #5db1ff;
    --color-primary-light-4: #74bcff;
    --color-primary-light-5: #8cc8ff;
    --color-primary-light-6: #a3d3ff;
    --color-primary-light-7: #badeff;
    --color-primary-light-8: #d1e9ff;
    --color-primary-light-9: #e8f4ff;
    --color-primary-light-0-5: #2496ff;
    --color-primary-light-1-5: #3ba1ff;
    --color-primary-light-2-5: #52acff;
    --color-primary-light-3-5: #69b7ff;
    --color-primary-light-4-5: #80c2ff;
    --color-primary-light-5-5: #97cdff;
    --color-primary-light-6-5: #aed8ff;
    --color-primary-light-7-5: #c5e3ff;
    --color-primary-light-8-5: #dceeff;
    --color-primary-light-9-5: #f3f9ff;
    --color-primary-dark-1: #1682e6;
    --color-primary-dark-2: #1373cc;
    --color-primary-dark-3: #1165b3;
    --color-primary-dark-4: #0e5699;
    --color-primary-dark-5: #0c4880;
    --color-primary-dark-6: #0a3a66;
    --color-primary-dark-7: #072b4d;
    --color-primary-dark-8: #051d33;
    --color-primary-dark-9: #020e1a;
    --color-primary-dark-0-5: #1789f2;
    --color-primary-dark-1-5: #147ad9;
    --color-primary-dark-2-5: #126cbf;
    --color-primary-dark-3-5: #105ea6;
    --color-primary-dark-4-5: #0d4f8c;
    --color-primary-dark-5-5: #0b4173;
    --color-primary-dark-6-5: #083259;
    --color-primary-dark-7-5: #062440;
    --color-primary-dark-8-5: #041626;
    --color-primary-dark-9-5: #01070d;
    --color-primary-opacity-0: rgba(24, 144, 255, 0);
    --color-primary-opacity-0-1: rgba(24, 144, 255, 0.01);
    --color-primary-opacity-0-2: rgba(24, 144, 255, 0.02);
    --color-primary-opacity-0-3: rgba(24, 144, 255, 0.03);
    --color-primary-opacity-0-4: rgba(24, 144, 255, 0.04);
    --color-primary-opacity-0-5: rgba(24, 144, 255, 0.05);
    --color-primary-opacity-0-6: rgba(24, 144, 255, 0.06);
    --color-primary-opacity-0-7: rgba(24, 144, 255, 0.07);
    --color-primary-opacity-0-8: rgba(24, 144, 255, 0.08);
    --color-primary-opacity-0-9: rgba(24, 144, 255, 0.09);
    --color-primary-opacity-1: rgba(24, 144, 255, 0.1);
    --color-primary-opacity-2: rgba(24, 144, 255, 0.2);
    --color-primary-opacity-3: rgba(24, 144, 255, 0.3);
    --color-primary-opacity-4: rgba(24, 144, 255, 0.4);
    --color-primary-opacity-5: rgba(24, 144, 255, 0.5);
    --color-primary-opacity-6: rgba(24, 144, 255, 0.6);
    --color-primary-opacity-7: rgba(24, 144, 255, 0.7);
    --color-primary-opacity-8: rgba(24, 144, 255, 0.8);
    --color-primary-opacity-9: rgba(24, 144, 255, 0.9);
    --color-primary-opacity-1-5: rgba(24, 144, 255, 0.15);
    --color-primary-opacity-2-5: rgba(24, 144, 255, 0.25);
    --color-primary-opacity-3-5: rgba(24, 144, 255, 0.35);
    --color-primary-opacity-4-5: rgba(24, 144, 255, 0.45);
    --color-primary-opacity-5-5: rgba(24, 144, 255, 0.55);
    --color-primary-opacity-6-5: rgba(24, 144, 255, 0.65);
    --color-primary-opacity-7-5: rgba(24, 144, 255, 0.75);
    --color-primary-opacity-8-5: rgba(24, 144, 255, 0.85);
    --color-primary-opacity-9-5: rgba(24, 144, 255, 0.95);
    --color-primary-lighter: var(--color-primary-light-9);
    --color-primary-assist-1: var(--color-primary-opacity-1);
    --color-primary-assist-2: var(--color-primary-light-1-5);
    --color-primary-assist-3: var(--color-primary-light-2-5);
    --color-primary-assist-4: var(--color-primary-light-4);
    --color-primary-assist-5: var(--color-primary-light-3);
    --color-success: #49aa19;
    --color-success-rgb: 73, 170, 25;
    --color-success-light-1: #5bb330;
    --color-success-light-2: #6dbb47;
    --color-success-light-3: #80c45e;
    --color-success-light-4: #92cc75;
    --color-success-light-5: #a4d58c;
    --color-success-light-6: #b6dda3;
    --color-success-light-7: #c8e6ba;
    --color-success-light-8: #dbeed1;
    --color-success-light-9: #edf7e8;
    --color-success-light-0-5: #52ae25;
    --color-success-light-1-5: #64b73c;
    --color-success-light-2-5: #77bf53;
    --color-success-light-3-5: #89c86a;
    --color-success-light-4-5: #9bd081;
    --color-success-light-5-5: #add998;
    --color-success-light-6-5: #bfe1af;
    --color-success-light-7-5: #d2eac6;
    --color-success-light-8-5: #e4f2dd;
    --color-success-light-9-5: #f6fbf4;
    --color-success-dark-1: #429917;
    --color-success-dark-2: #3a8814;
    --color-success-dark-3: #337712;
    --color-success-dark-4: #2c660f;
    --color-success-dark-5: #25550d;
    --color-success-dark-6: #1d440a;
    --color-success-dark-7: #163308;
    --color-success-dark-8: #0f2205;
    --color-success-dark-9: #071103;
    --color-success-dark-0-5: #45a218;
    --color-success-dark-1-5: #3e9115;
    --color-success-dark-2-5: #378013;
    --color-success-dark-3-5: #2f6f10;
    --color-success-dark-4-5: #285e0e;
    --color-success-dark-5-5: #214d0b;
    --color-success-dark-6-5: #1a3c09;
    --color-success-dark-7-5: #122b06;
    --color-success-dark-8-5: #0b1a04;
    --color-success-dark-9-5: #040901;
    --color-success-opacity-0: rgba(73, 170, 25, 0);
    --color-success-opacity-0-1: rgba(73, 170, 25, 0.01);
    --color-success-opacity-0-2: rgba(73, 170, 25, 0.02);
    --color-success-opacity-0-3: rgba(73, 170, 25, 0.03);
    --color-success-opacity-0-4: rgba(73, 170, 25, 0.04);
    --color-success-opacity-0-5: rgba(73, 170, 25, 0.05);
    --color-success-opacity-0-6: rgba(73, 170, 25, 0.06);
    --color-success-opacity-0-7: rgba(73, 170, 25, 0.07);
    --color-success-opacity-0-8: rgba(73, 170, 25, 0.08);
    --color-success-opacity-0-9: rgba(73, 170, 25, 0.09);
    --color-success-opacity-1: rgba(73, 170, 25, 0.1);
    --color-success-opacity-2: rgba(73, 170, 25, 0.2);
    --color-success-opacity-3: rgba(73, 170, 25, 0.3);
    --color-success-opacity-4: rgba(73, 170, 25, 0.4);
    --color-success-opacity-5: rgba(73, 170, 25, 0.5);
    --color-success-opacity-6: rgba(73, 170, 25, 0.6);
    --color-success-opacity-7: rgba(73, 170, 25, 0.7);
    --color-success-opacity-8: rgba(73, 170, 25, 0.8);
    --color-success-opacity-9: rgba(73, 170, 25, 0.9);
    --color-success-opacity-1-5: rgba(73, 170, 25, 0.15);
    --color-success-opacity-2-5: rgba(73, 170, 25, 0.25);
    --color-success-opacity-3-5: rgba(73, 170, 25, 0.35);
    --color-success-opacity-4-5: rgba(73, 170, 25, 0.45);
    --color-success-opacity-5-5: rgba(73, 170, 25, 0.55);
    --color-success-opacity-6-5: rgba(73, 170, 25, 0.65);
    --color-success-opacity-7-5: rgba(73, 170, 25, 0.75);
    --color-success-opacity-8-5: rgba(73, 170, 25, 0.85);
    --color-success-opacity-9-5: rgba(73, 170, 25, 0.95);
    --color-success-lighter: var(--color-success-light-9);
    --color-success-assist-1: var(--color-success-opacity-1);
    --color-success-assist-2: var(--color-success-light-1-5);
    --color-success-assist-3: var(--color-success-light-2-5);
    --color-success-assist-4: var(--color-success-light-4);
    --color-success-assist-5: var(--color-success-light-3);
    --color-warning: #d89614;
    --color-warning-rgb: 216, 150, 20;
    --color-warning-light-1: #dca12c;
    --color-warning-light-2: #e0ab43;
    --color-warning-light-3: #e4b65b;
    --color-warning-light-4: #e8c072;
    --color-warning-light-5: #eccb8a;
    --color-warning-light-6: #efd5a1;
    --color-warning-light-7: #f3e0b9;
    --color-warning-light-8: #f7ead0;
    --color-warning-light-9: #fbf5e8;
    --color-warning-light-0-5: #da9b20;
    --color-warning-light-1-5: #dea637;
    --color-warning-light-2-5: #e2b04f;
    --color-warning-light-3-5: #e6bb66;
    --color-warning-light-4-5: #eac57e;
    --color-warning-light-5-5: #edd095;
    --color-warning-light-6-5: #f1daad;
    --color-warning-light-7-5: #f5e5c4;
    --color-warning-light-8-5: #f9efdc;
    --color-warning-light-9-5: #fdfaf3;
    --color-warning-dark-1: #c28712;
    --color-warning-dark-2: #ad7810;
    --color-warning-dark-3: #97690e;
    --color-warning-dark-4: #825a0c;
    --color-warning-dark-5: #6c4b0a;
    --color-warning-dark-6: #563c08;
    --color-warning-dark-7: #412d06;
    --color-warning-dark-8: #2b1e04;
    --color-warning-dark-9: #160f02;
    --color-warning-dark-0-5: #cd8f13;
    --color-warning-dark-1-5: #b88011;
    --color-warning-dark-2-5: #a2710f;
    --color-warning-dark-3-5: #8c620d;
    --color-warning-dark-4-5: #77530b;
    --color-warning-dark-5-5: #614409;
    --color-warning-dark-6-5: #4c3507;
    --color-warning-dark-7-5: #362605;
    --color-warning-dark-8-5: #201703;
    --color-warning-dark-9-5: #0b0801;
    --color-warning-opacity-0: rgba(216, 150, 20, 0);
    --color-warning-opacity-0-1: rgba(216, 150, 20, 0.01);
    --color-warning-opacity-0-2: rgba(216, 150, 20, 0.02);
    --color-warning-opacity-0-3: rgba(216, 150, 20, 0.03);
    --color-warning-opacity-0-4: rgba(216, 150, 20, 0.04);
    --color-warning-opacity-0-5: rgba(216, 150, 20, 0.05);
    --color-warning-opacity-0-6: rgba(216, 150, 20, 0.06);
    --color-warning-opacity-0-7: rgba(216, 150, 20, 0.07);
    --color-warning-opacity-0-8: rgba(216, 150, 20, 0.08);
    --color-warning-opacity-0-9: rgba(216, 150, 20, 0.09);
    --color-warning-opacity-1: rgba(216, 150, 20, 0.1);
    --color-warning-opacity-2: rgba(216, 150, 20, 0.2);
    --color-warning-opacity-3: rgba(216, 150, 20, 0.3);
    --color-warning-opacity-4: rgba(216, 150, 20, 0.4);
    --color-warning-opacity-5: rgba(216, 150, 20, 0.5);
    --color-warning-opacity-6: rgba(216, 150, 20, 0.6);
    --color-warning-opacity-7: rgba(216, 150, 20, 0.7);
    --color-warning-opacity-8: rgba(216, 150, 20, 0.8);
    --color-warning-opacity-9: rgba(216, 150, 20, 0.9);
    --color-warning-opacity-1-5: rgba(216, 150, 20, 0.15);
    --color-warning-opacity-2-5: rgba(216, 150, 20, 0.25);
    --color-warning-opacity-3-5: rgba(216, 150, 20, 0.35);
    --color-warning-opacity-4-5: rgba(216, 150, 20, 0.45);
    --color-warning-opacity-5-5: rgba(216, 150, 20, 0.55);
    --color-warning-opacity-6-5: rgba(216, 150, 20, 0.65);
    --color-warning-opacity-7-5: rgba(216, 150, 20, 0.75);
    --color-warning-opacity-8-5: rgba(216, 150, 20, 0.85);
    --color-warning-opacity-9-5: rgba(216, 150, 20, 0.95);
    --color-warning-lighter: var(--color-warning-light-9);
    --color-warning-assist-1: var(--color-warning-opacity-1);
    --color-warning-assist-2: var(--color-warning-light-1-5);
    --color-warning-assist-3: var(--color-warning-light-2-5);
    --color-warning-assist-4: var(--color-warning-light-4);
    --color-warning-assist-5: var(--color-warning-light-3);
    --color-danger: #a61d24;
    --color-danger-rgb: 166, 29, 36;
    --color-danger-light-1: #af343a;
    --color-danger-light-2: #b84a50;
    --color-danger-light-3: #c16166;
    --color-danger-light-4: #ca777c;
    --color-danger-light-5: #d38e92;
    --color-danger-light-6: #dba5a7;
    --color-danger-light-7: #e4bbbd;
    --color-danger-light-8: #edd2d3;
    --color-danger-light-9: #f6e8e9;
    --color-danger-light-0-5: #aa282f;
    --color-danger-light-1-5: #b33f45;
    --color-danger-light-2-5: #bc565b;
    --color-danger-light-3-5: #c56c71;
    --color-danger-light-4-5: #ce8387;
    --color-danger-light-5-5: #d7999c;
    --color-danger-light-6-5: #e0b0b2;
    --color-danger-light-7-5: #e9c7c8;
    --color-danger-light-8-5: #f2ddde;
    --color-danger-light-9-5: #fbf4f4;
    --color-danger-dark-1: #951a20;
    --color-danger-dark-2: #85171d;
    --color-danger-dark-3: #741419;
    --color-danger-dark-4: #641116;
    --color-danger-dark-5: #530f12;
    --color-danger-dark-6: #420c0e;
    --color-danger-dark-7: #32090b;
    --color-danger-dark-8: #210607;
    --color-danger-dark-9: #110304;
    --color-danger-dark-0-5: #9e1c22;
    --color-danger-dark-1-5: #8d191f;
    --color-danger-dark-2-5: #7d161b;
    --color-danger-dark-3-5: #6c1317;
    --color-danger-dark-4-5: #5b1014;
    --color-danger-dark-5-5: #4b0d10;
    --color-danger-dark-6-5: #3a0a0d;
    --color-danger-dark-7-5: #2a0709;
    --color-danger-dark-8-5: #190405;
    --color-danger-dark-9-5: #080102;
    --color-danger-opacity-0: rgba(166, 29, 36, 0);
    --color-danger-opacity-0-1: rgba(166, 29, 36, 0.01);
    --color-danger-opacity-0-2: rgba(166, 29, 36, 0.02);
    --color-danger-opacity-0-3: rgba(166, 29, 36, 0.03);
    --color-danger-opacity-0-4: rgba(166, 29, 36, 0.04);
    --color-danger-opacity-0-5: rgba(166, 29, 36, 0.05);
    --color-danger-opacity-0-6: rgba(166, 29, 36, 0.06);
    --color-danger-opacity-0-7: rgba(166, 29, 36, 0.07);
    --color-danger-opacity-0-8: rgba(166, 29, 36, 0.08);
    --color-danger-opacity-0-9: rgba(166, 29, 36, 0.09);
    --color-danger-opacity-1: rgba(166, 29, 36, 0.1);
    --color-danger-opacity-2: rgba(166, 29, 36, 0.2);
    --color-danger-opacity-3: rgba(166, 29, 36, 0.3);
    --color-danger-opacity-4: rgba(166, 29, 36, 0.4);
    --color-danger-opacity-5: rgba(166, 29, 36, 0.5);
    --color-danger-opacity-6: rgba(166, 29, 36, 0.6);
    --color-danger-opacity-7: rgba(166, 29, 36, 0.7);
    --color-danger-opacity-8: rgba(166, 29, 36, 0.8);
    --color-danger-opacity-9: rgba(166, 29, 36, 0.9);
    --color-danger-opacity-1-5: rgba(166, 29, 36, 0.15);
    --color-danger-opacity-2-5: rgba(166, 29, 36, 0.25);
    --color-danger-opacity-3-5: rgba(166, 29, 36, 0.35);
    --color-danger-opacity-4-5: rgba(166, 29, 36, 0.45);
    --color-danger-opacity-5-5: rgba(166, 29, 36, 0.55);
    --color-danger-opacity-6-5: rgba(166, 29, 36, 0.65);
    --color-danger-opacity-7-5: rgba(166, 29, 36, 0.75);
    --color-danger-opacity-8-5: rgba(166, 29, 36, 0.85);
    --color-danger-opacity-9-5: rgba(166, 29, 36, 0.95);
    --color-danger-lighter: var(--color-danger-light-9);
    --color-danger-assist-1: var(--color-danger-opacity-1);
    --color-danger-assist-2: var(--color-danger-light-1-5);
    --color-danger-assist-3: var(--color-danger-light-2-5);
    --color-danger-assist-4: var(--color-danger-light-4);
    --color-danger-assist-5: var(--color-danger-light-3);
    --color-error: #a61d24;
    --color-error-rgb: 166, 29, 36;
    --color-error-light-1: #af343a;
    --color-error-light-2: #b84a50;
    --color-error-light-3: #c16166;
    --color-error-light-4: #ca777c;
    --color-error-light-5: #d38e92;
    --color-error-light-6: #dba5a7;
    --color-error-light-7: #e4bbbd;
    --color-error-light-8: #edd2d3;
    --color-error-light-9: #f6e8e9;
    --color-error-light-0-5: #aa282f;
    --color-error-light-1-5: #b33f45;
    --color-error-light-2-5: #bc565b;
    --color-error-light-3-5: #c56c71;
    --color-error-light-4-5: #ce8387;
    --color-error-light-5-5: #d7999c;
    --color-error-light-6-5: #e0b0b2;
    --color-error-light-7-5: #e9c7c8;
    --color-error-light-8-5: #f2ddde;
    --color-error-light-9-5: #fbf4f4;
    --color-error-dark-1: #951a20;
    --color-error-dark-2: #85171d;
    --color-error-dark-3: #741419;
    --color-error-dark-4: #641116;
    --color-error-dark-5: #530f12;
    --color-error-dark-6: #420c0e;
    --color-error-dark-7: #32090b;
    --color-error-dark-8: #210607;
    --color-error-dark-9: #110304;
    --color-error-dark-0-5: #9e1c22;
    --color-error-dark-1-5: #8d191f;
    --color-error-dark-2-5: #7d161b;
    --color-error-dark-3-5: #6c1317;
    --color-error-dark-4-5: #5b1014;
    --color-error-dark-5-5: #4b0d10;
    --color-error-dark-6-5: #3a0a0d;
    --color-error-dark-7-5: #2a0709;
    --color-error-dark-8-5: #190405;
    --color-error-dark-9-5: #080102;
    --color-error-opacity-0: rgba(166, 29, 36, 0);
    --color-error-opacity-0-1: rgba(166, 29, 36, 0.01);
    --color-error-opacity-0-2: rgba(166, 29, 36, 0.02);
    --color-error-opacity-0-3: rgba(166, 29, 36, 0.03);
    --color-error-opacity-0-4: rgba(166, 29, 36, 0.04);
    --color-error-opacity-0-5: rgba(166, 29, 36, 0.05);
    --color-error-opacity-0-6: rgba(166, 29, 36, 0.06);
    --color-error-opacity-0-7: rgba(166, 29, 36, 0.07);
    --color-error-opacity-0-8: rgba(166, 29, 36, 0.08);
    --color-error-opacity-0-9: rgba(166, 29, 36, 0.09);
    --color-error-opacity-1: rgba(166, 29, 36, 0.1);
    --color-error-opacity-2: rgba(166, 29, 36, 0.2);
    --color-error-opacity-3: rgba(166, 29, 36, 0.3);
    --color-error-opacity-4: rgba(166, 29, 36, 0.4);
    --color-error-opacity-5: rgba(166, 29, 36, 0.5);
    --color-error-opacity-6: rgba(166, 29, 36, 0.6);
    --color-error-opacity-7: rgba(166, 29, 36, 0.7);
    --color-error-opacity-8: rgba(166, 29, 36, 0.8);
    --color-error-opacity-9: rgba(166, 29, 36, 0.9);
    --color-error-opacity-1-5: rgba(166, 29, 36, 0.15);
    --color-error-opacity-2-5: rgba(166, 29, 36, 0.25);
    --color-error-opacity-3-5: rgba(166, 29, 36, 0.35);
    --color-error-opacity-4-5: rgba(166, 29, 36, 0.45);
    --color-error-opacity-5-5: rgba(166, 29, 36, 0.55);
    --color-error-opacity-6-5: rgba(166, 29, 36, 0.65);
    --color-error-opacity-7-5: rgba(166, 29, 36, 0.75);
    --color-error-opacity-8-5: rgba(166, 29, 36, 0.85);
    --color-error-opacity-9-5: rgba(166, 29, 36, 0.95);
    --color-error-lighter: var(--color-error-light-9);
    --color-error-assist-1: var(--color-error-opacity-1);
    --color-error-assist-2: var(--color-error-light-1-5);
    --color-error-assist-3: var(--color-error-light-2-5);
    --color-error-assist-4: var(--color-error-light-4);
    --color-error-assist-5: var(--color-error-light-3);
    --color-info: rgba(0, 0, 0, 0.45);
    --color-info-rgb: 0, 0, 0;
    --color-info-light-1: rgba(71, 71, 71, 0.505);
    --color-info-light-2: rgba(118, 118, 118, 0.56);
    --color-info-light-3: rgba(152, 152, 152, 0.615);
    --color-info-light-4: rgba(178, 178, 178, 0.67);
    --color-info-light-5: rgba(198, 198, 198, 0.725);
    --color-info-light-6: rgba(214, 214, 214, 0.78);
    --color-info-light-7: rgba(227, 227, 227, 0.835);
    --color-info-light-8: rgba(238, 238, 238, 0.89);
    --color-info-light-9: rgba(247, 247, 247, 0.945);
    --color-info-light-0-5: rgba(39, 39, 39, 0.4775);
    --color-info-light-1-5: rgba(96, 96, 96, 0.5325);
    --color-info-light-2-5: rgba(136, 136, 136, 0.5875);
    --color-info-light-3-5: rgba(166, 166, 166, 0.6425);
    --color-info-light-4-5: rgba(188, 188, 188, 0.6975);
    --color-info-light-5-5: rgba(206, 206, 206, 0.7525);
    --color-info-light-6-5: rgba(221, 221, 221, 0.8075);
    --color-info-light-7-5: rgba(233, 233, 233, 0.8625);
    --color-info-light-8-5: rgba(243, 243, 243, 0.9175);
    --color-info-light-9-5: rgba(251, 251, 251, 0.9725);
    --color-info-dark-1: rgba(0, 0, 0, 0.505);
    --color-info-dark-2: rgba(0, 0, 0, 0.56);
    --color-info-dark-3: rgba(0, 0, 0, 0.615);
    --color-info-dark-4: rgba(0, 0, 0, 0.67);
    --color-info-dark-5: rgba(0, 0, 0, 0.725);
    --color-info-dark-6: rgba(0, 0, 0, 0.78);
    --color-info-dark-7: rgba(0, 0, 0, 0.835);
    --color-info-dark-8: rgba(0, 0, 0, 0.89);
    --color-info-dark-9: rgba(0, 0, 0, 0.945);
    --color-info-dark-0-5: rgba(0, 0, 0, 0.4775);
    --color-info-dark-1-5: rgba(0, 0, 0, 0.5325);
    --color-info-dark-2-5: rgba(0, 0, 0, 0.5875);
    --color-info-dark-3-5: rgba(0, 0, 0, 0.6425);
    --color-info-dark-4-5: rgba(0, 0, 0, 0.6975);
    --color-info-dark-5-5: rgba(0, 0, 0, 0.7525);
    --color-info-dark-6-5: rgba(0, 0, 0, 0.8075);
    --color-info-dark-7-5: rgba(0, 0, 0, 0.8625);
    --color-info-dark-8-5: rgba(0, 0, 0, 0.9175);
    --color-info-dark-9-5: rgba(0, 0, 0, 0.9725);
    --color-info-opacity-0: rgba(0, 0, 0, 0);
    --color-info-opacity-0-1: rgba(0, 0, 0, 0.01);
    --color-info-opacity-0-2: rgba(0, 0, 0, 0.02);
    --color-info-opacity-0-3: rgba(0, 0, 0, 0.03);
    --color-info-opacity-0-4: rgba(0, 0, 0, 0.04);
    --color-info-opacity-0-5: rgba(0, 0, 0, 0.05);
    --color-info-opacity-0-6: rgba(0, 0, 0, 0.06);
    --color-info-opacity-0-7: rgba(0, 0, 0, 0.07);
    --color-info-opacity-0-8: rgba(0, 0, 0, 0.08);
    --color-info-opacity-0-9: rgba(0, 0, 0, 0.09);
    --color-info-opacity-1: rgba(0, 0, 0, 0.1);
    --color-info-opacity-2: rgba(0, 0, 0, 0.2);
    --color-info-opacity-3: rgba(0, 0, 0, 0.3);
    --color-info-opacity-4: rgba(0, 0, 0, 0.4);
    --color-info-opacity-5: rgba(0, 0, 0, 0.5);
    --color-info-opacity-6: rgba(0, 0, 0, 0.6);
    --color-info-opacity-7: rgba(0, 0, 0, 0.7);
    --color-info-opacity-8: rgba(0, 0, 0, 0.8);
    --color-info-opacity-9: rgba(0, 0, 0, 0.9);
    --color-info-opacity-1-5: rgba(0, 0, 0, 0.15);
    --color-info-opacity-2-5: rgba(0, 0, 0, 0.25);
    --color-info-opacity-3-5: rgba(0, 0, 0, 0.35);
    --color-info-opacity-4-5: rgba(0, 0, 0, 0.45);
    --color-info-opacity-5-5: rgba(0, 0, 0, 0.55);
    --color-info-opacity-6-5: rgba(0, 0, 0, 0.65);
    --color-info-opacity-7-5: rgba(0, 0, 0, 0.75);
    --color-info-opacity-8-5: rgba(0, 0, 0, 0.85);
    --color-info-opacity-9-5: rgba(0, 0, 0, 0.95);
    --color-info-lighter: var(--color-info-light-9);
    --color-info-assist-1: var(--color-info-opacity-1);
    --color-info-assist-2: var(--color-info-light-1-5);
    --color-info-assist-3: var(--color-info-light-2-5);
    --color-info-assist-4: var(--color-info-light-4);
    --color-info-assist-5: var(--color-info-light-3);
    --color-text-light: var(--color-white);
    --color-text-primary: var(--color-white-opacity-8-5);
    --color-text-regular: var(--color-white-opacity-6-5);
    --color-text-secondary: var(--color-white-opacity-4-5);
    --color-text-placeholder: var(--color-white-opacity-3);
    --color-text-mark: var(--color-white-opacity-1-5);
    --color-text-shadow: var(--color-white-opacity-0-9);
    --color-text-light-darken: var(--color-white-opacity-4);
    --color-text-disabled: var(--color-white-opacity-3);
    --color-text-light-reverse: var(--color-black);
    --color-text-primary-reverse: var(--color-black-opacity-8-5);
    --color-text-regular-reverse: var(--color-black-opacity-6-5);
    --color-text-secondary-reverse: var(--color-black-opacity-4-5);
    --color-text-placeholder-reverse: var(--color-black-opacity-2-5);
    --color-text-mark-reverse: var(--color-black-opacity-1-5);
    --color-text-shadow-reverse: var(--color-black-opacity-0-9);
    --color-text-light-darken-reverse: var(--color-black-opacity-5);
    --color-text-disabled-reverse: var(--color-black-opacity-2-5);
    --background-color: #233048;
    --background-color-page: #18202f;
    --background-color-base: var(--color-white-opacity-0-8);
    --background-color-light: var(--color-white-opacity-0-4);
    --background-color-primary: #1e293e;
    --background-color-dialog: #233048;
    --background-color-overlay: #233048;
    --border-color: var(--color-white-opacity-2);
    --border-color-base: var(--color-white-opacity-2);
    --border-color-light: rgba(var(--color-white-rgb), 12%);
    --border-color-lighter: var(--color-white-opacity-0-4);
    --border-color-extra-light: var(--color-white-opacity-0-2);
    --border-color-dark: rgba(var(--color-white-rgb), 14%);
    --border-color-darker: var(--color-white-opacity-2);
    --border-color-none: var(--color-white-opacity-0);
    --border-color-dash: rgba(var(--color-white-rgb), 12%);
    --border-color-disabled: var(--color-white-opacity-2);
    --border-color-hover: var(--color-primary);
    --border-width: 1px;
    --border-width-base: 1px;
    --border-style: solid;
    --border-style-base: solid;
    --border: 1px solid var(--border-color-base);
    --border-base: 1px solid var(--border-color-base);
    --border-dash: 1px dashed var(--border-color-base);
    --border-hover: 1px solid var(--border-color-hover);
    --scrollbar-opacity: 0;
    --scrollbar-bg-color: #ffffff;
    --scrollbar-color: #ffffff;
    --scrollbar-bg-color-webkit: transparent;
    --scrollbar-visible-opacity: 0.15;
    --scrollbar-visible-bg-color-webkit: var(--color-white-opacity-1-5);
    --scrollbar-hover-opacity: 0.25;
    --scrollbar-hover-bg-color: #ffffff;
    --scrollbar-color-hover: var(--color-white-opacity-2-5);
    --scrollbar-hover-bg-color-webkit: var(--color-white-opacity-2-5);
    --fill-color: var(--color-white-opacity-1);
    --fill-color-base: var(--color-white);
    --fill-color-light: var(--color-white-opacity-1);
    --fill-color-lighter: var(--color-white-opacity-0-4);
    --fill-color-extra-light: var(--color-white-opacity-0-2);
    --fill-color-dark: var(--color-white-opacity-1-5);
    --fill-color-darker: var(--color-white-opacity-2);
    --fill-color-blank: transparent;
    --fill-color-primary: var(--color-black-opacity-6-5);
    --fill-color-secondary: var(--color-black-opacity-4-5);
    --fill-color-placeholder: var(--color-black-opacity-2-5);
    --box-shadow: 0px 12px 32px 4px rgba(0, 0, 0, 0.04), 0px 8px 20px rgba(0, 0, 0, 0.08);
    --box-shadow-base: 0px 2px 8px 0px var(--color-black-opacity-2);
    --box-shadow-bottom-select: 0px 2px 8px 0px var(--box-shadow-color-base);
    --box-shadow-bottom: 0px 4px 12px 0px var(--box-shadow-color-base);
    --box-shadow-left: -2px 0px 8px 0px var(--box-shadow-color-base);
    --box-shadow-right: 2px 0px 8px 0px var(--box-shadow-color-base);
    --box-shadow-top: 0px -2px 8px 0px var(--box-shadow-color-base);
    --box-shadow-input-focus: 0px 0px 0px 2px var(--color-primary-opacity-2-5);
    --box-shadow-light: 0px 0px 12px rgba(var(--color-black-rgb), 12%);
    --box-shadow-lighter: 0px 0px 6px rgba(var(--color-black-rgb), 12%);
    --box-shadow-dark: 0px 16px 48px 16px var(--color-black-opacity-0-8), 0px 12px 32px rgba(var(--color-black-rgb), 12%), 0px 8px 16px -8px rgba(var(--color-black-rgb), 16%);
    --disabled-bg-color: var(--background-color-base);
    --disabled-text-color: var(--color-text-placeholder);
    --disabled-border-color: var(--border-color-light);
    --disabled-fill-color: var(--background-color-base);
    --disabled-color-base: var(--color-text-placeholder);
    --overlay-color: var(--color-black-opacity-8);
    --overlay-color-light: var(--color-black-opacity-7);
    --overlay-color-lighter: var(--color-black-opacity-5);
    --mask-color: var(--color-white-opacity-9);
    --mask-color-extra-light: var(--color-white-opacity-3);
    --table-header-bg-color: var(--color-primary-dark-9);
    --table-row-hover-bg-color: var(--color-primary-dark-9);
    --table-row-striped: var(--color-primary-dark-8);
}
```
