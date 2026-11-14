---
title: 大学物理B（下）期中突击清单
date: 2026-11-14
tags:
  - 大学物理
  - 期中复习
  - 电磁学
---

# 大学物理B（下）期中突击清单

> [!info] 怎么用这份清单
> - **范围**：第 5～8 章（第八章是期中考前最后一章）
> - **题型**：选择 20 分（10×2）+ 填空 20 分（10 空×2）+ 计算 60 分（5×12）
> - **依据**：笔记全文 + 两份真题（A 卷两套）+ 老师课上划的复习重点
> - **分级**：🔴 必考｜🟡 常考｜⚪ 了解

> [!important] 🔴 老师明确划的复习重点（原话）
> 1. **第五章的电场 / 电势计算**：叠加原理、高斯定理、电势叠加
> 2. **第六章的电容计算**——「把电场与电势计算统一在一起，**必考**」
> 3. **电介质与导体的文字叙述型结论**——注意「**条件满足才能用**」
> 4. 老师提示：**期中考是四次考试里最难的一次，用到的数学最多**
> 5. **安培力、磁力计算是难点，可能出大题**

---

> [!important] 考前 2 小时只看这页
> **第五章**
> 1. 点电荷场强 $E=\dfrac{q}{4\pi\varepsilon_0 r^2}$；**无限长直线** $\dfrac{\lambda}{2\pi\varepsilon_0 r}$；**无限大平面** $\dfrac{\sigma}{2\varepsilon_0}$
> 2. 高斯定理 $\oint_S\vec E\cdot\mathrm d\vec S=\dfrac{\sum q_{\text{内}}}{\varepsilon_0}$——**只数面内电荷**，面外电荷对通量无贡献
> 3. 均匀带电球面：内 $E=0$、外 $\dfrac{q}{4\pi\varepsilon_0 r^2}$；球体内 $E=\dfrac{\rho r}{3\varepsilon_0}\propto r$
> 4. 电势 $V_a=\displaystyle\int_a^{\infty}\vec E\cdot\mathrm d\vec l$；点电荷 $V=\dfrac{q}{4\pi\varepsilon_0 r}$——**标量直接加，不分解方向**
>
> **第六章**
> 5. 导体静电平衡：内部 $E=0$、表面 $E=\dfrac{\sigma}{\varepsilon_0}$ 垂直表面、**等势体**
> 6. 有介质高斯定理 $\oint\vec D\cdot\mathrm d\vec S=\sum q_0$（只数**自由电荷**）；解题顺序 $\vec D\to\vec E\to\vec P\to\sigma'$
> 7. 平板电容 $C=\dfrac{\varepsilon_0\varepsilon_r S}{d}$；串并联与电阻**相反**
> 8. 电场能量 $W=\dfrac{Q^2}{2C}=\dfrac12CV^2$；能量密度 $w_e=\dfrac12\varepsilon E^2$
>
> **第七章**
> 9. 毕奥-萨伐尔 $\mathrm d\vec B=\dfrac{\mu_0}{4\pi}\dfrac{I\mathrm d\vec l\times\vec e_r}{r^2}$；**无限长直线** $\dfrac{\mu_0 I}{2\pi a}$；**圆心** $\dfrac{\mu_0 I}{2R}$；**螺线管** $\mu_0 nI$
> 10. 安培环路定理 $\oint\vec B\cdot\mathrm d\vec l=\mu_0\sum I_{\text{套住}}$——**只数套住的**，右手螺旋定正负
> 11. 洛伦兹力 $F=qvB$（垂直时）；回旋半径 $R=\dfrac{mv}{qB}$、周期 $T=\dfrac{2\pi m}{qB}$（**与速度无关**）
> 12. 安培力 $\mathrm d\vec F=I\mathrm d\vec l\times\vec B$；磁力矩 $\vec M=\vec m\times\vec B$，$m=NIS$（**只对均匀磁场**）
>
> **第八章**
> 13. 法拉第 $\varepsilon=-\dfrac{\mathrm d\Phi}{\mathrm dt}$；动生 $\varepsilon=Blv$；感生电场 $\oint\vec E_k\cdot\mathrm d\vec l=-\dfrac{\mathrm d\Phi}{\mathrm dt}$
> 14. 自感 $\varepsilon_L=-L\dfrac{\mathrm dI}{\mathrm dt}$、互感 $\varepsilon_M=-M\dfrac{\mathrm dI}{\mathrm dt}$；$L=M$ 之间的关系
> 15. 磁能 $W=\dfrac12LI^2$；磁能密度 $w_m=\dfrac{B^2}{2\mu}$
> 16. 麦克斯韦四方程：$\oint\vec D\cdot\mathrm d\vec S=\sum q_0$、$\oint\vec B\cdot\mathrm d\vec S=0$、$\oint\vec E\cdot\mathrm d\vec l=-\dfrac{\mathrm d\Phi_B}{\mathrm dt}$、$\oint\vec H\cdot\mathrm d\vec l=\sum I_0+\dfrac{\mathrm d\Phi_D}{\mathrm dt}$

---

# 第 5 章 静电场

## 5-1 库仑定律

> [!definition] 🔴 库仑定律
> $$\vec F=\frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r^2}\vec e_r$$
> 其中 $\varepsilon_0=8.85\times10^{-12}\ \mathrm{C^2/(N\cdot m^2)}$，$\dfrac{1}{4\pi\varepsilon_0}=9\times10^9$。
> **只适用于真空中的两个静止点电荷。**

## 5-2 电场强度

> [!definition] 🔴 定义
> $$\vec E=\frac{\vec F}{q_0}$$
> 方向：**正电荷**在该处受力方向。单位 $\mathrm{N/C}=\mathrm{V/m}$。反过来 $F=q\vec E$。

**点电荷的场强**：

$$\vec E=\frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\vec e_r$$

> [!important] 🔴 求场强的三条路
> | 情形 | 方法 |
> |---|---|
> | 点电荷系 | **矢量叠加** $\vec E=\sum\vec E_i$ |
> | 连续带电体 | 取电荷元 $\mathrm dq$ → $\mathrm d\vec E$ → **先分解、后积分** |
> | 电荷分布对称 | **高斯定理**（最快） |

**连续带电体三个必背结果**（$r$ 为到场点的距离）：

| 带电体 | 场强 |
|---|---|
| **无限长带电直线**（线密度 $\lambda$） | $E=\dfrac{\lambda}{2\pi\varepsilon_0 r}$ |
| **无限大带电平面**（面密度 $\sigma$） | $E=\dfrac{\sigma}{2\varepsilon_0}$ |
| **均匀带电球面**（半径 $R$、电量 $q$） | 外 $E=\dfrac{q}{4\pi\varepsilon_0 r^2}$，**内 $E=0$** |

> [!warning] 🟡 电偶极子的远区场，两处差一个因子 2
> | 场点 | 大小 | 方向 |
> |---|---|---|
> | 延长线上 | $\dfrac{2p}{4\pi\varepsilon_0 r^3}$ | 与 $\vec p$ **同向** |
> | 中垂线上 | $\dfrac{p}{4\pi\varepsilon_0 r^3}$ | 与 $\vec p$ **反向** |
>
> 都按 $1/r^3$ 衰减（比点电荷的 $1/r^2$ 快一个幂次）。电偶极矩 $\vec p=q\vec l$，$\vec l$ **由负电荷指向正电荷**。

## 5-3 高斯定理（重点）

> [!important] 🔴 求电通量的三种方法（选择题高频）
> | 情形 | 方法 |
> |---|---|
> | 闭合面 + 已知电荷 | **高斯定理**：$\Phi=\dfrac{\sum q_{\text{内}}}{\varepsilon_0}$ |
> | 闭合面 + 点在面外 | 直接 **0** |
> | **局部面**（平面、锥面、一个面） | **对称补全法**：补成闭合面，再按对称性分份数 |
>
> **对称补全的常用结果**：
> - 点电荷在**立方体中心** → 每个面 $\dfrac{q}{6\varepsilon_0}$
> - 点电荷在**立方体一个顶点** → 对该顶点相邻的三个面，每个 $\dfrac{q}{24\varepsilon_0}$
> - 点电荷在**无限大平面一侧** → 穿过该平面 $\dfrac{q}{2\varepsilon_0}$
>
> ⚠️ 前提：$q$ 必须在补出来的闭合面**内部**，否则通量为 0。

> [!important] 🔴 高斯定理（真空）
> $$\oint_S\vec E\cdot\mathrm d\vec S=\frac{1}{\varepsilon_0}\sum_{i}q_i$$
> 右边是**高斯面内**电荷的**代数和**。

> [!warning] 🔴 最容易搞混的一点
> 闭合面**外**的电荷：
> - 对**通量**没有贡献（不进总和）
> - 但对闭合面上**各点的场强有贡献**——面上每点的 $\vec E$ 由**内外所有**电荷共同激发
>
> 一句话：**通量只数面内，场强要算全部。**

> [!important] 🔴 用高斯定理求场强的四步
> 1. 由电荷分布的**对称性**判定场强方向
> 2. 作合适的**高斯面**（球面 / 圆柱面），使面上各点 $E$ 大小相等
> 3. 数**面内**电荷的代数和
> 4. 代公式求 $E$

**四个标准结果**（必须能默）：

| 带电体 | 内部 | 外部 |
|---|---|---|
| 均匀带电**球面** | $E=0$ | $\dfrac{q}{4\pi\varepsilon_0 r^2}$ |
| 均匀带电**球体** | $E=\dfrac{\rho r}{3\varepsilon_0}$（$\propto r$） | $\dfrac{q}{4\pi\varepsilon_0 r^2}$ |
| 无限长带电**圆柱面** | $E=0$ | $\dfrac{\lambda}{2\pi\varepsilon_0 r}$ |
| 无限长**均匀带电圆柱** | $E=\dfrac{\lambda r}{2\pi\varepsilon_0 R^2}$（$\propto r$） | $\dfrac{\lambda}{2\pi\varepsilon_0 r}$ |

