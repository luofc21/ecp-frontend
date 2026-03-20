<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/api/composables/use-theme.html -->

# UseTheme 主题切换

> 配合 [Theme 主题定义](/ecp-ui-plus/docs/design/theme.html) 使用。

```js
import { useTheme } from "@ecp/ecp-ui-plus";
const { isDark, theme, setTheme } = useTheme({ /* ...UseThemeConfig */ });
```

## 入参

> 主题属性 key 支持自定义, 注意主题样式 css 作用域属性 key 与变更主题时传入的 key 对应。

| 字段 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| modes | Object<String, String> |  | 是 | 主题标识 key 枚举 |
| auto | Boolean | false |  | 是否根据系统颜色模式自动更新 |
| transition | Boolean | false |  | 是否开启主题切换过渡效果，详见 [添加过渡效果](#添加过渡效果)。 |
| ... |  |  |  | 其它参数见 [VueUse - useColorMode](https://vueuse.org/core/useColorMode/) |

## 返回

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| isDark | ComputedRef<Boolean> | 是否深色模式 |
| theme | WritableComputedRef<String> | 主题标识 key |
| setTheme | Function | 设置主题标识 key |

## 示例代码

### 基础用法

点击查看代码片段

```vue
<!-- path/to/custom-theme-control.vue -->
<template>
    <ecp-button text="切换至主题 theme-x" @click="toThemeX" />
    <ecp-button text="切换至主题 theme-y" @click="toThemeY" />
    <ecp-button text="切换至主题 theme-z" @click="toThemeZ" />
</template>

<script setup>
import { useTheme } from '@ecp/ecp-ui-plus';

const { isDark, theme, setTheme } = useTheme({
    modes: {
        'theme-x': ' theme-x',
        'theme-y': ' theme-y',
        'theme-z': ' theme-z'
        // ...
    }
});

// 切换至主题 theme-x
const toThemeX = () => setTheme('theme-x');

// 切换至主题 theme-x
const toThemeY = () => setTheme('theme-y');

// 切换至主题 theme-x
const toThemeZ = () => setTheme('theme-z');
</script>
```

## 添加过渡效果

`🧪 Experimental`

UseTheme 支持添加主题切换过渡效果。

> - 将 `transition` 设为 `true` 后，`主题标识` 和 `深色/浅色模式` 标识会在 `document.startViewTransition` 回调中更新，需要注意 [浏览器兼容性](https://developer.mozilla.org/zh-CN/docs/Web/API/View_Transitions_API#%E6%B5%8F%E8%A7%88%E5%99%A8%E5%85%BC%E5%AE%B9%E6%80%A7)；
> - 过渡效果需自行添加所需 CSS，详见 [View Transitions API](https://developer.mozilla.org/zh-CN/docs/Web/API/View_Transitions_API)。

### 过渡效果示例

> 可点击文档右上角切换主题，查看过渡动效。

点击查看代码片段

```vue
<template>
    <ecp-button @change="setThemeKey">点击随机切换主题</ecp-button>
</template>

<script setup>
import { useTheme } from '@ecp/ecp-ui-plus';

const modes = {

    // modesPresets
    default: 'default',
    dark: 'dark',

    // modesLight
    'blue-grey': 'blue-grey',
    pink: 'pink',
    purple: 'purple',
    teal: 'teal',

    // modesDark
    'blue-grey-dark': 'blue-grey-dark',
    'pink-dark': 'pink-dark',
    'purple-dark': 'purple-dark',
    'teal-dark': 'teal-dark'
};
const modesCounts = Object.keys(modes).length;

const { isDark, theme, setTheme } = useTheme({
    modes,
    auto: true, // 开启自动根据系统主题切换
    transition: true // 开启过渡动画
});

const isDarkTheme = ref(false);
// 当前激活的主题
const activeTheme = reactive(theme);

// 更改当前激活的主题
const setThemeKey = () => {
    activeTheme.value = modes[Object.keys(modes)[Date.now() % modesCounts]];
};

const onChange = (value) => {
    setTheme(value);
};
watch(
    () => activeTheme.value,
    (newVal) => {
        if (newVal) {
            onChange(newVal);
        }
    },
    {
        immediate: true,
        deep: true
    }
);

// 系统主题切换时，isDark 值会更新，需要同步到当前激活的主题
watch(
    () => isDark.value,
    newVal => {
        if (activeTheme.value === 'dark' || activeTheme.value === 'default') {
            setThemeKey(newVal ? 'dark' : 'default');
        } else {
            setThemeKey(newVal ? `${activeTheme.value}-dark` : activeTheme.value.replace(/-dark/, ''));
        }
    }
);
</script>

<style lang="scss">
/* 主题切换动效 */
@keyframes theme-transition {
    0% {
        clip-path: polygon(0 0, 0 0, -30vh 100%, -30vh 100%);
    }

    100% {
        clip-path: polygon(0 0, calc(100% + 30vh) 0, 100% 100%, -30vh 100%);
    }
}

::view-transition-old(root) {
    animation: none;
}

::view-transition-new(root) {
    mix-blend-mode: normal;
    animation: theme-transition 750ms ease-in-out;
}
</style>
```
