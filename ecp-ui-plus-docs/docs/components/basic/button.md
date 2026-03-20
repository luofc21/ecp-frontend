<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/basic/button.html -->

# <ecp-button> 按钮

> 基于el-button 封装的按钮。

## Attributes

| 参数 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| type | 按钮风格（同 el-button 的 type） | string | primary / success / warning / danger / info / text | -- |
| size | 按钮的大小 （同 el-button 的 size） | string | default / large / small | -- |
| text | 文字按钮的内容 | string |  | -- |
| regular | icon+文字按钮(常态下字体颜色是正文色，非主色) （需要配合使用 type=text 属性） | boolean | -- | false |
| horizontal | 是否横向排列按钮图标与文字 （需要配合 regular 属性） | boolean | -- | false |
| dashed | 是否虚线按钮 （需要配合使用 plain 属性，将 plain 属性设置为 true） | boolean | -- | false |
| plain | 是否朴素按钮（同 el-button 的 plain） | boolean | -- | false |
| round | 是否圆角按钮（同 el-button 的 round） | boolean | -- | false |
| circle | 是否圆形按钮（同 el-button 的 circle） | boolean | -- | false |
| loading | 是否加载中状态（同 el-button 的 loading） | boolean | -- | false |
| disabled | 是否禁用状态（同 el-button 的 disabled） | boolean | -- | false |
| icon | 图标类名(不再支持svg格式图标) | string | -- | -- |
| title | icon 的 title | string | -- | -- |
| font-size | iconfont 的 font-size 值（默认单位 px） | string | -- | 14 |
