# 精读笔记 · π0: A Vision-Language-Action Flow Model for General Robot Control

> arXiv 2410.24164v4 · Physical Intelligence（PI）· 2024-10-31（v4 更新 2026-01-08）· 代码：[openpi](https://github.com/Physical-Intelligence/openpi) · 权重：openpi 开源（π0 base / π0-FAST / π0.5 等）
> 本地材料：`C:\Users\24431\Zotero\storage\papers\pi0-flow-model\`（paper.pdf / paper.tex / figures/ / code/）

## 基本情况

- 一句话：输入「2–3 路相机图像 + 语言指令 + 机器人本体状态 q_t」→ 输出「未来 50 步的连续动作块 A_t = [a_t … a_{t+H-1}]」。
- 结构：PaliGemma VLM（SigLIP 400M + Gemma 2B，共 3B）+ 一个从零训的 action expert（300M，width 1024），总 3.3B；单塔双专家（MoE 风格）。
- 开源：代码 openpi（2025-02 放出，含 π0 / π0-FAST / 后来 π0.5）；权重开放但需同意条款；数据不公开（OXE 公开，自采 10,000 小时不公开）。
- 和读过的哪篇最像、差在哪：和 RT-2 / OpenVLA 同为 VLA，但那两篇把动作**离散成 token 走自回归**，π0 把动作当**连续向量用 flow matching 回归**——这是全文最关键的一处改动。

## 导读地图

| 站 | 这一站讲清楚什么（一句话） | 图 | 原文位置 | 代码 |
|---|---|---|---|---|
| ① 动机 | 离散 token 的动作精度/频率上不去，要用连续生成 + 大规模跨本体预训练 | 图 1（teaser）、图 2 | §1 L88–113 | — |
| ② 架构 | VLM 塔 + action expert 塔，块状因果 mask，专家只在 attention 里交互 | 图 3 | §4 L139–162 · §A.2 L394–414 | `models/pi0.py:106` `embed_prefix` / `:140` `embed_suffix` |
| ③ 训练 | flow matching 损失：从噪声回归到动作的速度场；两阶段 pre/post-training | 式 1 L149 · 式 2 L155 | §4 / §5.1 | `models/pi0.py:189` `compute_loss` |
| ④ 数据 | 一个时刻的样本 = 3 图 + 语言 + q_t(18) + A_t(50×18)；10,000 小时 / 7 种机器人 / 68 任务 | 图 4、图 5 | §5.1–5.3 L168–217 | `transforms.py` / `training/config.py` |
| ⑤ 信息流 | prefix 只算一次进 KV cache，10 步 Euler 只跑 suffix | 表 I | §4 L153–157 · §A.4 L421–445 | `models/pi0.py:217` `sample_actions` |
| ⑥ 例子 | 场景：「把桌上的马克笔放进杯子里」 | — | — | `pi0.py:217–279` |
| ⑦ 实验 | 开箱即用碾压 OpenVLA/Octo；微调 1 小时数据就超 ACT/DP；能做叠衣服/装盒 | 图 7、图 11、图 13 | §6 L218–354 | — |

## ① 动机

（讲完补）

## ② 架构

（讲完补）

## ③ 训练

（讲完补）

## ④ 数据

（讲完补）

## ⑤ 输入输出信息流

（讲完补）

## ⑥ 例子走一遍

（讲完补）

## ⑦ 实验与地位

（讲完补）

## 问答

- **Q（开讲前）**：这篇你读过/和 RT-2 的关系？
  **A**：他读过 RT-2 精读、OpenVLA 泛读。π0 和它们的核心分歧就在「动作怎么表示」。

## 代码 ↔ 论文

| 论文里 | 代码位置 | 备注（对不上的地方写这里） |
|---|---|---|
| τ=0 是噪声、τ=1 是干净动作 | `pi0.py:226-228` | **代码约定相反**：t=1 是噪声、t=0 是目标，`dt=-1/num_steps`，注释里作者自己写了 sorry |
| A^τ = τA + (1-τ)ε，u = A − ε | `pi0.py:199-200` | 代码：`x_t = t*noise + (1-t)*actions`，`u_t = noise - actions`——把 τ 换成 1−t 后完全等价 |
| 动作维度 18（最大机器人） | `pi0_config.py:25` | 代码默认 `action_dim=32`（留余量），horizon 50 一致 |
| 状态 q_t 是单独一个 block | `pi0.py:143-149` | 代码里 state 是 suffix 里**一个 token**，`ar_mask += [True]` 断在它后面 |
| β((s−τ)/s; 1.5, 1)，s=0.999 | `pi0.py:197` | `jax.random.beta(1.5,1)*0.999+0.001` |
