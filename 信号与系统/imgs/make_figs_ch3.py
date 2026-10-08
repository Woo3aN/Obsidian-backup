# -*- coding: utf-8 -*-
"""信号与系统 第三章 配图生成脚本（可重跑，输出到本文件所在目录）

配图约定：
  - 文件名 ch3-{节}-{中文描述}.png，与库内 `<课程>/imgs/` 约定一致
  - 中文必须显式设字体；上下标一律用 mathtext（Unicode 下标字形 Microsoft YaHei 没有）
  - 配色统一：主信号蓝 #1f6fd0 / 变换后红 #d62728 / 辅灰 #999999 / 标注绿 #2e9e5b

重跑：把本文件放 imgs/ 目录下直接执行，5 张图原地重新生成。
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
    """画成带箭头的数学坐标轴（比默认方框更像教材）。"""
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
        ax.set_ylabel(ylabel, fontsize=9)


def save(fig, name):
    p = os.path.join(OUT, name)
    fig.savefig(p, dpi=190, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("saved", name, os.path.getsize(p) // 1024, "KB")


# ============ 图 1：方波的有限项逼近 + 吉布斯现象 ============
def fig_gibbs():
    def para(x, N):
        y = np.zeros_like(x)
        for n in range(1, 2 * N + 1, 2):
            y += 4 / np.pi * ((-1) ** ((n - 1) // 2)) * np.sin(n * x) / n
        return y

    fig, axs = plt.subplots(1, 4, figsize=(13.6, 3.5))
    for k, N in enumerate([1, 2, 5, 25]):
        ax = axs[k]
        t = np.linspace(-1.5, 2.5, 9000)
        sq = np.where(np.sin(t) >= 0, 1.0, -1.0)          # 理想方波（周期 2π）
        ax.plot(t, sq, color=GRAY, lw=1.3, ls="--", zorder=1)
        ax.plot(t, para(t, N), color=RED if k == 3 else BLUE, lw=1.8, zorder=2)
        axes_arrows(ax, r"$\omega_1 t$", r"$f(t)$" if k == 0 else "",
                    (-1.75, 2.75), (-1.45, 1.45))
        ax.set_yticks([-1, 0, 1])
        ax.set_xticks([0, 1, 2])
        ax.set_xticklabels(["0", r"$\pi$", r"$2\pi$"], fontsize=8)
        ax.tick_params(labelsize=8)
        ax.set_title(f"取前 {N} 项", fontsize=9.2)
        ax.legend(handles=[plt.Line2D([], [], color=GRAY, lw=1.3, ls="--"),
                           plt.Line2D([], [], color=RED if k == 3 else BLUE, lw=1.8)],
                  labels=["理想方波", "有限项叠加"], fontsize=6.8,
                  loc="lower center", bbox_to_anchor=(0.5, -0.03),
                  frameon=False, handlelength=1.3, ncol=2,
                  columnspacing=0.9, labelspacing=0.2, borderpad=0.1)
    axs[3].annotate("跳变处振荡过冲\n——吉布斯现象", xy=(1.02, 1.15),
                    xytext=(1.35, 0.30), fontsize=7.6, color=GREEN,
                    ha="left",
                    arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.0))
    fig.tight_layout()
    save(fig, "ch3-3.6-方波的有限项逼近与吉布斯现象.png")


# ============ 图 2：单边幅度谱 / 相位谱 ============
def fig_spectrum():
    fig, axs = plt.subplots(2, 1, figsize=(7.2, 5.0), sharex=True)

    w = np.linspace(0.001, 6.4, 3000)
    env = np.abs(np.sinc(w / np.pi))          # Sa 形状包络
    ws = np.arange(1, 7) * 1.0
    cs = np.abs(np.sinc(ws / np.pi))

    ax = axs[0]
    ax.plot(w, env, color="#333", lw=1.0, ls=":")
    ax.vlines(ws, 0, cs, color=BLUE, lw=2.2)
    ax.plot(ws, cs, "o", color=BLUE, ms=3.4)
    ax.annotate("包络线", xy=(5.35, float(np.abs(np.sinc(5.35 / np.pi)))),
                xytext=(4.5, 0.55), fontsize=8.2, color="#333",
                arrowprops=dict(arrowstyle="-|>", color="#333", lw=0.9))
    ax.annotate("谱线", xy=(2.0, float(np.abs(np.sinc(2.0 / np.pi)))),
                xytext=(1.8, 0.62), fontsize=8.2, color=BLUE,
                arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=0.9))
    ax.annotate(r"$c_0$", xy=(0, 1.0), xytext=(-0.42, 1.02), fontsize=8.5)
    ax.annotate(r"$c_1$", xy=(1.0, cs[0]), xytext=(0.62, cs[0] - 0.13), fontsize=8.5)
    ax.annotate(r"$c_2$", xy=(2.0, cs[1]), xytext=(2.1, cs[1] + 0.03), fontsize=8.5)
    ax.annotate(r"$c_3$", xy=(3.0, cs[2]), xytext=(2.72, cs[2] + 0.06), fontsize=8.5)
    axes_arrows(ax, "", r"$c_n$", (-1.05, 7.0), (-0.08, 1.18))
    ax.set_yticks([0, 0.5, 1])
    ax.tick_params(labelsize=8)
    ax.set_title("单边幅度谱（各频率分量幅度 $c_n$）", fontsize=9.5, pad=6)

    ax = axs[1]
    ph = np.where(np.arange(1, 7) % 2 == 0, -np.pi, 0.0)
    ax.vlines(ws, 0, ph, color=RED, lw=2.2)
    ax.plot(ws, ph, "o", color=RED, ms=3.4)
    ax.axhline(-np.pi, color="#333", lw=1.0, ls=":")
    ax.set_yticks([-np.pi, 0])
    ax.set_yticklabels([r"$-\pi$", "0"])
    axes_arrows(ax, r"$\omega$", r"$\varphi_n$", (-1.05, 7.0), (-3.9, 1.4))
    ax.set_xticks([0, 1, 2, 3, 4, 5, 6])
    ax.set_xticklabels(["0", r"$\omega_1$", r"$2\omega_1$", r"$3\omega_1$",
                        r"$4\omega_1$", r"$5\omega_1$", r"$6\omega_1$"])
    ax.tick_params(labelsize=8)
    ax.set_title("单边相位谱（各频率分量相位 $\\varphi_n$）", fontsize=9.5, pad=6)
    fig.tight_layout()
    save(fig, "ch3-3.4-单边幅度谱与相位谱.png")


# ============ 图 3：双边频谱（幅度谱 + 相位谱）============
def fig_double_spectrum():
    """双边频谱 = 双边幅度谱（非负、偶对称）+ 双边相位谱（奇对称）。

    坑记牢：幅度谱的谱线**必须非负**，且**必须落在包络线上**。
    第一版把包络画成 |Sa|（全在轴上方）、谱线却用带符号的 Sa，
    结果 |n| >= 4 处谱线朝下、包络朝上，两者对不上 —— 这是错的。
    """
    wn = np.arange(-6, 7) * 1.0
    wnz = wn[wn != 0]
    A = np.abs(np.sinc(wnz / np.pi))            # |F_n| = ½c_n（示意：偶、非负）
    A0 = 1.0
    A1 = float(np.abs(np.sinc(1.0 / np.pi)))    # |F_±1|
    w = np.linspace(-6.6, 6.6, 9000)
    env = np.abs(np.sinc(w / np.pi))            # 包络：穿过所有谱线顶点（含直流）

    fig, axs = plt.subplots(2, 1, figsize=(8.0, 5.9), sharex=True)

    # (a) 双边幅度谱
    ax = axs[0]
    ax.plot(w, env, color="#333", lw=1.1, ls=":")
    ax.vlines(wnz, 0, A, color=BLUE, lw=2.0)
    ax.vlines(0, 0, A0, color=BLUE, lw=2.6)
    ax.plot(wnz, A, "o", color=BLUE, ms=3.2)
    ax.plot([0], [A0], "o", color=BLUE, ms=3.8)
    ax.text(0.40, 1.01, r"$F_0=c_0$", fontsize=9.2)
    ax.annotate(r"$\frac{1}{2}c_1$", xy=(1.0, A1), xytext=(1.30, A1 + 0.07),
                fontsize=9.2, arrowprops=dict(arrowstyle="-", color="#888", lw=0.8))
    ax.annotate(r"$\frac{1}{2}c_1$", xy=(-1.0, A1), xytext=(-2.30, A1 + 0.07),
                fontsize=9.2, arrowprops=dict(arrowstyle="-", color="#888", lw=0.8))
    ax.annotate("包络线", xy=(3.9, float(np.abs(np.sinc(3.9 / np.pi)))),
                xytext=(4.85, 0.42), fontsize=8.6, color="#333",
                arrowprops=dict(arrowstyle="-|>", color="#333", lw=0.9))
    ax.annotate(r"左右同高：$|F_{-n}|=|F_n|=\frac{1}{2}c_n$（偶函数）",
                xy=(-2.0, 0.30), xytext=(-6.6, 0.68), fontsize=8.6, color=GREEN,
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.0))
    axes_arrows(ax, "", r"$|F_n|$", (-7.3, 7.5), (-0.05, 1.22))
    ax.set_yticks([0, 0.5, 1])
    ax.tick_params(labelsize=8)
    ax.set_title("(a) 双边幅度谱：谱线全部非负，左右一样高", fontsize=9.8, pad=6)

    # (b) 双边相位谱
    ax = axs[1]
    ph = np.where(wnz > 0, -np.pi / 2, np.pi / 2)
    ax.axhline(np.pi / 2, color="#333", lw=0.9, ls=":")
    ax.axhline(-np.pi / 2, color="#333", lw=0.9, ls=":")
    ax.vlines(wnz, 0, ph, color=RED, lw=2.0)
    ax.plot(wnz, ph, "o", color=RED, ms=3.2)
    ax.text(6.30, np.pi / 2 + 0.18, r"$+\frac{\pi}{2}$", fontsize=9.2,
            va="bottom", ha="left")
    ax.text(6.30, -np.pi / 2 - 0.18, r"$-\frac{\pi}{2}$", fontsize=9.2,
            va="top", ha="left")
    ax.annotate(r"左右反号：$\varphi_{-n}=-\varphi_n$（奇函数）",
                xy=(-1.6, np.pi / 2), xytext=(-6.6, np.pi / 2 + 0.34),
                fontsize=8.6, color=GREEN,
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.0))
    axes_arrows(ax, r"$\omega$", r"$\varphi_n$", (-7.3, 7.5), (-2.40, 2.40))
    ax.set_xlabel(r"$\omega$", fontsize=9, loc="right")
    ax.yaxis.set_label_coords(-0.045, 0.62)
    ax.set_yticks([-np.pi / 2, 0, np.pi / 2])
    ax.set_yticklabels([])
    ax.tick_params(labelsize=8)

    xt = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
    xl = [r"$-6\omega_1$", r"$-5\omega_1$", r"$-4\omega_1$", r"$-3\omega_1$",
          r"$-2\omega_1$", r"$-\omega_1$", "0", r"$\omega_1$", r"$2\omega_1$",
          r"$3\omega_1$", r"$4\omega_1$", r"$5\omega_1$", r"$6\omega_1$"]
    ax.set_xticks(xt)
    ax.set_xticklabels(xl, fontsize=7.6)

    fig.tight_layout()
    save(fig, "ch3-3.4-双边频谱.png")


# ============ 图 4：周期矩形脉冲及其频谱 ============
def fig_rect_pulse_spectrum():
    fig = plt.figure(figsize=(13.0, 3.6))
    gs = fig.add_gridspec(1, 3, width_ratios=[1.0, 1.5, 1.3], wspace=0.30)

    # (a) 时域
    ax = fig.add_subplot(gs[0, 0])
    T, tau, E = 2.0, 0.8, 1.0
    for k in range(-2, 4):
        x0 = k * T - tau / 2
        ax.plot([x0, x0, x0 + tau, x0 + tau], [0, E, E, 0], color=BLUE, lw=1.9)
    ax.plot([-2.9, 5.4], [0, 0], color="#555", lw=1.0)
    ax.annotate("", xy=(5.4, 0), xytext=(-2.9, 0),
                arrowprops=dict(arrowstyle="-|>", color="#555", lw=1.0))
    ax.annotate("", xy=(-2.5, 1.35), xytext=(-2.5, -0.22),
                arrowprops=dict(arrowstyle="-|>", color="#555", lw=1.0))
    ax.annotate("", xy=(0.42, 0.55), xytext=(-0.42, 0.55),
                arrowprops=dict(arrowstyle="<|-|>", color=GREEN, lw=1.1))
    ax.text(0.0, 0.60, r"$\tau$", fontsize=10, color=GREEN, ha="center")
    ax.annotate("", xy=(T, -0.16), xytext=(0, -0.16),
                arrowprops=dict(arrowstyle="<|-|>", color=RED, lw=1.1))
    ax.text(T / 2, -0.30, r"$T$", fontsize=10, color=RED, ha="center")
    ax.text(tau / 2 + 0.14, E + 0.02, r"$E$", fontsize=10)
    ax.text(2.6, 0.05, r"$\cdots\ \cdots$", fontsize=11)
    ax.set_xlim(-3.0, 5.5)
    ax.set_ylim(-0.42, 1.42)
    ax.axis("off")
    ax.set_title("(a) 周期矩形脉冲（周期 $T$，脉宽 $\\tau$，幅度 $E$）", fontsize=9.3)

    # (b) 包络线 + 等间隔谱线
    ax = fig.add_subplot(gs[0, 1])
    tau1, T1, E1 = 0.8, 2.0, 1.0
    w1 = 2 * np.pi / T1
    env_h = 2 * E1 * tau1 / T1
    w = np.linspace(-13.0, 13.0, 9000)
    env = env_h * np.abs(np.sinc(w * tau1 / (2 * np.pi)))
    wn = np.arange(-13, 14) * w1
    wn = wn[np.abs(wn) <= 13.0]
    Fn = env_h * np.sinc(wn * tau1 / (2 * np.pi))
    ax.plot(w, env, color="#333", lw=1.0, ls=":", label="包络线")
    ax.vlines(wn, 0, Fn, color=BLUE, lw=1.5)
    ax.vlines(0, 0, env_h, color=BLUE, lw=2.2)
    for m in (1, 2, 3):
        xp = 2 * np.pi * m / tau1
        if xp <= 13.0:
            ax.plot([xp], [0], "v", color=GREEN, ms=3.8)
            ax.plot([-xp], [0], "v", color=GREEN, ms=3.8)
    ax.annotate(r"过零点：$\frac{2\pi}{\tau},\frac{4\pi}{\tau},\frac{6\pi}{\tau}\cdots$",
                xy=(2 * np.pi / tau1, 0.02), xytext=(-12.7, 0.62),
                fontsize=8.0, color=GREEN,
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=0.95))
    ax.annotate(r"谱线：在 $\omega_1,2\omega_1,3\omega_1\cdots$ 处取值",
                xy=(3 * w1, env_h * float(np.sinc(3 * w1 * tau1 / (2 * np.pi)))),
                xytext=(3.0, 0.56), fontsize=8.0, color=BLUE,
                arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=0.95))
    ax.set_yticks([0, env_h])
    ax.set_yticklabels(["0", r"$\frac{2E\tau}{T}$"], fontsize=8.5)
    ax.set_xticks([0, w1, -w1, 2 * w1, -2 * w1])
    ax.set_xticklabels(["0", r"$\omega_1$", r"$-\omega_1$", r"$2\omega_1$", r"$-2\omega_1$"],
                       fontsize=8)
    ax.legend(fontsize=8, loc="upper right", frameon=False, handlelength=1.5)
    axes_arrows(ax, r"$\omega$", r"$F_n$", (-14.2, 14.8), (-0.30, 0.95))
    ax.set_title("(b) 它的频谱：包络线 + 等间隔谱线", fontsize=9.3)

    # (c) 脉宽与包络宽度
    ax = fig.add_subplot(gs[0, 2])
    for tau2, c, lab in [(0.4, RED, r"窄脉冲 $\tau'=\tau/2$"),
                         (0.8, BLUE, r"原脉冲 $\tau$")]:
        ww = np.linspace(-13.0, 13.0, 9000)
        e2 = np.abs(np.sinc(ww * tau2 / (2 * np.pi)))
        ax.plot(ww, e2, color=c, lw=1.7, label=lab)
        z = 2 * np.pi / tau2
        if z <= 13.0:
            ax.axvline(z, color=c, lw=0.8, ls=":", alpha=0.75)
            ax.text(z + 0.25, 0.06,
                    r"$\frac{2\pi}{\tau'}$" if c == RED else r"$\frac{2\pi}{\tau}$",
                    fontsize=8.5, color=c)
    ax.legend(fontsize=8, loc="upper right", frameon=False, handlelength=1.5)
    axes_arrows(ax, r"$\omega$", "归一化包络", (-14.2, 14.8), (-0.12, 1.18))
    ax.set_yticks([0, 1])
    ax.set_title("(c) 脉宽越窄，包络越宽\n（时宽 × 带宽 ∝ 常数）", fontsize=9.3)
    ax.tick_params(labelsize=8)

    save(fig, "ch3-3.8-周期矩形脉冲及其频谱.png")


# ============ 图 5：周期信号功率的帕塞瓦尔关系 ============
def fig_parseval():
    fig, ax = plt.subplots(figsize=(7.4, 3.4))
    ws = np.arange(0, 7) * 1.0
    cs = np.abs(np.sinc(ws / np.pi))
    p = np.array([cs[0] ** 2] + [0.5 * c ** 2 for c in cs[1:]])
    ax.bar(ws + 0.42, p, width=0.34, color=BLUE, label=r"各次谐波功率 $\frac{1}{2}c_n^2$")
    ax.bar(ws, cs ** 2, width=0.34, color=GRAY, alpha=0.75,
           label=r"幅度平方 $c_n^2$（仅作对照）")
    ax.bar([0], [1.0], width=0.34, color=RED, label=r"直流功率 $c_0^2$")
    ax.annotate("总平均功率 $P=\\overline{f^2(t)}$\n= 各分量功率之和",
                xy=(3.4, 0.10), xytext=(3.3, 0.72), fontsize=8.6, color=GREEN,
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.0))
    ax.set_xticks(ws + 0.2)
    ax.set_xticklabels(["0", r"$\omega_1$", r"$2\omega_1$", r"$3\omega_1$",
                        r"$4\omega_1$", r"$5\omega_1$", r"$6\omega_1$"], fontsize=8)
    ax.set_xlabel(r"$\omega$", fontsize=9)
    ax.set_ylabel("功率", fontsize=9)
    ax.legend(fontsize=8, loc="upper right", frameon=False, handlelength=1.4)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(labelsize=8)
    fig.tight_layout()
    save(fig, "ch3-3.4-周期信号功率的帕塞瓦尔关系.png")


if __name__ == "__main__":
    fig_gibbs()
    fig_spectrum()
    fig_double_spectrum()
    fig_rect_pulse_spectrum()
    fig_parseval()
    print("ALL DONE")