> [!warning] 🟡 球体内部与 $r$ 成正比
> 均匀带电球体**外部**和点电荷一样（$\propto 1/r^2$），**内部**线性增长（$\propto r$），球心处 $E=0$、球面处最大。
> 别把球内场点当点电荷代公式算——那会算出错误的大值。

## 5-4 电势

> [!important] 🔴 环路定理（说明静电场是保守场）
> $$\oint_l\vec E\cdot\mathrm d\vec l=0$$
> 等价说法：静电力做功**与路径无关**，只与始末位置有关。

> [!definition] 🔴 电势
> $$V_a=\frac{E_{pa}}{q_0}=\int_a^{\text{零点}}\vec E\cdot\mathrm d\vec l$$
> 有限带电体**取无穷远为零点**。两点间电势差 $V_{ab}=V_a-V_b$，电场力做功 $W_{ab}=q(V_a-V_b)$。

> [!important] 🔴 求电势的两条路
> | 方法 | 式子 | 什么时候用 |
> |---|---|---|
> | **定义式** | $V_a=\displaystyle\int_a^{\infty}\vec E\cdot\mathrm d\vec l$ | **已知 $\vec E$ 分布**时 |
> | **叠加原理** | $V=\sum V_i$ 或 $V=\displaystyle\int\frac{\mathrm dq}{4\pi\varepsilon_0 r}$ | 电荷分布规则时 |
>
> **点电荷电势**：$V=\dfrac{q}{4\pi\varepsilon_0 r}$

> [!warning] 🔴 电势叠加是纯代数加法，不分解方向
> 积分里只有 $\mathrm dq$ 到**场点的距离** $r$，没有方向。这是电势比场强好算的地方——场强要拆分量、判断抵消，电势直接加。

## 5-5 等势面与电势梯度

**⚪ 等势面**：电势相等的点组成的曲面，相邻等势面电势差相等。$\vec E$ 垂直于等势面、指向电势降低的方向。

> [!important] 🟡 场强与电势的关系
> $$E_l=-\frac{\partial V}{\partial l}$$
> 直角坐标下 $\vec E=-\nabla V$。**负号表示 $\vec E$ 指向电势降低最快的方向。**
>
> 本课程不要求掌握梯度运算，理解即可；**用错坐标形式反而会算错**。

---

# 第 6 章 静电场中的导体和电介质

## 6-1 导体的静电平衡

> [!important] 🔴 静电平衡的三条性质
> 1. **电荷分布**：净电荷只能分布在**外表面**（内部无净电荷）
> 2. **电场**：内部 $E=0$；表面 $E=\dfrac{\sigma}{\varepsilon_0}$，**垂直于表面**
> 3. **电势**：处处相等，整个导体是**等势体**

> [!warning] 🔴 导体表面是 $\dfrac{\sigma}{\varepsilon_0}$，不是 $\dfrac{\sigma}{2\varepsilon_0}$
> 第五章的**无限大带电平面**是 $\dfrac{\sigma}{2\varepsilon_0}$（电力线往两边散）；
> **导体表面**是 $\dfrac{\sigma}{\varepsilon_0}$（内部 $E=0$，电力线全被压到外面一侧）。
>
> **但做电场叠加时用的是 $\dfrac{\sigma}{2\varepsilon_0}$**——那是"单个面单独存在"时的场，$\dfrac{\sigma}{\varepsilon_0}$ 是相互作用完以后的结果。这里最容易写错。

**空腔导体**：
- 腔内无电荷 → 电荷全在外表面，内表面无电荷
- 腔内有电荷 $q$ → 内表面感应 $-q$，外表面感应 $+q$

> [!definition] 🟡 静电屏蔽
> **接地的空腔导体**可以隔离内外电场的影响。

> [!warning] 🟡 接地 ≠ 外表面电荷全部消失
> 要按具体情况分析：只要那里还有电场线（而电场线必须垂直导体表面），外表面电荷就还在。**不能看到"接地"就把外表面电荷全抹掉。**

> [!important] 🔴 做本章题目的两个前提（老师反复强调）
> 1. **先判材料**：题目说的是**导体**还是**电介质**？导体要用导体的性质。
> 2. **从初态过渡到平衡态**：题目给的带电量是"初态"，没告诉你电荷怎么分布。要先用导体性质演化到**静电平衡态**，才能往下算。
>
> 口诀：**判材料 → 过渡到平衡 → 定电荷分布 → 高斯定理/叠加求场强与电势**。

## 6-2 电介质

**⚪ 极化两种机制**：位移极化（无极分子被拉长）、转向极化（有极分子转向）。微观过程不同，**末态相同**——表面出现束缚电荷。

> [!important] 🟡 电介质内的总场被削弱
> $$\vec E=\vec E_0+\vec E',\qquad E<E_0$$
> $\vec E'$ 与 $\vec E_0$ **永远反向**（靠近正极板那面感生负电荷）。

**新物理量两个**：

$$\vec P=\frac{\sum\vec p_i}{\Delta V}\qquad \vec D=\varepsilon_0\vec E+\vec P=\varepsilon\vec E$$

其中 $\varepsilon_r=1+\chi_e$、$\varepsilon=\varepsilon_0\varepsilon_r$。

> [!important] 🔴 有介质时的高斯定理
> $$\oint_S\vec D\cdot\mathrm d\vec S=\sum q_0$$
> 右边是**自由电荷**的代数和——**极化电荷不算**。

> [!warning] 🟡 两个 $\vec D$ 式子的适用范围不同
> - $\vec D=\varepsilon_0\vec E+\vec P$：**定义式，普遍成立**
> - $\vec D=\varepsilon\vec E$：**只适用于各向同性的均匀介质**

> [!important] 🔴 解题顺序（和讲课顺序相反）
> 讲课是 $q'\to\vec P\to\vec D$；**做题要倒过来**：
> 1. 用 $\oint\vec D\cdot\mathrm d\vec S=\sum q_0$ 求 $\vec D$（只数自由电荷）
> 2. 由 $\vec E=\vec D/\varepsilon$ 求 $\vec E$
> 3. 由 $\vec P=\vec D-\varepsilon_0\vec E$ 求 $\vec P$
> 4. 由 $\sigma'=P_n$ 求极化电荷面密度

## 6-3 电容与电容器（必考）

> [!definition] 🔴 电容
> $$C=\frac{q}{\Delta V}$$
> 只由**几何形状和介质**决定，与带电量无关。单位法拉 $\mathrm F$，$1\mathrm F=10^6\mu\mathrm F=10^{12}\mathrm{pF}$。

> [!important] 🔴 计算电容的四步
> 1. 设两极板带 $\pm q$
> 2. 求极板间场强 $\vec E$（一般用高斯定理）
> 3. 求电势差 $\Delta V=\displaystyle\int_A^B\vec E\cdot\mathrm d\vec l$
> 4. 代 $C=\dfrac{q}{\Delta V}$

**三个必背公式**：

| 电容器 | 电容 |
|---|---|
| **平板** | $C=\dfrac{\varepsilon_0\varepsilon_r S}{d}$ |
| **球形**（内外半径 $R_A,R_B$） | $C=\dfrac{4\pi\varepsilon_0\varepsilon_r R_AR_B}{R_B-R_A}$ |
| **圆柱形**（长度 $l$） | $C=\dfrac{2\pi\varepsilon_0\varepsilon_r l}{\ln(R_B/R_A)}$ |

> [!warning] 🔴 串并联要跟电阻反着记
> - **串联**：$\dfrac{1}{C}=\sum\dfrac{1}{C_i}$（相当于电阻并联）
> - **并联**：$C=\sum C_i$（相当于电阻串联）

> [!important] 🔴 插入介质的两种情形（选择题必考，结果完全相反）
> | | **断开电源**（$Q$ 不变） | **接通电源**（$U$ 不变） |
> |---|---|---|
> | $C$ | 变大 $\varepsilon_r$ 倍 | 变大 $\varepsilon_r$ 倍 |
> | $Q$ | **不变** | 变大 $\varepsilon_r$ 倍 |
> | $U$ | 变小到 $U/\varepsilon_r$ | **不变** |
> | $E$ | 变小到 $E/\varepsilon_r$ | **不变** |
> | 能量 $W$ | **变小**到 $W/\varepsilon_r$ | **变大** $\varepsilon_r$ 倍 |
>
> **判断流程**：先看断不断电 → 定住 $Q$ 还是 $U$ → 其余全由 $C$ 的变化推。
> 选公式时也要配对：$Q$ 不变用 $W=\dfrac{Q^2}{2C}$，$U$ 不变用 $W=\dfrac12CU^2$。

> [!warning] 🟡 两个电容并联后能量一定减少
> 一个充电的电容（$Q$、$U$、$C$）与一个未充电的相同电容**并联**：
> 总电荷 $Q$ 不变、等效电容变成 $2C$，所以 $W'=\dfrac{Q^2}{2(2C)}=\dfrac{W}{2}$——**能量减半**。
> 少掉的那一半变成了**导线电阻上的热**。这类"能量去哪了"的问题，答案基本都是"变成热/辐射"。

