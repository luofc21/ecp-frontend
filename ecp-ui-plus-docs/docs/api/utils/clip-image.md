<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/api/utils/clip-image.html -->

# ClipImage 图片裁剪

> 根据指定裁剪区域范围裁剪图片。

```js
import { clipImage } from '@ecp/ecp-ui-plus';

const startClip = async () => {
    // 单一区域
    const clipResult = await clipImage(imgUrl, options);

    // 多区域
    const clipResultArray = await clipImage(imgUrl, optionsArray);
};
```

- **入参**
  - `String` imgUrl: 图片路径
  - `Array<Options>` / `Options` 裁剪区域配置，传入Array 时裁剪多个区域
    - Options.x: `Number` 裁剪左上角 X 坐标，单位 px
    - Options.y: `Number` 裁剪左上角 Y 坐标，单位 px
    - Options.w: `Number` 裁剪宽度，单位 px
    - Options.h: `Number` 裁剪高度，单位 px
- **返回**
  - `Promise` 裁剪结果，成功返回 `Array<ClipResult>` 或 `<ClipResult>`
    - ClipResult.w: `Number` 裁剪宽度，单位 px
    - ClipResult.h: `Number` 裁剪高度，单位 px
    - ClipResult.url: `String` 裁剪结果图片 url
