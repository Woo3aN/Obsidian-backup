---
title: "OpenVLA: An Open-Source Vision-Language-Action Model"
citekey: ""
doi: "10.48550/arXiv.2406.09246"
year: "2024"
journal: "arXiv"
created: "2026-10-11"
tags: [zotero, paper-note]
---

# OpenVLA: An Open-Source Vision-Language-Action Model

> **一句话概述**：OpenVLA 是一个 70 亿参数、完全开源的视觉-语言-动作（VLA）模型，它把融合 DINOv2 与 SigLIP 视觉特征的 Llama 2 7B 视觉语言模型在 Open X-Embodiment 的 97 万条真实机器人演示上微调，从而成为能开箱即用控制多种机器人本体、并可借助 LoRA 等参数高效方法快速适配新任务的通用操作策略。(Kim 等, 2024)

## Summary（摘要）

- **问题**：现有 VLA 大多闭源、且缺乏面向新机器人/新任务的微调最佳实践。
- **方案**：7B 参数的 OpenVLA，在 Open X-Embodiment 的 970k 条真实演示上微调 Prismatic-7B VLM。
- **结果**：在 29 项任务上比 55B 的 RT-2-X 高 16.5% 绝对成功率（参数量少 7 倍）；多任务微调比从零训练的 Diffusion Policy 高 20.4%。
- **开源**：模型、部署/微调 notebook 与训练代码库全部开放。

## Key Findings（主要发现）

| 对比项 | RT-1-X | Octo | RT-2-X | OpenVLA |
| --- | --- | --- | --- | --- |
| 参数量 | 35M | 93M | 55B | 7B |
| WidowX 平均成功率 | 18.5% | 20.0% | 50.6% | **70.6%** |
| Google Robot 平均成功率 | 33.3% | 26.7% | 78.3% | **85.0%** |

| 量化精度 | Bridge 成功率 | 显存 |
| --- | --- | --- |
| bfloat16 | 71.3% | 16.8 GB |
| int8 | 58.1% | 10.2 GB |
| int4 | 71.9% | 7.0 GB |

- RT-2-X 在语义泛化上更强（作者归因于更大规模互联网预训练 + 机器人数据与互联网数据联合微调）；OpenVLA 在其余所有任务类别上相当或更好。
- OpenVLA 的整体优势归因于更大训练集（970k vs 350k 轨迹）、更细致清洗（如过滤 Bridge 数据集的全零动作）与融合视觉编码器。
- LoRA 以仅 1.4% 可训练参数达到与全量微调相当的性能；rank 影响可忽略（推荐 r=32）。

## Methodology（方法）

### 3.1 Preliminaries: Vision-Language Models
近期 VLM 由视觉编码器、投影器与 LLM 骨干三部分组成，以下一文本词元预测端到端训练。OpenVLA 基于 **Prismatic-7B**（600M 视觉编码器、2 层 MLP 投影器、7B Llama 2），其 SigLIP 与 DINOv2 特征按通道拼接，DINOv2 带来的空间信息被认为对机器人控制尤其有用。

### 3.2 OpenVLA Training Procedure
- 形式化为"视觉-语言"任务：动作预测映射为文本 token 序列。
- 每个动作维度离散化为 **256 个 bin**，宽度按训练数据动作的 **1st–99th 分位数**均匀划分（而非 min-max），以规避离群动作拉宽区间、降低有效粒度。
- Llama 分词器只留 100 个特殊词元，故直接覆写词表中最少使用的 256 个词元作为动作词元。
- 只对预测动作词元计算交叉熵。

### 3.3 Training Data
以 OpenX 为基础，过滤为至少含一个第三人称相机、使用单臂末端控制的操控数据集，并沿用 Octo 的数据混合权重。曾以 10% 保守权重加入 DROID，但因动作词元准确率始终偏低，在训练最后三分之一阶段移除。

### 3.4 OpenVLA Design Decisions
- **骨干**：Prismatic 在单物体与多物体语言接地任务上都优于 LLaVA（LLaVA 又比 IDEFICS-1 高 35%），归因于 SigLIP-DINOv2 融合的空间推理能力。
- **分辨率**：224×224 与 384×384 无性能差异（后者训练慢 3 倍）→ 选 224。
- **视觉编码器**：必须微调，冻结会明显掉点。
- **训练轮次**：27 个 epoch，token 准确率超 95% 后性能仍在涨。
- **学习率**：固定 2e-5，预热无收益。

### 3.5 Infrastructure for Training and Inference
64 张 A100 训练 14 天（21,500 A100-hours，批大小 2048）。推理 bfloat16 需 15GB 显存、单张 RTX 4090 上约 6Hz；附带远程推理服务器。

## 实验（Experiments）

### 5.1 Direct Evaluations on Multiple Robot Platforms
BridgeData V2 WidowX 17 任务×10 试次 = 170 次推演；Google Robot 12×5 = 60 次。OpenVLA 在 WidowX 平均 **70.6%**，Google Robot **85.0%**。

### 5.2 Data-Efficient Adaptation to New Robot Setups
Franka-Tabletop / Franka-DROID，每任务 10–150 条演示全量微调。Diffusion Policy 在窄单指令任务更强，OpenVLA 在需语言接地的多样多指令任务更优，且两种设置平均成功率均最高，是唯一在所有任务上达到 ≥50% 的方案。

### 5.3 Parameter-Efficient Fine-Tuning
仅微调最后一层或冻结视觉编码器效果明显较差 → **视觉特征向目标场景的适配很关键**。LoRA 以仅 1.4% 可训练参数达到与全量微调相当的性能，单张 A100 上 10–15 小时完成微调，计算量约为全量微调的 1/8。

### 5.4 Memory-Efficient Inference via Quantization
8-bit 量化因额外开销降低推理速度（A5000 上仅 1.2Hz，显著改变系统动力学）→ 成功率降至 58.1%。4-bit 达到 71.9%，与 bfloat16 的 71.3% 相当，显存从 16.8GB 降至 7.0GB。

## 讨论与局限（Discussion and Limitations）

- 只支持**单图像观测**；扩展到多图像、本体感知与观测历史是重要方向。
- 推理吞吐需提升以支持 ALOHA 这类 50Hz 高频控制。
- 测试任务上可靠性有限，通常 **< 90%** 成功率。
- 受算力限制，基座 VLM 规模、与互联网数据联合训练、何种视觉特征最合适等问题仍未充分探索。

## 附录（Appendix A–E）

- **A**：完整数据混合表（主要沿用 Octo 权重并加入 DROID 等）。
- **B**：WidowX / Google Robot / Franka 各任务的设置、初始化差异、部分得分规则与逐任务结果。
- **C**：RT-2-X 对比中对 Bridge 数据集全零动作问题的处理方式。
- **D**：消融 —— OpenX 预训练影响最大（绝对成功率约降 **30%**），去掉 DINOv2 约降 **5%**，微调视觉编码器明显优于冻结（**80.0% vs 46.7%**），阻塞控制下 8-bit / 4-bit / bfloat16 表现相当。
- **E**：LIBERO 仿真中微调 OpenVLA 取得最高平均成功率（**76.5%**）与最佳平均排名，但相对其他方法的领先幅度小于真实世界微调。

## My Notes（我的疑问 / 待查）

- [ ] 
- [ ] 

## References（参考文献）

- Kim, M. J., Pertsch, K., Karamcheti, S., et al. (2024). *OpenVLA: An Open-Source Vision-Language-Action Model*. arXiv:2406.09246. https://doi.org/10.48550/arXiv.2406.09246

---

Written by LLM-for-Zotero.