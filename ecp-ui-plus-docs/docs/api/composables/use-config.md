<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/api/composables/use-config.html -->

# UseConfig 全局配置

> - Ecp-ui-plus 配置全局生效的组件参数默认值；
> - 支持的参数，在对应文档中标记为 Global 。

```js
import { useConfig } from "@ecp/ecp-ui-plus";
useConfig({ 
    empty: {
        // ... EcpEmpty Attribute Configs
    },
    pagination: {
        // ... EcpPagination Attribute Configs
    },
    imageToolbar: {
        default: {
            // ... EcpImageToolbar - Default - Attribute Configs
        },
        preview: {
            // ... EcpImageToolbar - Type "preview" - Attribute Configs
        },
        cropper: {
            // ... EcpImageToolbar - Type "cropper" - Attribute Configs
        }
    },
    importDialog: {
        // ... EcpImportDialog Attribute Configs
    }
    // ...
 });
```

## 支持全局配置的组件

| key | 生效组件 | 说明 |
| --- | --- | --- |
| empty | `ecp-empty` | 详见 [Empty 空状态 - Attributes](/ecp-ui-plus/docs/components/data/empty.html#attributes) |
| pagination | `ecp-pagination`、`ecp-layout-pagination` | 详见 [Pagination 分页器 - Attributes](/ecp-ui-plus/docs/components/navigation/pagination.html#attributes) |
| imageToolbar | `ecp-image-toolbar`、`ecp-img-view`、`ecp-preview-img-content`、`ecp-preview-img` | 详见 [Image-toolbar 图片操作栏 - Attributes](/ecp-ui-plus/docs/components/layout/image-toolbar.html#attributes) |
| importDialog | `ecp-import-dialog` | 详见 [Import-dialog 导入弹窗 - Attributes](/ecp-ui-plus/docs/components/form/import-dialog.html#attributes) |