> [!important] 🔴 复合结构：上下分层 vs 左右并排
> | 结构 | 关系 | 关键 |
> |---|---|---|
> | **上下分层**（介质叠起来） | **串联** | 两部分 $D$ 相同、电荷相同、**电压相加** |
> | **左右并排**（介质并排） | **并联** | 两部分 $E$ 相同、**电压相同**、电荷相加 |
>
> ⚠️ **左右并排时两边的自由电荷密度 $\sigma_1$、$\sigma_2$ 一般不相等**——这是它和上下结构最大的区别。
>
> 老师建议：**别硬套串并联，容易混**。设未知量直接联立两个方程：
> ① **电荷守恒**：两边电荷之和 = 总电量
> ② **电压相等**：极板是等势体，左右两段电势差必须一样
>
> 「只要一个表达式解决不了，就用联立」——这是很正常的思路。

> [!warning] 🔴 老师原话：这是必掌握的基本题型
> 「这个题目**非常典型，而且会有非常重的演化**；回去一定要练到熟练——**没掌握后面会有很多障碍**。（期中考会出类似的东西。）」

## 6-4 静电场的能量

> [!important] 🔴 三个等价形式
> $$W_e=\frac{Q^2}{2C}=\frac12CV^2=\frac12QV$$
> **能量密度**：$w_e=\dfrac12\varepsilon E^2$（普遍适用），$W_e=\displaystyle\int_V w_e\,\mathrm dV$

**点电荷系的电能**：$W_e=\dfrac12\displaystyle\sum_i q_iV_i$（其中 $V_i$ 是除 $q_i$ 以外其它电荷在 $q_i$ 处产生的电势）。

> [!warning] 🟡 两种算法至少掌握一种
> 老师原话：「每年在这里算不出来的同学比例不小，别"看会了"就等于会了，**一定要动手算一遍**。」
> - **解法一**：积「有电荷的地方」（$0\to a$）
> - **解法二**：积「有电场的地方」（$0\to\infty$，**分球内球外两段，最容易漏球外那段**）

> [!important] 🟡 求电容的第二条路：能量法
> 算出 $W_e$，和 $W_e=\dfrac{q^2}{2C}$ 一比就得到 $C$。
> **结构复杂的电容器（多层介质等）用能量法往往更顺。**

> [!warning] 🟡 公式的前提别丢
> 电容定义、电容器能量公式的前提都是「**两极板等量异号**」。
> 题目给的带电情况不满足时，先演化到平衡态，再按**一般带电体**算——电容器公式全部失效。

# 第 7 章 恒定磁场

> [!important] 🔴 本章的规律（老师给的路线图）
> | 研究层面 | 规律 |
> |---|---|
> | 电流产生磁场 | **毕奥-萨伐尔定律** |
> | 磁场对电流的作用 | **安培定律** |
> | 运动电荷产生磁场 / 磁场对运动电荷的作用 | **洛伦兹公式** |

## 7-1 恒定电流

> [!important] 🟡 恒定电场和静电场相同
> **恒定电场也遵守静电场的高斯定理和环路定理。**
> 这条是整章的枢纽——第 5、6 章关于静电场的结论可以原样搬过来用。

**电流密度**：$\vec j=nq\vec v_d$，$I=\displaystyle\int_S\vec j\cdot\mathrm d\vec S$；对均匀截面 $I=nqSv_d$。
（⚠️ 这个模型只对**金属导体**成立。）

> [!important] 🟡 电动势
> 数值上等于**把单位正电荷从负极经电源内部移到正极时，非静电力做的功**：
> $$\varepsilon=\frac{W}{q}=\oint\vec E_k\cdot\mathrm d\vec l$$
> **方向**：电源内部**电势升高**的方向（负极 → 正极）。

## 7-2 磁感应强度

> [!definition] 🟡 两种定义法
> - **运动电荷**：$B=\dfrac{F_{\max}}{q_0v}$（$F_{\max}$ 出现在 $\vec v\perp\vec B$ 时）
> - **载流线圈**：$B=\dfrac{\tau_{\max}}{p_m}$
>
> 方向取**小磁针 N 极的指向**。

> [!warning] 🟡 磁场的大小和方向只能拆开定义
> 电场一个式子 $\vec E=\vec F/q$ 就同时定了大小和方向；磁场不行——因为 $F=qv\times B$ 里 $\vec F$ 与 $\vec B$ **不同向**，必须先定方向、再定大小。

**磁感应线两条特点**：① 连续、不相交；② **闭合、无头无尾**（与电场线起于正电荷止于负电荷形成对照）。

## 7-3 毕奥-萨伐尔定律

> [!important] 🔴 定律本身
> $$\mathrm d\vec B=\frac{\mu_0}{4\pi}\frac{I\,\mathrm d\vec l\times\vec e_r}{r^2},\qquad \mu_0=4\pi\times10^{-7}\ \mathrm{T\cdot m/A}$$

> [!important] 🔴 四个必背结果
> | 电流分布 | 磁感应强度 |
> |---|---|
> | **无限长直导线** | $B=\dfrac{\mu_0 I}{2\pi a}$ |
> | **半无限长直导线** | $B=\dfrac{\mu_0 I}{4\pi a}$（折半） |
> | **有限长直导线** | $B=\dfrac{\mu_0 I}{4\pi a}(\cos\theta_1-\cos\theta_2)$ |
> | **圆电流圆心** | $B=\dfrac{\mu_0 I}{2R}$；半圆 $\dfrac{\mu_0 I}{4R}$ |
> | **圆电流轴线上** | $B=\dfrac{\mu_0 IR^2}{2(R^2+x^2)^{3/2}}$ |
> | **无限长螺线管内** | $B=\mu_0 nI$（**匀强**） |
> | **运动电荷** | $B=\dfrac{\mu_0}{4\pi}\dfrac{qv\sin\alpha}{r^2}$ |

> [!warning] 🟡 三个容易记错的地方
> - **有限长直导线的角度次序**：$\theta_1$ 是左端、$\theta_2$ 是右端。**先拿无限长验算**——若化简结果不是 $\dfrac{\mu_0 I}{2\pi a}$，就说明次序反了。
> - **圆电流远场是 $\dfrac{\mu_0 IS}{2\pi x^3}$**，分母是 $x^3$ 不是 $x^2$——磁偶极子的场比点电荷衰减快一个幂次。
> - **运动电荷的场**：$B$ 沿 $\vec v\times\vec e_r$ 方向；**正负电荷方向相反**。

> [!tip] 🟡 无限长螺线管：管外场强接近零，管口处约为管内一半
> $B=\mu_0 nI$ 不依赖位置、不依赖半径，只由**单位长度匝数** $n$ 和电流 $I$ 决定——这就是它被用来产生匀强磁场的原因。

**叠加原理**：任意电流分布的磁场 = 各电流元产生磁场的**矢量叠加**。

> [!warning] 🟡 叠加时"只叠加所需分量"
> 圆电流、载流平板这类有对称性的题，垂直于所求方向的**分量会互相抵消**，只需积分平行分量。硬积全部会白算一半。

## 7-4 磁场的高斯定理

> [!important] 🔴 磁场是无源场
> $$\oint_S\vec B\cdot\mathrm d\vec S=0$$
> 右边是 **0**，含义是**没有"磁荷"**——自然界不存在磁单极子。

| | 静电场 | 磁场 |
|---|---|---|
| 定理 | $\oint\vec E\cdot\mathrm d\vec S=\dfrac{\sum q}{\varepsilon_0}$ | $\oint\vec B\cdot\mathrm d\vec S=0$ |
| 场的性质 | **有源场** | **无源场** |
| 场线 | 起于正电荷、止于负电荷 | 闭合，无头无尾 |

> [!warning] 🟡 通量为零 ≠ 场为零
> 高斯定理只说明"净通量为零"，不代表 $\vec B$ 不存在。

## 7-5 安培环路定理（重点）

> [!important] 🔴 定理
> $$\oint_L\vec B\cdot\mathrm d\vec l=\mu_0\sum I_{\text{套住}}$$

> [!warning] 🔴 三条注意
> 1. 右边的电流只算**被环路套住并穿过**的，环路外的**不贡献**
> 2. 左边的 $\vec B$ 却是**内外所有电流**产生的场
> 3. **符号**：电流方向与绕行方向成**右手螺旋**时取正，反之取负
>
> 第 1、2 条合起来最容易绕晕：**右边只数套住的，左边是全部的场。**

**三个标准结果**：

| 情形 | 结果 |
|---|---|
| 长直螺线管内 | $B=\mu_0 nI$ |
| 螺线环内 | $B=\mu_0 nI$（或 $\dfrac{\mu_0 NI}{2\pi r}$） |
| **无限长载流圆柱导体** | 外 $B=\dfrac{\mu_0 I}{2\pi r}$；内 $B=\dfrac{\mu_0 rI}{2\pi R^2}$ |

> [!important] 🟡 用"表面处连续"自查
> 圆柱**外** $B\propto1/r$，**内** $B\propto r$。在 $r=R$ 处两式都给出 $\dfrac{\mu_0 I}{2\pi R}$。
> **算完两边都代 $r=R$ 验一下**——对不上就说明积分的电流范围写错了。

> [!tip] 🟡 两条路怎么选
> 毕奥-萨伐尔是**普适的**（任何分布都能积）；安培环路定理**只对高对称情形好用**，但快得多。
> **做题先看对称性——能套环路定理就别去积微元。**

## 7-6 磁场对运动电荷（洛伦兹力）

> [!important] 🔴 洛伦兹力
> $$\vec F=q\vec v\times\vec B$$
> 大小 $F=qvB\sin\theta$，方向垂直于 $\vec v$、$\vec B$ 决定的平面。
> **只改变方向，不做功**（$\vec F\perp\vec v$）。

**三种运动**：

| $\vec v$ 与 $\vec B$ 夹角 | 运动 | 关键量 |
|---|---|---|
| 平行（$0°$） | 匀速直线 | — |
| 垂直（$90°$） | **匀速圆周** | $R=\dfrac{mv}{qB}$，$T=\dfrac{2\pi m}{qB}$ |
| 斜向 | 螺旋线 | 螺距 $h=v_\parallel T$ |

