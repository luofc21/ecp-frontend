<!-- source: http://frontend.pcitech.online/ecp-ui-plus/docs/instruction/commit-specification.html -->

# 开发规范

## Git 提交规范

### ecp-git-commit

> 详见 [ECP Git 提交工具](http://frontend.pcitech.online/docs/ecp-git-commit/)

- 第一步：全局安装 `ecp-git-commit`

```bash
# 全局安装
npm i -g ecp-git-commit --registry http://172.25.20.65:4873/
```

- 第二步：全局初始化

```bash
# 全局初始化
ecpgit init -g
```

- 第三步：项目初始化

```bash
# 默认初始化当前路径的项目
ecpgit init -l

# 或 指定项目路径
ecpgit init -l -p [project-path]
```

### 日常提交

```bash
# 添加所有文件到暂存区，和之前保持一致
git add .

# 请使用 git cz 代替 git commit
git cz

# 和之前保持一致
git push
```

## 发版

### 更新版本号

```bash
# 在上次打 tag 的基础上叠加版本号，并将增量提交写入 CHANGELOG.md
ecpgit release

# 如果需要指定 tag, 示例：
ecpgit release -r v2.0.0-test

git push

git push -- tags
```

### 发布

请在 [Jenkins](http://172.25.20.65:8088/) 上构建并发布。
