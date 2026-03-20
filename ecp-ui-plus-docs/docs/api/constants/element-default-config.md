<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/api/constants/element-default-config.html -->

# ElementDefaultConfig 默认配置

> 提供默认的 ElementPlus 全局配置，参考：
>
> - [ElementPlus - Config Provider 全局配置](https://element-plus.gitee.io/zh-CN/component/config-provider.html)
> - [ElementPlus - 自定义命名空间](https://element-plus.gitee.io/zh-CN/guide/namespace.html)

```js
import zhCN from 'element-plus/dist/locale/zh-cn.mjs';
export const ElementDefaultConfig = {
    namespace: 'elp', // 默认 ElementPlus 命名空间 elp
    locale: zhCN, // 默认中文
    button: {
        autoInsertSpace: true // 二字汉字按钮型按钮中间插入空格
    }
};
```
