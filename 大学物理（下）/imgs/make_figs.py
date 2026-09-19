# -*- coding: utf-8 -*-
"""画静电场这一章的分布曲线。

放到 imgs/ 下直接跑就会原地重新生成（OUT 取脚本所在目录）。
配色沿用库内约定：主 #1f6fd0 蓝、次 #d62728 红、辅助 #999999 灰、标注 #2e9e5b 绿。

  ch5-3.4-典型场强分布曲线.png    §5-3 四种对称性的 E–r
  ch5-4.4-球体的电势分布曲线.png  §5-4 球体 / 球面的 V–r
"""
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

OUT = os.path.dirname(os.path.abspath(__file__))
BLUE, RED, GRAY, GREEN = "#1f6fd0", "#d62728", "#999999", "#2e9e5b"
XPAD = 3.2          # r/R 画到 3.2

x1 = np.linspace(0, 1, 200)
x2 = np.linspace(1, XPAD, 400)


def axis_arrows(ax, xmax=XPAD, ymax=1.35, xt=r"$r/R$", yt=r"$E/E_R$", xtick="$R$"):
    ax.set_xlim(-0.08, xmax)
    ax.set_ylim(-0.06, ymax)
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    if xtick is None:
        ax.set_xticks([])
    else:
        ax.set_xticks([1])
        ax.set_xticklabels([xtick])
    ax.set_yticks([])
    ax.tick_params(length=0)
    ax.annotate("", xy=(xmax - 0.05, 0), xytext=(xmax - 0.24, 0),
                arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    ax.annotate("", xy=(0, ymax - 0.05), xytext=(0, ymax - 0.26),
                arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    ax.text(xmax - 0.30, -0.05, xt, color="k", ha="center", va="top")
    ax.text(0.06, ymax - 0.24, yt, color="k", ha="left", va="center")


# ==================== 图一：§5-3 典型 E–r 分布 ====================
fig, axes = plt.subplots(2, 2, figsize=(9.4, 7.0))

# ---------- (a) 均匀带电球面（球壳） ----------
ax = axes[0, 0]
ax.plot(x1, np.zeros_like(x1), color=BLUE, lw=2.4)
ax.plot(x2, 1 / x2 ** 2, color=BLUE, lw=2.4)
ax.plot([1, 1], [0, 1], color=BLUE, lw=2.4, ls=":")
ax.axvline(1, color=GRAY, ls="--", lw=1.0)
axis_arrows(ax)
ax.text(0.45, 0.17, "$E=0$\n$(r<R)$", color=BLUE, ha="center", fontsize=10)
ax.text(2.0, 0.44, r"$E=\dfrac{q}{4\pi\varepsilon_0 r^2}$", color=BLUE,
        ha="center", fontsize=10)
ax.set_title("(a) 均匀带电球面：$R$ 处跳变", fontsize=11.5, pad=10)

# ---------- (b) 均匀带电球体（实心） ----------
ax = axes[0, 1]
ax.plot(x1, x1, color=RED, lw=2.4)
ax.plot(x2, 1 / x2 ** 2, color=RED, lw=2.4)
ax.plot([1], [1], "o", color=RED, ms=5)
ax.axvline(1, color=GRAY, ls="--", lw=1.0)
axis_arrows(ax)
ax.text(0.45, 0.60, "$E\\propto r$", color=RED, ha="center", fontsize=10.5)
ax.text(2.0, 0.44, r"$E\propto 1/r^2$", color=RED, ha="center", fontsize=10.5)
ax.annotate("在 $r=R$ 处\n取最大值", xy=(1, 1), xytext=(1.8, 1.0),
            color=GREEN, fontsize=10, ha="left",
            arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.1))
ax.set_title("(b) 均匀带电球体：$R$ 处连续", fontsize=11.5, pad=10)

# ---------- (c) 无限长带电直线 ----------
ax = axes[1, 0]
xc = np.linspace(0.12, XPAD, 500)
ax.plot(xc, 1 / xc, color=BLUE, lw=2.4)
axis_arrows(ax, yt=r"$E/E_{r_0}$", ymax=3.4, xt=r"$r/r_0$", xtick="$r_0$")
ax.text(2.3, 1.55, r"$E=\dfrac{\lambda}{2\pi\varepsilon_0 r}$",
        color=BLUE, ha="center", fontsize=10)
ax.text(2.3, 0.78, r"$E\propto \dfrac{1}{r}$", color=BLUE, ha="center", fontsize=10)
ax.annotate("$r\\to 0$ 时 $E\\to\\infty$", xy=(0.5, 2.0), xytext=(1.35, 2.9),
            color=GREEN, fontsize=10, ha="left",
            arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.1))
