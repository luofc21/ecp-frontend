<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/micro-frontends/micro-constants.html -->

# MicroConstants 辅助常量

> 可能会用到的辅助常量，挂载在 MicroUtils 上。

```js
import { MicroUtils } from '@ecp/ecp-ui-plus';
const { constants: MicroConstants } = MicroUtils;
```

## 应用加载相关

### SYMBOL\_REG

路由标记匹配规则，`完全匹配 / (0 或者 1 次) + 字母 (1 个) + 数字 (0 或多次) + - (1 个)`

SYMBOL\_REG<RegExp>

```js
MicroConstants.SYMBOL_REG = /^(\/?[a-z]\d*-)/;
```

### UNI\_PLUGIN\_EXTERNALS

UniPlugin 提供的外部资源

UNI\_PLUGIN\_EXTERNALS<Array>

```js
MicroConstants.UNI_PLUGIN_EXTERNALS = [
    '/externals/vue.min.js',
    '/externals/vue-router.min.js',
    '/externals/vuex.min.js',
    '/externals/lodash.min.js'
];
```

## 菜单相关

### MENU\_TYPE

菜单类型枚举

MENU\_TYPE<Object>

```js
MicroConstants.MENU_TYPE = {
    1: 'router', // 路由跳转
    2: 'iframe', // iframe
    3: 'open', // 新浏览器页签
    4: 'reload' // 重载
};
```

### MENU\_TYPE\_MAP

菜单类型反枚举

MENU\_TYPE\_MAP<Object>

```js
MicroConstants.MENU_TYPE_MAP = {
    router: '1', // 路由跳转
    iframe: '2', // iframe
    open: '3', // 新浏览器页签
    reload: '4' // 重载
};
```

### MENU\_MAP

菜单类型值枚举

MENU\_MAP<Object>

```js
MicroConstants.MENU_MAP = {
    router: 'router', // 路由跳转
    iframe: 'iframe', // iframe
    open: 'open', // 新浏览器页签
    reload: 'reload' // 重载
};
```

## MicroEvent 消息相关

### MESSAGE\_INSTANCE\_STATUS

MicroEvent 消息实例状态

MESSAGE\_INSTANCE\_STATUS<Object>

```js
MicroConstants.MESSAGE_INSTANCE_STATUS = {
    INIT: 'initial', // 初始化
    ACTIVE: 'active', // 活动中
    DESTROYED: 'destroyed' // 已销毁
};
```

### MESSAGE\_TYPE

MicroEvent 分发类型枚举

MESSAGE\_TYPE<Object>

```js
MicroConstants.MESSAGE_TYPE = {
    BROADCAST: 'BROADCAST', // 广播
    CHANNEL: 'CHANNEL', // 特定频道多播
    SINGLE: 'SINGLE' // 指定对象单播
};
```

### MESSAGE\_TYPE\_KEY

MicroEvent 分发类型对应标识的 key

MESSAGE\_TYPE\_KEY<Object>

```js
MicroConstants.MESSAGE_TYPE_KEY = {
    // 广播不需要指定频道或唯一标识
    [MESSAGE_TYPE.BROADCAST]: '',

    // 特定频道多播需要指定频道
    [MESSAGE_TYPE.CHANNEL]: 'channel',

    // 单播需要指定唯一标识
    [MESSAGE_TYPE.SINGLE]: 'key'
};
```

### EVENT\_SYMBOL

MicroEvent 消息过滤标识

EVENT\_SYMBOL<String>

```js
// MicroEvent 消息过滤标识
MicroConstants.EVENT_SYMBOL = '__ECP_MICRO_EVENT_SYMBOL__';
```

### EVENT\_MESSAGE\_SYMBOL

MicroEvent 调用的 addEventListener 的回调方法挂在到 window 上的 key

EVENT\_MESSAGE\_SYMBOL<String>

```js
// MicroEvent 调用的 addEventListener 的回调方法挂在到 window 上的 key
MicroConstants.EVENT_MESSAGE_SYMBOL = '__ECP_MICRO_EVENT_MESSAGE_SYMBOL__';
```

### EVENT\_MESSAGE\_WINDOW\_NAME

MicroEvent 消息窗口标识的 key

EVENT\_MESSAGE\_WINDOW\_NAME<String>

```js
// MicroEvent 消息窗口标识的 key
MicroConstants.EVENT_MESSAGE_WINDOW_NAME = '__ECP_MICRO_EVENT_MESSAGE_WINDOW_NAME__';
```

### EVENT\_COLLECTION\_SYMBOL

MicroEvent 消息类型回调队列 Map 挂载到消息窗口的 key

EVENT\_COLLECTION\_SYMBOL<String>

```js
// MicroEvent 消息类型回调队列 Map 挂载到消息窗口的 key
MicroConstants.EVENT_COLLECTION_SYMBOL = '__ECP_MICRO_EVENT_COLLECTION_SYMBOL__';
```
