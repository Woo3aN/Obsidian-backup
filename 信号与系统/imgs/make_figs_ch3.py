# ======== 来源: make_figs_ch3.py ========

# -*- coding: utf-8 -*-
"""第三章 傅里叶变换 配图（第6次课）—— 输出到 信号与系统/imgs/"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["mathtext.fontset"] = "cm"

OUT = r"D:\我的坚果云\计算机\信号与系统\imgs"
os.makedirs(OUT, exist_ok=True)

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
    ax.spines["left"].set_color("#444")
    ax.spines["bottom"].set_color("#444")
    ax.annotate("", xy=(xlim[1], 0), xytext=(xlim[0], 0),
                arrowprops=dict(arrowstyle="-|>", color="#444", lw=1.1))
    ax.annotate("", xy=(0, ylim[1]), xytext=(0, ylim[0]),
                arrowprops=dict(arrowstyle="-|>", color="#444", lw=1.1))
    ax.set_xlabel(xlabel, fontsize=9)
    ax.set_ylabel(ylabel, fontsize=9)


def save(fig, name):
    p = os.path.join(OUT, name)
    fig.savefig(p, dpi=190, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("saved", name, os.path.getsize(p) // 1024, "KB")


# ---------- 图 1：周期方波的有限项逼近 + 吉布斯现象 ----------
def fig_gibbs():
    fig, axs = plt.subplots(1, 4, figsize=(13.2, 3.1))
    t = np.linspace(-1.6, 1.6, 4000)

    def para(x, N):
        y = 4 / np.pi * np.sin(x)
        for n in range(3, 2 * N, 2):
            y += 4 / np.pi * ((-1) ** ((n - 1) // 2)) * np.sin(n * x) / n
        return y

    for k, N in enumerate([1, 2, 3, 8]):
        ax = axs[k]
        lim = 1.35 if k < 3 else 1.35
        # 理想方波
        sq = np.where(np.sin(t) >= 0, 1.0, -1.0)
        ax.plot(t, sq, color=GRAY, lw=1.3, ls="--", label="理想方波")
        ax.plot(t, para(t, N), color=RED if k == 3 else BLUE, lw=1.7,
                label=f"取 {N} 项")
        axes_arrows(ax, r"$\omega_1 t$", r"$f(t)$" if k == 0 else "",
                    (-1.75, 1.75), (-lim, lim))
        ax.set_yticks([-1, 0, 1])
        ax.tick_params(labelsize=7.5)
        ax.legend(fontsize=7.2, loc="upper right", frameon=False,
                  handlelength=1.4, labelspacing=0.2, borderpad=0.1)
        if k == 3:
            ax.annotate("跳变处振荡\n（吉布斯现象）", xy=(0.0, 1.18),
                        xytext=(-1.6, 0.62), fontsize=7.2, color=GREEN,
                        arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.0))
    fig.tight_layout()
    save(fig, "ch3-2.2-方波的有限项逼近与吉布斯现象.png")


# ---------- 图 2：单边幅度谱 / 相位谱（一般周期信号） ----------
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
    ax.annotate("包络线", xy=(5.35, np.abs(np.sinc(5.35 / np.pi))),
                xytext=(4.5, 0.55), fontsize=8.2, color="#333",
                arrowprops=dict(arrowstyle="-|>", color="#333", lw=0.9))
    ax.annotate("谱线", xy=(2.0, np.abs(np.sinc(2.0 / np.pi))),
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
    save(fig, "ch3-2.2-单边幅度谱与相位谱.png")


# ---------- 图 3：双边频谱（复数频谱） ----------
def fig_double_spectrum():
    fig, ax = plt.subplots(figsize=(7.6, 3.6))
    w = np.linspace(-6.4, 6.4, 6000)
    env = 0.5 * np.abs(np.sinc(w / np.pi))
    wn = np.arange(-6, 7) * 1.0
    wn = wn[wn != 0]
    Fn = 0.5 * np.abs(np.sinc(wn / np.pi)) * np.where(wn > 0, 1, 1)
    # 用双边的正负交替符号体现相位
    Fn_signed = np.sinc(wn / np.pi) * 0.5

    ax.plot(w, env, color="#333", lw=1.0, ls=":")
    ax.vlines(wn, 0, Fn_signed, color=BLUE, lw=2.0)
    ax.plot(wn, Fn_signed, "o", color=BLUE, ms=3.0)
    ax.vlines(0, 0, 1.0, color=BLUE, lw=2.6)
    ax.plot([0], [1.0], "o", color=BLUE, ms=3.6)
    ax.annotate(r"$F_0=c_0$", xy=(0, 1.0), xytext=(0.32, 1.03), fontsize=8.6)
    ax.annotate(r"$\frac{1}{2}c_1$", xy=(1.0, 0.5), xytext=(1.25, 0.58), fontsize=8.6)
    ax.annotate(r"$-\frac{1}{2}c_1$", xy=(-1.0, -0.5), xytext=(-3.5, -0.72), fontsize=8.6)
    ax.annotate("正、负频率成对出现\n（负频率只是数学处理）",
                xy=(-2.0, -0.14), xytext=(-6.2, 0.62), fontsize=8.0, color=GREEN,
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.0))
    axes_arrows(ax, r"$\omega$", r"$F_n$", (-7.2, 7.4), (-1.05, 1.22))
    ax.set_xticks([-4, -3, -2, -1, 0, 1, 2, 3, 4])
    ax.set_xticklabels([r"$-4\omega_1$", r"$-3\omega_1$", r"$-2\omega_1$", r"$-\omega_1$",
                        "0", r"$\omega_1$", r"$2\omega_1$", r"$3\omega_1$", r"$4\omega_1$"])
    ax.set_yticks([0, 0.5, 1])
    ax.tick_params(labelsize=8)
    fig.tight_layout()
    save(fig, "ch3-2.2-双边频谱.png")


# ---------- 图 4：周期矩形脉冲 + 其频谱 ----------
def fig_rect_pulse_spectrum():
    fig = plt.figure(figsize=(12.6, 3.4))
    gs = fig.add_gridspec(1, 3, width_ratios=[1.05, 1.35, 1.35], wspace=0.32)

    # (a) 时域波形
    ax = fig.add_subplot(gs[0, 0])
    T, tau, E = 2.0, 0.9, 1.0
    for k in range(-2, 3):
        x0 = k * T - tau / 2
        ax.plot([x0, x0, x0 + tau, x0 + tau], [0, E, E, 0], color=BLUE, lw=1.9)
    ax.plot([-4.6, 4.6], [0, 0], color="#444", lw=1.1)
    ax.annotate("", xy=(4.6, 0), xytext=(-4.6, 0),
                arrowprops=dict(arrowstyle="-|>", color="#444", lw=1.1))
    ax.annotate("", xy=(0, 1.35), xytext=(0, -0.2),
                arrowprops=dict(arrowstyle="-|>", color="#444", lw=1.1))
    ax.annotate("", xy=(0.45, E), xytext=(-tau / 2, E),
                arrowprops=dict(arrowstyle="<|-|>", color=GREEN, lw=1.0))
    ax.text(0.02, E + 0.06, r"$\tau$", fontsize=9, color=GREEN, ha="center")
    ax.annotate("", xy=(T - tau / 2, 0.55), xytext=(-tau / 2, 0.55),
                arrowprops=dict(arrowstyle="<|-|>", color=RED, lw=1.0))
    ax.text(T / 2, 0.60, r"$T$", fontsize=9, color=RED, ha="center")
    ax.text(-tau / 2 - 0.22, E + 0.03, r"$E$", fontsize=9)
    ax.text(2.05, 0.06, r"$\cdots$", fontsize=11)
    ax.text(-2.05, 0.06, r"$\cdots$", fontsize=11)
    ax.set_xlim(-4.7, 4.7)
    ax.set_ylim(-0.22, 1.45)
    ax.axis("off")
    ax.set_title("(a) 周期矩形脉冲", fontsize=9.5)

    # (b) 包络 + 谱线
    ax = fig.add_subplot(gs[0, 1])
    tau1, T1 = 0.9, 2.0
    w = np.linspace(-14.6, 14.6, 8000)
    env = (2 * E * tau1 / T1) * np.abs(np.sinc(w * tau1 / (2 * np.pi)))
    wn = np.arange(-14, 15) * (2 * np.pi / T1)
    wn = wn[np.abs(wn) <= 14.6]
    Fn = (2 * E * tau1 / T1) * np.sinc(wn * tau1 / (2 * np.pi))
    ax.plot(w, env, color="#333", lw=1.0, ls=":")
    ax.vlines(wn, 0, Fn, color=BLUE, lw=1.4)
    ax.vlines(0, 0, 2 * E * tau1 / T1, color=BLUE, lw=1.9)
    # 过零点标注
    for m, c in zip([1, 2, 3], [GREEN, GRAY, GREEN]):
        xp = 2 * np.pi * m / tau1
        ax.plot([xp], [0], "v", color=c, ms=3.6)
    ax.text(2 * np.pi / tau1 + 0.25, 0.11, r"$\frac{2\pi}{\tau}$",
            fontsize=8.2, color=GREEN)
    ax.text(4 * np.pi / tau1 + 0.05, 0.12, r"$\frac{4\pi}{\tau}$",
            fontsize=8.2, color=GRAY)
    ax.text(6 * np.pi / tau1 - 1.15, 0.12, r"$\frac{6\pi}{\tau}$",
            fontsize=8.2, color=GREEN)
    ax.annotate("过零点都是 $\\frac{2m\\pi}{\\tau}$", xy=(2 * np.pi / tau1, 0.03),
                xytext=(-14.2, 0.62), fontsize=8.2, color=GREEN,
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=0.9))
    ax.plot([], [], color="#333", lw=1.0, ls=":", label="包络线")
    ax.legend(fontsize=8, loc="upper right", frameon=False, handlelength=1.5)
    axes_arrows(ax, r"$\omega$", r"$F_n$", (-15.6, 15.6), (-0.30, 0.92))
    ax.set_yticks([0, 2 * E * tau1 / T1])
    ax.set_yticklabels(["0", r"$\frac{2E\tau}{T}$"])
    ax.set_xticks([0, 2 * np.pi / T1, -2 * np.pi / T1, 4 * np.pi / T1, -4 * np.pi / T1])
    ax.set_xticklabels(["0", r"$\omega_1$", r"$-\omega_1$", r"$2\omega_1$", r"$-2\omega_1$"],
                       fontsize=8)
    ax.tick_params(labelsize=8)
    ax.set_title("(b) 幅度谱：谱线落在包络线上（$\\tau<2\\pi/\\omega_1$ 情形）", fontsize=9.5)

    # (c) 脉宽变窄 → 包络展宽
    ax = fig.add_subplot(gs[0, 2])
    for tau2, c, lab in [(0.45, RED, r"脉宽减半 $\tau/2$"), (0.9, BLUE, r"原脉宽 $\tau$")]:
        w2 = np.linspace(-14.6, 14.6, 8000)
        e2 = (2 * E * tau2 / T1) * np.abs(np.sinc(w2 * tau2 / (2 * np.pi)))
        ax.plot(w2, e2 / (2 * E * tau2 / T1), color=c, lw=1.6, label=lab)
        for m in range(1, 4):
            xp = 2 * np.pi * m / tau2
            if xp <= 14.6:
                ax.plot([xp], [0], "v", color=c, ms=3.2)
    ax.legend(fontsize=8, loc="upper right", frameon=False, handlelength=1.5)
    axes_arrows(ax, r"$\omega$", "归一化包络", (-15.6, 15.6), (-0.12, 1.16))
    ax.set_yticks([0, 1])
    ax.set_title("(c) 脉宽越窄，包络越宽（时宽带宽积为常数）", fontsize=9.5)
    ax.tick_params(labelsize=8)

    save(fig, "ch3-2.2-周期矩形脉冲及其频谱.png")


# ---------- 图 5：矩形脉冲的两种阶跃表示 ----------
def fig_gate_forms():
    fig, axs = plt.subplots(1, 3, figsize=(11.4, 2.9))
    tt = np.linspace(-2.2, 3.2, 2000)

    # (a) 相减
    ax = axs[0]
    y = ((tt >= 0) & (tt <= 1)).astype(float)
    ax.plot(tt, y, color=BLUE, lw=2.0)
    ax.plot([-2.2, 3.2], [0, 0], color="#444", lw=1.0)
    ax.text(0.5, 1.12, r"$u(t)-u(t-1)$", fontsize=9.5, ha="center", color=BLUE)
    ax.set_title("(a) 两个阶跃相减", fontsize=9.2)
    axes_arrows(ax, r"$t$", "", (-2.3, 3.3), (-0.22, 1.35))

    # (b) 相乘
    ax = axs[1]
    y = ((tt >= 0) & (tt <= 1)).astype(float)
    ax.plot(tt, y, color=RED, lw=2.0)
    ax.plot([-2.2, 3.2], [0, 0], color="#444", lw=1.0)
    ax.text(0.5, 1.12, r"$u(t)\cdot u(1-t)$", fontsize=9.5, ha="center", color=RED)
    ax.set_title("(b) 两个阶跃相乘", fontsize=9.2)
    axes_arrows(ax, r"$t$", "", (-2.3, 3.3), (-0.22, 1.35))

    # (c) 一般形式
    ax = axs[2]
    a, b = 1.0, 3.0
    y = ((tt >= a) & (tt <= b)).astype(float)
    ax.plot(tt, y, color=GREEN, lw=2.0)
    ax.plot([-2.2, 3.2], [0, 0], color="#444", lw=1.0)
    ax.text((a + b) / 2, 1.12, r"$u(\tau+a)\cdot u(b-\tau)$",
            fontsize=9.2, ha="center", color=GREEN)
    ax.annotate("", xy=(b, 0.5), xytext=(a, 0.5),
                arrowprops=dict(arrowstyle="<|-|>", color=GREEN, lw=1.0))
    ax.text((a + b) / 2, 0.56, r"$-a \sim b$", fontsize=8.5,
            ha="center", color=GREEN)
    ax.set_title("(c) 一般区间", fontsize=9.2)
    axes_arrows(ax, r"$t$", "", (-2.3, 3.3), (-0.22, 1.35))

    for ax in axs:
        ax.set_yticks([0, 1])
        ax.tick_params(labelsize=8)
    fig.tight_layout()
    save(fig, "ch3-2.2-矩形脉冲的两种阶跃表示.png")


# ---------- 图 6：周期信号功率的帕塞瓦尔关系 ----------
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
    save(fig, "ch3-2.2-周期信号功率的帕塞瓦尔关系.png")


fig_gibbs()
fig_spectrum()
fig_double_spectrum()
fig_rect_pulse_spectrum()
fig_gate_forms()
fig_parseval()
print("ALL DONE")


# ======== 来源: fix2.py ========

# -*- coding: utf-8 -*-
"""修正版 2：吉布斯现象 + 周期矩形脉冲频谱"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["mathtext.fontset"] = "cm"

