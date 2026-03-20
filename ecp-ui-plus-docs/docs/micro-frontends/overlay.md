<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/micro-frontends/overlay.html -->

# UsePopupZIndex 弹出层级管理

> - 获取、更新全局管理的 z-index 值；
> - `路由式加载` 与 `组件式加载` 均已添加全局弹出层层级维护，一般无需额外调用；
> - 也适用于一般独立应用。

```js
import { usePopupZIndex } from '@ecp/ecp-ui-plus';
const {
    cachedZIndex,
    currentZIndex,
    nextZIndex,
    updateZIndex,
    PopupManagerV1Init,
    PopupManagerV1Reset
} = usePopupZIndex();
```

## 入参

无

## 返回

### cachedZIndex

`Ref<number>` 缓存的 z-index 值。

```js
watch(
    () => cachedZIndex.value,
    (newVal, oldVal) => {
        console.log('cachedZIndex: ', newVal, oldVal);
    }
);
const setZIndexTo99999 = () => {
    cachedZIndex.value = 99999;
};
```

### currentZIndex

`ComputedRef<number>` ElementPlus 当前 z-index 值。

```js
watch(
    () => currentZIndex.value,
    (newVal, oldVal) => {
        console.log('currentZIndex: ', newVal, oldVal);
    }
);
```

### nextZIndex

`Function` 更新并返回下一个 z-index 值。

- **入参**

  - 无
- **返回**

  - `Number` 下一个 z-index 值

```js
const setNextZIndex = () => {
    const index = nextZIndex();
    console.log('Jump To zIndex: ', index);
};
```

### updateZIndex

`Function` 更新 z-index 为指定值。

> - 实际更新值为 `传入的指定值` 、`当前值` 、`缓存值` 三者中的最大值；
> - 为避免自定义组件设置层级直接设为实际更新值，而导致同层级的组件展示被覆盖，`需要更新的缓存值` 与 `返回的实际更新值` 会 `+ 1` 处理。

- **入参**

  - `Number` 指定的 z-index 值
- **返回**

  - `Number` 实际更新值

```js
const setTargetZIndex = () => {
    const index = updateZIndex(5000);
    console.log('zIndex Updated: ', index);
};
```

### PopupManagerV1Init

`Function` 初始化或更新 PopupManager。

> 一般无需调用，主要用于兼容 Ecp-ui 重写覆盖的 Element-ui PopupManager。

- **入参**

  - 无
- **返回**

  - 无

### PopupManagerV1Reset

`Function` 重置 PopupManager。

> 一般无需调用，主要用于处理子应用切换时 PopupManager 内部调用找不到 document.body 的问题。

- **入参**

  - 无
- **返回**

  - 无
