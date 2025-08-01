# 🎯 双色球智能分析系统

<div align="center">

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-automated-green.svg)](https://github.com/features/actions)
[![Data Update](https://img.shields.io/badge/数据更新-每日自动-brightgreen.svg)](#)

**🎲 基于历史数据的智能分析 | 📊 多维度统计建模 | 🤖 自动化数据更新**

</div>

---

## ⚠️ 重要免责声明

<div align="center">

**🚨 本项目仅用于技术学习和数据分析研究目的 🚨**

</div>

| ⚠️ 重要提醒     | 详细说明                                      |
|--------------|-------------------------------------------|
| 🎲 **随机性**   | 彩票开奖结果完全随机，历史数据无法预测未来结果 |
| 📊 **仅供参考** | 本分析结果仅供学习参考，不构成任何投注建议     |
| 💰 **理性购彩** | 请量力而行，未满18周岁禁止购买彩票             |
| ⚖️ **免责条款** | 开发者不承担因使用本项目产生的任何损失        |

---

<!-- RECOMMENDATIONS_START -->
### 📊 最新开奖信息

| 期号 | 开奖日期 | 红球号码 | 蓝球 |
|------|----------|----------|------|
| 2025087 | 2025-07-31 | `02 06 14 15 24 26` | `08` |

**📈 数据统计**: 已收录 1894 期开奖数据 | 最后更新: 2025年08月02日 22:43:35

---
### 🎯 智能推荐号码

**⚠️ 以下推荐基于历史统计分析，仅供参考，不保证中奖！**

| 序号 | 推荐类型 | 红球号码 | 蓝球 | 特征分析 |
|------|----------|----------|------|----------|
| 1 | 高频主导 | `02 06 10 17 18 25` | `01` | 基于最高频号码的稳定组合<br/>2奇4偶 \| 和值:78 \| 跨度:23 |
| 2 | 均衡分布 | `01 09 15 19 26 30` | `15` | 高中低频均衡的平衡组合<br/>4奇2偶 \| 和值:100 \| 跨度:29 |
| 3 | 中频优先 | `06 07 16 23 27 32` | `16` | 中频主导的稳健组合<br/>3奇3偶 \| 和值:111 \| 跨度:26 |
| 4 | 冷热结合 | `01 04 06 17 18 28` | `07` | 热号与冷号结合的对冲组合<br/>2奇4偶 \| 和值:74 \| 跨度:27 |
| 5 | 超高频 | `01 09 14 20 26 27` | `01` | 超高频号码的激进组合<br/>3奇3偶 \| 和值:97 \| 跨度:26 |

**🎲 温馨提示**:
- 📊 推荐基于 1894 期历史数据统计分析
- 🎯 采用多种策略组合，提高号码覆盖面
- ⚠️ 彩票具有随机性，请理性购彩，适度娱乐
<!-- RECOMMENDATIONS_END -->

## 🚀 核心功能

<div align="center">

| 🎯 智能分析    | 📊 数据处理  | 🤖 自动化      |
|------------|----------|----------------|
| 多维度统计建模 | 实时数据抓取 | GitHub Actions |
| 智能推荐算法   | 可视化图表   | 自动报告生成   |
| 趋势识别分析   | 历史数据管理 | 定时更新部署   |

</div>

### 📈 数据分析能力

- **🔍 深度统计**: 号码频率、奇偶分布、和值跨度等多维度分析
- **📉 趋势识别**: 冷热号码分析、遗漏统计、走势预测
- **🎯 智能推荐**: 基于概率统计的多策略号码推荐
- **📊 可视化**: 生成直观的频率分析图表和统计报告

### 🤖 自动化特性

- **⏰ 定时更新**: 每日自动抓取最新开奖数据
- **📝 报告生成**: 自动生成详细的Markdown格式分析报告
- **🔄 持续集成**: GitHub Actions自动运行和数据同步
- **📱 实时展示**: README自动更新最新推荐和开奖信息

## 📁 项目结构

```
Lottery_Analysis/
├── .github/
│   └── workflows/
│       └── update-lottery-data.yml  # GitHub Actions工作流
├── data/
│   ├── lottery_aggregated_data.hjson # 聚合分析数据
│   └── lottery_data.json           # 双色球开奖数据
├── pics/
│   └── lottery_frequency_analysis.png # 号码频率分析图
├── reports/
│   └── analysis_report.md          # 分析报告
├── scripts/
│   └── lottery_analyzer.py          # 数据分析器
├── test/                            # 测试代码
├── .gitignore
├── LICENSE
├── README.md
├── main.py                        # 主运行脚本
└── requirements.txt               # Python依赖
```

## 🛠️ 安装使用

### 本地运行

1. **克隆仓库**

   ```bash
   git clone https://github.com/your-username/Lottery_Analysis.git
   cd Lottery_Analysis
   ```

2. **安装依赖**

   ```bash
   pip install -r requirements.txt
   ```

3. **运行分析**

   ```bash
   python main.py
   ```

### 🤖 GitHub Actions自动化

<div align="center">

| 触发方式         | 运行时间           | 执行内容        | 输出结果        |
|--------------|------------------|-------------|-------------|
| ⏰ **定时任务**   | 每日 21:45 (UTC+8) | 数据抓取 + 分析 | 自动提交 + 发布 |
| 🖱️ **手动触发** | 随时可用           | 完整分析流程    | 实时日志查看    |
| 🔄 **代码更新**  | Push 触发          | 测试 + 验证     | 状态反馈        |

</div>

**🎯 自动化流程**:
1. **数据采集** → 抓取最新双色球开奖数据
2. **智能分析** → 多维度统计分析和趋势识别
3. **报告生成** → 自动生成分析报告和可视化图表
4. **内容更新** → 更新README推荐号码和开奖信息
5. **版本发布** → 创建带数据文件的GitHub Release

## 📊 分析功能

### 1. 号码频率分析

- 红球和蓝球的出现频率统计
- 热号和冷号识别
- 可视化频率分布图

### 2. 号码规律分析

- 奇偶分布规律
- 和值分布统计
- 跨度分布分析

### 3. 走势分析

- 最近期数走势
- 冷热号码变化
- 号码遗漏统计

### 4. 智能推荐

- 基于概率统计的号码推荐
- 多组号码生成
- 权重算法优化

### 5. 分析报告

- 自动生成Markdown格式报告
- 包含完整的统计分析数据
- 提供详细的使用说明和风险提醒
- 每日自动更新

## 🔧 配置说明

### 修改抓取参数

在 `scripts/lottery_analyzer.py` 中可以调整以下参数：

```python
# 修改请求头
self.headers = {
    'User-Agent': '...'  # 可根据需要更新
}

# 修改生成推荐组数
recommendations = analyzer.generate_recommendations(num_sets=5)
```

### 修改GitHub Actions运行时间

在 `.github/workflows/update-lottery-data.yml` 中修改cron表达式：

```yaml
schedule:
  # 晚上23:00 (UTC+8)
  - cron: '0 15 * * *'
```

## 📈 数据来源

数据来源于中国福利彩票官方网站API：

- **API地址**: `https://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice`
- **数据格式**: JSON
- **更新频率**: 每周二、四、日开奖后更新

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

1. Fork本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开Pull Request

## 📄 开源协议

本项目基于 [MIT License](LICENSE) 开源协议。

## 🙏 致谢

- 感谢中国福利彩票官方提供的开放数据
- 感谢所有开源贡献者的工具和库

## ⚖️ 法律声明

- 本项目严格遵守相关法律法规
- 仅用于技术研究和学习交流
- 不鼓励任何形式的赌博行为
- 如有违法违规使用，后果自负

---

**记住：彩票有风险，投注需谨慎！理性购彩，快乐生活！** 🍀