> [!important] 🔴 周期与速度无关——回旋加速器的依据
> $T=\dfrac{2\pi m}{qB}$ 里**没有 $v$**。所以可以每隔固定半个周期加一次电压，让粒子一次次被加速、半径不断变大。

**四个实例**（选择/填空常考）：

| 装置 | 原理 |
|---|---|
| **速度选择器** | $v=\dfrac{E}{B}$（电场力与洛伦兹力平衡） |
| **汤姆孙实验** | 测电子比荷 $e/m$ |
| **霍耳效应** | $V_H=\dfrac{IB}{nqd}$，$R_H=\dfrac{1}{nq}$，**极性能判断载流子正负** |
| **质谱仪** | $R=\dfrac{mv}{qB}$，按质量分开 |

> [!warning] 🟡 霍耳系数的用处
> $R_H=\dfrac{1}{nq}$，与载流子密度**成反比**（金属里 $n$ 大、效应弱；半导体里 $n$ 小、效应明显）。
> 更关键的是带 $q$ 的符号——**正负载流子给出的霍耳电压极性相反**，测极性就能判断是电子导电还是空穴导电。

## 7-7 磁场对载流导线的作用

> [!important] 🔴 安培力
> $$\mathrm d\vec F=I\,\mathrm d\vec l\times\vec B,\qquad F=BIL\sin\theta$$
> 匀强磁场中**直导线**：$\vec F=I\vec L\times\vec B$，方向垂直 $\vec L$ 和 $\vec B$ 所在平面。

> [!warning] 🟡 受力用左手，判断磁场用右手
> **左手定则**：磁感线穿入掌心，四指指电流方向，拇指即安培力方向。
> **左手管力，右手管场**——别混。

**平行电流**：**同向相吸、反向相斥**，单位长度受力

$$\frac{F}{l}=\frac{\mu_0I_1I_2}{2\pi a}$$

> [!important] 🔴 磁矩与磁力矩
> $$\vec m=NIS\vec e_n,\qquad \vec M=\vec m\times\vec B$$
> 大小 $M=mB\sin\theta$，$\theta$ 是**线圈法线**与 $\vec B$ 的夹角。
> 均匀磁场中平面线圈**合外力为零，只受力偶矩**。

> [!warning] 🔴 三个易错点
> - **$\vec M=\vec m\times\vec B$ 只对均匀磁场成立**。非均匀磁场里合外力不为零，力矩也不是这个式子，**不能直接套**。
> - **$\theta$ 是法线与磁场的夹角**，不是"线圈平面与磁场的夹角"（两者互余）。先画法线再量角。
> - **三个方位**：$\theta=0°$ **稳定平衡**（磁矩与场同向）；$90°$ 力矩**最大**；$180°$ **不稳定平衡**。

> [!important] 🟡 磁力做功只记一个式子
> $$W=I\Delta\Phi$$
> 等于电流乘**磁通量的改变量**。其他形状推出来也一样。

> [!tip] 🟡 带电体旋转类题的固定套路
> 取环带 → 求 $\mathrm dq$ → 求 $\mathrm dI=\dfrac{\omega}{2\pi}\mathrm dq$ → 套圆电流公式 → 积分。
> ⚠️ 磁矩增量写 $\mathrm dp_m=S\,\mathrm dI$，**不能**写 $I\,\mathrm dS+S\,\mathrm dI$（$I\mathrm dS$ 无物理意义，各圈电流不同）。

## 7-8 磁介质

**⚪ 四类磁介质**：

| 类型 | $\mu_r$ | 特点 |
|---|---|---|
| **顺磁质** | 略大于 1 | 微弱增强 |
| **抗磁质** | 略小于 1 | 微弱减弱 |
| **铁磁质** | $\gg1$ | 强磁性，有磁滞 |
| 完全抗磁（超导） | $=0$ | 迈斯纳效应 |

> [!important] 🟡 为什么要引入 $\vec H$
> $$\vec H=\frac{\vec B}{\mu_0}-\vec M,\qquad \oint\vec H\cdot\mathrm d\vec l=\sum I_0,\qquad \vec B=\mu\vec H$$
> $\vec B$ 的环路定理要同时算传导电流和**磁化电流**，而磁化电流测不到。$\vec H$ 把磁化部分吸收进去，**右边只剩能用仪器测的传导电流**。
>
> 这和电介质里引入 $\vec D$ 是同一个套路：$\vec D$ 藏起极化电荷，$\vec H$ 藏起磁化电流。

**⚪ 铁磁质**：有**磁滞回线**（$B_r$ 剩磁、$H_c$ 矫顽力），存在**磁畴**，超过**居里点**失去铁磁性。

> [!important] 🔴 本章必考题型（老师强调）
> 1. **求 $\vec B$**：先判对称性 → 能套安培环路定理就直接用；不能就毕奥-萨伐尔 + 叠加，**只叠加所需分量**
> 2. **带电体旋转**：取环带 → $\mathrm dq$ → $\mathrm dI$ → 圆电流公式 → 积分
> 3. **算完务必用极限或连续性验算**（无限长、圆心、$r=R$ 处）
> 4. **安培力、磁力计算是本章难点，可能出大题**

# 第 8 章 变化的电磁场

> [!important] 🟡 这一章最特殊的地方：不动就看不见
> 感应电动势本身看不见，能看见的只有电流计指针的偏转——而指针**只在磁通量变化时动**。
> 法拉第定律是物理定律里极少数**必须在运动中才看得到现象**的定律。

## 8-1 法拉第电磁感应定律

> [!important] 🔴 定律
> $$\varepsilon=-\frac{\mathrm d\Phi}{\mathrm dt}$$
> 负号来自楞次定律。若有 $N$ 匝：$\varepsilon=-N\dfrac{\mathrm d\Phi}{\mathrm dt}$。

> [!definition] 🟡 楞次定律
> 感应电流的**磁场**总是**阻碍**引起感应电流的磁通量的变化。
> - 磁通量增大 → 感应磁场反向 → 阻碍增大
> - 磁通量减小 → 感应磁场同向 → 维持原状

> [!tip] 🟡 实际做题只用绝对值 + 楞次定律
> 先按 $|\mathrm d\Phi/\mathrm dt|$ 算大小，方向单独用楞次定律判断。**别去套那套三步符号规则**，又啰嗦又容易错。

> [!important] 🟡 感应电荷只与磁通量改变量有关
> $$q=\int I\,\mathrm dt=\frac{\Delta\Phi}{R}$$
> **与变化快慢无关**——快插慢插，只要始末磁通量相同，流过的电荷就一样。
> 这就是**磁通计**的原理。

## 8-2 动生电动势与感生电动势

> [!important] 🔴 动生电动势（导体动、磁场不变）
> $$\varepsilon=\int_A^B(\vec v\times\vec B)\cdot\mathrm d\vec l$$
> **匀强磁场中直导线垂直切割**：$\varepsilon=Blv$。

> [!important] 🔴 两种算法都要会
> | 算法 | 式子 | 什么时候用 |
> |---|---|---|
> | **积分法** | $\varepsilon=\displaystyle\int(\vec v\times\vec B)\cdot\mathrm d\vec l$ | 导体各点 $\vec v$ 不同（如转动） |
> | **通量法** | 补成闭合回路，$\varepsilon=-\dfrac{\mathrm d\Phi}{\mathrm dt}$ | **形状不规则、积分积不出来**时 |
>
> 补上的那几边如果不动、不切割磁感线，对电动势**没有贡献**，随便补。

> [!warning] 🟡 转动的情形不能直接用 $Blv$
> 转动的棒每点速度不同（但**角速度相同**），必须积 $\omega l\,\mathrm dl$，结果 $\varepsilon=\dfrac12B\omega l^2$。
>
> 把棒扩成整个线框在磁场中转动，就是**所有发电机的原理**——输出的交流电天然带 $\sin\omega t$。

> [!important] 🔴 感生电动势（导体不动、磁场变）
> $$\varepsilon=-\frac{\mathrm d\Phi}{\mathrm dt},\qquad \oint_L\vec E_k\cdot\mathrm d\vec l=-\frac{\mathrm d\Phi}{\mathrm dt}$$

> [!important] 🔴 感生电场与静电场的三点区别
> | | 静电场 | 感生电场 |
> |---|---|---|
> | 产生原因 | 静止电荷 | **变化的磁场** |
> | 环流 | $\oint\vec E\cdot\mathrm d\vec l=0$（保守场） | $\oint\vec E_k\cdot\mathrm d\vec l\ne0$（**非保守**） |
> | 电场线 | 起于正电荷止于负电荷 | **闭合曲线** |

> [!warning] 🟡 棒上的电动势 ≠ 沿棒"走一圈"的环流
> 感生电场是涡旋场，$\int_A^B\vec E_k\cdot\mathrm d\vec l$ **与路径有关**。求棒上的电动势必须**沿棒本身**积分（$\cos\theta$ 逐点变），不能套 $E_k\cdot L$。
>
> **更省事的办法**：把棒与圆心补成闭合三角形，用 $\varepsilon=-\mathrm d\Phi/\mathrm dt$ 算整个回路，再减去两条半径上的贡献（半径方向与 $\vec E_k$ 垂直，贡献为零）。

## 8-3 自感与互感

> [!important] 🔴 自感
> $$\varepsilon_L=-L\frac{\mathrm dI}{\mathrm dt},\qquad L=\frac{\Phi}{I}$$
> 单位亨利（H）。$L$ 只由线圈的**几何形状和介质**决定。
>
> **负号的含义：永远阻碍电流变化**——电流增大时反向阻碍，减小时同向维持。
> 这解释了**断电时的火花**：$\mathrm dI/\mathrm dt$ 很大，自感电动势能击穿空气。

