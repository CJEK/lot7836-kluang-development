# Lot 7836 Kluang Development Pack — Codex & Multi-Agent Collaboration Guide

本指南专为 **Codex / GitHub Copilot / Antigravity / Claude Agent** 等多个 AI Agent 跨平台协同打造。它记录了项目的**全部建筑逻辑、尺寸约束、工程规范与公网发布配置**，确保所有 Agent 共享完全一致的技术与设计逻辑。

---

## 🚀 项目核心在线信息 (Public Deployment Links)

* **🌐 公网实时可分享 Link (Vercel)**: [https://lot7836-kluang-development.vercel.app](https://lot7836-kluang-development.vercel.app)
* **🐙 GitHub 协同仓库**: [https://github.com/CJEK/lot7836-kluang-development](https://github.com/CJEK/lot7836-kluang-development)
* **⚙️ 自动 CI/CD**: 任何提交推送至 `master` 分支均会触发 Vercel 与 GitHub Pages 的自动打包发布。

---

## 📐 建筑与工程硬性逻辑规范 (Core Design Principles)

为确保项目不发生设计退化或逻辑冲突，任何 Agent 修改项目必须遵守以下规则：

### 1. 物理尺寸与地块布局 (Site & Physical Dimensions)
* **地块与占地**: 50ft 面宽 (Frontage) × 75ft 进深 (Depth) = **3,750 sqft** 总占地。
* **正面朝向**: 50ft 面宽正面面向 **Jalan Pakis 道路** (位于 Site Plan & Floor Plan 图纸下方)，75ft 进深向北延伸。
* **集装箱摆放方向**: 2 个 40ft HC 集装箱 (各 8ft W × 40ft L) 必须**纵向双侧排列**（40ft 沿 75ft 进深方向，仅占据前 40ft）。
* **中央大厅**: 左右集装箱之间留下 **34ft 宽** 挑高中庭 (8ft + 34ft + 8ft = 50ft 总面宽)。
* **后区延伸段**: 40ft 以后为 35ft 轻钢框架延伸段（后区湿区、900sqft Mezzanine 二层办公平台与仓储扩展）。

### 2. 屋顶几何与标高公式 (Roof Geometry Calculations)
* **屋檐标高 (Eave Height)**: `+24'-0"` (7.3m)。
* **30° 坡屋顶几何标高**:
  $$\text{屋脊基座标高 } = 24\text{ft} + 25\text{ft} \times \tan(30^\circ) = +38\text{ft } 5\text{in}$$
* **拔风塔顶脊标高**: Raised Jack Roof 拔风塔顶部为 `+47'-0"`。

### 3. Mezzanine 阁楼垂直空间
* **物理位置**: 900 sqft Mezzanine 阁楼**必须位于后区 35ft 高顶钢构区**（檐高 24ft/7.3m），一楼与二楼净高各 11ft (3.35m)。
* **严禁规则**: 严禁将阁楼设计在 40ft HC 集装箱箱体内部（因箱内净高仅 8'10" / 2.69m）。

---

## 🛠️ Codex 工具链操作快速指令 (Codex Quick CLI Commands)

在 Codex / Copilot CLI 环境中接管本项目时，可直接运行以下指令：

```bash
# 1. 克隆 / 同步最新代码
git pull origin master

# 2. 本地 Web 开发预览
python3 -m http.server 8080
# 浏览器访问 http://localhost:8080

# 3. 运行自动化稳定性逻辑审计脚本
./venv/bin/python3 -c "
import os, re
# 检查资产与 HTML 匹配
"

# 4. 一键部署更新至 Vercel
vercel --prod --yes
```

---

## 🤝 跨 Agent 相互配合与学习流 (Multi-Agent Workflow)

1. **修改规范**: 涉及修改工程图纸、配色、HTML 或逻辑时，请务必更新根目录下的 `CODEX_GUIDE.md` 与 `architectural_design_drawings.md`。
2. **提交规范**: 使用清晰的 Conventional Commits（如 `fix(cad): update elevation pitch height`）。
3. **推送到 Master**: `git push origin master` 触发 Vercel 自动增量更新，保证公网分享链接实时最新。