ax.set_title("(c) 无限长带电直线", fontsize=11.5, pad=10)

# ---------- (d) 无限大带电平面 ----------
ax = axes[1, 1]
xe = np.linspace(0.1, XPAD, 200)
ax.plot(xe, np.ones_like(xe), color=BLUE, lw=2.4)
ax.plot(xe, np.full_like(xe, 2.0), color=GRAY, ls="--", lw=1.8)
axis_arrows(ax, yt=r"$E/E_{\rm plane}$", ymax=2.55,
            xt=r"$r$（离平面的距离）", xtick=None)
ax.text(1.55, 0.50, "单块平面：$E=\\dfrac{\\sigma}{2\\varepsilon_0}$\n与距离无关（匀强电场）",
        color=BLUE, ha="center", fontsize=10)
ax.text(1.55, 2.18, "两异号平面之间：$E=\\dfrac{\\sigma}{\\varepsilon_0}$",
        color=GRAY, ha="center", fontsize=10)
ax.text(2.9, 0.28, "两板外侧 $E=0$", color=GRAY, ha="center", fontsize=9.5)
ax.set_title("(d) 无限大带电平面", fontsize=11.5, pad=10)

fig.tight_layout(h_pad=2.8, w_pad=2.4)
fp = os.path.join(OUT, "ch5-3.4-典型场强分布曲线.png")
fig.savefig(fp, dpi=190, bbox_inches="tight", facecolor="white")
print("saved:", fp, os.path.getsize(fp) // 1024, "KB")

# ==================== 图二：§5-4 球体 / 球面的 V–r 分布 ====================
fig2, ax2 = plt.subplots(1, 2, figsize=(9.4, 3.9))

# ---------- (a) 均匀带电球体：球内 1.5V_R -> V_R，球外 1/r ----------
ax = ax2[0]
ax.plot(x1, (3 - x1 ** 2) / 2, color=RED, lw=2.4)
ax.plot(x2, 1 / x2, color=RED, lw=2.4)
ax.plot([1], [1], "o", color=RED, ms=5)
ax.axvline(1, color=GRAY, ls="--", lw=1.0)
ax.axhline(1.5, color=GREEN, ls=":", lw=1.2)
axis_arrows(ax, ymax=2.02, yt=r"$V/V_R$")
ax.text(0.55, 1.28, r"$V=\dfrac{q(3R^2-r^2)}{8\pi\varepsilon_0R^3}$", color=RED,
        ha="center", fontsize=9.5)
ax.text(2.1, 0.60, r"$V=\dfrac{q}{4\pi\varepsilon_0 r}$", color=RED, ha="center", fontsize=9.5)
ax.annotate("球心处电势最高\n$V_0=1.5\\,V_R$", xy=(0, 1.5), xytext=(0.34, 1.60),
            color=GREEN, fontsize=9.5, ha="left",
            arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.1))
ax.set_title("(a) 均匀带电球体", fontsize=11.5, pad=8)

# ---------- (b) 均匀带电球面：球内为常量 ----------
ax = ax2[1]
ax.plot(x1, np.ones_like(x1), color=BLUE, lw=2.4)
ax.plot(x2, 1 / x2, color=BLUE, lw=2.4)
ax.plot([1], [1], "o", color=BLUE, ms=5)
ax.axvline(1, color=GRAY, ls="--", lw=1.0)
axis_arrows(ax, ymax=2.02, yt=r"$V/V_R$")
ax.text(0.5, 1.18, "球内 $V$ 为常量\n$V=\\dfrac{q}{4\\pi\\varepsilon_0 R}$", color=BLUE,
        ha="center", fontsize=9.5)
ax.text(2.1, 0.60, r"$V=\dfrac{q}{4\pi\varepsilon_0 r}$", color=BLUE, ha="center", fontsize=9.5)
ax.set_title("(b) 均匀带电球面", fontsize=11.5, pad=8)

fig2.tight_layout(w_pad=2.6)
fp2 = os.path.join(OUT, "ch5-4.4-球体的电势分布曲线.png")
fig2.savefig(fp2, dpi=190, bbox_inches="tight", facecolor="white")
print("saved:", fp2, os.path.getsize(fp2) // 1024, "KB")
