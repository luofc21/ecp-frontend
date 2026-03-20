<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/design/spacer.html -->

# Spacer 间距类名

> - 更新布局而无需创建新的类，间距辅助器对于修改元素的填充（padding）和边距（margin）都非常有用。
> - 对于一般情况，通常应用 xx-2 间距。

## 使用说明

将 **margin** 或者 **padding** 应用于一个元素，范围在 0 到 5 之间。每个尺寸增量都设计成与常用 `Material Design` 间距对齐。这些类可以使用 `{property}{direction}-{size}` 这个格式来应用。

### Property 类型

- *m* - 对应 *margin* ；
- *p* - 对应 *padding* ；

### Direction 方向

- *t* - 对应 *margin-top* 或者 *padding-top* 属性 ；
- *b* - 对应 *margin-bottom* or *padding-bottom* ；
- *l* - 对应 *margin-left* or *padding-left* ；
- *r* - 对应 *margin-right* or *padding-right* ；
- *x* - 同时对应 *\*-left* 和 *\*-right* 属性 ；
- *y* - 同时对应 *\*-top* 和 *\*-bottom* 属性 ；

### Size 增量

> 计算基数: spacer: 16px

- *0* - 将 *margin* 或者 *padding* 设置为 *0* ，会使这些属性被删除 ；
- *1* - 将 *margin* 或者 *padding* 属性设置为 *spacer \* .25* ；
- *2* - 将 *margin* 或者 *padding* 属性设置为 *spacer \* .5* ；
- *3* - 将 *margin* 或者 *padding* 属性设置为 *spacer* ；
- *4* - 将 *margin* 或者 *padding* 属性设置为 *spacer \* 1.5* ；
- *5* - 将 *margin* 或者 *padding* 属性设置为 *spacer \* 2* ；
- *6* - 将 *margin* 或者 *padding* 属性设置为 *spacer \* 2.5* ；
- *7* - 将 *margin* 或者 *padding* 属性设置为 *spacer \* 3* 。
