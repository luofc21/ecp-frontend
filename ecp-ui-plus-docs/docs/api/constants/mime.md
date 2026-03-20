<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/api/constants/mime.html -->

# Mime 文档类型

参考：

- [Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml)

## 基本用法

> - MIME\_CLASSIFY 常用文档类型 (按文档大类分类枚举)；
> - MIME\_MAP 后缀-文档类型枚举 (即 MIME\_CLASSIFY 末级 key-value 平铺)

### 组件中使用

#### Options Api

- 从 `this.$constant.MIME_CLASSIFY` 、 `this.$constant.MIME_MAP` 获取

```vue
<template>
    <div>{{ $constant.MIME_CLASSIFY.xxx }}</div>
    <div>{{ $constant.MIME_MAP.xxx }}</div>
</template>
<script>
export default {
    mounted () {
        console.log('this.$constant.MIME_CLASSIFY', this.$constant.MIME_CLASSIFY);
        console.log('this.$constant.MIME_MAP', this.$constant.MIME_MAP);
    }
};
</script>
```

#### Composition Api

- 直接引入

```vue
<template>
    <div>{{ MIME_CLASSIFY.xxx }}</div>
    <div>{{ MIME_MAP.xxx }}</div>
</template>
<script setup>
import { MIME_CLASSIFY, MIME_MAP } from '@ecp/ecp-ui-plus';
console.log('MIME_CLASSIFY', MIME_CLASSIFY);
console.log('MIME_MAP', MIME_MAP);
</script>
```

### JS 中使用

- 直接引入

```js
import { MIME_CLASSIFY, MIME_MAP } from '@ecp/ecp-ui-plus';
console.log('MIME_CLASSIFY', MIME_CLASSIFY);
console.log('MIME_MAP', MIME_MAP);
```

## 常量枚举

```ts
export const MIME_CLASSIFY = {
    // 文本
    text: {
        txt: 'text/plain',
        html: 'text/html',
        md: 'text/markdown',
        csv: 'text/csv',
        json: 'application/json',
        xml: 'application/xml',
        yaml: 'application/yaml',
        yml: 'application/yaml',
        toml: 'application/toml',
        properties: 'application/properties'
    },

    // 图像
    image: {
        png: 'image/png',
        jpg: 'image/jpeg',
        jpeg: 'image/jpeg',
        jng: 'image/x-jng',
        gif: 'image/gif',
        svg: 'image/svg+xml',
        bmp: 'image/bmp',
        webp: 'image/webp',
        ico: 'image/x-icon'
        // tiff: 'image/tiff',
        // tif: 'image/tiff',
        // psd: 'image/vnd.adobe.photoshop'
    },

    // 音频
    audio: {
        mp3: 'audio/mpeg',
        wav: 'audio/wav',
        ogg: 'audio/ogg',
        flac: 'audio/flac',
        aac: 'audio/aac',
        m4a: 'audio/mp4',
        wma: 'audio/x-ms-wma',
        mid: 'audio/midi',
        midi: 'audio/midi'
    },

    // 视频
    video: {
        mp4: 'video/mp4',
        webm: 'video/webm',
        ogg: 'video/ogg',
        mpg: 'video/mpeg',
        mpeg: 'video/mpeg',
        avi: 'video/x-msvideo',
        wmv: 'video/x-ms-wmv',
        flv: 'video/x-flv',
        mkv: 'video/x-matroska',
        mov: 'video/quicktime',
        '3gp': 'video/3gpp',
        ts: 'video/mp2t'
    },

    // 文档
    document: {
        pdf: 'application/pdf',
        doc: 'application/msword',
        docx: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        xls: 'application/vnd.ms-excel',
        xlsx: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        ppt: 'application/vnd.ms-powerpoint',
        pptx: 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
        pptm: 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
        xps: 'application/vnd.ms-xpsdocument'
        // odt: 'application/vnd.oasis.opendocument.text',
        // ods: 'application/vnd.oasis.opendocument.spreadsheet',
        // odp: 'application/vnd.oasis.opendocument.presentation',
        // otp: 'application/vnd.oasis.opendocument.presentation-template',
        // ots: 'application/vnd.oasis.opendocument.spreadsheet-template',
        // ott: 'application/vnd.oasis.opendocument.text-template',
        // odg: 'application/vnd.oasis.opendocument.graphics',
        // odc: 'application/vnd.oasis.opendocument.chart'
    },

    // 压缩包
    compress: {
        zip: 'application/zip',
        rar: 'application/x-rar-compressed',
        '7z': 'application/x-7z-compressed',
        tar: 'application/x-tar',
        gz: 'application/gzip',
        bz2: 'application/x-bzip2',
        xz: 'application/x-xz',
        zst: 'application/zstd'
        // lz4: 'application/lz4',
        // zstd: 'application/zstd',
        // lzma: 'application/x-lzma',
        // lzop: 'application/x-lzop',
        // cpio: 'application/x-cpio',
        // rpm: 'application/x-rpm',
        // deb: 'application/x-deb',
        // dmg: 'application/x-apple-diskimage',
        // iso: 'application/x-iso9660-image',
        // vhd: 'application/vnd.microsoft.hyper-v.system',
        // vhdx: 'application/vnd.microsoft.hyper-v.vhdx',
        // vmdk: 'application/vnd.vmware.vmdk',
        // vdi: 'application/x-virtualbox-vdi',
        // vhdm: 'application/x-virtualbox-vhd',
        // vhdf: 'application/x-virtualbox-vhdf'
    },

    // 传真
    fax: {
        tiff: 'image/tiff',
        tif: 'image/tiff'
        // psd: 'image/vnd.adobe.photoshop'
    },

    // 证书
    certificate: {
        pem: 'application/x-pem-file',
        cer: 'application/pkix-cert',
        crt: 'application/x-x509-ca-cert',
        der: 'application/x-x509-ca-cert'
        // p7b: 'application/x-pkcs7-certificates',
        // p7c: 'application/pkcs7-mime',
        // p7m: 'application/pkcs7-mime',
        // p7r: 'application/x-pkcs7-certreqresp',
        // p7s: 'application/pkcs7-signature',
        // p7v: 'application/pkcs7-mime',
        // p7x: 'application/pkcs7-mime',
        // p10: 'application/pkcs10',
        // p12: 'application/x-pkcs12',
        // pfx: 'application/x-pkcs12',
        // spc: 'application/x-pkcs7-certificates',
        // spfx: 'application/x-pkcs7-certificates',
        // spkac: 'application/x-pkcs10',
        // spki: 'application/x-pkcs7-certificates',
        // spkid: 'application/x-pkcs7-certificates',
        // spsk: 'application/x-pkcs7-certificates',
        // spskac: 'application/x-pkcs7-certificates'
    },

    // 其他
    other: {
        // exe: 'application/x-msdownload',
        // msi: 'application/x-msi',
        // msu: 'application/x-msu-windows-update',
        // msix: 'application/msix',
        // msixbundle: 'application/msixbundle',
        // msixdelta: 'application/msixdelta',
        // msixpackage: 'application/msixpackage',
        unknown: 'application/octet-stream'
    }
};

export const MIME_MAP = Object.values(MIME_CLASSIFY).reduce((prev, curr) => {
    Object.entries(curr).forEach(([key, value]) => {
        const validKey = key.toLowerCase();
        if (prev[validKey]) {
            const valueArr = [...new Set([...prev[validKey].split(','), value])];
            prev[validKey] = valueArr.filter(Boolean).join(',');
        } else {
            prev[validKey] = value;
        }
    });
    return prev;
}, {});
```
