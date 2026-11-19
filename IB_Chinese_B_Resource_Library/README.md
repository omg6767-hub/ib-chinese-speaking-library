# IB Chinese B Speaking Library — 教师使用指南

## 推荐方案：GitHub Pages + Pages CMS（不需要 Supabase / Google OAuth / 学生账号）

**学生**：打开公开网页，无需登录。  
**教师**：通过 GitHub 账号登录 [Pages CMS](https://pagescms.org)，可在网页中新增/编辑图片、提示问题、词汇及发布状态。CMS 保存改动到 GitHub；GitHub Actions 自动更新学生网页。  
**录音功能**：本版本没有录音、学生信息或上传功能。

> 注意：GitHub Pages 站点及公开仓库里的图片、词汇和草稿文件是**公开可访问**的。`published: false` 仅隐藏网页中的任务，**不等于私密存储**。不要放学生姓名、录音、私密照片或未获授权的图片。

## 第一次部署（约 15–30 分钟，不含学校 IT 审批）

1. 注册或登录 https://github.com 。建议使用你个人可管理的 GitHub 账号，或学校认可的账号。
2. 新建一个 **Public** repository（例如 `ib-chinese-speaking`）。将 ZIP 解压后的**全部文件和隐藏文件**上传到仓库根目录，包括 `.pages.yml` 和 `.github/workflows/deploy.yml`。上传时可以使用 GitHub 的 **Add file → Upload files**；Mac Finder 按 `Cmd + Shift + .` 可以显示隐藏文件。请确保分支名为 `main`。
3. 在 GitHub 仓库进入 **Settings → Pages**，在 **Build and deployment → Source** 选择 **GitHub Actions**。
4. 打开 **Actions**，等待 **Publish speaking library** 工作流成功。然后在 **Settings → Pages** 找到网址，通常类似 `https://YOURNAME.github.io/ib-chinese-speaking/`。
5. 打开 https://pagescms.org ，通过 **GitHub** 授权登录。选择该 repository。Pages CMS 会读取仓库根目录 `.pages.yml`，出现 **Speaking Pictures / 图片口语任务** 集合。
6. 点击新增任务，选择 IB 主题，上传图片，填写中英提示和词汇；先将 **Published** 设为 false（草稿），准备好后改为 true。点击保存。Pages CMS 会提交到 GitHub；稍等 GitHub Actions 自动发布后，学生页面更新。
7. 将 GitHub Pages 学生网址发给学生，**不要**发 Pages CMS 编辑网址。

### 如果 Pages CMS 看不到仓库
- 检查 GitHub 授权是否允许 Pages CMS 访问该仓库。
- 检查 `.pages.yml` 是否位于仓库根目录；注意它是隐藏文件。
- 如果 Pages CMS 显示配置字段错误，请按其当前版本的配置提示调整 `.pages.yml`。第三方平台界面和字段规范可能更新。

### 如果学生网站打不开或显示空白
- 在 GitHub **Actions** 查看是否成功；需要启用 GitHub Actions 和 Pages。
- 检查 `main` 分支与 workflow 的 `branches: [main]` 一致。
- 若网页能打开却提示无法读取资料，检查 `data.json` 是否由构建步骤生成；不要直接双击 `index.html`，浏览器本地文件模式通常无法 `fetch` JSON。
- 图片若无法显示，确认 YAML 的 `image` 路径是 `/assets/images/filename.jpg`，并且图片确实在仓库里。

## 日常维护

- **添加图片**：Pages CMS → Speaking Pictures → New → 上传图片，填标题、主题、四组中英提示和词汇 → Save。
- **只发布已有材料**：设为 `published: true`；其他任务可以暂存为 `false`。
- **修改图片/词汇**：打开已有任务编辑并保存；无需重新上传整个网站。
- **隐藏任务**：把 Published 关掉；网页隐藏，但公开仓库的原始文件仍可访问。
- **删除任务**：在 CMS 删除该条内容（如果平台支持），或在 GitHub 删除对应的 `content/tasks/*.yml` 文件。
- **五大主题**：身份认同、体验、人类创造力、社会组织、共享地球。
- **准备时间**：学生页面有15分钟倒计时和仅保存在当前浏览器的临时笔记区；无录音上传。

## 本地预览（可选）

安装 Python 3 后，在解压目录运行：

```bash
pip install -r requirements.txt
python build.py
python -m http.server 8000
```

浏览器打开 `http://localhost:8000`。不需要本地预览也可以直接部署。

## 关于学校与版权

该方案不需要学校 Google 账号登录，学生可通过网址直接浏览，因此适合**可公开分享的教学图片和词汇**。请确认图片使用权限；本 ZIP 中的第一张图片来自你在聊天中提供的截图，仅作为演示，公开发布前请确认有权在网站上使用或换成已授权图片。学校若禁止公开发布教学资源，请改用学校批准的受限访问平台（如 Google Sites）。