OUT = r"D:\我的坚果云\计算机\信号与系统\imgs"
BLUE = "#1f6fd0"
RED = "#d62728"
GRAY = "#999999"
GREEN = "#2e9e5b"


def axes_arrows(ax, xlabel, xlim, ylim, ylabel=""):
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


# ================= 图 1：有限项逼近 + 吉布斯 =================
def fig_gibbs():
    N_PERIOD = 1
    def para(x, N):
        y = np.zeros_like(x)
        for n in range(1, 2 * N + 1, 2):
            y += 4 / np.pi * ((-1) ** ((n - 1) // 2)) * np.sin(n * x) / n
        return y

    fig, axs = plt.subplots(1, 4, figsize=(13.6, 3.5))
    for k, N in enumerate([1, 2, 5, 25]):
        ax = axs[k]
        t = np.linspace(-1.5 * N_PERIOD, 2.5 * N_PERIOD, 9000)
        # 理想方波：以 2π 为周期
        sq = np.where(np.sin(t) >= 0, 1.0, -1.0)
        ax.plot(t, sq, color=GRAY, lw=1.3, ls="--", zorder=1)
        ax.plot(t, para(t, N), color=RED if k == 3 else BLUE, lw=1.8, zorder=2)
        axes_arrows(ax, r"$\omega_1 t$", (-1.75, 2.75), (-1.45, 1.45),
                    ylabel=r"$f(t)$" if k == 0 else "")
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
    # 吉布斯标注放在第 4 图右侧空白
    axs[3].annotate("跳变处振荡过冲\n——吉布斯现象", xy=(1.02, 1.15),
                    xytext=(1.35, 0.30), fontsize=7.6, color=GREEN,
                    ha="left",
                    arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.0))
    fig.tight_layout()
    p = os.path.join(OUT, "ch3-2.2-方波的有限项逼近与吉布斯现象.png")
    fig.savefig(p, dpi=190, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("gibbs", os.path.getsize(p) // 1024, "KB")


# ================= 图 2：周期矩形脉冲及其频谱 =================
def fig_rect():
    fig = plt.figure(figsize=(13.0, 3.6))
    gs = fig.add_gridspec(1, 3, width_ratios=[1.0, 1.5, 1.3], wspace=0.30)

    # --- (a) 时域 ---
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
    ax.set_title("(a) 周期矩形脉冲（周期 $T$，脉宽 $\\tau$，幅度 $E$）",
                 fontsize=9.3)

    # --- (b) 图解法画频谱：先包络、再取离散点 ---
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
    # 过零点
    for m in (1, 2, 3):
        xp = 2 * np.pi * m / tau1
        if xp <= 13.0:
            ax.plot([xp], [0], "v", color=GREEN, ms=3.8)
            ax.plot([-xp], [0], "v", color=GREEN, ms=3.8)
    ax.annotate(r"过零点：$\frac{2\pi}{\tau},\frac{4\pi}{\tau},\frac{6\pi}{\tau}\cdots$",
                xy=(2 * np.pi / tau1, 0.02), xytext=(-12.7, 0.62),
                fontsize=8.0, color=GREEN,
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=0.95))
    ax.annotate("谱线：在 $\\omega_1,2\\omega_1,3\\omega_1\\cdots$ 处取值",
                xy=(3 * w1, env_h * np.sinc(3 * w1 * tau1 / (2 * np.pi))),
                xytext=(3.0, 0.56), fontsize=8.0, color=BLUE,
                arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=0.95))
    ax.set_yticks([0, env_h])
    ax.set_yticklabels(["0", r"$\frac{2E\tau}{T}$"], fontsize=8.5)
    ax.set_xticks([0, w1, -w1, 2 * w1, -2 * w1])
    ax.set_xticklabels(["0", r"$\omega_1$", r"$-\omega_1$", r"$2\omega_1$", r"$-2\omega_1$"],
                       fontsize=8)
    ax.legend(fontsize=8, loc="upper right", frameon=False, handlelength=1.5)
    axes_arrows(ax, r"$\omega$", (-14.2, 14.8), (-0.30, 0.95), ylabel=r"$F_n$")
    ax.set_title("(b) 它的频谱：包络线 + 等间隔谱线", fontsize=9.3)

    # --- (c) 脉宽与包络宽度的关系 ---
    ax = fig.add_subplot(gs[0, 2])
    for tau2, c, lab in [(0.4, RED, r"窄脉冲 $\tau'=\tau/2$"),
                         (0.8, BLUE, r"原脉冲 $\tau$")]:
        ww = np.linspace(-13.0, 13.0, 9000)
        e2 = np.abs(np.sinc(ww * tau2 / (2 * np.pi)))
        ax.plot(ww, e2, color=c, lw=1.7, label=lab)
        z = 2 * np.pi / tau2
        if z <= 13.0:
            ax.axvline(z, color=c, lw=0.8, ls=":", alpha=0.75)
            ax.text(z + 0.25, 0.06, r"$\frac{2\pi}{\tau'}$" if c == RED else r"$\frac{2\pi}{\tau}$",
                    fontsize=8.5, color=c)
    ax.legend(fontsize=8, loc="upper right", frameon=False, handlelength=1.5)
    axes_arrows(ax, r"$\omega$", (-14.2, 14.8), (-0.12, 1.18), ylabel="归一化包络")
    ax.set_yticks([0, 1])
    ax.set_title("(c) 脉宽越窄，包络越宽\n（时宽 × 带宽 ∝ 常数）", fontsize=9.3)
    ax.tick_params(labelsize=8)

    p = os.path.join(OUT, "ch3-2.2-周期矩形脉冲及其频谱.png")
    fig.savefig(p, dpi=190, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("rect", os.path.getsize(p) // 1024, "KB")


fig_gibbs()
fig_rect()
print("OK")
