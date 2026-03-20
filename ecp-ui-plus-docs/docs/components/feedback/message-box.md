<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/feedback/message-box.html -->

# MessageBox 消息弹框

> - 在 `ElMessageBox` 的基础上作样式重置。
> - 模拟系统的消息提示框而实现的一套模态对话框组件，用于消息提示、确认消息和提交内容。
> - 从设计上来说，MessageBox 的作用是美化系统自带的 `alert`、`confirm` 和 `prompt`，因此适合展示较为简单的内容。 如果需要弹出较为复杂的内容，请使用 Dialog。

## 消息提示

当用户进行操作时会被触发，该对话框中断用户操作，直到用户确认知晓后才可关闭。

## 确认消息

提示用户确认其已经触发的动作，并询问是否进行此操作时会用到此对话框。

## 提交内容

当需要用户输入内容时，可以使用 Prompt 类型的消息框。

## 使用 VNode

`message` 可以是 VNode。

## 个性化

消息弹框可以被定制来展示各种内容。

## 使用 HTML 片段

`message` 支持传入 HTML 字符串来作为正文内容。

WARNING

`message` 属性虽然支持传入 HTML 片段，但是在网站上动态渲染任意 HTML 是非常危险的，因为容易导致 [XSS 攻击](https://en.wikipedia.org/wiki/Cross-site_scripting)。 因此在 `dangerouslyUseHTMLString` 打开的情况下，请确保 `message` 的内容是可信的，**永远不要**将用户提交的内容赋值给 `message` 属性。

## 区分取消操作与关闭操作

有些场景下，点击取消按钮与点击关闭按钮有着不同的含义。

## 内容居中

消息弹框支持使用居中布局。

## 自定义图标

图标可以使用任意Vue 组件或 [渲染函数 (JSX)](https://vuejs.org/guide/extras/render-function.html)来自定义。

## 可拖放

设置 MessageBox 可以拖拽。

## 全局方法

如果你完整引入了 Element，它会为 `app.config.globalProperties` 添加如下全局方法：`$msgbox`、 `$alert`、 `$confirm` 和 `$prompt`。 因此在 Vue 实例中可以采用本页面中的方式来调用`MessageBox`。 参数如下：

- `$msgbox(options)`
- `$alert(message, title, options)` 或 `$alert(message, options)`
- `$confirm(message, title, options)` 或 `$confirm(message, options)`
- `$prompt(message, title, options)` 或 `$prompt(message, options)`

## 应用程序上下文继承

现在 MessageBox 接受构造器的 `context` 作为第二个(如果你正在使用消息框变量的话) 参数，这个参数允许你将当前应用的上下文注入到消息中，这将允许你继承应用程序的所有属性。

```js
import { getCurrentInstance } from 'vue';
import { ElMessageBox } from 'element-plus';

// 在你的 setup 方法中
const { appContext } = getCurrentInstance();

// 你可以像这样传递参数：
ElMessageBox({}, appContext);
// 或者正在使用不同的调用方式
ElMessageBox.alert('Hello world!', 'Title', {}, appContext);
```

## 按需引入

如果您需要按需引入 `MessageBox`：

```js
import { ElMessageBox } from 'element-plus'
```

那么对应于上述四个全局方法的调用方法依次为：`ElMessageBox`、`ElMessageBox.alert`、`ElMessageBox.confirm` 和 `ElMessageBox.prompt`。参数同上所述。

## API

### 配置项

见 [ElementPlus - MessageBox 配置项](https://element-plus.gitee.io/zh-CN/component/message-box.html#%E9%85%8D%E7%BD%AE%E9%A1%B9)
