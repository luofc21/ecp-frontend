<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/form/form.html -->

# <el-form> 表单

> - 由输入框、选择器、单选框、多选框等控件组成，用以收集、校验、提交数据。
> - 表单布局：
>   - 两列、三列固定式表单布局，见 [Layouts 布局类名 - 表单相关](/ecp-ui-plus/docs/design/layouts.html#表单相关)；
>   - 响应式检索表单布局，见 [Query-row 基础检索条件容器](/ecp-ui-plus/docs/components/layout/query-row.html)。

## 典型表单

包括各种表单项，比如输入框、选择器、开关、单选框、多选框等。

在 Form 组件中，每一个表单域由一个 Form-Item 组件构成，表单域中可以放置各种类型的表单控件，包括 Input、Select、Checkbox、Radio、Switch、DatePicker、TimePicker

- W3C 标准中有如下 [规定](https://www.w3.org/MarkUp/html-spec/html-spec_8.html#SEC8.2)：*When there is only one single-line text input field in a form, the user agent should accept Enter in that field as a request to submit the form.*
- 即：当一个 form 元素中只有一个输入框时，在该输入框中按下回车应提交该表单。如果希望阻止这一默认行为，可以在 `<el-form>` 标签上添加 `@submit.native.prevent`。

## 表单验证

在防止用户犯错的前提下，尽可能让用户更早地发现并纠正错误。

Form 组件提供了表单验证的功能，只需要通过 `rules` 属性传入约定的验证规则，并将 Form-Item 的 `prop` 属性设置为需校验的字段名即可。校验规则参见 [async-validator](https://github.com/yiminghe/async-validator)

## 自定义校验规则

这个例子中展示了如何使用自定义验证规则来完成密码的二次验证。

本例还使用`status-icon`属性为输入框添加了表示校验结果的反馈图标。

- 自定义校验 callback 必须被调用；
- 更多高级用法可参考 [async-validator](https://github.com/yiminghe/async-validator)。

## 动态增减表单项

> 除了在 Form 组件上一次性传递所有的验证规则外还可以在单个的表单域上传递属性的验证规则。

## 数字类型验证

> 数字类型的验证需要在 `v-model` 处加上 `.number` 的修饰符，这是 `Vue` 自身提供的用于将绑定值转化为 `number` 类型的修饰符。

## Form Api

### Form Attributes

见 [ElementPlus - Form Attributes](https://element-plus.gitee.io/zh-CN/component/form.html#form-attributes)

### Form Events

见 [ElementPlus - Form 事件](https://element-plus.gitee.io/zh-CN/component/form.html#form-%E4%BA%8B%E4%BB%B6)

### Form Slots

见 [ElementPlus - Form Slots](https://element-plus.gitee.io/zh-CN/component/form.html#form-slots)

### Form Exposes

见 [ElementPlus - Form Exposes](https://element-plus.gitee.io/zh-CN/component/form.html#form-exposes)

## Form-Item Api

### Form-Item Attributes

见 [ElementPlus - FormItem Attributes](https://element-plus.gitee.io/zh-CN/component/form.html#formitem-attributes)

### Form-Item Slots

见 [ElementPlus - FormItem Slots](https://element-plus.gitee.io/zh-CN/component/form.html#formitem-slots)

### Form-Item Exposes

见 [ElementPlus - FormItem Exposes](https://element-plus.gitee.io/zh-CN/component/form.html#formitem-exposes)
