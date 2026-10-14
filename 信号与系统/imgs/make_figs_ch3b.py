# -*- coding: utf-8 -*-
"""信号与系统 第三章 配图（第二批：从课件难以直接截取的两张）

为什么只有两张：
  - 「画频谱图例题」「由频谱反推波形」「三角波求导成冲激串」都有白底或
    清晰的课件原图，直接截取即可（见 imgs/ 下同名 png），不重画；
  - 本文件只画课件里**截不出来**的两张：
      * 单边谱/双边谱对照 —— 课件原图是浅蓝底 + 白字，对比度太低；
      * 直流隐藏对称性 —— 课件原图被橙色文本框压住波形。
重跑：把本文件放 imgs/ 目录下直接执行。
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["mathtext.fontset"] = "cm"

OUT = os.path.dirname(os.path.abspath(__file__))

BLUE = "#1f6fd0"
RED = "#d62728"
GRAY = "#999999"
GREEN = "#2e9e5b"


def axes_arrows(ax, xlabel, ylabel, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["left"].set_color("#555")
    ax.spines["bottom"].set_color("#555")
    ax.annotate("", xy=(xlim[1], 0), xytext=(xlim[0], 0),
                arrowprops=dict(arrowstyle="-|>", color="#555", lw=1.0))
    ax.annotate("", xy=(0, ylim[1]), xytext=(0, ylim[0]),
                arrowprops=dict(arrowstyle="-|>", color="#555", lw=1.0))
    ax.set_xlabel(xlabel, fontsize=9)
    if ylabel:
        # 标签放在 y 轴顶端右侧 —— 轴挪到 zero 位置时 set_ylabel 会和刻度标签叠在一起
        ax.annotate(ylabel, xy=(0, ylim[1]), xytext=(5, -4), textcoords="offset points",
                    fontsize=9, ha="left", va="top")


def save(fig, name):
    p = os.path.join(OUT, name)
    fig.savefig(p, dpi=190, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("saved", name, os.path.getsize(p) // 1024, "KB")


# ============ 图 B：单边谱与双边谱的对照 ============
# 信号 f(t) = 3 + 4cos(12πt + 30°) − 6sin(24πt)
#   A0=3, A1=4(6Hz,30°), A2=6(12Hz,90°)      → 单边
#   F0=3, |F1|=2(±6Hz), |F2|=3(±12Hz)        → 双边
#   单边 P = 3² + 0.5(4²+6²) = 9+8+18 = 35 W
#   双边 P = 3²+2²+3²+2²+3² = 9+4+9+4+9 = 35 W
def fig_uni_vs_bi():
    fig, axes = plt.subplots(2, 2, figsize=(8.0, 5.4))

    # 左上：单边幅度谱
    ax = axes[0][0]
    xs, ys = [0, 6, 12], [3, 4, 6]
    axes_arrows(ax, r"$f\,/\mathrm{Hz}$", r"$A_n$", (-2.2, 15.5), (-0.6, 7.6))
    ax.vlines(xs, 0, ys, color=BLUE, lw=1.8)
    ax.plot(xs, ys, "o", ms=4.4, color=BLUE)
    ax.set_xticks([0, 6, 12]); ax.set_xticklabels(["0", "6", "12"], fontsize=8.5)
    ax.set_yticks([0, 3, 4, 6]); ax.set_yticklabels(["0", "3", "4", "6"], fontsize=8.5)
    for x, y in zip(xs, ys):
        ax.text(x + 0.4, y + 0.18, str(y), fontsize=8.8, color=BLUE)
    ax.set_title("单边幅度谱", fontsize=9.6, pad=5)

    # 左下：单边相位谱
    ax = axes[1][0]
    xs, ys = [6, 12], [30, 90]
    axes_arrows(ax, r"$f\,/\mathrm{Hz}$", r"$\varphi_n\,/^\circ$", (-2.2, 15.5), (-20, 115))
    ax.vlines(xs, 0, ys, color=RED, lw=1.8)
    ax.plot(xs, ys, "o", ms=4.4, color=RED)
    ax.set_xticks([0, 6, 12]); ax.set_xticklabels(["0", "6", "12"], fontsize=8.5)
    ax.set_yticks([0, 30, 90]); ax.set_yticklabels(["0", "30", "90"], fontsize=8.5)
    for x, y in zip(xs, ys):
        ax.text(x + 0.4, y + 4.0, f"{y}", fontsize=8.8, color=RED)
    ax.set_title("单边相位谱", fontsize=9.6, pad=5)

    # 右上：双边幅度谱
    ax = axes[0][1]
    xs = np.array([-12, -6, 0, 6, 12]); ys = np.array([3, 2, 3, 2, 3])
    axes_arrows(ax, r"$f\,/\mathrm{Hz}$", r"$|F_n|$", (-16.5, 16.5), (-0.6, 4.3))
    ax.vlines(xs, 0, ys, color=BLUE, lw=1.8)
    ax.plot(xs, ys, "o", ms=4.4, color=BLUE)
    ax.set_xticks([-12, -6, 0, 6, 12])
    ax.set_xticklabels([r"$-12$", r"$-6$", "0", "6", "12"], fontsize=8.5)
    ax.set_yticks([0, 3]); ax.set_yticklabels(["0", "3"], fontsize=8.5)
    for x, y in zip(xs, ys):
        ax.text(x - 0.7, y + 0.14, str(int(y)), fontsize=8.8, color=BLUE)
    ax.set_title("双边幅度谱", fontsize=9.6, pad=5)

    # 右下：双边相位谱
    ax = axes[1][1]
    xs = np.array([-12, -6, 6, 12]); ys = np.array([-90, -30, 30, 90])
    axes_arrows(ax, r"$f\,/\mathrm{Hz}$", r"$\varphi_n\,/^\circ$", (-16.5, 16.5), (-125, 125))
    ax.vlines(xs, 0, ys, color=RED, lw=1.8)
    ax.plot(xs, ys, "o", ms=4.4, color=RED)
    ax.set_xticks([-12, -6, 0, 6, 12])
    ax.set_xticklabels([r"$-12$", r"$-6$", "0", "6", "12"], fontsize=8.5)
    ax.set_yticks([-90, 0, 90]); ax.set_yticklabels([r"$-90$", "0", "90"], fontsize=8.5)
    for x, y in zip(xs, ys):
        if y > 0:
            ax.text(x + 0.6, y + 8, str(int(y)), fontsize=8.8, color=RED)
        else:
            ax.text(x + 0.6, y - 22, str(int(y)), fontsize=8.8, color=RED)
    ax.set_title("双边相位谱", fontsize=9.6, pad=5)

    fig.tight_layout()
    save(fig, "ch3-3.4-单边谱与双边谱的对照.png")


# ============ 图 C：直流分量隐藏对称性 ============
def fig_dc_hides_symmetry():
    T = 4.0

    def tri(t):
        """周期 4 的三角波：奇函数 + 奇谐函数，峰值 ±1（减掉直流后就是它）"""
        u = (t + T / 2) % T - T / 2
        return np.where(np.abs(u) <= 1.0, u, np.sign(u) * (2.0 - np.abs(u)))

    t = np.linspace(-3.0, 5.0, 4000)
    fig, axes = plt.subplots(1, 2, figsize=(8.2, 3.1), sharey=True)

    ax = axes[0]
    axes_arrows(ax, r"$t$", r"$f(t)$", (-3.7, 5.6), (-1.55, 1.70))
    ax.plot(t, tri(t) + 0.5, color=BLUE, lw=1.8)
    ax.axhline(0.5, color=GRAY, lw=0.9, ls=(0, (5, 4)))
    ax.set_xticks([-2, 0, 2, 4]); ax.set_xticklabels([r"$-2$", "0", "2", "4"], fontsize=8.5)
    ax.set_yticks([-1, 0, 0.5, 1])
    ax.set_yticklabels([r"$-1$", "0", r"$\frac{1}{2}$", "1"], fontsize=8.5)
    ax.text(-3.55, 1.10, "看上去既非奇也非偶", fontsize=8.6, color=BLUE)
    ax.set_title("原信号", fontsize=9.8, pad=5)

    ax = axes[1]
    axes_arrows(ax, r"$t$", "", (-3.7, 5.6), (-1.55, 1.70))
    ax.plot(t, tri(t), color=RED, lw=1.8)
    ax.set_xticks([-2, 0, 2, 4]); ax.set_xticklabels([r"$-2$", "0", "2", "4"], fontsize=8.5)
    ax.text(-3.55, 1.10, "奇函数 + 奇谐函数", fontsize=8.6, color=RED)
    ax.set_title("减去直流 $\\frac{1}{2}$ 之后", fontsize=9.8, pad=5)

    fig.tight_layout()
    save(fig, "ch3-3.7-直流分量隐藏对称性.png")


if __name__ == "__main__":
    fig_uni_vs_bi()
    fig_dc_hides_symmetry()