**必背**：长直螺线管 $L=\mu n^2V=\mu n^2 lS$。

> [!important] 🔴 互感
> $$\varepsilon_M=-M\frac{\mathrm dI_1}{\mathrm dt},\qquad M=\frac{\Phi_{21}}{I_1}$$
> 单位也是 H。**$M$ 与两个线圈的形状、大小、相对位置和介质有关**，且 $M_{12}=M_{21}$。
> 理论上 $M=k\sqrt{L_1L_2}$（$k$ 为耦合系数，$0\le k\le1$）。

**两个线圈串联**：顺串 $L=L_1+L_2+2M$；反串 $L=L_1+L_2-2M$。

## 8-4 磁场的能量

> [!important] 🔴 自感磁能
> $$W_m=\frac12LI^2$$

> [!important] 🔴 磁能密度
> $$w_m=\frac{B^2}{2\mu}=\frac12\mu H^2=\frac12BH$$
> 任意区域的磁能 $W_m=\displaystyle\int_V w_m\,\mathrm dV$。

> [!important] 🟡 磁能的来源是电源
> 电场是**保守场**，本身有势能；磁场**不是保守场**，它的能量是在电流建立过程中由**电源**输进来的。
> 这也解释了断开电路时能量去了哪：回路闭合则全部变成电阻的热；**断开没有回路**，能量以击穿空气的方式释放（拔插头的火花）。

## 8-5 位移电流

> [!important] 🔴 位移电流
> $$I_d=\frac{\mathrm d\Phi_D}{\mathrm dt}=\varepsilon_0\frac{\mathrm d\Phi_E}{\mathrm dt}\quad(\text{真空})$$
> 位移电流密度 $\vec j_d=\dfrac{\partial\vec D}{\partial t}$。

> [!warning] 🟡 位移电流"像"电流，但不是电流
> **相同**：都能激发涡旋磁场。
> **不同**：位移电流**不产生焦耳热**（没有电荷定向移动），也**不能用安培计测量**。
> 两者只在"产生磁场"这一件事上等价。

> [!important] 🔴 全电流安培环路定律
> $$\oint_L\vec H\cdot\mathrm d\vec l=I_0+\frac{\mathrm d\Phi_D}{\mathrm dt}$$
> 这就补上了对称性的另一半：法拉第说"变化的磁场产生电场"，位移电流说"变化的电场产生磁场"。两者合起来才有电磁波。

## 8-6 麦克斯韦方程组

> [!important] 🔴 四个方程（积分形式，必背）
> $$\oint_S\vec D\cdot\mathrm d\vec S=\sum q_0 \qquad\text{（电场高斯定理）}$$
> $$\oint_S\vec B\cdot\mathrm d\vec S=0 \qquad\text{（磁场高斯定理）}$$
> $$\oint_L\vec E\cdot\mathrm d\vec l=-\frac{\mathrm d\Phi_B}{\mathrm dt} \qquad\text{（法拉第定律）}$$
> $$\oint_L\vec H\cdot\mathrm d\vec l=\sum I_0+\frac{\mathrm d\Phi_D}{\mathrm dt} \qquad\text{（全电流定律）}$$

> [!important] 🟡 第四个方程是麦克斯韦的贡献
> 前三个都是别人已经得到的，只有第四个——把**位移电流**加进安培环路定理——是他补上的。补上这一项，方程组才在非稳恒情况下自洽。
>
> 四项凑齐后，方程组**自动允许电磁波存在**：变化的电场生磁场、变化的磁场生电场，互相激发、向前传播。
> 麦克斯韦由此算出 $c=1/\sqrt{\mu_0\varepsilon_0}$，正好等于光速——从而断定**光就是电磁波**。

**⚪ 电磁波**：横波，$\vec E\perp\vec B\perp$ 传播方向；同相位；$E=cB$；$c=\dfrac{1}{\sqrt{\mu_0\varepsilon_0}}$；在介质中 $v=\dfrac{1}{\sqrt{\mu\varepsilon}}=\dfrac{c}{n}$。

---

# 附录 A　公式总表

> [!important] 🔴 静电场
> | 量 | 公式 |
> |---|---|
> | 库仑定律 | $F=\dfrac{1}{4\pi\varepsilon_0}\dfrac{q_1q_2}{r^2}$ |
> | 点电荷场强 | $E=\dfrac{q}{4\pi\varepsilon_0r^2}$ |
> | 无限长直线 | $E=\dfrac{\lambda}{2\pi\varepsilon_0r}$ |
> | 无限大平面 | $E=\dfrac{\sigma}{2\varepsilon_0}$ |
> | 带电球面 | 内 $0$，外 $\dfrac{q}{4\pi\varepsilon_0r^2}$ |
> | 带电球体 | 内 $\dfrac{\rho r}{3\varepsilon_0}$，外 $\dfrac{q}{4\pi\varepsilon_0r^2}$ |
> | 高斯定理 | $\oint\vec E\cdot\mathrm d\vec S=\dfrac{\sum q_{\text{内}}}{\varepsilon_0}$ |
> | 环路定理 | $\oint\vec E\cdot\mathrm d\vec l=0$ |
> | 点电荷电势 | $V=\dfrac{q}{4\pi\varepsilon_0r}$ |
> | 电势定义 | $V_a=\displaystyle\int_a^\infty\vec E\cdot\mathrm d\vec l$ |
> | 场强与电势 | $E_l=-\dfrac{\partial V}{\partial l}$ |

> [!important] 🔴 导体与电介质
> | 量 | 公式 |
> |---|---|
> | 导体表面场强 | $E=\dfrac{\sigma}{\varepsilon_0}$（垂直表面） |
> | 电位移 | $\vec D=\varepsilon_0\vec E+\vec P=\varepsilon\vec E$ |
> | 极化电荷 | $\sigma'=P_n$ |
> | 有介质高斯定理 | $\oint\vec D\cdot\mathrm d\vec S=\sum q_0$ |
> | 平板电容 | $C=\dfrac{\varepsilon_0\varepsilon_rS}{d}$ |
> | 球形电容 | $C=\dfrac{4\pi\varepsilon_0\varepsilon_rR_AR_B}{R_B-R_A}$ |
> | 圆柱电容 | $C=\dfrac{2\pi\varepsilon_0\varepsilon_rl}{\ln(R_B/R_A)}$ |
> | 串并联 | 串联 $\dfrac1C=\sum\dfrac1{C_i}$；并联 $C=\sum C_i$（**与电阻相反**） |
> | 电容储能 | $W=\dfrac{Q^2}{2C}=\dfrac12CV^2=\dfrac12QV$ |
> | 电场能量密度 | $w_e=\dfrac12\varepsilon E^2$ |

> [!important] 🔴 恒定磁场
> | 量 | 公式 |
> |---|---|
> | 毕奥-萨伐尔 | $\mathrm d\vec B=\dfrac{\mu_0}{4\pi}\dfrac{I\mathrm d\vec l\times\vec e_r}{r^2}$ |
> | 无限长直导线 | $B=\dfrac{\mu_0I}{2\pi a}$ |
> | 有限长直导线 | $B=\dfrac{\mu_0I}{4\pi a}(\cos\theta_1-\cos\theta_2)$ |
> | 圆电流圆心 | $B=\dfrac{\mu_0I}{2R}$ |
> | 圆电流轴线 | $B=\dfrac{\mu_0IR^2}{2(R^2+x^2)^{3/2}}$ |
> | 螺线管内 | $B=\mu_0nI$ |
> | 运动电荷 | $B=\dfrac{\mu_0}{4\pi}\dfrac{qv\sin\alpha}{r^2}$ |
> | 磁场高斯定理 | $\oint\vec B\cdot\mathrm d\vec S=0$ |
> | 安培环路定理 | $\oint\vec B\cdot\mathrm d\vec l=\mu_0\sum I_{\text{套住}}$ |
> | 圆柱导体内 | $B=\dfrac{\mu_0rI}{2\pi R^2}$ |
> | 洛伦兹力 | $\vec F=q\vec v\times\vec B$ |
> | 回旋半径/周期 | $R=\dfrac{mv}{qB}$，$T=\dfrac{2\pi m}{qB}$ |
> | 安培力 | $\mathrm d\vec F=I\mathrm d\vec l\times\vec B$ |
> | 磁矩 | $\vec m=NIS\vec e_n$ |
> | 磁力矩 | $\vec M=\vec m\times\vec B$（**只对均匀磁场**） |
> | 磁力做功 | $W=I\Delta\Phi$ |

> [!important] 🔴 电磁感应
> | 量 | 公式 |
> |---|---|
> | 法拉第定律 | $\varepsilon=-\dfrac{\mathrm d\Phi}{\mathrm dt}$ |
> | 动生电动势 | $\varepsilon=Blv$；转动棒 $\dfrac12B\omega l^2$ |
> | 感生电场 | $\oint\vec E_k\cdot\mathrm d\vec l=-\dfrac{\mathrm d\Phi}{\mathrm dt}$ |
> | 自感 | $\varepsilon_L=-L\dfrac{\mathrm dI}{\mathrm dt}$，$L=\dfrac{\Phi}{I}$ |
> | 互感 | $\varepsilon_M=-M\dfrac{\mathrm dI}{\mathrm dt}$，$M=\dfrac{\Phi_{21}}{I_1}$ |
> | 螺线管自感 | $L=\mu n^2V$ |
> | 磁能 | $W_m=\dfrac12LI^2$ |
> | 磁能密度 | $w_m=\dfrac{B^2}{2\mu}$ |
> | 位移电流 | $I_d=\dfrac{\mathrm d\Phi_D}{\mathrm dt}$ |

