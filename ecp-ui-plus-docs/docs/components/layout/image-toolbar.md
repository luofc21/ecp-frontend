<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/layout/image-toolbar.html -->

# <ecp-image-toolbar> 图片操作栏

> - 图片图标操作按钮栏；
> - 沿用 `.elp-image-viewer__actions` 系列样式，并在此基础上拓展；
> - 图片预览、图片裁剪不需要手动使用该组件，仅需传参传进去。

## 基础用法

## 自由搭配

- 以 `<ecp-img-view />` 为例，使用 layout 可以自定义按钮显隐；
- 使用 iconConfig 可以自定义按钮图标参数，详见 [<ecp-icon> 图标](/ecp-ui-plus/docs/components/basic/icon.html)。

## 使用按钮插槽

## Attributes

| 参数 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| type | 操作栏类型， 图片预览类固定 `preview`， 图片裁剪类固定 `cropper`， 可在全局配置 `imageToolbar` 中添加/修改对应类型的属性配置项，会覆盖通用 `imageToolbar` 的默认属性配置项。 | String |  |  |
| effect Global | 操作栏的颜色模式，`不会` 根据主题自动切换 | String | `dark`、`light` | `dark` |
| position Global | 操作栏的位置 | String | `top`、`bottom`、`left`、`right` | `bottom` |
| direction Global | 按钮排列方向 | String | `horizontal`、`vertical` | `horizontal` |
| layout Global | 按钮布局 | String/Array | 见 [layout 可选值](#layout-可选值) |  |
| icon-config Global | 工具项图标配置 | Object | 见 [icon-config 的结构](#icon-config-的结构) |  |

### layout 可选值

| 值 | 说明 |
| --- | --- |
| zoomOut | 缩小 |
| zoomIn | 放大 |
| reset | 重置 |
| mirror | 镜像 |
| counterclockwise | 逆时针旋转 |
| clockwise | 顺时针旋转 |
| download | 下载 |
| refresh | 刷新 |
| ... | 可添加自定义按钮，需要在 icon-config 中添加对应项图标配置 |

### icon-config 的结构

> - 属性名，`String`, layout 对应项：
>   - 如 `zoomOut`；
> - 属性值，`Object`, layout 对应项的图标配置项：
>   - title: `String` 按钮标题；
>   - disabled: `Boolean` 是否禁用；
>   - 其它图标配置项，见 [<ecp-icon> 图标 - Attributes](/ecp-ui-plus/docs/components/basic/icon.html#attributes)；
>   - 还可以添加其它其定义配置项，在 `click-icon` 事件中会一并回传。

点击查看 icon-config 默认值

```js
export const imageToolbar = {
    default: {
        // ...
        iconConfig: {
            zoomOut: {
                icon: 'ecp-icon-zoom-out',
                title: '缩小'
            },
            zoomIn: {
                icon: 'ecp-icon-zoom-in',
                title: '放大'
            },
            reset: {
                icon: 'ecp-icon-one-one',
                title: '重置'
            },
            mirror: {
                icon: 'ecp-icon-mirror',
                title: '镜像'
            },
            counterclockwise: {
                icon: 'ecp-icon-revolve-left',
                title: '逆时针旋转'
            },
            clockwise: {
                icon: 'ecp-icon-revolve-right',
                title: '顺时针旋转'
            },
            download: {
                icon: 'ecp-icon-download',
                title: '下载'
            },
            refresh: {
                icon: 'ecp-icon-refresh',
                title: '刷新'
            }
        }
    },
    preview: {},
    cropper: {}
}
```

## Events

| 事件名称 | 说明 | 回调参数 |
| --- | --- | --- |
| click-icon | 图片操作按钮点击事件， 注意禁用状态的按钮也会触发这个事件，请在业务代码中处理 | action: 点击的 layout 对应项， iconProps: 点击的 layout 对应项的图标配置 |

## Slots

| 插槽名称 | 说明 |
| --- | --- |
| buttons-prepend | 按钮前缀插槽 |
| buttons | 按钮后缀插槽 |

## Style Variables

点击查看默认样式变量

```css
.elp-image-viewer__actions {
    --ecpp-image-toolbar-size: 32px;
    --ecpp-image-toolbar-margin: var(--spacer-large-3);
    --ecpp-image-toolbar-padding: var(--spacer-large);
    --ecpp-image-toolbar-gap: var(--spacer);
    --ecpp-image-toolbar-radius: var(--border-radius-capsule);
    --ecpp-image-toolbar-color: rgba(var(--color-white-rgb), 0.85);
    --ecpp-image-toolbar-bg-color: rgba(var(--color-black-rgb), 0.45);
    --ecpp-image-toolbar-border-color: rgba(var(--color-white-rgb), 0.09);
}

.elp-image-viewer__actions.ecpp-image-toolbar--light {
    --ecpp-image-toolbar-color: rgba(var(--color-black-rgb), 0.85);
    --ecpp-image-toolbar-bg-color: rgba(var(--color-white-rgb), 0.45);
    --ecpp-image-toolbar-border-color: rgba(var(--color-black-rgb), 0.09);
}
```
