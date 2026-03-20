<!-- source: http://frontend.pcitech.online/docs/guidance/induction/chapter-technic/architecture-system/sso.html -->

# SSO 鉴权

## SSO 定义及鉴权流程

SSO（SingleSignOn，单点登录)，就是通过用户的一次性鉴别登录。当用户在身份认证服务器上登录一次以后，即可获得访问单点登录系统中其他关联系统和应用软件的权限。

![SSO 鉴权](../../../assets/images/guidance/induction/sso.png)

使用SSO鉴权，前端主要参与解决三部分：登录、退出登录、登录过期接口拦截。以下将对这三部分处理进行讲解，要注意的是，这里的示例仅适用于简单内网环境下的一般处理。

## 登录

### 自定义登录页

#### 新增登录页

![SSO 自定义登录页目录结构](../../../assets/images/guidance/induction/sso-login-category.png)

![SSO 鉴权](../../../assets/images/guidance/induction/sso-login-config.png)

#### 登录组件

前端私有源已提供登录组件与相关处理方法集成 ecp-login-component，该组件实现了登录表单和修改密码表单两登录功能模块，表单提交参数默认使用了AES加密，且使用了最新的前后端协商好的登录校验规则（具体规则请咨询相关开发人员）；

#### 返回处理

返回字段 OpCode 为 1001 或 1002 时会自动弹出修改密码表单的 dialog。

### SSO 默认登录页

#### 实现原理

通过代理远程sso-server的静态资源及http接口，从而实现本应用域的登录（前提应用已配置 sso 的proxy代理）。

#### 实现方式

将loginUrl 配置为 应用域+/sso/login， 即 loginUrl = window.location.origin + '/sso/login'；

## 退出登录

直接调用 /sso/logout 接口，返回后代码处理跳转登录页

### 使用自定义登录页的处理

```js
Api.Login.logout().then(res => {
   if(res.OpCode === 0){
     window.location.href = Login.LOGIN_CONFIG.LoginUrl;
   }else{
     this.$message.warning(res.OpDesc || '服务访问异常');
   }
 });
```

### 使用 SSO 默认登录页的处理

```js
Api.Login.logout().then(res => {
  if(res.OpCode === 0){
    window.location.href = `${Login.LOGIN_CONFIG.LoginUrl} + ?service=${LoginUtils.stringsToHex(window.location.origin)} `;
  }else{
    this.$message.warning(res.OpDesc || '服务访问异常');
  }
});
```

### 登录过期接口拦截

> 这里涉及的主应用与子应用的概念，将在后续的微前端进行讲解。

#### 主应用处理

- 接口统一拦截

```js
import { LoginUtils } from 'ecp-login-component';
import * as Login from '../login/config';

// ...
// 新建响应拦截器
Axios.interceptors.response.use(function (response) {
    // ...
    
    //登录拦截处理
    if (response.data.OpCode === 403) {
        var param = {
            response: response.data,
            loginUrl: Login.LOGIN_CONFIG.LoginUrl
        };
        LoginUtils.loginInterceptors(param);
        return response;
    }
  
    // ...
});
```

- portal.js 监听子应用退出

```js
import { LoginUtils } from 'ecp-login-component';

// ...

// 处理微应用发送的sso登录消息
window.eventBus.on('loginStatus', (data) => {
    const param = {
        isPrimaryApp: true,
        response: data.response,
        loginUrl: '/multi/login',
    };
    LoginUtils.loginInterceptors(param);
});
```

#### 子应用处理

- 接口统一拦截

```js
import { LoginUtils } from 'ecp-login-component';
import * as Login from '../login/config';

// ...

// 新建响应拦截器
Axios.interceptors.response.use(function (response) {
    // ...
    
    //登录拦截处理
    if (response.data.OpCode === 403) {
        var param = {
            response: response.data,
            loginUrl: Login.LOGIN_CONFIG.LoginUrl,
          	isPrimaryApp: false,  //是否主应用
            appName: 'multi-info-frontend'
        };
        LoginUtils.loginInterceptors(param);
        return response;
    }
  
    // ...
});
```