---

# 附录 B　真题逐题对照

> 2022 年 11 月 A 卷（8 页，100 分）。**答案已按卷末答案页核对**。

## B1 选择题逐题详解（10 题）

> 不只看答案，每题给「考什么 → 怎么判 → 关联公式」。**这些就是卷面能直接命中的 20 分。**

### 第 1 题（答案 C）密立根油滴实验

**考点**：物理学史——谁测出了电子电荷量。

| 人物 | 贡献 |
|---|---|
| **库仑** | 库仑定律 |
| **安培** | 安培定律、分子电流假说 |
| **密立根** | **油滴实验测电子电荷量** $e$ |
| **汤姆孙** | 测电子**比荷** $e/m$ |

> 记住这条区分：**汤姆孙测比荷，密立根测电荷量。** 一个测比值，一个测绝对值。

### 第 2 题（答案 D）$\oint\vec D\cdot\mathrm d\vec S=0$ 的含义

**考点**：有介质时的高斯定理只数**自由电荷**。

$$\oint_S\vec D\cdot\mathrm d\vec S=\sum q_0\quad(\text{自由电荷})$$

所以式子为 0 ⟹ **面内自由电荷的代数和为零**。

> [!warning] 三个干扰项都在"多算"
> - 「既无自由电荷也无束缚电荷」——错，束缚电荷本来就不进这个式子
> - 「没有自由电荷」——错，可以是**代数和**为零（有正有负）
> - 「自由电荷和束缚电荷代数和为零」——错，束缚电荷不参与

### 第 3 题（答案 D）点电荷对一个正方形平面的电通量

**考点**：**电通量的对称补全法**——这个技巧在本章反复出现。

**题目**：边长 $a$ 的正方形，点电荷 $q$ 在过中心的垂线上、距中心 $a/2$ 处。

**解法**：把正方形补成一个**立方体**，让 $q$ 落在立方体中心。立方体有 6 个面，由对称性每个面分到的通量相同，而通过整个闭合面的通量是 $q/\varepsilon_0$：

$$\Phi_{\text{一个面}}=\frac16\cdot\frac{q}{\varepsilon_0}=\frac{q}{6\varepsilon_0}$$

> [!important] 这个方法的通用性
> **凡是"点电荷对某个局部的面/角"求通量，都可以补成闭合面再按份数分。**
> - 正方体中心 → 每面 $\dfrac{q}{6\varepsilon_0}$
> - 立方体一个顶点 → 用 8 个立方体补成整块，对**三个**相邻面的通量是 $\dfrac{q}{8\varepsilon_0}$ 每个
> - 半无限大平面 → 补成无限大平面，得 $\dfrac{q}{2\varepsilon_0}$
>
> 前提：$q$ 必须在补出来的闭合面**内部**，否则通量为 0。

### 第 4 题（答案 A）均匀平行电场线区域

**考点**：**$E$ 与 $U$ 是两个不同的量**。

**题目**：区域内电场线是均匀分布的平行直线，问同一电场线上两点的 $E$ 和 $U$。

**判断**：
- 电场线**均匀且平行** ⟹ 各处 $E$ **大小和方向都相同** ⟹ $E$ 相同
- 电势沿电场线方向**逐渐降低** ⟹ 同一线上不同点 $U$ **不同**

所以选 A（$E$ 相同，$U$ 不同）。

> [!warning] 别把两者绑在一起
> $E$ 描述的是"单位电荷受的力"，$U$ 描述的是"单位电荷的电势能"。
> **$E$ 相同不代表 $U$ 相同**——就像匀速运动里"速度相同"但"位移不同"。

### 第 5 题（答案 C）断开电源后插入介质，能量怎么变

**考点**：**断开电源 ⟹ $Q$ 不变**；再插介质 $C$ 变大 ⟹ 能量变小。

**推导**：

$$W=\frac{Q^2}{2C}$$

$Q$ 不变、$C$ 变为 $\varepsilon_r C_0$，所以

$$\frac{W_2}{W_1}=\frac{C_0}{\varepsilon_r C_0}=\frac{1}{\varepsilon_r}$$

> [!important] 🔴 这张表必须背下来（两种情形完全相反）
> | | **断开电源**（$Q$ 不变） | **连接电源**（$U$ 不变） |
> |---|---|---|
> | 插入介质后 $C$ | 变大 $\varepsilon_r$ 倍 | 变大 $\varepsilon_r$ 倍 |
> | $Q$ | **不变** | 变大 $\varepsilon_r$ 倍 |
> | $U$ | 变小到 $U/\varepsilon_r$ | **不变** |
> | $E$ | 变小到 $E/\varepsilon_r$ | **不变** |
> | 能量 $W$ | **变小**到 $W/\varepsilon_r$ | **变大** $\varepsilon_r$ 倍 |
>
> **判断口诀**：先看断不断电 → 定住 $Q$ 还是 $U$ → 其余全由 $C$ 的变化推。
> 用 $W=\dfrac{Q^2}{2C}$（$Q$ 不变时）或 $W=\dfrac12CU^2$（$U$ 不变时）**挑对公式**，别用错。

### 第 6 题（答案 D）导轨上导线的运动方向

**考点**：**楞次定律 + 安培力方向**。

**分析**：ab 向右移动 → 回路面积增大 → 穿过回路的磁通量（向上）增大 → 感应电流要产生**向下**的磁场 → 由右手定则，回路中感应电流为**顺时针** → cd 中电流方向为由 c 到 d（向下？按图判断）→ 再用左手定则判断 cd 受的安培力 → **向右**。

> [!important] 更快的判法（老师常说的"来拒去留"）
> **导体运动导致磁通增大 → 安培力阻碍这个运动（反向）；磁通减小 → 安培力维持运动（同向）。**
> 本题磁通增大 ⟹ 安培力要**阻止面积继续增大** ⟹ cd 被推着往右走（跟着 ab，缩小相对距离）。
>
> 注意：cd 向右是因为它想"追上"ab 来减小面积，而不是被 ab 推开的。

### 第 7 题（答案 B）串联的两根铜棒

**考点**：**串联电路里"电流强度相同"是唯一的不变量**。

**题目**：两根截面积不同、长度相同的铜棒**串联**，加电压 $U$。

| 量 | 是否相同 | 原因 |
|---|---|---|
| **电流强度 $I$** | ✅ **相同** | 串联电路的电荷守恒，单位时间通过任一截面的电荷一样 |
| 电流密度 $j=I/S$ | ❌ 不同 | 截面积不同 |
| 电场强度 $E=\rho j$ | ❌ 不同 | $j$ 不同 |
| 端电压 $U=IR$ | ❌ 不同 | 截面积小的电阻大，分压多 |

> [!warning] 这题的正确选项只有 B
> 别被"铜棒一样"误导——**电阻 $R=\rho\dfrac{l}{S}$，截面积不同则电阻不同**。

### 第 8 题（答案 C）直导线与圆环在 O 点的磁场叠加

**考点**：**叠加原理 + "延长线过场点则贡献为零"**。

**题目**：电流 1 沿半径进入圆环 a 点，圆环电流从 b 点切向流出，经导线 2 返回。a、b、O 三点共线。

**逐部分分析**：

| 部分 | 在 O 点产生的 $B$ | 为什么 |
|---|---|---|
| **直导线 1** | **0** | 它的延长线**过圆心 O** ⟹ $\mathrm d\vec l\parallel\vec r$ ⟹ $\mathrm d\vec l\times\vec r=0$ |
| **直导线 2** | 非零 | 不沿径向 |
| **圆环**（两段并联） | **0** | 两段电流方向相反、且与半径成正比分配 ⟹ **互相抵消** |

所以只剩直导线 2，选 C。

> [!important] 两条常用结论
> 1. **载流直导线的延长线过某点时，该点 $B=0$**（因为 $\mathrm d\vec l$ 与 $\vec r$ 平行）
> 2. **均匀圆环上两段并联的电流在圆心产生的磁场互相抵消**（前提是电阻与弧长成正比）
>
> 这两条能秒掉一大类"叠加"选择题。

### 第 9 题（答案 B）电子绕质子运动的磁力矩

**考点**：**旋转带电体的等效磁矩**。

**推导**：电子绕核做圆周运动，等效于一个圆电流：

$$I=\frac{e}{T}=\frac{e\omega}{2\pi},\qquad S=\pi R^2$$

所以磁矩

$$m=IS=\frac{e\omega}{2\pi}\cdot\pi R^2=\frac12e\omega R^2$$

磁力矩 $M=mB\sin90°=\dfrac12e\omega R^2B$，选 B。

> [!important] 🔴 旋转带电体的磁矩（必背）
> $$m=\frac12q\omega R^2\quad(\text{电荷 }q\text{ 沿半径 }R\text{ 的圆转})$$
> 换成电流密度形式就是**旋转圆盘**题的做法：取环带 $\mathrm dq$、$\mathrm dI=\dfrac{\omega}{2\pi}\mathrm dq$、$\mathrm dp_m=S\,\mathrm dI$ 再积分。
>
> ⚠️ 磁矩增量只能写 $S\,\mathrm dI$，**不能写 $I\,\mathrm dS$**（各圈电流不同，不存在"总电流"）。

### 第 10 题（答案 D）自感系数由什么决定

**考点**：**$L$ 是线圈自身的属性，与电流无关**。

| 说法 | 判断 |
|---|---|
| 电流越大 $L$ 越大 | ❌ 无关 |
| 电流变化率越大 $L$ 越大 | ❌ 无关 |
| 与是否充磁介质无关 | ❌ **有关**（$L=\mu n^2V$，$\mu$ 变了 $L$ 就变） |
| **单位长度匝数越多 $L$ 越大** | ✅ 正确 |

