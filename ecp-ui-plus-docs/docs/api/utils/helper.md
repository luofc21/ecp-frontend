<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/api/utils/helper.html -->

# Helper 常用辅助方法

> 常用处理类辅助方法相关

```js
import { Helper } from '@ecp/ecp-ui-plus';
```

## 通用

### isEmptyValue

判断是否为空值

- **入参**

  - `Any` value: 需要判断的值
- **返回**

  - `Boolean`

### formatNumberRound

`数字格式化` 数值保留小数

- **入参**
  - `Number` num: 需要格式化的数字
  - `Number` ind: 保留小数位数
- **返回**
  - `Number` 格式化后的数字

## 数值处理

### formatUnitNumber

`数值处理` 大数值加单位格式化

- **入参**
  - `Number|String` num: 需要格式化的数字
- **返回**
  - `Object` result 格式化结果
    - `Number` value: 格式化后的数字
    - `Number` min: 匹配单位的最小值
    - `Number` unit: 匹配单位字符串

### formatBankNumber

`数值处理` 整数位从右往左每三位插入一个逗号

- **入参**
  - `Number|String` num: 需要格式化的数字
- **返回**
  - `String` 格式化后的数字

## 字符串处理

### joinStr

`字符串处理` 拼合为字符串

- **入参**

  - `Array<String|Number|Null|Undefined>` valueArr: 需要拼合的值数组
  - `Object` options: 拼合的配置项
    - `String` options.seperator: 分隔符
    - `String` options.keepEmpty: 是否保留空值
    - `String` options.emptyText: 空值替换文本
- **返回**

  - `String` 拼合字符串

### estimateWidth

`字符串处理` 获取字符串文本宽度

- **入参**

  - `String` value: 需要计算的字符串
- **返回**

  - `Number` 字符串文本宽度

### strGetDotted

`字符串处理` 数据脱敏显示

- **入参**

  - `String` orginStr: 原始数据
  - `Number` visibleStartNum: 头部明文显示位数
  - `Number` visibleEndNum: 尾部明文显示位数
  - `Number` maxInvisibleLength: 星号最多展示数
- **返回**

  - `String` 脱敏后的数据

### labelValueFormatter

`字符串处理` 按 **名称 (值)** 格式化显示

- **入参**

  - `String|Number` label: 名称
  - `String|Number` value: 值
- **返回**

  - `String` 格式化后的字符串
- **入参**

  - `String` string: 需要格式化的字符串
- **返回**

  - `String` resultString: 格式化后的字符串

### fillTemplate

`字符串处理` 字符串模板替换

