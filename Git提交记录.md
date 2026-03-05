# Git 提交记录

## 提交信息

- **仓库地址**: https://github.com/123skkda/Python-Web-FastAPI-.git
- **提交时间**: 2026-03-04
- **提交内容**: FastAPI 学习项目（day01-05 全部代码和文档）

---

## 使用的 Git 命令

### 1. 初始化仓库

```bash
cd "e:/BaiduNetdiskDownload/Python Web开发：FastAPI从入门到实战"
git init
```

**说明**: 在项目目录下初始化一个新的 Git 仓库

---

### 2. 创建 .gitignore 文件

```bash
# 创建 .gitignore 文件，排除不需要提交的文件
```

**排除内容**:
```
# Python
__pycache__/
*.py[cod]
venv/

# Node.js
node_modules/

# 大文件（视频、PDF等）
*.mp4
*.pdf
*.zip
```

**说明**: 防止大文件和不必要的文件被提交到仓库

---

### 3. 添加远程仓库

```bash
git remote add origin https://github.com/123skkda/Python-Web-FastAPI-.git
```

**说明**: 将本地仓库与 GitHub 远程仓库关联

---

### 4. 添加文件到暂存区

```bash
git add .
```

**说明**: 将所有修改的文件添加到暂存区（.gitignore 中的文件会被自动排除）

---

### 5. 提交更改

```bash
git commit -m "添加 FastAPI 学习项目

包含内容：
- day01 FastAPI基础（路由、参数、响应）
- day02 FastAPI进阶（中间件、依赖注入、ORM）
- day03 AI掘金头条新闻模块（完整项目实战）
- 学习文档和对话记录

Co-Authored-By: Claude <noreply@anthropic.com>"
```

**说明**: 将暂存区的文件提交到本地仓库，-m 参数后跟提交信息

---

### 6. 设置主分支并推送

```bash
git branch -M main
git push -u origin main
```

**说明**:
- `git branch -M main`: 将当前分支重命名为 main
- `git push -u origin main`: 推送到远程仓库的 main 分支，并设置上游跟踪

---

## 常用 Git 命令速查

| 命令 | 说明 |
|-----|------|
| `git status` | 查看当前状态 |
| `git add .` | 添加所有文件到暂存区 |
| `git add 文件名` | 添加指定文件到暂存区 |
| `git commit -m "信息"` | 提交更改 |
| `git push` | 推送到远程仓库 |
| `git pull` | 拉取远程更新 |
| `git log` | 查看提交历史 |
| `git diff` | 查看文件差异 |
| `git branch` | 查看分支 |
| `git checkout -b 分支名` | 创建并切换分支 |

---

## 后续更新项目

如果之后有新的修改，可以使用以下命令更新到 GitHub：

```bash
# 1. 查看修改
git status

# 2. 添加修改的文件
git add .

# 3. 提交
git commit -m "更新说明"

# 4. 推送
git push
```

---

## 提交结果

成功提交 **111 个文件**，包含 **12892 行代码**！

项目地址: https://github.com/123skkda/Python-Web-FastAPI-
