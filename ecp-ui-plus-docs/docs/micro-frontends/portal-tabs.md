<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/micro-frontends/portal-tabs.html -->

# Portal-tabs 门户多页签

> - 搭配 `UseHistoryApp 的 keepAlive` 和 `主应用、各子应用 <keep-alive> 组件` 使用；
> - 长按拖动可排序，右键点击弹出操作菜单；
> - 当展示的页签宽度大于区间容器的宽度时，页签列表可以横向滚动；
> - 支持自定义页签项样式。

## TabItem 数据项的结构

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | String | 是 | tab 项展示名称 |
| url | String | 是 | tab 项路由链接，tab 的激活标识，如需要添加多个相同的 url，请自行为 url 追加参数加以区分，参考 [子应用添加页签](#子应用添加页签) |

## Attributes

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| presetList | Array |  | 预置访问后自动添加 tab 的列表，可以把菜单传进来 |
| menuProps | Object<String, String> | [MenuProps](#menuprops-的结构) | presetList 关键字段映射配置，可以把菜单关键字段映射配置传进来，详见 [MenuProps 的结构](#menuprops-的结构) |
| showScrollBtn | Boolean | true | 当展示的页签宽度大于组件容器宽度时，是否展示左右滚动按钮，点击后向左/右滚动一版组件容器宽度 |
| min | Number / String | 0 | 最小展示页签数，当展示的页签数小于等于 min 时，页签就不能删除了 |
| beforeAdd | Function |  | tab 添加前的处理, (item<Object>: 操作的 tab) => {} |
| beforeRemove | Function |  | tab 移除前的处理, (item<Object>: 操作的 tab, tabsRecords<Array>: 当前记录的 tab 列表) => {} |
| customClosable | Function |  | 自定义判断可否移除 tab, ({ item<Object>: 操作的 tab, active<Boolean>: 操作的 tab是否已激活, closable<Boolean>: 按组件内置默认逻辑判断可否移除 }) => {} |

### MenuProps 的结构

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| id | String | 'id' | tab 项 Id key |
| label | String | 'Text' | tab 项名称 (展示文本) key |
| route | String | 'Target' | tab 项路由链接 key |
| url | String | 'url' | tab 项路由链接 key (在菜单配置里面与route不一样，但在Portal-tabs 这里和tabs 是一样的) |
| symbol | String | 'symbol' | tab 项 Symbol key |
| children | String | 'ChildNodes' | 子级 tab 项 key |
| Text | String | 'Text' | label 的冗余兼容项 |
| Target | String | 'Target' | route 的冗余兼容项 |
| ChildNodes | String | 'ChildNodes' | children 的冗余兼容项 |

## Events

| 事件名称 | 说明 | 回调参数 |
| --- | --- | --- |
| add | tab 添加完成时的回调 | { tabsRecords<Array>: 添加完成后记录的 tab 列表, validTabItem<Object>: 添加的 tab(直接修改name会同步更新) } |
| remove | tab 移除完成时的回调 | { tabsRecords<Array>: 移除完成后记录的 tab 列表, removedItems<Array>: 移除的 tab 列表, nextActiveItem<Object>: 下一个激活的 tab } |
| update | 激活的 tab 变更后的回调 | activeUrl<String>: 激活 tab 的 url |
| refresh | 刷新操作回调 | item<Object>: 操作的 tab |
| goto | 跳转操作回调 | { [menuProps.label]: 菜单项名称, [menuProps.route]: 菜单项路由链接, [menuProps.url]: 菜单项路由外链 } |

## Slots

| 插槽名 | 说明 | 传参 |
| --- | --- | --- |
| item | 自定义页签模板 | item<Object>: 页签项, active<Boolean>: 是否激活, isFirst<Boolean>: 是否第一个页签, isLast<Boolean>: 是否最后一个页签, closable<Boolean>: 可否移除, close<Function>: 移除页签的方法（调用可将该页签移除） |

## Exposes

| 方法/属性 | 说明 |
| --- | --- |
| PortalTabsActionsInst | PortalTabsActions 实例，详见 [PortalTabsActions 实现类](#portaltabsactions-实现类)。注意主应用**不会**挂载到自己的 window.PortalTabsActions 上。 |

## PortalTabsActions 实现类

多页签操作实现类

> Tab 记录会缓存在 sessionStorage 中，全局唯一，多实例共享同一个 Tab 记录； 为方便子应用自由添加 Tab，使用 `路由式加载` 且用 `keepAlive` 时，会在每个做了适配改造的子应用 window 上注入一个 PortalTabsActions 实例，可以通过子应用 window.PortalTabsActions 访问。

```js
import { MicroUtils } from '@ecp/ecp-ui-plus';
const { PortalTabsActions } = MicroUtils;
const portalTabsActionsInst = new PortalTabsActions(options)
```

### 构造函数的入参

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| presetList | Array |  |  | 对应 Portal-tabs 组件的 presetList |
| props | Object<String, String> | [Props](#props-的结构) |  | presetList 关键字段映射配置, 详见 [Props 的结构](#props-的结构) |

#### Props 的结构

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| name | String | 'name' | tab 项名称 (展示文本) key，对应 Portal-tabs 组件 `menuProps.Text || menuProps.label` |
| url | String | 'Text' | tab 项路由链接 key，对应 Portal-tabs 组件 `menuProps.Target || menuProps.route || menuProps.url` |
| children | String | 'Target' | t子级 tab 项 key，对应 Portal-tabs 组件 `menuProps.ChildNodes || menuProps.children` |

### 其它可用属性

#### isDestroyed

`Boolean` 当前实例是否已销毁

```js
portalTabsActionsInst.isDestroyed<Boolean>;
```

#### destroy

`Function` 销毁当前实例方法，调用后会同时销毁。

```js
portalTabsActionsInst.destroy();
```

#### getPresetLists

`Function` 获取当前预设列表

```js
portalTabsActionsInst.getPresetLists(list<Array>, blockUpdateActive<Boolean>);
```

#### updatePresetLists

`Function` 更新预设列表

- 会将方法传入的预设列表与实例当前的预设列表，做根据 url 去重的合并处理

```js
portalTabsActionsInst.updatePresetLists(list<Array>, blockUpdateActive<Boolean>);
```

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| list | Array | 需要添加的预设列表 |
| blockUpdateActive | Boolean | 预设列表添加完成后，是否自动调用一次更新激活的 tab 项，传 true 不会自动调用 |

#### on

`Function` 注册当前实例事件监听器

- 将一个回调函数注册到指定的回调队列中，当相应的事件触发时会调用这些回调函数。

```js
portalTabsActionsInst.on(callbackName<String>, callback<Function>, options<Object>);
```

入参：

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| callbackName | String | 监听器 |
| callback | Function | 需要注册的回调函数 |
| options | Object | 额外配置，{ once<Boolean>: 是否一次性执行 } |

每种监听器对应维护一个队列，每个队列全局唯一，多实例共享，但实例内有做映射处理，移除操作只能移除当前实例注册的监听器。

支持的监听器：

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| beforeAdd | String | 添加操作前的回调 |
| beforeRemove | Function | 移除操作前的回调 |
| add | Object | 添加操作完成时的回调 |
| remove | String | 移除操作完成时的回调 |
| update | Function | 更新操作完成时的回调 |
| goto | Object | 跳转操作相关的回调 |

返回：

- 注册的监听器的唯一键值 key。

#### off

`Function` 移除在当前实例注册的事件监听器

```js
portalTabsActionsInst.off(callbackName<String>, key<String>);
```

入参：

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| callbackName | String | 回调名称 |
| key | String | 注册监听器返回的的唯一键值 key，如果不提供，会清空在当前实例注册的该回调名称下的**所有**监听器 |

#### offAll

`Function` 移除在当前实例注册的**所有**事件监听器方法

```js
portalTabsActionsInst.offAll();
```

#### add

`Function` 添加一个新的 Tab

- **不会**更新激活状态；
- 在移除之前会按顺序调用所有实例注册的 beforeAdd 方法；
- 全部执行成功后，将新的 Tab 添加到记录中；
- 最后触发 add 回调。

```js
portalTabsActionsInst.add(tabItem<Object>, addOptions<Object>);
```

入参 addOptions 的结构：

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| insertAfterActive | Boolean |  | 是否插入到当前激活的 Tab 项之后 |
| insertIndex | Number |  | 指定插入的索引位置，优先级高于 insertAfterActive |

返回：

- Promise<void>

#### remove

`Function` 移除一个 Tab

- 在移除之前会按顺序调用所有实例注册的 beforeRemove 方法；
- 全部执行成功后，移除指定 Tab 并更新激活状态；
- 最后触发 remove 回调。

```js
portalTabsActionsInst.remove(tabItem<Object>, nextOptions<Object>);
```

入参 tabItem 的结构：

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | String |  | tab 项展示名称 |
| url | String | 是 | tab 项路由链接 |

入参 nextOptions 的结构：

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| block | Boolean |  | 是否阻止自动跳转到下一个 Tab |
| nextActiveItem | TabItem |  | 自定义下一个激活的 Tab 项数据 |

返回：

- Promise<void>

#### removeBatch

`Function` 批量移除 Tab

- 在移除之前会按顺序调用所有实例注册的 beforeRemove 方法；
- 全部执行成功后，根据指定索引范围和其它限制条件，批量移除 Tab 并更新激活状态；
- 最后触发 remove 回调。

```js
portalTabsActionsInst.removeBatch(options<Object>);
```

入参 options 的结构：

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startIndex | String | 是 | 移除范围的起始索引 (包含) |
| endIndex | String | 是 | 移除范围的结束索引 (包含) |
| tabItem | Object | 是 | 当前处理的 Tab 项数据 |
| excludeItems | Array<TabItem> |  | 需要排除的 Tab 项数据数组 |

返回：

- Promise<void>

#### clear

`Function` 清空所有 Tab

- 激活态的 Tab 也会清除掉；
- 在移除之前会按顺序调用所有实例注册的 beforeRemove 方法；
- 全部执行成功后，移除所有 Tab；
- 最后触发 remove 回调。

```js
portalTabsActionsInst.clear(options<Object>);
```

返回：

- Promise<void>

#### getByUrl

`Function` 根据 Url 获取 Tab 项

- 从 Tab 记录中查找匹配 Url 的 Tab 项；
- 返回的 Tab 项可用于修改名称等操作。

```js
portalTabsActionsInst.getByUrl(url<String>);
```

返回：

- tabItem<Object> 匹配的 Tab 项数据，找不到时返回 null

#### getActiveItem

`Function` 获取当前激活的 Tab 项

- 从 Tab 记录中查找匹配 URL 的 Tab 项，并返回当前激活的 Tab 项数据；
- 返回的 Tab 项可用于修改名称等操作。

```js
portalTabsActionsInst.getActiveItem();
```

返回：

- tabItem<Object> 前激活的 Tab 项数据，找不到时返回 null

#### getAll

`Function` 获取响应式 Tab 记录

- 返回整个 Tab 记录集合，便于外部访问。

```js
portalTabsActionsInst.getAll();
```

返回：

- Ref<JSONArray> 响应式的 Tab 记录数组，响应仅适用于 Vue3，Vue2 只能取值

## 示例

### 基础用法

![Portal-tabs 基础用法](../../../assets/ecp-ui-plus/images/ecp-portal-tabs-01.png)

查看代码片段

```vue
<template>
    <!-- ... -->
    <ecp-portal-tabs :preset-list="menu" :menu-props="menuProps" show-scroll-btn min="1"
                    :custom-closable="customClosable" @goto="handleSelect"></ecp-portal-tabs>
    <!-- ... -->
</template>

<script setup>
import { EcpPortalTabs, MicroUtils } from '@ecp/ecp-ui-plus';

const props = defineProps({
    config: {
        type: Object,
        require: true
    },
    menu: {
        type: Array
    },
    menuProps: {
        type: Object,
        default: () => ({
            id: 'id',
            label: 'name',
            route: 'Target',
            url: 'url',
            symbol: 'symbol',
            children: 'children',
            ChildNodes: 'ChildNodes',
            Text: 'Text',
            Target: 'Target'
        })
    }
});

const customClosable = (options) => {
    const { item, active, closable } = options;
    const url = item?.url || '';
    return !url.match('/some-specific-path');
};

const handleSelect = (data) => {
    let href = data?.[props.menuProps?.route || 'route'] || data?.[props.menuProps?.url || 'url'];
    if (href.match(PACKAGE_NAME)) {
        href = MicroUtils.getUri(MicroUtils.getAppOriginHref(href, startsWith));

        const targetName = MicroUtils.getAppNameFromHref(href, startsWith);
        const currentName = MicroUtils.getAppNameFromHref(location.href, startsWith);
        const fullPath = MicroUtils.getAppFullPath(href);

        if (targetName !== currentName) {
            window.history.pushState({}, '', href);

            const matchedRoute = router.resolve(fullPath);
            const matchedRouteQuery = matchedRoute?.query || {};
            router.replace({
                path: matchedRoute.path,
                query: matchedRouteQuery,
                force: true
            });
        } else {
            router.push(force ? `/redirect${fullPath}` : fullPath);
        }
    } else {
        window.history[force ? 'replaceState' : 'pushState']({
            force
        }, '', href);
    }
};
</script>
```

### 使用自定义页签

![Portal-tabs 使用自定义页签](../../../assets/ecp-ui-plus/images/ecp-portal-tabs-02.png)

查看代码片段

```vue
<template>
    <!-- ... -->
    <ecp-portal-tabs :preset-list="menu" :menu-props="menuProps" show-scroll-btn min="1"
        :custom-closable="customClosable" @goto="handleSelect">
        <template #item="{ item, active, close, closable }">
            <div class="portal-layout-nav-tab-item" :class="{ active }">
                <div class="portal-layout-nav-tab-item-text">{{ item.name }}</div>
                <ecp-icon :class="[`ecpp-portal-tab__trigger--icon`]" icon="ecp-icon-close" @click.stop="close"
                    v-if="closable"></ecp-icon>
            </div>
        </template>
    </ecp-portal-tabs>
    <!-- ... -->
</template>

<script setup>
import { EcpPortalTabs, MicroUtils } from '@ecp/ecp-ui-plus';

// ...
</script>

<style lange="scss" scoped>
.portal-layout-nav-tab-item {
    /* ...Some Custom Styles... */
}
</style>
```

### 子应用添加页签

子应用跳转的二级页面一般不在 `presetList`，需要手动添加。

查看代码片段

```js
const path = '/some/route/path';
let query = { 
    // ...
    t: Date.now() // 如需要支持添加多个相同的 url 的 tab, 需要添加额外的参数
};
const resolved = router.resolve({ path, query });
if (window.PortalTabsActions && resolved?.fullPath) {
    window.PortalTabsActions.add({
        name: '自定义 Tab 名称',
        url: `/s-${PACKAGE_NAME}/#${resolved.fullPath}`
    });
}
router.push({ path, query }); // 跳转后, PortalTabs 会自动更新激活态
```