```js
const templateStr = `
Lorem ipsum dolor sit āmet,
consetetur sadipscing elitr,
{# sed #} {#diam#} nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
{# sed #} {#diam#} voluptua.
`;
const resultString = Helper.fillTemplate(
    templateStr,
    {
        replacements: {
            sed: 'SOME_VALUE',
            diam: 'SOME_OTHER_VALUE'
        },
        symbolStart: '{#',
        symbolEnd: '#}'
    }
);
/**
 * `
 * Lorem ipsum dolor sit āmet,
 * consetetur sadipscing elitr,
 * SOME_VALUE diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
 * SOME_OTHER_VALUE diam voluptua.
 * `
 */
```

- **入参**

  - `String` stringTemplate: 字符串模板
  - `Object` options: 字符串模板配置
    - `Object` options.replacements: 替换项
    - `String` options.symbolStart: 模板替换项匹配开始符号
    - `String` options.symbolEnd: 模板替换项匹配结束符号
- **返回**

  - `String` resultString: 替换后的字符串

### toCamelCase

`字符串格式转换` 字符串转为 camelCase 字符串

> `Helper.kebabCaseToCamelCase`、`Helper.pascalCaseToCamelCase` 等使用的也是这一个方法。

### toKebabCase

`字符串格式转换` 字符串转为 kebab-case 字符串

> `Helper.camelCaseToKebabCase`、`Helper.pascalCaseToKebabCase` 等使用的也是这一个方法。

- **入参**

  - `String` string: 需要格式化的字符串
- **返回**

  - `String` resultString: 格式化后的字符串

### toPascalCase

`字符串格式转换` 字符串转为 PascalCase 字符串

> `Helper.camelCaseToPascalCase`、`Helper.kebabCaseToPascalCase` 等使用的也是这一个方法。

- **入参**

  - `String` string: 需要格式化的字符串
- **返回**

  - `String` resultString: 格式化后的字符串

### toSnakeCase

`字符串格式转换` 字符串转为 snake\_case 字符串

- **入参**

  - `String` string: 需要格式化的字符串
- **返回**

  - `String` resultString: 格式化后的字符串

### toUpperSnakeCase

`字符串格式转换` 字符串转为 UPPER\_SNAKE\_CASE 字符串

- **入参**

  - `String` string: 需要格式化的字符串
- **返回**

  - `String` resultString: 格式化后的字符

## 对象处理

### getValueByKeyPath

`对象处理` 获取对象中指定路径的值

点击查看示例代码

```js
import { Helper } from '@ecp/ecp-ui-plus';

const data = {
    a: {
        b: [
            { c: 'value1' },
            { c: 'value2' },
            { c: 'value3' }
        ]
    }
};
const c2Value = Helper.getValueByKeyPath(data, 'a.b.1.c');
// c2Value === 'value2'
```

- **入参**

  - `Object / Array` data: 源对象
  - `String / Array / Number` path: 需要获取的值的键路径
  - `String` seperator: path 为 String 时，用于切割路径的分隔符, 默认为 '.'
- **返回**

  - `Any` result: 获取到的值

### findDeepItem

`对象处理` 获取指定对象中符合匹配条件的项

点击查看示例代码

```js
import { Helper } from '@ecp/ecp-ui-plus';

const data = [
    {
        Text: 'T-1',
        Value: 'V-1',
        Children: [
            {
                Text: 'T-1-1',
                Value: 'V-1-1',
                Children: [
                    { Text: 'T-1-1-1', Value: 'V-1-1-1' },
                    { Text: 'T-1-1-2', Value: 'V-1-1-2' },
                    { Text: 'T-1-1-3', Value: 'V-1-1-3' }
                ]
            },
            {
                Text: 'T-1-2',
                Value: 'V-1-2',
                Children: [
                    { Text: 'T-1-2-1', Value: 'V-1-2-1' },
                    { Text: 'T-1-2-2', Value: 'V-1-2-2' },
                    { Text: 'T-1-2-3', Value: 'V-1-2-3' }
                ]
            },
            {
                Text: 'T-1-3',
                Value: 'V-1-3',
                Children: [
                    { Text: 'T-1-3-1', Value: 'V-1-3-1' },
                    { Text: 'T-1-3-2', Value: 'V-1-3-2' },
                    { Text: 'T-1-3-3', Value: 'V-1-3-3' }
                ]
            }
        ]
    }
];
const matchedValuePath = Helper.findDeepItem(data, {
    key: 'Value',
    value: 'V-1-2-2',
    children: 'Children'
    // , matcher: (item, key, value) => item[key] === value
});
// matchedValuePath === [{Text: 'T-1', Value: 'V-1'}, {Text: 'T-1-2', Value: 'V-1-2'}, { Text: 'T-1-2-2', Value: 'V-1-2-2' }]
```

- **入参**

  - `Object / Array` data: 源对象
  - `Object` options: 处理配置项
    - `String / Number` options.key: 匹配键名
    - `String / Number` options.value: 匹配值
    - `String / Number` options.children: 子级项键名
    - `String / Number` options.matcher: 自定义匹配函数
- **返回**

  - `Array` result: 复合条件的各级对象，最后一项为命中对象
