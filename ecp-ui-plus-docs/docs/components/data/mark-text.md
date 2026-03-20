<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/data/mark-text.html -->

# <ecp-mark-text> 文本标记

> - 用于突出显示文段中命中的关键词；
> - 使用 [split(RegExp)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/split#%E4%BD%BF%E7%94%A8_regexp_%E6%9D%A5%E5%88%86%E5%89%B2%E4%BD%BF%E7%BB%93%E6%9E%9C%E4%B8%AD%E5%8C%85%E5%90%AB%E5%88%86%E5%89%B2%E7%AC%A6) 分割文本、[match(RegExp)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/match) 匹配关键词，请注意正则使用问题。

温馨提示

包裹复合组件 (`EcpButtonGroup` 、 `ElTable`...之类) 或者多组件嵌套组合时，如果插槽已更新，但未正确展示更新后的内容的，请为 `EcpMarkText` 组件添加 `key`，以触发组件响应式更新。

## 基础用法

> - 直接传入关键词字符串使用；
> - 字符串会组装为 `/(关键词)/` 形式的正则表达式；
>   - 不符合正则规则的字符串会转义处理；
>   - 如果需要将正则特殊字符作为普通字符匹配，请自行转义处理。

## 使用自定义正则

> 匹配关键词也可以传入自定义正则。

## 嵌套组件

> 标记简单组件，可直接包裹使用。

## 使用自定义函数

> - 匹配关键词也可以传入 `Function`，来自定义文本切割与匹配处理；
>   - 需要返回 `[{ text: string, matched: boolean }]` 格式的数组，参考示例代码；
> - 使用复合组件或者多组件嵌套时，需要在 `EcpMarkText` 添加 key。

## Attributes

| 参数 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| keywords | 匹配关键词 | String / RegExp / Function |  |
| selector | 指定组件内的关键词匹配 DOM，默认不指定 | HTMLElement / CssSelectorString |  |
| tagName | `EcpMarkText` 组件 DOM 的 tagName | String | 'span' |

## Slots

| 插槽名 | 说明 | 注意事项 |
| --- | --- | --- |
| default | 需要标注的内容或内容元素 |  |

## Style Variables

点击查看默认样式变量

```css
.ecpp-mark-text {
    /* 命中关键词的颜色 */
    --ecpp-mark-text-color: var(--color-danger);

    /* 命中关键词选中状态的背景颜色 */
    --ecpp-mark-text-selected-bg-color: var(--color-danger-assist-2);
}
```
