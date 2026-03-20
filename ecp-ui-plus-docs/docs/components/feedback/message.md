<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/feedback/message.html -->

# Message 消息提示

> - 在 `ElMessage` 的基础上作样式重置。
> - 常用于主动操作后的反馈提示。 与 Notification 的区别是后者更多用于系统级通知的被动提醒。

## 基础用法

从顶部出现，3 秒后自动消失。

## 不同状态

用来显示「成功、警告、消息、错误」类的操作反馈。

## 可关闭的消息提示

可以添加关闭按钮。

## 文字居中

使用 `center` 属性让文字水平居中。

## 使用 HTML 片段作为正文内容

`message` 还支持使用 HTML 字符串作为正文内容。

WARNING

`message` 属性虽然支持传入 HTML 片段，但是在网站上动态渲染任意 HTML 是非常危险的，因为容易导致 [XSS 攻击](https://en.wikipedia.org/wiki/Cross-site_scripting)。 因此在 `dangerouslyUseHTMLString` 打开的情况下，请确保 `message` 的内容是可信的，**永远不要**将用户提交的内容赋值给 `message` 属性。

## 分组消息合并

合并相同内容的消息。

## 全局方法

Element Plus 为 `app.config.globalProperties` 添加了全局方法 `$message`。 因此在 vue 实例中你可以使用当前页面中的调用方式调用 `Message`

## 单独引用

```js
import { ElMessage } from 'element-plus';
```

此时调用方法为 `ElMessage(options)`。 我们也为每个 type 定义了各自的方法，如 `ElMessage.success(options)`。 并且可以调用 `ElMessage.closeAll()` 手动关闭所有实例。

## 应用程序上下文继承

现在 Message 接受一条 `context` 作为消息构造器的第二个参数，允许你将当前应用的上下文注入到 Message 中，这将允许你继承应用程序的所有属性。

你可以像这样使用它：

TIP

如果您全局注册了 ElMessage 组件，它将自动继承应用的上下文环境。

```js
import { getCurrentInstance } from 'vue';
import { ElMessage } from 'element-plus';

// 在你的 setup 方法中
const { appContext } = getCurrentInstance();
ElMessage({}, appContext);
```

## API

### Message 配置项

见 [ElementPlus - Message 配置项](https://element-plus.gitee.io/zh-CN/component/message.html#message-%E9%85%8D%E7%BD%AE%E9%A1%B9)

### Message 方法

见 [ElementPlus - Message 方法](https://element-plus.gitee.io/zh-CN/component/message.html#message-%E6%96%B9%E6%B3%95)