> 类比电容：$C$ 只由几何和介质决定；$L$ 也一样。**"越大/越快就越怎样"的选项基本都是错的。**

---

## B2 填空题逐题详解（10 空）

### 11（答案 0）均匀带电圆柱面内部

**考点**：高斯定理的标准应用。取半径 $r<R$ 的圆柱高斯面，面内无电荷 ⟹ $E=0$。

> 同一类结论：均匀带电**球面**内部也是 0；均匀带电**圆柱体/球体**内部则不为零（$\propto r$）。

### 12（答案 $\dfrac{q}{6\pi\varepsilon_0R}$）沿半圆弧移动电荷的做功

**考点**：**静电力做功只与始末位置有关，与路径无关**。

$$W_{B\to D}=q_0(V_B-V_D)$$

题目：$A$ 点有 $+q$、$O$ 点有 $-q$，$BA=R$，半圆弧半径 $R$。

关键：**$B$ 和 $D$ 到两电荷的距离要分别算**，不要以为"沿圆弧走"就要沿路径积分。$O$ 点的 $-q$ 到 $B$、$D$ 距离都是 $R$，$A$ 点的 $+q$ 到两点距离也相同，所以 $-q$ 的贡献**相消**，只剩 $+q$ 的贡献。

> [!warning] 两个思路要点
> - **路径无所谓**——这是保守场的核心性质，直接用 $q(V_B-V_D)$
> - **先算两点电势再相减**，比沿路径积分快得多
>
> 补充：如果是"外力做功"，符号要反过来。

### 13（答案 $\dfrac{C_1}{C_2}$）并联电容的电荷比

**考点**：并联电压相同。

$$Q_1=C_1U,\quad Q_2=C_2U\Rightarrow\frac{Q_1}{Q_2}=\frac{C_1}{C_2}$$

> 对照记忆：**串联电荷相同（$Q$ 相等），并联电压相同（$U$ 相等）**。
> 所以串联时 $U_1:U_2=C_2:C_1$（反比），并联时 $Q_1:Q_2=C_1:C_2$（正比）。

### 14（答案 $\dfrac{\lambda_0}{4\pi\varepsilon_0}\left[a\ln\dfrac{a+l}{a}-l\right]$）不均匀带电细棒在 O 点的电势

**考点**：**电势叠加（积分法）**，且 $\lambda$ 是**变化的**。

**做法**：在 $x$ 处取电荷元 $\mathrm dq=\lambda_0(x-a)\mathrm dx$，它到 O 点的距离就是 $x$：

$$V=\int_a^{a+l}\frac{\lambda_0(x-a)\,\mathrm dx}{4\pi\varepsilon_0 x}=\frac{\lambda_0}{4\pi\varepsilon_0}\int_a^{a+l}\left(1-\frac ax\right)\mathrm dx$$

$$=\frac{\lambda_0}{4\pi\varepsilon_0}\left[l-a\ln\frac{a+l}{a}\right]$$

（与卷面答案差一个整体符号，取决于 $\lambda_0$ 的正负约定——按题目给的 $\lambda=\lambda_0(x-a)$ 展开时要注意 $x>a$ 时为正是负。）

> [!warning] 三个易错点
> - **积分限**：棒从 $a$ 到 $a+l$，不是 $0$ 到 $l$
> - **分母是 $x$**（到原点距离），不是 $(x-a)$
> - $\lambda$ 随位置变，**必须留在积分号内**，不能提出来

### 15（答案 $-\dfrac23\varepsilon_0E_0$）两块无限大带电平面的面密度

**考点**：**场强叠加 + 方向判断**。

两块无限大平面各自产生 $\dfrac{\sigma}{2\varepsilon_0}$ 的场，方向由电荷正负决定。题目给了三个区域的场强（外侧 $E_0/3$、之间 $E_0$），列两个方程解 $\sigma_A$、$\sigma_B$。

**一般方法**（三类题通用）：

| 区域 | 合场强 |
|---|---|
| A 左侧 | $E_A+E_B$（按方向代数和） |
| A、B 之间 | $E_A-E_B$（或反向） |
| B 右侧 | $E_A+E_B$ |

> [!important] 这类题的固定解法
> 1. 设 $\sigma_A$、$\sigma_B$（带符号）
> 2. 每个区域写出**矢量和**（同向加、反向减）
> 3. 用题目给的数值列方程，解出 $\sigma$
> 4. **最后验算**：代入后看三个区域的场是否符合题目描述
>
> ⚠️ 判方向时以"垂直平面向外为正"统一，别中途换约定。

### 16（答案 $\oint_S\vec B\cdot\mathrm d\vec S=0$）反映"磁场无源"的方程

**考点**：麦克斯韦方程组的**物理含义**对应关系。

| 方程 | 含义 |
|---|---|
| $\oint\vec D\cdot\mathrm d\vec S=\sum q_0$ | 电场**有源**（电荷是源头） |
| $\oint\vec B\cdot\mathrm d\vec S=0$ | 磁场**无源**（无磁单极子）← **本题** |
| $\oint\vec E\cdot\mathrm d\vec l=-\dfrac{\mathrm d\Phi_B}{\mathrm dt}$ | 变化的磁场生电场 |
| $\oint\vec H\cdot\mathrm d\vec l=I_0+\dfrac{\mathrm d\Phi_D}{\mathrm dt}$ | 传导电流和变化电场生磁场 |

> 题干出现"无源场""磁感应线闭合"就答第二个。

### 17（答案 0）回路平行于直导线运动

**考点**：**磁通量没变 ⟹ 没有感应电动势**。

**题目**：矩形回路与长直导线共面，回路以速度 $v$ **平行于直导线方向**运动。

**判断**：回路到直导线的距离 $r$ 保持不变 ⟹ 穿过回路的磁通量 $\Phi$ **不变** ⟹ $\varepsilon=-\dfrac{\mathrm d\Phi}{\mathrm dt}=0$。

> [!important] 🔴 "动就有电动势"是错的
> 产生感应电动势的**唯一条件**是**磁通量发生变化**，不是"导体在动"。
>
> | 运动方式 | 磁通量 | 电动势 |
> |---|---|---|
> | 平行于导线平移 | 不变 | **0** |
> | 垂直导线方向平移（远离/靠近） | 变 | 非零 |
> | 绕导线转动 | 变 | 非零 |
>
> 同类陷阱：线圈在**均匀磁场中平移**（不转动）也是 0。

### 18（答案 $\dfrac{\mu_0ih}{2\pi R}$）割缝圆柱管的轴线磁场

**考点**：**补偿法（叠加法）**——把"缺一块"补成"完整的 + 反向的一块"。

**思路**：

$$\vec B_{\text{割缝管}}=\vec B_{\text{完整管}}+\vec B_{\text{反向电流带}}$$

- 完整的无限长圆柱面，轴线上的 $B = 0$（管内无场）
- 割掉的宽 $h$ 的窄条，相当于一条**反向**的无限长直电流，电流 $I=ih$
- 这条"直导线"到轴线的距离是 $R$

所以轴线处

$$B=\frac{\mu_0(ih)}{2\pi R}$$

> [!important] 补偿法适用的一类题
> 「从某个完整结构里挖掉一块」——都先补成完整的，再叠加一个"反向的挖掉部分"。
> 电学里同样用：球壳挖小孔、带电板挖圆孔，都是这个套路。

### 19（答案 $2.14\times10^{-8}\ \mathrm{Wb}$）电子圆周运动包围的磁通量

**考点**：**洛伦兹力提供向心力 → 求 $B$ → 求磁通量**。这是"力学 + 磁场"的典型串联。

$$\frac{mv^2}{R}=qvB\Rightarrow B=\frac{mv}{qR}$$

$$\Phi=B\cdot\pi R^2=\frac{mv}{qR}\cdot\pi R^2=\frac{\pi mvR}{q}$$

代入 $v=10^5$、$R=1.2\times10^{-2}$、$m_e=9.1\times10^{-31}$、$e=1.6\times10^{-19}$：

$$\Phi=\frac{3.14\times9.1\times10^{-31}\times10^5\times1.2\times10^{-2}}{1.6\times10^{-19}}\approx2.14\times10^{-8}\ \mathrm{Wb}$$

> [!warning] 三个易错
> - 用 $R=\dfrac{mv}{qB}$ **反解 $B$**，别忘了这是"电子"，$q=e$
> - 面积是 $\pi R^2$，不是 $R^2$
> - 数量级要对：$10^{-8}$ 量级合理，若算出 $10^{-3}$ 就是幂次错了

### 20（答案 $L_1+L_2+2M$）两个线圈串联的等效自感

**考点**：**顺串（同向）取加号，反串（反向）取减号**。

$$L_{\text{顺}}=L_1+L_2+2M,\qquad L_{\text{反}}=L_1+L_2-2M$$

> [!important] 怎么判断顺串还是反串
> 看**两个线圈的磁场方向是否相同**：
> - 绕向相同、电流从同名端流入 → 磁场同向 → 顺串 → **+2M**
> - 绕向相反，或从异名端流入 → 磁场反向 → 反串 → **−2M**
>
> 卷面给了图（两线圈同轴、绕向相同），所以是顺串。

---

## B2.5 另一套卷（2024–2025）的选择题考点

> 未拿到该卷答案页，**只列考点**，不写答案。这几道都能在上面正文找到对应。

