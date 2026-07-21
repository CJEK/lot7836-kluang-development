# Lot 7836 居銮 50' × 75' 现代热带 Loft Bungalow 完整开发提案
**Lot 7836 Kluang Modern Tropical Warehouse Bungalow Comprehensive Development Pack**

> 🌐 **公网实时在线分享地址**: [https://lot7836-kluang-development.vercel.app](https://lot7836-kluang-development.vercel.app)  
> 🐙 **GitHub 协同仓库**: [https://github.com/CJEK/lot7836-kluang-development](https://github.com/CJEK/lot7836-kluang-development)

---

## 📌 项目概述 (Project Overview)

本项目为位于马来西亚柔佛州居銮 (Jalan Pakis, Kluang, Johor) 的 **50ft 面宽 × 75ft 进深 (3,750 sqft)** 现代热带度假村风格 Loft Bungalow 仓库完整开发提案。

包含：
* **3 套独立风格外观与内部图纸**（居銮赤陶红现代热带风、马六甲 Batu Angin 风砖屏风墙主推风格、南洋纯白复古谷仓风）。
* **集装箱 0-1 步骤与进度条 GIF 动图**（真实呈现纵向双侧 40ft HC 集装箱切割、补强与花砖屏风墙砌筑过程）。
* **符合 MPK 规范的 2D CAD 工程蓝图集**（总平面图、平面图、正立面图、MEP 水电图、切割节点 Detail）。
* **RM 400k - RM 450k 精细化造价拆解与降本策略**。

---

## 🧮 工程预验算摘要（方案控制，不替代专业签证）

### 热浮力自然排风

以居銮 32°C 室外、36°C 室内、+1ft 至 +47ft 的 46ft 有效高度、`Cd=0.60` 和进 / 排风各 3.0m² 自由面积（等效面积 2.121m²）计算，Jack Roof 烟囱效应约为 **2.401m³/s = 5,087 CFM**。按 3,750 sqft、24ft 檐高与 30° 屋面体积约 117,063ft³ 计算，为 **2.61 ACH**。

此风量在 4°C 温差下可移除约 **11.6kW** 显热；结合 PU 隔热屋面、深檐及 Batu Angin 风砖双层墙，可作为“相对无通风工况降低 3–5°C”的条件性推演。它不保证室温低于 32°C 室外干球温度，最终须由热负荷模拟与现场测试验证。

### 900 sqft Mezzanine 结构预验算

按 `Gk=1.5kN/m²`、`Qk=2.5kN/m²`，17ft 简支 250×125mm UB 主梁（采用不小于 H250×125×6×9 的 `Ixx=38.93×10⁶mm⁴`）及最大 2.90m 分担宽度：服务弯矩为 **38.93kN·m**、ULS 弯矩为 **56.21kN·m**、挠度为 **13.98mm < L/360 = 14.39mm**。150×150mm H 柱的概念轴力亦有初步余量。该结果依赖未侧移柱、横向支撑与连接假设，须由马来西亚注册结构工程师完成最终设计。

### Site Plan 审批控制

总平面图应在送审前红线标出 **6.0m（20ft）消防车通道**、**300mm U-Drain 流向 / 检修井 / 接驳点**，并预留初步 **4.0m³ 化粪池**（8 人办公室、150L/人·日、2 日停留及 1.5m³ 污泥余量）。MPK 的实际退缩线、消防车道和污水要求必须由 [MPK OSC](https://www.mpkluang.gov.my/en/department/project-management/one-stop-center-unit) 依据该地块地契、分区和测量图确认。

---

## 🤖 Codex & 多 Agent 跨平台协同 (Multi-Agent Synergy)

在 Codex 或其他 AI Agent 环境中导入本项目：

1. **直接导入 GitHub 仓库**:
   ```bash
   git clone https://github.com/CJEK/lot7836-kluang-development.git
   ```
2. **跨 Agent 规则文件**:
   详细的工程几何规范、尺寸推演与规则请查阅 [CODEX_GUIDE.md](./CODEX_GUIDE.md)。

---

## 💻 本地预览与部署 (Local Preview & Deployment)

```bash
# 启动本地 Server 预览
python3 -m http.server 8080
# 浏览器访问 http://localhost:8080

# 推送发布至 Vercel 生产环境
vercel --prod --yes
```
