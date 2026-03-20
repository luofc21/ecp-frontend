<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/api/utils/anchor-utils.html -->

# AnchorUtils 锚点相关

> Anchor 锚点相关辅助方法。

```js
import { AnchorUtils } from '@ecp/ecp-ui-plus';
```

## hasScrollElement

判断一个元素是否是滚动元素

```js
const booleanResult = AnchorUtils.hasScrollElement(element, direction);
```

- **入参**

  - `HTMLElement` element: 需要判断的元素
  - `String` direction: 滚动方向，默认 `vertical` 垂直方向，可选 `vertical` 垂直方向、`horizontal` 水平方向
- **返回**

  - `Boolean` 是否是滚动元素

## getFirstScrollElement

获取从指定元素开始获取的第一个祖先级滚动元素

```js
const element = AnchorUtils.getFirstScrollElement(element, direction);
```

- **入参**

  - `HTMLElement` element: 指定元素
  - `String` direction: 滚动方向，默认 `vertical` 垂直方向，可选 `vertical` 垂直方向、`horizontal` 水平方向
- **返回**

  - `HTMLElement` 从指定元素开始获取的第一个祖先级滚动元素

## edgeTop

计算目标元素距离指定祖先元素的 offsetTop

```js
const numberResult = AnchorUtils.edgeTop(element, direction);
```

- **入参**

  - `HTMLElement` element: 目标 Dom 元素
  - `HTMLElement` targetAncestor: 指定祖先 Dom 元素
- **返回**

  - `Number` offsetTop 数值
