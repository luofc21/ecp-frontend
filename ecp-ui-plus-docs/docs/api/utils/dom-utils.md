<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/api/utils/dom-utils.html -->

# DomUtils 节点相关

> Dom 节点相关辅助方法。

```js
import { DomUtils } from '@ecp/ecp-ui-plus';
```

## on

绑定事件

```js
DomUtils.on(element, event, handler);
```

- **入参**

  - `HTMLElement` element: Dom 元素
  - `String` event: 事件名称
  - `Function` handler: 事件处理函数
- **返回**

  - 无

## off

解绑事件

```js
DomUtils.off(element, event, handler);
```

- **入参**

  - `HTMLElement` element: Dom 元素
  - `String` event: 事件名称
  - `Function` handler: 事件处理函数
- **返回**

  - 无

## once

绑定一次性事件

- **入参**

  - `HTMLElement` element: Dom 元素
  - `String` event: 事件名称
  - `Function` handler: 事件处理函数
- **返回**

  - 无
