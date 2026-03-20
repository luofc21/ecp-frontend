<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/feedback/loading.html -->

# Loading 加载

> - 重置 `ElLoading` 组件，并覆盖 `v-loading` 指令与 `app.config.globalProperties` 上的全局方法。
> - 用于加载数据时显示动效。

## 局部加载

在需要的时候展示加载动画，防止页面失去响应提高用户体验（例如表格）。

Ecp-ui-plus 提供了两种调用 Loading 的方法：指令和服务。 对于自定义指令 `v-loading`，只需要绑定 `boolean` 值即可。 默认状况下，Loading 遮罩会插入到绑定元素的子节点。 通过添加 `body` 修饰符，可以使遮罩插入至 Dom 中的 body 上。

## 自定义加载中组件内容

你可以自定义加载中组件的文字，图标，以及背景颜色。

在绑定了`v-loading`指令的元素上添加`element-loading-text`属性，其值会被渲染为加载文案，并显示在加载图标的下方。 类似地，`element-loading-spinner`、`element-loading-background` 和 `element-loading-svg` 属性分别用来设定 svg 图标、背景色值、加载图标。

WARNING

虽然 `element-loading-spinner / element-loading-svg` 属性支持传入的 HTML 片段，但是动态在网站上渲染任意的 HTML 是非常危险的，因为很容易导致 [XSS 攻击](https://en.wikipedia.org/wiki/Cross-site_scripting)。 请确保 `element-loading-spinner / element-loading-svg`的内容是可信的， **不要**将用户提交的内容赋值给 `element-loading-spinner / element-loading-svg` 属性。

## 全屏加载

加载数据时显示全屏动画。

- 当使用指令方式时，全屏遮罩需要添加 `fullscreen` 修饰符（遮罩会插入至 body 上） 此时若需要锁定屏幕的滚动，可以使用 `lock` 修饰符；
- 当使用服务方式时，遮罩默认即为全屏，无需额外设置。

## Api 服务方式

Loading 还可以以服务的方式调用。 你可以像这样引入 Loading 服务：

```ts
import { EcpLoading } from '@ecp/ecp-ui-plus'
```

在你需要的时候通过下面的方式调用：

```ts
EcpLoading.service(options)
```

其中 `options` 参数为 Loading 的配置项，具体见 [ElementPlus - Loading 配置项](https://element-plus.gitee.io/zh-CN/component/loading.html#%E9%85%8D%E7%BD%AE%E9%A1%B9)。 `LoadingService` 会返回一个 Loading 实例，可通过调用该实例的 `close` 方法来关闭它：

```ts
const loadingInstance = EcpLoading.service(options)
nextTick(() => {
  // Loading should be closed asynchronously
  loadingInstance.close()
})
```

需要注意的是，以服务的方式调用的全屏 Loading 是单例的。 若在前一个全屏 Loading 关闭前再次调用全屏 Loading，并不会创建一个新的 Loading 实例，而是返回现有全屏 Loading 的实例：

```ts
const loadingInstance1 = EcpLoading.service({ fullscreen: true })
const loadingInstance2 = EcpLoading.service({ fullscreen: true })
console.log(loadingInstance1 === loadingInstance2) // true
```

此时调用它们中任意一个的 `close` 方法都能关闭这个全屏 Loading。

如果完整引入了 Ecp-ui-plus，那么 `app.config.globalProperties` 上会有一个全局方法 `$loading`， 它的调用方式为：`this.$loading(options)`，同样会返回一个 Loading 实例。

## API

### Attributes

见 [ElementPlus - Loading 配置项](https://element-plus.gitee.io/zh-CN/component/loading.html#%E9%85%8D%E7%BD%AE%E9%A1%B9)

### Directive

见 [ElementPlus - Loading 指令](https://element-plus.gitee.io/zh-CN/component/loading.html#%E6%8C%87%E4%BB%A4)
