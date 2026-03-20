<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/data/table.html -->

# Table 表格

> - 在 `ElTable` 的基础上作样式重置。
> - 用于展示多条结构类似的数据，可对数据进行排序、筛选、对比或其他自定义操作。
> - 在 SSR 场景下，您需要将组件包裹在 `<client-only></client-only>` 之中 (如: [Nuxt](https://nuxt.com/v3)) 和 SSG (e.g: [VitePress](https://vitepress.vuejs.org/)).

## 基础表格

基础的表格展示用法。

- 当 `el-table` 元素中注入 `data` 对象数组后，在 `el-table-column` 中用 `prop` 属性来对应对象中的键名即可填入数据，用 `label` 属性来定义表格的列名。 可以使用 `width` 属性来定义列宽。

## 带斑马纹表格

使用带斑马纹的表格，可以更容易区分出不同行的数据。

- `stripe` 可以创建带斑马纹的表格；
- 如果 `true`, 表格将会带有斑马纹。

## 带边框表格

默认情况下，Table 组件是不具有竖直方向的边框的，如果需要，可以使用 `border` 属性，把该属性设置为 `true` 即可启用。

## 带状态表格

可将表格内容 highlight 显示，方便区分「成功、信息、警告、危险」等内容。

- 可以通过指定 Table 组件的 `row-class-name` 属性来为 Table 中的某一行添加 class，这样就可以自定义每一行的样式了。

## 固定表头

纵向内容过多时，可选择固定表头。

- 只要在 `el-table` 元素中定义了 `height` 属性，即可实现固定表头的表格，而不需要额外的代码。

## 固定列

横向内容过多时，可选择固定列。

- 固定列需要使用 `fixed` 属性，它接受 `Boolean` 值。
- 如果为 `true`, 列将被左侧固定. 它还接受传入字符串，left 或 right，表示左边固定还是右边固定。

## 固定列和表头

当您有大量数据块放入表中，您可以同时固定表头和列。

- 固定列和表头可以同时使用，只需要将上述两个属性分别设置好即可。

## 流体高度

当数据量动态变化时，可以为 Table 设置一个最大高度。

- 通过设置 `max-height` 属性为 `el-table` 指定最大高度。
- 此时若表格所需的高度大于最大高度，则会显示一个滚动条。

## 多级表头

数据结构比较复杂的时候，可使用多级表头来展现数据的层次关系。

- 只需要将el-table-column 放置于el-table-column 中，你可以实现组头。

## 固定群组头

支持固定群组头

## 单选

选择单行数据时使用色块表示。

- Table 组件提供了单选的支持，只需要配置 `highlight-current-row` 属性即可实现单选。
- 之后由 `current-change` 事件来管理选中时触发的事件，它会传入 `currentRow`，`oldCurrentRow`。
- 如果需要显示索引，可以增加一列 `el-table-column`，设置 `type` 属性为 `index` 即可显示从 1 开始的索引号。

## 多选

你也可以选择多行。

- 实现多选非常简单: 手动添加一个 `el-table-column`，设 `type` 属性为 `selection` 即可；
- 除了多选，这里还使用到了 `show-overflow-tooltip`属性。
- 默认情况下，如果单元格内容过长，会占用多行显示。
- 若需要单行显示可以使用 `show-overflow-tooltip` 属性，它接受一个 `Boolean`，为 `true` 时多余的内容会在 hover 时以 tooltip 的形式显示出来。

## 排序

对表格进行排序，可快速查找或对比数据。

- 在列中设置 `sortable` 属性即可实现以该列为基准的排序，接受一个 `Boolean`，默认为 `false`。
- 可以通过 Table 的 `default-sort` 属性设置默认的排序列和排序顺序。
- 可以使用 `sort-method` 或者 `sort-by` 使用自定义的排序规则。 如果需要后端排序，需将 `sortable` 设置为 `custom`，同时在 Table 上监听 `sort-change` 事件，在事件回调中可以获取当前排序的字段名和排序顺序，从而向接口请求排序后的表格数据。
- 在本例中，我们还使用了 `formatter` 属性，它用于格式化指定列的值，接受一个 `Function`，会传入两个参数：`row` 和 `column`，可以根据自己的需求进行处理。

## 筛选

对表格进行筛选，可快速查找到自己想看的数据。

- 在列中设置 `filters` 和 `filter-method` 属性即可开启该列的筛选，filters 是一个数组，`filter-method` 是一个方法，它用于决定某些数据是否显示，会传入三个参数：`value`, `row` 和 `column`。

## 自定义列模板

自定义列的显示内容，可组合其他组件使用。

- 通过 `slot` 可以获取到 row, column, $index 和 store（table 内部的状态管理）的数据，用法参考 demo。

## 自定义表头

表头支持自定义。

- 通过设置 [slot](https://v3.vuejs.org/guide/component-slots.html) 来自定义表头。

## 展开行

当行内容过多并且不想显示横向滚动条时，可以使用 Table 展开行功能。

- 通过设置 type="expand" 和 slot 可以开启展开行功能，el-table-column 的模板会被渲染成为展开行的内容，展开行可访问的属性与使用自定义列模板时的 slot 相同。

## 树形数据与懒加载

支持树类型的数据的显示。

- 当 row 中包含 `children` 字段时，被视为树形数据。
- 渲染嵌套数据需要 prop 的 `row-key`。
- 此外，子行数据可以异步加载。
- 设置 Table 的`lazy`属性为 true 与加载函数 `load` 。
- 通过指定 row 中的`hasChildren`字段来指定哪些行是包含子节点。
- `children` 与`hasChildren`都可以通过 `tree-props`配置。

## 表尾合计行

若表格展示的是各类数字，可以在表尾显示各列的合计。

- 将 `show-summary` 设置为`true`就会在表格尾部展示合计行。
- 默认情况下，对于合计行，第一列不进行数据求合操作，而是显示「合计」二字（可通过`sum-text`配置），其余列会将本列所有数值进行求合操作，并显示出来。
- 当然，你也可以定义自己的合计逻辑。
- 使用 `summary-method` 并传入一个方法，返回一个数组，这个数组中的各项就会显示在合计行的各列中，具体可以参考本例中的第二个表格。

## 合并行或列

多行或多列共用一个数据时，可以合并行或列。

- 通过给 table 传入`span-method`方法可以实现合并行或列，方法的参数是一个对象，里面包含当前行`row`、当前列 `column`、当前行号`rowIndex`、当前列号 `columnIndex` 四个属性。
- 该函数可以返回一个包含两个元素的数组，第一个元素代表 `rowspan`，第二个元素代表 `colspan`。
- 也可以返回一个键名为`rowspan` 和`colspan` 的对象。

## 自定义索引

自定义 `type=index` 列的行号。

- 通过给`type=index` 的列传入 index 属性，可以自定义索引。
- 该属性传入数字时，将作为索引的起始值。
- 也可以传入一个方法，它提供当前行的行号（从 `0` 开始）作为参数，返回值将作为索引展示。

## 表格布局

通过属性 [table-layout](https://developer.mozilla.org/en-US/docs/Web/CSS/table-layout) 可以指定表格中单元格、行和列的布局方式

## Table Api

### Table Attributes

见 [ElementPlus - Table 属性](https://element-plus.gitee.io/zh-CN/component/table.html#table-%E5%B1%9E%E6%80%A7)

### Table Events

见 [ElementPlus - Table 事件](https://element-plus.gitee.io/zh-CN/component/table.html#table-%E4%BA%8B%E4%BB%B6)

### Table Exposes

见 [ElementPlus - Table 方法](https://element-plus.gitee.io/zh-CN/component/table.html#table-%E6%96%B9%E6%B3%95)

### Table Slots

见 [ElementPlus - Table 插槽](https://element-plus.gitee.io/zh-CN/component/table.html#table-%E6%8F%92%E6%A7%BD)

## Table-column Api

### Table-column Attributes

见 [ElementPlus - Table-column 属性](https://element-plus.gitee.io/zh-CN/component/table.html#table-column-%E5%B1%9E%E6%80%A7)

### Table-column Slots

见 [ElementPlus - Table-column 插槽](https://element-plus.gitee.io/zh-CN/component/table.html#table-column-%E6%8F%92%E6%A7%BD)
