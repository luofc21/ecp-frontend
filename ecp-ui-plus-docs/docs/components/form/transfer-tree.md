<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/form/transfer-tree.html -->

# TransferTree 树形穿梭选择

> - 基于 `el-tree-v2` 虚拟树实现；
> - 解决 `el-tree` 无法满足大量数据时导致卡顿的问题，可对数据进行勾选、回显、搜索等操作。

## 基础用法

> - 内部使用的是el-tree-v2虚拟树逻辑，默认treeProps配置为 `{value: 'id', children: 'children', label: 'label'}`；
> - 由于 `el-tree-v2` 不支持全展开，默认只展开第一级。

## 仅勾选叶节点

> - `treeProps.isLeaf` 属性可以设置是否为叶子节点：
>   - 当 `treeData` 里某项有 `isLeaf` 属性并且值为 `false` 时，该项会被标记为目录级；
>   - 当目录级没有子项时（空目录），勾选后不会将该目录级节点作为右侧选中项；
> - 使用 `empty-left`、`empty-right` 插槽，可自定义空状态展示。

## 使用弹窗

> - `<ecp-tree-transfer-tree-dialog />` 以弹窗形式使用；
> - 传入 `selectedNodeKeys` 参数，可回显渲染默认选中的节点；
>   - `selectedNodeKeys` 数组由 `NodeData[treeProps.value]` 组成。

## 限制多选个数

> - 使用弹窗时，可添加 `limitNum` 设置最多选择的个数，超过该值时，会抛出 `onLimit` 事件并返回当前所有选中项。

## TransferTree Api

### TransferTree Attributes

| 参数 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| treeProps | 树配置项 | Object |  | [见 TreeProps 的结构](#treeprops-的结构) |
| treeData | 树数据 | Array |  | [] |
| selectedNodeKeys/v-model:selectedNodeKeys | 外部传入已选择的节点key列表（依据treePops里配置的value作为key） | Array |  | [] |
| panelTitles | 左右两侧目录树标题 | Array<String> |  | ['候选项', '已选列表'] |
| placeholder | 左右两侧搜索框占位文案 | String |  | '请输入关键字进行过滤' |

#### treeProps 的结构

| key | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| label | 指定节点标签为节点对象的某个属性值 | String | 'label' |
| value | 每个树节点用来作为唯一标识的属性，在整棵树中应该是唯一的 | String | 'value' |
| children | 指定子树为节点对象的某个属性值 | String | 'children' |
| isLeaf | 指定节点是否为叶子节点的某个属性值 | String | 'isLeaf' |
| ... | 其余配置项见 [ElTreeV2 - props](https://element-plus.org/zh-CN/component/tree-v2.html#props) |  |  |

### TransferTree Events

| 事件名称 | 说明 | 回调参数 |
| --- | --- | --- |
| update:selectedNodeKeys | 已选列表更新事件 |  |

### TransferTree Slots

| 插槽名 | 说明 | 传参 |
| --- | --- | --- |
| header-left | 候选项面板头部插槽 |  |
| node-left | 候选项节点插槽 | `{ node: TreeNode, data: TreeNodeData }` |
| empty-left | 候选项为空时，空状态展示插槽 |  |
| header-right | 已选项面板头部插槽 | `{ clear: Function }` |
| node-right | 已选项节点插槽 | `{ node: TreeNode, data: TreeNodeData }` |
| empty-right | 已选项为空时，空状态展示插槽 |  |
| middle | 候选项、已选项面板之间的插槽 |  |

### TransferTree Exposes

| 方法/属性 | 类型 | 说明 | 入参 |
| --- | --- | --- | --- |
| treeLeftRef | ComputedRef | 左侧树实例 |  |
| treeRightRef | ComputedRef | 右侧树实例 |  |
| getCheckKeys | Function | 获取所有已选项 |  |
| reset | Function | 重置为初始化状态 |  |
| clear | Function | 清空所有已选项 |  |

## TransferTreeDialog Api

### TransferTreeDialog Attributes

| 参数 | 说明 | 类型 | 可选值 | 默认值 |
| --- | --- | --- | --- | --- |
| selectedNodeKeys | 同 `TransferTree > selectedNodeKeys` | Array |  | [] |
| visible/v-model:visible | 控制弹窗的显隐 | Boolean |  |  |
| dialogTitle | 弹窗标题 | String |  |  |
| limitNum | 允许最大选中数量 | Number |  |  |
| elDialogProps | element-plus的el-dialog配置项Attributes | Object |  |  |
| ... | 其余参数同 [TransferTree Attributes](#transfertree-attributes) |  |  |  |

### TransferTreeDialog Events

| 事件名称 | 说明 | 回调参数 |
| --- | --- | --- |
| close | 关闭弹窗事件 |  |
| onLimit | 触发选中项数量限制事件 | 当前选中项列表keys |
| confirm | 点击确定时触发 | `{ selectedNodeKeys: keys }` |

### TransferTreeDialog Slots

同 [TransferTree Slots](#transfertree-slots) 。

### TransferTreeDialog Exposes

| 方法/属性 | 类型 | 说明 |
| --- | --- | --- |
| dialogRef | ComputedRef | ElDialog 实例 |
| transferTreeRef | ComputedRef | TransferTree 实例 |
