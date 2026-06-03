# Google家族产品

*本人是在windows电脑上进行相关的安装和各种操作，注意甄别*

---

## 引言

!!!
    Google家的目前产品大致可以分成下面3类，每一类包含不同的存在形式，并且与下文的详细介绍保持一一对应：

* **Gemini 通用智能体与知识库：**
  * Gemini 官方网页端
  * NotebookLM 智能知识库网页端


* **Google 开发者与云端全栈 AI 平台：**
  * Google AI Studio 网页工作区（含 Build Mode）
  * Firebase Studio（原 Project IDX）


* **Gemma 开放大模型：**
  * Google Gemma 4 本地 CLI 命令行端 (Ollama)
  * Google Gemma 4 本地图形化 Web 界面 (Open WebUI)



## 1. Gemini 官方网页端

* **产品名称：** Gemini Web
* **形式：** **网页端**（Web 浏览器 / 可作为 PWA 独立窗口运行）
* **下载方法：** **无需常规安装**。在电脑浏览器中直接访问官方主站：`gemini.google.com`，登录 Google 账号。如果想更方便地使用，可以点击 Edge 或 Chrome 浏览器地址栏右侧的“安装”图标，将其转为 PWA 桌面独立窗口，并常驻在 Windows 任务栏。
* **常用用处：**
* **通用多模态生产力：** 支持日常文本编写、跨语言高级翻译、复杂的逻辑分析与联网搜索。支持“对话内可视化（Interactive visuals）”，能够直接将高难度问题在聊天框内转变为可交互的流向图或数据图表。
* **生态数据联动（Extensions）：** 开启扩展程序后，能安全地直接检索和调用你的 Gmail 邮件、Google Docs 文档、云端硬盘以及 YouTube 视频内容，进行智能摘要、跨文档提炼或视频要点梳理。

## 2. NotebookLM 智能知识库网页端

* **产品名称：** NotebookLM
* **形式：** **网页端**（Web 浏览器）
* **下载方法：** **无需下载**。在电脑浏览器中直接访问官方专属站点：`notebooklm.google.com` 即可。
* **常用用处：**
* **重度文献与科研管理：** 专为论文阅读和深度笔记管理打造。你可以把几十篇 PDF 学术论文、本地 Markdown 笔记库或长网页链接一次性塞进一个“笔记本”里，Gemini 会基于这些**专属语料**进行高精度、严格遵循原文的问答与多源交叉引用，绝不胡说八道。
* **自动生成音频对谈（Audio Overview）：** 能够一键把复杂的学术文本、算法架构或研究大纲自动转化为两个 AI 角色模拟对谈的英文音频（播客格式），帮你换种方式轻松听懂核心观点。

## 3. Google AI Studio 网页工作区（含 Build Mode）

* **产品名称：** Google AI Studio
* **形式：** **网页端高级开发工具 / 原型构建看板**
* **下载方法：** **无需下载**。直接访问官方开发者平台：`aistudio.google.com`。登录后可免费且极其方便地创建并获取拥有百万级超长上下文模型的 API Key。
* **常用用处：**
* **Vibe Coding 全栈应用生成（Build Mode）：** 最新升级的 Build Mode 支持“全栈运行时”。你只需用自然语言描述想法，它就能自动生成包含 React 前端、Node.js 后端服务、集成 npm 依赖包以及 Firebase 数据库的完整全栈应用，并支持通过页面框选标注实时调整 UI 与功能。
* **前沿模型极限调试：** 可以在 Playground 中自由调配 Gemini 3、Flash Live（极速实时音视频流交互模型）、Veo（高画质视频生成）以及 Lyria（专业级音频生成）等底层前沿引擎的各项参数并进行 Prompt 测试与工程调用。

## 4. Firebase Studio（原 Project IDX）

* **产品名称：** Firebase Studio
* **形式：** **云端全功能 IDE / 全栈开发工作区**
* **下载方法：** **无需下载**。直接通过浏览器访问官方主页：`idx.dev` 自动重定向进入 Firebase Studio 控制台，直接在浏览器里写代码。
* **常用用处：**
* **无缝 AI 编程辅助：** 原 Project IDX 完美并入 Firebase 家族后的全形态。内置原生 Gemini 编程智能体，支持直接通过对话让 AI 增改、补全和解释代码，支持 Angular, Flutter, Next.js, React 等全栈框架模板，秒级初始化云端项目。
* **多端云模拟器协同：** 完美的云端沙箱开发环境。由于它直接在浏览器右侧提供集成的多端虚拟预览窗，你不再需要在本地 Windows 上配置繁重的 Android 或 Web 模拟器环境，结合本地一键部署（Cloud Run）即可完成闭环。

## 5. Google Gemma 4 本地 CLI 命令行端 (Ollama)

* **产品名称：** Google Gemma 4 (Ollama CLI 运行版)
* **形式：** **终端命令行工具 (CMD / PowerShell)**
* **下载方法：** 确保电脑安装了 Ollama 环境。在 Windows 的 CMD 或 PowerShell 中直接执行指令：`ollama run gemma4`（可按需选择 e2b, e4b, 26b 或 31b 等不同参数大小）。
* **常用用处：**
* **本地轻量快速推理：** 极其适合在 Windows 终端中进行快速代码补全、Linux 脚本咨询、或直接作为本地 Python 脚本的后台调用模型。
* **压榨显卡极限性能：** 针对拯救者 Y9000P 强大的标压处理器与 NVIDIA RTX 独显，纯命令行运行完全不占用系统多余的图形资源，能跑出最高的 Token 生成速率（极速吐字），丝滑体验本地大模型推理。

## 6. Google Gemma 4 本地图形化 Web 界面 (Open WebUI)

* **产品名称：** Google Gemma 4 (Open WebUI 前端整合版)
* **形式：** **本地图形化网页界面 (Local Web Interface)**
* **下载方法：** 配合本地 Docker 环境，在 Windows 的终端中运行一行命令拉取并运行：`docker run -d -p 3000:8080 --gpus all -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:cuda`，随后在电脑浏览器访问 `localhost:3000` 即可。
* **常用用处：**
* **100% 隐私离线私域知识库：** 可以完全断网工作。你可以放心地把本地最核心的代码工程、未发表的科研数据、敏感资产或私人 Markdown 笔记库直接喂给它，实现完美的本地 RAG（检索增强生成）且绝无任何数据泄露风险。
* **ChatGPT 级别的全功能体验：** 提供和 ChatGPT 几乎一致的完美图形界面，支持文档批量上传解析、多轮对话、对话历史管理以及模型核心参数（如 Temperature）的可视化精细调节。