<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/micro-frontends/routing-scheduling.html -->

# 路由调度

## Session history 原理

在同一浏览器页签/窗口中，iframe 内部和外部的 documents 在创建的时候都有自己的 session history 实例，但每个 session history 实例都会关联到当前页签/窗口中全局唯一的 History 对象，这个对象记录了一个在当前页签/窗口中的浏览历史。

history.pushState 和 history.replaceState 虽然都会更新浏览历史，但是只能操作当前 document 对应的 session history 实例中创建的浏览历史项。

**🌰 举个栗子**

top 代表最外层的 document，所展示 Url 即浏览器地址栏的 Url。

top 页面嵌入了一个 src 是 /iframe/#/i-a 的 iframe ：

|  | 0 | 1 |  |  | History |
| --- | --- | --- | --- | --- | --- |
| top | /top/#/old-path | /s-iframe/#/i-a |  |  | history.length = 2 |
| iframe[0] |  | /iframe/#/i-a |  |  | history.length = 2 |

iframe 先调用 pushState, 添加记录 /iframe/#/i-b。

然后，top 调用 replaceState, 试图将 History 最新的一条记录覆盖为 /s-iframe/#/i-b，但 session history 会变成这样：

|  | 0 | 1 | 2 |  | History |
| --- | --- | --- | --- | --- | --- |
| top | /top/#/old-path | /s-iframe/#/i-b | |  | history.length = 3 |
| iframe[0] |  | /iframe/#/i-a | /iframe/#/i-b |  | history.length = 3 |

可以看到 top 调用 replaceState 之后，浏览器地址虽然替换为最新的地址了，但 History 并没有替换掉全局管理的最新一条记录，只是替换了 top 自己的 history 实例创建的最新一条记录。

最后，top 调用 pushState, 添加记录 /top/#/c，session history 就会变成：

|  | 0 | 1 | 2 | 3 | History |
| --- | --- | --- | --- | --- | --- |
| top | /top/#/old-path | /s-iframe/#/i-b | | /top/#/c | history.length = 4 |
| iframe[0] |  | /iframe/#/i-a | /iframe/#/i-b |  | history.length = 4 |

从这里开始一级级回退的话，可以看到地址栏变化记录是：

/top/#/c → /s-iframe/#/i-b → **`/s-iframe/#/i-b`** → /top/#/old-path

这也不符合我们预期，我们希望应该是这样的：

/top/#/c → /s-iframe/#/i-b → **`/s-iframe/#/i-a`** → /top/#/old-path

因此，需要对 history 进行劫持改造。

## 路由式加载 History 改造

> 子应用匹配规则: `/s-子应用唯一标识/#/子应用fullPath`

### 主应用 History 重写

页面更新流程如下：

1. HistoryApp 初始化时，备份原始定义的 pushState 和 replaceState，重写对应方法，并添加对应执行回调、添加事件抛出；
2. 调用 pushState / replaceState 后，重写方法中先抛出对应事件，然后调用备份的 pushState / replaceState，最后执行回调；
3. 回调执行之后，更新 HistoryApp 的 name 和 url；
4. 如果当前地址链接规则符合子应用匹配规则，执行 Wujie startApp 队列更新；
   - 如果子应用有做适配改造，且子应用已加载过，会在执行队列更新之前，调用匹配上的子应用的挂载在对应 window 上的 router.replace 方法更新子应用页面组件；
5. 如果不符合子应用匹配规则，则不更新 Wujie 子应用实例，并替换展示区域为主应用页面。

### 子应用 History 劫持

子应用通过 $router 跳转的流程如下：

1. 初始化时备份 iframe 原始定义的 pushState 和 replaceState，重写 iframe 的 pushState 和 replaceState；
2. 子应用调用 $router.push / $router.replace 更新页面组件，router 调用 pushState / replaceState；
3. 重写的方法中，先拼接符合子应用匹配规则 的 uri；
4. 然后调用 top 的 pushState / replaceState，传入上一步拼接好的 uri；
5. 最后调用备份的 replaceState，替换 iframe 内维护的 history 项为 `/子应用唯一标识/sub.html#/子应用fullPath`。

## 组件式加载 History 改造

对于手动加载的子应用，不允许更新 history，应通过回调，交由父组件执行对应逻辑处理：

1. 手动加载初始化时，备份该实例对应 iframe 原始定义的 pushState、replaceState、go、back、forward；
2. 重写对应方法，并添加对应执行回调；
3. 该子应用调用相关方法后，直接执行回调，不调用原始定义方法。
