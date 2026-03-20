<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/design/colors.html -->

# Colors 色彩表

> - 所有包含在 Material Design 规范中的色彩，都可以通过 `html-class`、 `javascript`、 `css` 及 `css 预编译语言` 应用。

## 命名规则

### 基础规则

每种色彩都会拓展为 `背景`、`文本`、`边框` 等 html-class；

> - #{color}: 指颜色名称，如 red 、 pink 等；
> - #{n}: 指 亮化 lighten / 暗化 darken / 强调 accent 程度，亮化 取值范围为 1~5，暗化 / 强调 取值范围为 1~4，步长 1。

- 背景：`#{color}`；
  - 亮化：`lighten-#{n}`；
  - 暗化：`darken-#{n}`；
  - 强调：`accent-#{n}`；
- 文本：`#{color}--text`；
  - 亮化：`text--lighten-#{n}`；
  - 暗化：`text--darken-#{n}`；
  - 强调：`text--accent-#{n}`；
- 边框：`#{color}--border`；
  - 亮化：`border--lighten-#{n}`；
  - 暗化：`border--darken-#{n}`；
  - 强调：`border--accent-#{n}`。

### 灰度颜色

针对灰度颜色 `brown`、`blue-grey`、`grey`，去除了强调变体。

### CSS 变量

所有非 white、black 的颜色及其所有变体色，都会生成对应的 CSS 变量：

- 基础色：`--material-#{color}`;
  - 亮化：`--material-#{color}-lighten-#{n}`；
  - 暗化：`--material-#{color}-darken-#{n}`；
  - 强调：`--material-#{color}-accent-#{n}`；

### 黑白

针对 white 和 black，去除了亮化、暗化、强调变体，补充了透明度变体：

- 透明度 0.04: `opacity-04`；
- 透明度 0.09: `opacity-09`；
- 透明度 0.15: `opacity-15`；
- 透明度 0.25: `opacity-25`；
- 透明度 0.45: `opacity-45`；
- 透明度 0.65: `opacity-65`；
- 透明度 0.85: `opacity-85`。

## 扩展的 Material 色彩表
