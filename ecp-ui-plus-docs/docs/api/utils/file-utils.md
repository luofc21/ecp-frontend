<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/api/utils/file-utils.html -->

# FileUtils 常用文件处理方法

> 常用文件处理相关

```js
import { FileUtils } from '@ecp/ecp-ui-plus';
```

## 相关常量

### FILE\_SIZE\_BASE

`Number` 文件大小的基本单位，定义为 1024 B(字节)

```js
/**
 * @constant { Number } FILE_SIZE_BASE 文件大小的基本单位，定义为 1024 B(字节)
 */
export const FILE_SIZE_BASE = 1024;
```

### FILE\_SIZE

`Array` 文件大小单位数组，每项包含从B到PB的单位、单位对应的最小值、中文单位

```js
/**
 * @constant { Array } FILE_SIZE 文件大小单位数组
 * 每项包含从B到PB的单位、单位对应的最小值、中文单位
 */
export const FILE_SIZE = [
    { unit: 'B', min: Math.pow(FILE_SIZE_BASE, 0), unitCHN: '字节' },
    { unit: 'KB', min: Math.pow(FILE_SIZE_BASE, 1), unitCHN: '千字节' },
    { unit: 'MB', min: Math.pow(FILE_SIZE_BASE, 2), unitCHN: '兆字节' },
    { unit: 'GB', min: Math.pow(FILE_SIZE_BASE, 3), unitCHN: '吉字节' },
    { unit: 'TB', min: Math.pow(FILE_SIZE_BASE, 4), unitCHN: '太字节' },
    { unit: 'PB', min: Math.pow(FILE_SIZE_BASE, 5), unitCHN: '拍字节' }
];
```

### FILE\_SIZE\_UNIT\_MAP

`Array` 文件大小单位映射对象

> key: 单位, value: 该单位对应的最小字节数

```js
/**
 * @constant { Object } FILE_SIZE_UNIT_MAP 文件大小单位映射对象
 * key: 单位
 * value: 该单位对应的最小字节数
 */
export const FILE_SIZE_UNIT_MAP = FILE_SIZE.reduce((prev, curr) => ({
    ...prev,
    [curr.unit]: curr.min
}), {});
```

## 文件信息

### getValidFileUnit

`格式化` 获取有效的文件大小单位

- **入参**
  - `String` fileUnit: 文件单位
  - `Boolean` includeMaxUnit: 是否返回最大单位
- **返回**
  - `String` 格式化后的文件大小单位

### formatFileSize

`格式化` 文件大小展示格式化

- **入参**
  - `Number` fileSize: 文件大小
  - `String` fileSizeUnit: 文件大小单位
  - `String` targetUnit: 目标文件大小单位
- **返回**
  - `Object` result: 文件大小展示格式化对象
    - `Number` result.value: 单位格式化后的文件大小数值
    - `String` result.unit: 单位格式化后的文件大小单位

### getFileNameFromUrl

`信息提取` 从文件 URL 获取文件名

- **入参**
  - `String / URL` fileUrl: 文件 URL
- **返回**
  - `String` 文件名

### getFileExtFromUrl

`信息提取` 从文件 URL 获取文件扩展名

- **入参**
  - `String / URL` fileUrl: 文件 URL
- **返回**
  - `String` 文件扩展名

### getMimeFromFileExt

`信息提取` 从文件 URL 的文件扩展名获取 MIME 类型

- **入参**
  - `String / URL` fileUrl: 文件 URL
- **返回**
  - `String` MIME 类型

## 文件校验

### validateFileSize

`文件校验` 文件大小校验

```js
const result = FileUtils.validateFileSize(file, options);
if (result.code === 0) {
  // ...
} else {
  throw new Error(result.message);
}
```

- **入参**
  - `File / Number` file: 文件对象或文件大小
  - `Object` options: 校验配置项
    - `Number` options.minFileSize: 最小文件大小数值
    - `String` options.minFileUnit: 最小文件大小单位
    - `Number` options.maxFileSize: 最大文件大小数值
    - `String` options.maxFileUnit: 最大文件大小单位