| 题 | 考点 | 在本文哪里 |
|---|---|---|
| 1 | 圆柱面 + **接地的外金属筒**，求两柱面之间某点的 $E$ 与 $U$ | 5-3 高斯定理 + 6-1 接地导体 |
| 2 | $E=F/q_0$ 的定义式**只是量度式**，$E$ 由场源决定 | 5-2 电场强度 |
| 3 | 充电后**断开**、再与未充电电容并联 → 总能量**减少** | 6-3 电容 + 6-4 能量（与 B1 第 5 题同源） |
| 4 | 带正电的 A 靠近孤立导体 B → B 的**电势升高** | 6-1 导体电势 |
| 5 | 两球壳 + 三个点电荷，改变 $Q_2$ 谁的电势变 | 6-1 静电屏蔽 + 电势叠加 |
| 6 | 点电荷做圆周运动，圆心处 $B$ | 7-3 运动电荷的磁场 |

> [!important] 第 3 题和第 5 题最能说明"要理解而不是背"
> - 第 3 题：两电容并联后总电荷不变、等效电容变大 ⟹ $W=Q^2/(2C)$ **减小**（能量去哪了？变成导线电阻的热）
> - 第 5 题：**接地**的球壳把内外隔开——改变腔内电荷只影响腔内，外部不受影响；反之亦然。这正是静电屏蔽的考点。

## B3 五道计算题：考什么、怎么做

> 卷面 5 题各 12 分。下面给**解题骨架**，具体数字按题目条件代入。

### 第三题　同轴圆柱面 + 带电粒子圆周运动

**题目**：两同轴圆柱面 $R_1<R_2$，内柱带 $-\lambda$、外柱带 $+\lambda$。带正电 $q$、质量 $m$ 的质点在两柱之间半径 $r$ 的轨道上做圆周运动。求 (1) 该处场强 (2) 速率 (3) 动能。

**做法**：
1. **高斯定理**：取半径 $r$、高 $h$ 的圆柱面，$\oint\vec E\cdot\mathrm d\vec S=E\cdot2\pi rh=\dfrac{-\lambda h}{\varepsilon_0}$
 $$\Rightarrow E=\frac{\lambda}{2\pi\varepsilon_0 r}\quad(\text{方向指向轴线})$$
2. **向心力 = 电场力**：$\dfrac{q\lambda}{2\pi\varepsilon_0r}=\dfrac{mv^2}{r}\Rightarrow v=\sqrt{\dfrac{q\lambda}{2\pi\varepsilon_0m}}$
3. **动能**：$E_k=\dfrac12mv^2=\dfrac{q\lambda}{4\pi\varepsilon_0}$

> [!tip] 这题的三个得分点
> 高斯面要画（4 分）→ 列出向心力方程（4 分）→ 算动能（4 分）。
> **注意 $v$ 与 $r$ 无关**——这是 $\dfrac1r$ 场的一个重要特点。

### 第四题　体电荷密度 $\rho=Ar^{1/2}$ 的带电球

**题目**：求球内外场强、电势、静电场能。

**做法**：
1. **先求包围电荷**：$Q(r)=\displaystyle\int_0^r Ar'^{1/2}\cdot4\pi r'^2\,\mathrm dr'=4\pi A\cdot\frac27 r^{7/2}$
2. **球内**：$E\cdot4\pi r^2=\dfrac{Q(r)}{\varepsilon_0}\Rightarrow E_{内}=\dfrac{2A}{7\varepsilon_0}r^{3/2}$
3. **球外**：$E_{外}=\dfrac{Q(R)}{4\pi\varepsilon_0r^2}=\dfrac{2AR^{7/2}}{7\varepsilon_0r^2}$
4. **电势**：球外积分、球内分段积分（从 $\infty$ 到 $R$ 再用球内场积到 $r$）
5. **静电场能**：$W=\displaystyle\int\frac12\varepsilon_0E^2\,\mathrm dV$，**分球内球外两段**

> [!warning] 两个易错
> - **积分上限是 $r$ 不是 $R$**（算球内场时只数半径 $r$ 以内的电荷）
> - **球内电势要分段积分**，不能直接用 $\dfrac{Q}{4\pi\varepsilon_0r}$

### 第五题　两个运动电荷的磁场与电磁力

**题目**：$q_1,q_2$ 相距 $d$，速度 $v_1,v_2$。求各自在对方处产生的磁场和作用力。

**做法**：
1. $q_1$ 在 $q_2$ 处的磁场是**运动电荷的磁场**：$B_1=\dfrac{\mu_0}{4\pi}\dfrac{q_1v_1\sin\alpha}{d^2}$
2. $q_2$ 受到的**洛伦兹力** $F_m=q_2v_2B_1$（方向由右手定则）
3. 同时 $q_1$ 还产生电场，$q_2$ 受电场力 $F_e=\dfrac{q_1q_2}{4\pi\varepsilon_0d^2}$
4. **合力** $F=\sqrt{F_m^2+F_e^2}$，夹角 $\theta=\arctan\dfrac{F_e}{F_m}$
5. 反过来求 $q_2$ 在 $q_1$ 处的场时，注意**$v_2$ 与径矢同向 ⟹ $B_2=0$**，只剩电场力

> [!warning] 这题的陷阱
> $v_2$ 沿 $q_2\to q_1$ 方向时，$\vec v\parallel\vec r$，所以 $\sin\alpha=0$、**$B_2=0$**——不要惯性照抄 $B_1$ 的式子。

### 第六题　半无限长导线 + 圆弧的磁场叠加

**题目**：两根半无限长导线接在圆弧 A、B 两点，圆弧 ACB 电阻是 AB 的 2 倍，求圆心 O 的磁感应强度。

**做法**（纯叠加，分三部分算）：
1. **半无限长导线 KB**：其延长线过 O ⟹ 在 O 处 **$B=0$**
2. **半无限长导线 EA**：$B=\dfrac{\mu_0I}{4\pi R}$，方向由右手定则
3. **两段圆弧并联**：电阻比 2:1 ⟹ **电流比 1:2**（电阻大的电流小）
 - ACB（大弧，2/3 圆周）：$I_1=I/3$，$B_1=\dfrac{\mu_0I_1}{2R}\cdot\dfrac{2\pi}{2\pi}$ 按圆弧比例算
 - AB（小弧）：$I_2=2I/3$
4. **按方向取代数和**（垂直纸面向里为正）

> [!warning] 这题的关键
> **两段圆弧是并联的，电流按电阻反比分配**——这是最容易漏的一步，很多人直接当同一个 $I$ 算。
> 另外注意方向：两段圆弧的电流方向相反，磁场方向也相反，要**相减**。

### 第七题　两个同轴圆线圈（互感）

**题目**：大线圈 $R$ 通电流 $I$，小线圈 $r$ 在轴线上距 $x$ 处、以速率 $v$ 沿轴运动。求 (1) 小线圈圆心处 $B$ (2) 感应电动势 (3) 互感。

**做法**：
1. **轴线上磁场**：$B=\dfrac{\mu_0IR^2}{2(R^2+x^2)^{3/2}}$
2. **$r\ll R$ 时小线圈内可视为匀强场**：$\Phi=B\cdot\pi r^2$
3. **感应电动势**：$\varepsilon=\left|\dfrac{\mathrm d\Phi}{\mathrm dt}\right|=\left|\dfrac{\mathrm d\Phi}{\mathrm dx}\cdot v\right|$（对 $x$ 求导再乘 $v$）
4. **互感**：$M=\dfrac{\Phi}{I}=\dfrac{\mu_0\pi R^2r^2}{2(R^2+x^2)^{3/2}}$

> [!warning] $r\ll R$ 这个条件
> 它让你可以用"圆心处的 $B$"代替整个小线圈内的 $B$。**没有这个条件就得积分**。

---

# 附录 C　易错点速查

| 章 | 易错点 |
|---|---|
| 5 | 高斯定理**只数面内电荷**，但场强由内外全部电荷决定 |
| 5 | 球体内部 $E\propto r$，别当点电荷算；球心处 $E=0$ |
| 5 | 电势叠加是**标量加**，不分解方向；场强才要分解 |
| 5 | 电势零点：有限带电体取无穷远；无限长带电体不能取无穷远 |
| 6 | 导体表面 $E=\dfrac{\sigma}{\varepsilon_0}$，但**叠加时用的是 $\dfrac{\sigma}{2\varepsilon_0}$** |
| 6 | 接地 ≠ 外表面电荷全消失；要按具体条件分析 |
| 6 | 左右并排的两介质**电荷密度不相等**，别当串联算（联立：电荷守恒 + 电压相等） |
| 6 | 电容器公式前提是"**等量异号**"；不满足时先演化到平衡态再算 |
| 7 | 安培环路定理：右边只数**套住的**电流，左边是**全部**电流产生的场 |
| 7 | 有限长直导线的 $\theta_1,\theta_2$ 次序容易反——用无限长情形验算 |
| 7 | $\vec M=\vec m\times\vec B$ **只对均匀磁场成立** |
| 7 | 磁力矩的 $\theta$ 是**法线**与 $\vec B$ 的夹角，不是平面与 $\vec B$ 的夹角 |
| 7 | 左手管力、右手管场；运动电荷的场方向：$\vec v\times\vec e_r$ |
| 8 | 沿导线平移**磁通量不变** ⟹ 电动势为 0（别以为"动就有"） |
| 8 | 转动棒不能用 $Blv$，要积 $\omega l\,\mathrm dl$ |
| 8 | 感生电场是**涡旋场**，路径有关，不能套 $E\cdot L$ |
| 8 | 位移电流不产生焦耳热，也不能用安培计测量 |

---

# 相关链接

- 主笔记：[[大学物理（下）]]
- 复习优先级（按老师划的重点）：**电容计算（必考）→ 电场/电势计算 → 导体与电介质的结论 → 安培力与磁力 → 电磁感应**
- 考前节奏：过一遍「考前 2 小时」那 16 条 → 过一遍附录 A 公式表 → 看附录 B 的真题 → 重点默写三个计算套路（高斯定理求场、叠加求场、电容与能量）
