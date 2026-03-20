<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/components/form/import-dialog.html -->

# <ecp-import-dialog> 导入弹窗

> 一般导入功能比较单一，但实现处理又比较麻烦，所以封装了通用的导入弹窗，方便使用。

## 基础用法

## Attributes

| 参数 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| visible / v-model:visible | 控制弹窗的显隐 | Boolean |  |
| title Global | 弹窗标题 | String | '导入' |
| confirm-button-text Global | 弹窗提交按钮文本 | String | '提交' |
| cancel-button-text Global | 弹窗取消按钮文本 | String | '取消' |
| tip Global | 模板填写提示文本 | String | '按照模板格式填写导入数据。' |
| template-path | 导出模板的下载链接， 不传或为空会隐藏导入步骤、下载入口、模板填写提示 | String |  |
| template-name | 导出模板的文件名(需要带文件后缀)，一般不需要传入 | String |  |
| action | 导入接口链接 | String |  |
| method Global | 导入接口请求方法 | String | 'POST' |
| name Global | 导入文件的字段名 | String | 'file' |
| file-validate | 文件校验方法 | Function |  |
| data | 其它需要携带的参数 | Object / FormData |  |
| before-upload | 导入接口请求前调用的方法，返回 false 或 Promise.reject 会阻止请求 | Function |  |
| custom-request | 自定义导入接口请求，同 ElUpload 的 http-request | Function | 见 [responseProps 的结构](#responseprops-的结构) |
| response-props Global | 导入请求返回项配置 | Object |  |
| el-dialog-props | ElDialog 其它支持的属性 | Object |  |
| el-upload-props | ElUpload 其它支持的属性 | Object |  |

### responseProps 的结构

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| code Global | 业务状态码字段名 | String | 'OpCode' |
| successCode Global | 业务状态码成功状态值 | Number / String | 0 |
| desc Global | 描述字段名 | String | 'OpDesc' |
| data Global | 数据字段名 | String | 'Data' |
| successCount Global | 导入成功条数字段名 | String | 'Data.SuccessNum' |
| failCount Global | 导入失败条数字段名 | String | 'Data.FailNum' |
| failMsg Global | 导入失败描述字段名 | String | 'Data.Msg' |
| failList Global | 文件导入失败的详细描述字段名 | String | 'Data.FailList' |
| failRowNum Global | failList[index] 失败数据项所在文件行数字段名 | String | 'RowNum' |
| failRowNum Global | failList[index] 失败数据项失败原因字段名 | String | 'ErrorMsg' |

## Events

| 事件名称 | 说明 | 回调参数 |
| --- | --- | --- |
| update:visible | 更新弹窗的显隐 | Boolean |
| update | 有导入成功时的回调，可用于触发父组件的数据更新 |  |
| close | 弹窗关闭回调 |  |

## Slots

| 插槽名 | 说明 | 参数 |
| --- | --- | --- |
| step-title | 步骤项插槽 | { stepIndex: `Number` } |
| tip | 模板填写提示文本插槽 |  |
| file-name | 文件列表项的文件名插槽 (包含文件Icon) | { file: `UploadFile`, index: `Number` } |

## Exposes

| 方法/属性 | 类型 | 说明 | 入参 |
| --- | --- | --- | --- |
| uploadRef | ComponentRef | ElUpload 组件实例 |  |
| fileList | ArrayRef | 当前弹窗维护的文件列表 |  |
| removeFile | Function | 移除文件的方法 | file: `UploadFile`, index: `Number` |