- **返回**
  - `Object` result: 校验结果
    - `Number` result.code: 校验结果码, 0: 成功, 1: 超上限, 2: 不足下限, 999: 校验配置项上下限配置有误
    - `String` result.message: 校验结果描述信息
    - `Number` result.minFileSize: 有效的最小文件大小数值
    - `String` result.minFileUnit: 有效的最小文件大小单位
    - `Number` result.maxFileSize: 有效的最大文件大小数值
    - `String` result.maxFileUnit: 有效的最大文件大小单位

### validateFileType

`文件校验` 文件类型校验

```js
const result = FileUtils.validateFileType(file, options);
if (result) {
    // ...
} else {
    throw new Error('文件类型校验失败');
}
```

- **入参**
  - `File / Number` file: 文件对象或文件大小
  - `Object` options: 校验配置项
    - `String` options.accept: 支持的文件类型，优先级高于 options.fileType ，可用通配符、文件扩展名、 MIME 类型
    - `Number` options.fileType: 文件分类大类，适用于只限制文件大类的场景（如只允许选择证书文件）
      - fileType 可选值，同 [Mime 文档类型 - MIME\_CLASSIFY](/ecp-ui-plus/docs/api/constants/mime.html#常量枚举) 的一级 key
- **返回**
  - `Boolean` result: 是否校验通过

## 文件操作

### downloadFile

`文件操作` 下载文件

```js
FileUtils.downloadFile(file, fileName);
```

- **入参**
  - `String / File / Blob / URL` file: 文件路径或文件对象
  - `String / Function` fileName: 文件名
- **返回**
  - `Promise`

### blobDownloadFile

`文件操作` Blob 下载文件

```js
FileUtils.blobDownloadFile(file, fileName, fileType);
```

- **入参**
  - `String / File / Blob / URL` file: 文件路径或文件对象
  - `String / Function` fileName: 文件名, file 是 dataUrl 字符串时必填
  - `String` fileType: 文件 MIME 类型, file 是链接或 URL, 且无文件后缀名时必填
- **返回**
  - `Promise`

## 文件转换

### dataURLToFile

`文件转换` 将 dataURL 转换为 File 对象

```js
const file = FileUtils.dataURLToFile(dataURL, name);
```

- **入参**
  - `String` dataURL
  - `String` name: 文件名
- **返回**
  - `File` File 对象

### dataURLToBlob

`文件转换` 将 dataURL 转换为 Blob 对象

```js
const blob = FileUtils.dataURLToBlob(dataURL);
```

- **入参**
  - `String` dataURL
- **返回**
  - `Blob` Blob 对象

### fileToDataURL

`文件转换` 将 File 文件对象转换为 dataURL

```js
const dataURL = await FileUtils.fileToDataURL(file);
```

- **入参**
  - `File` file: File 文件
- **返回**
  - `Promise` Promise 对象
    - resolve: dataURL

### fileToBlob

`文件转换` 将 File 文件对象转换为 Blob 对象

```js
const blob = await FileUtils.fileToBlob(file);
```

- **入参**
  - `File` file: File 文件
- **返回**
  - `Promise` Promise 对象
    - resolve: Blob 文件

### blobToDataURL

`文件转换` 将 Blob 对象转换为 dataURL

```js
const dataURL = await FileUtils.blobToDataURL(blob);
```

- **入参**
  - `Blob` blob: Blob 文件
- **返回**
  - `Promise` Promise 对象
    - resolve: Blob 文件

### blobToFile

`文件转换` 将 Blob 文件对象转换为 File 文件对象

```js
const file = FileUtils.blobToFile(blob, name);
```

- **入参**
  - `Blob` blob: Blob 文件
  - `String` name: 文件名
- **返回**
  - `File` File 文件

## FormData 处理

### getFormData

`FormData 处理` 将数据转换为 FormData

```js
const formDataParams = FileUtils.getFormData(params, options);
```

- **入参**
  - `Object / Array` params: 参数对象或数组
  - `Object` options: 转换配置项
    - `FormData` options.formData: FormData 实例，不传会自动创建
    - `Boolean` options.flatten: 是否扁平化
      - false: 一级对象中值是对象的都会进行JSON.stringify处理，即 `key: JSON.stringify(value)`；
      - true: 嵌套对象会被扁平化，扁平化后的key为：`key1.key11.key111`，值是数组时key为：`key1.key11[]`
- **返回**
  - `FormData` 参数的 FormData 实例
