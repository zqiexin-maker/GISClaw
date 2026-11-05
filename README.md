# GISClaw

**面向地理科学数据处理的 AI 助手**

[快速开始](#快速开始) · [Skill 集市](#skill-集市) · [许可证](#许可证)

## 核心能力

通过自然语言组织 GIS 分析、遥感处理与 Python 工作流。

- **空间分析** — 基于 Python GIS 工具集 — 缓冲区、空间连接、叠加分析、路网与栅格处理。
- **自然语言交互** — 命令行与 Web 对话界面 — 数据加载、分析流程编排和制图输出。
- **Python** — 在隔离环境里跑**任意 Python 脚本**，完整科学计算栈 — 地理数据处理、专题地图制作、深度学习...
- **Skill** — 按需安装的能力包，**让 GISClaw 随需而长** — 随时获取社区共建的能力包，共筑地理科学生态...

## 快速开始

### 准备环境

准备 Python 3.9 或以上版本，建议通过 venv 或 [Miniconda](https://docs.anaconda.com/miniconda/) 创建独立环境。

> 给 GISClaw 的智能体准备**独立的 Python 环境**（用 Conda / Mamba 新建一个 env）。智能体执行任务时会自行装、卸载、升级 Python 依赖，独立环境能避免污染你其他项目，也能让智能体跑得更稳。

### 安装与配置

```bash
git clone https://github.com/zqiexin-maker/GISClaw.git
cd GISClaw
python -m venv .venv
# macOS / Linux；Windows 使用 .venv\Scripts\activate
source .venv/bin/activate
python -m pip install -e '.[web]'
gisclaw onboard
gisclaw chat
```

需要完整 GIS 扩展依赖时，执行 `python -m pip install -r requirements.txt`。

启动 Web 对话界面：

```bash
python web/server.py
# 离线规则模式，无需模型 API Key
python web/server.py --rule
```

浏览器访问 `http://localhost:7860`。通过 `gisclaw onboard` 配置模型服务；支持的服务取决于上游实现，也可使用 Ollama 本地模型。

## Skill 集市

GISClaw 内置常用分析技能，可以通过命令行查看和调用：

```
gisclaw skill list
gisclaw skill run vec_buffer --help
```

内置技能代码位于 [`gisclaw/skills/builtin/`](gisclaw/skills/builtin/)，自定义技能可通过 `gisclaw skill install` 安装。

> Skill 会被加载到智能体的提示词中，直接影响其行为。

## 许可证

MIT —— 详见 [LICENSE](LICENSE) 和 [NOTICE](NOTICE)。
