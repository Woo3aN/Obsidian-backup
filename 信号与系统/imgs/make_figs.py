# -*- coding: utf-8 -*-
"""信号与系统 第一章配图生成脚本（统一风格重画）"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["mathtext.fontset"] = "stix"

OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)

BLUE = "#1f6fd0"
RED = "#d62728"
GREEN = "#2e9e5b"
GREY = "#999999"


def axis(ax, xlim, ylim, xlabel="t", ylabel=None, xat=None, yat=0, fs=8.5):
    """十字坐标轴（带箭头）。xat = x 轴的 y 值；yat = y 轴的 x 值"""
    if xat is None:
        xat = xlim[0]
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis("off")
    ax.annotate("", xy=(xlim[1], xat), xytext=(xlim[0], xat),
                arrowprops=dict(arrowstyle="-|>", color="k", lw=1.0,
                                mutation_scale=11, shrinkA=0, shrinkB=0), zorder=1)
    ax.annotate("", xy=(yat, ylim[1]), xytext=(yat, ylim[0]),
                arrowprops=dict(arrowstyle="-|>", color="k", lw=1.0,
                                mutation_scale=11, shrinkA=0, shrinkB=0), zorder=1)
    if xlabel:
        ax.text(xlim[1] * 0.995, xat, " " + xlabel, ha="right", va="bottom", fontsize=fs + 1)
    if ylabel:
        ax.text(yat, ylim[1], ylabel, ha="left", va="bottom", fontsize=fs + 1)


def ticks(ax, xs=None, ys=None, xat=0, yat=0, fs=8, dx=0.045, dy=0.05):
    """在坐标轴上打刻度与数字"""
    xr = ax.get_xlim()[1] - ax.get_xlim()[0]
    yr = ax.get_ylim()[1] - ax.get_ylim()[0]
    if xs is not None:
        for v in xs:
            ax.plot([v, v], [xat - yr * 0.035, xat + yr * 0.035], color="k", lw=0.9, zorder=2)
            lab = str(v).replace("-", "\u2212")
            ax.text(v, xat - yr * dy, lab, ha="center", va="top", fontsize=fs)
    if ys is not None:
        for v in ys:
            ax.plot([yat - xr * 0.022, yat + xr * 0.022], [v, v], color="k", lw=0.9, zorder=2)
            if v != 0:
                ax.text(yat - xr * dx * 0.7, v, str(v).replace("-", "\u2212"),
                        ha="right", va="center", fontsize=fs)


def impulse(ax, x0, h, color=BLUE, label=None, lw=1.4, fs=8):
    """冲激箭头"""
    ax.annotate("", xy=(x0, h), xytext=(x0, 0),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                mutation_scale=13, shrinkA=0, shrinkB=0), zorder=5)
    if label:
        ax.text(x0, h, label, ha="center", va="bottom", fontsize=fs, color=color)


def save(fig, name, pad=0.12):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=190, bbox_inches="tight", pad_inches=pad,
                facecolor="white", edgecolor="none")
    plt.close(fig)
    print("  ok ->", name)


# ---------------------------------------------------------------- 1.2 时域与频域
def fig_time_freq():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.6, 2.3))
    t = np.linspace(0, 2, 2000)
    sig = 0.55 * np.sin(2 * np.pi * 1 * t) + 0.42 * np.sin(2 * np.pi * 3 * t + 1.0)
    axis(ax1, (-0.05, 2.15), (-1.15, 1.35), xlabel="t", ylabel="振幅", xat=0)
    ax1.plot(t, sig, color=BLUE, lw=1.5)
    ax1.set_title("时域：信号波形", fontsize=9.5, pad=2)

    axis(ax2, (-0.3, 4.0), (-0.15, 1.25), xlabel="f", ylabel="振幅", xat=0)
    for f, a in [(1, 0.55), (3, 0.42)]:
        ax2.annotate("", xy=(f, a), xytext=(f, 0),
                     arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.6,
                                     mutation_scale=13, shrinkA=0, shrinkB=0))
        ax2.text(f, a + 0.04, f"$f_{{{1 if f==1 else 2}}}$", ha="center",
                 va="bottom", fontsize=8.5, color=RED)
        ax2.plot([f - 0.1, f + 0.1], [a, a], color=RED, lw=1.0)
    ax2.set_title("频域：谱线", fontsize=9.5, pad=2)
    ticks(ax2, xs=[1, 3], xat=0, dy=0.07)
    save(fig, "ch1-1.2-时域与频域.png")


# ---------------------------------------------------------------- 1.2 四类信号
def fig_four_types():
    fig, axes = plt.subplots(2, 2, figsize=(6.4, 4.0))
    tt = np.linspace(0, 3.6, 600)

    ax = axes[0][0]
    axis(ax, (-0.15, 4.0), (-0.25, 1.35), xlabel="t", xat=0)
    ax.plot(tt, np.exp(-(tt - 0.4) ** 2 / 1.2) + 0.12 * tt, color=BLUE, lw=1.6)
    ticks(ax, xs=[1, 2, 3], xat=0)
    ax.set_title("模拟信号：时间连续、幅值连续", fontsize=8.8, pad=3)

    ax = axes[0][1]
    axis(ax, (-0.15, 4.0), (-0.25, 1.35), xlabel="n", xat=0)
    xs = np.arange(0, 3.7, 0.35)
    ax.plot(tt, np.exp(-(tt - 0.4) ** 2 / 1.2) + 0.12 * tt, color=GREY, lw=1.1, ls="--")
    ax.vlines(xs, 0, np.exp(-(xs - 0.4) ** 2 / 1.2) + 0.12 * xs, color=BLUE, lw=1.6)
    ax.set_title("抽样信号：时间离散、幅值连续", fontsize=8.8, pad=3)

    ax = axes[1][0]
    axis(ax, (-0.15, 4.0), (-0.25, 1.35), xlabel="t", xat=0)
    q = np.floor((np.exp(-(tt - 0.4) ** 2 / 1.2) + 0.12 * tt) * 4) / 4
    ax.step(tt, q, where="post", color=BLUE, lw=1.5)
    ax.set_title("量化信号：时间连续、幅值离散", fontsize=8.8, pad=3)

    ax = axes[1][1]
    axis(ax, (-0.15, 4.0), (-0.25, 1.35), xlabel="n", xat=0)
    xs = np.arange(0, 3.7, 0.35)
    q = np.floor((np.exp(-(xs - 0.4) ** 2 / 1.2) + 0.12 * xs) * 4) / 4
    ax.plot(tt, np.exp(-(tt - 0.4) ** 2 / 1.2) + 0.12 * tt, color=GREY, lw=1.1, ls="--")
    ax.vlines(xs, 0, q, color=BLUE, lw=1.6)
    ax.plot(xs, q, ls="none", marker="o", ms=2.6, color=BLUE)
    ax.set_title("数字信号：时间离散、幅值离散", fontsize=8.8, pad=3)

    fig.tight_layout(h_pad=1.6)
    save(fig, "ch1-1.2-四类信号.png")


# ---------------------------------------------------------------- 1.2 实指数 / 复指数
def fig_exp_signals():
    fig, axes = plt.subplots(2, 3, figsize=(8.4, 4.2))
    t = np.linspace(-1.6, 1.6, 800)

    for k, (a, title) in enumerate([(1.4, "$a>0$：随时间增长"),
                                    (-1.4, "$a<0$：随时间衰减"),
                                    (0.0, "$a=0$：直流信号")]):
        ax = axes[0][k]
        axis(ax, (-1.75, 1.75), (-0.3, 3.4), xlabel="t", xat=0)
        if a == 0:
            y = np.ones_like(t)
        elif a > 0:
            y = np.exp(a * t)
        else:
            y = np.exp(a * t)
        ax.plot(t, y, color=BLUE, lw=1.6)
        ax.axhline(1, color=GREY, lw=0.7, ls=":")
        ticks(ax, xs=[-1, 1], ys=[1], xat=0, yat=0)
        ax.set_title(title, fontsize=8.8, pad=3)

    for k, (sg, title) in enumerate([(0.55, r"$\sigma>0$：增幅振荡"),
                                     (-0.75, r"$\sigma<0$：衰减振荡"),
                                     (0.0, r"$\sigma=0$：等幅振荡")]):
        ax = axes[1][k]
        axis(ax, (-0.15, 2.3), (-2.3, 2.3), xlabel="t", xat=0)
        tt = np.linspace(0, 2.2, 1200)
        env = np.exp(sg * tt)
        ax.plot(tt, env, color=GREY, lw=0.9, ls="--")
        ax.plot(tt, -env, color=GREY, lw=0.9, ls="--")
        ax.plot(tt, env * np.cos(2 * np.pi * 1.15 * tt), color=RED, lw=1.5)
        ax.set_title(title, fontsize=8.8, pad=3)
    for k in range(3):
        axes[1][k].set_title(axes[1][k].get_title() + "  ($Ke^{st}$)", fontsize=8.5)

    fig.suptitle("典型连续时间信号：实指数 $Ke^{at}$（上）与复指数 $Ke^{st}$（下）",
                 fontsize=10, y=0.99)
    fig.tight_layout(h_pad=1.8, rect=(0, 0, 1, 0.94))
    save(fig, "ch1-1.2-典型连续时间信号.png")


# ---------------------------------------------------------------- 1.2 Sa(t)
def fig_sa():
    fig, ax = plt.subplots(figsize=(5.6, 2.4))
    t = np.linspace(-11, 11, 4000)
    sa = np.sinc(t / np.pi)          # sin(t)/t
    ax.axis("off")
    ax.set_xlim(-11.6, 11.6)
    ax.set_ylim(-0.42, 1.22)
    ax.annotate("", xy=(11.6, 0), xytext=(-11.6, 0),
                arrowprops=dict(arrowstyle="-|>", color="k", lw=1.0,
                                mutation_scale=11, shrinkA=0, shrinkB=0))
    ax.annotate("", xy=(0, 1.22), xytext=(0, -0.42),
                arrowprops=dict(arrowstyle="-|>", color="k", lw=1.0,
                                mutation_scale=11, shrinkA=0, shrinkB=0))
    ax.plot(t, sa, color=BLUE, lw=1.6)
    for n in [-3, -2, -1, 1, 2, 3]:
        ax.plot([n * np.pi, n * np.pi], [-0.035, 0.035], color="k", lw=0.9)
    ax.axhline(0, color="k", lw=1.0, xmin=0.0, xmax=1.0)
    ax.text(np.pi * 3, -0.075, r"$3\pi$", ha="center", va="top", fontsize=8)
    ax.text(np.pi, -0.075, r"$\pi$", ha="center", va="top", fontsize=8)
    ax.text(-np.pi, -0.075, r"$-\pi$", ha="center", va="top", fontsize=8)
    ax.text(0.12, 1.0, r"$\mathrm{Sa}(0)=1$", ha="left", va="center", fontsize=9)
    ax.plot([0], [1], marker="o", ms=3.4, color=BLUE)
    ax.plot([-np.pi, np.pi], [0, 0], marker="o", ms=3.4, color=BLUE)
    ax.text(11.5, 0.03, "$t$", ha="right", va="bottom", fontsize=10)
    ax.text(0.15, 1.2, r"$\mathrm{Sa}(t)=\dfrac{\sin t}{t}$", ha="left",
            va="top", fontsize=10.5)
    save(fig, "ch1-1.2-抽样信号Sa.png")


# ---------------------------------------------------------------- 1.3 三种基本运算
def fig_ops():
    fig, axes = plt.subplots(3, 2, figsize=(6.6, 6.0))
    t = np.linspace(-3.2, 3.2, 2000)

    def base(tt):
        y = np.zeros_like(tt)
        y += np.where((tt >= -2) & (tt < -1), 1.0, 0)
        y += np.where((tt >= -1) & (tt < 1), 1 + 0.5 * (tt[((tt >= -1) & (tt < 1))] + 1)
                      if False else 0, 0)
        return y

    def f(tt):
        y = np.zeros_like(tt)
        m1 = (tt >= -2) & (tt < -1)
        y[m1] = 1.0
        m2 = (tt >= -1) & (tt <= 1)
        y[m2] = 1 + 0.5 * (tt[m2] + 1)
        return y

    # 行1：移位
    for k, (shift, ttl) in enumerate([(0, "$f(t)$"), (0, "")]):
        pass
    ax = axes[0][0]
    axis(ax, (-3.3, 3.3), (-0.3, 2.5), xlabel="t", xat=0)
    ax.plot(t, f(t), color=BLUE, lw=1.7)
    ticks(ax, xs=[-2, -1, 1, 2], ys=[1, 2], xat=0)
    ax.set_title("$f(t)$", fontsize=9.5, pad=3)

    ax = axes[0][1]
    axis(ax, (-3.3, 3.3), (-0.3, 2.5), xlabel="t", xat=0)
    ax.plot(t, f(t - 1.5), color=RED, lw=1.7)
    ticks(ax, xs=[-2, -1, 1, 2], ys=[1, 2], xat=0)
    ax.annotate("", xy=(2.5, 2.05), xytext=(0.9, 2.05),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.6, mutation_scale=12))
    ax.text(1.7, 2.15, "右移 $t_0$", fontsize=8.5, color=GREEN, ha="center")
    ax.set_title("(1) 移位：$f(t-t_0)$", fontsize=9.5, pad=3)

    # 行2：反褶
    ax = axes[1][0]
    axis(ax, (-3.3, 3.3), (-0.3, 2.5), xlabel="t", xat=0)
    ax.plot(t, f(t), color=BLUE, lw=1.7)
    ticks(ax, xs=[-2, -1, 1, 2], ys=[1, 2], xat=0)
    ax.set_title("$f(t)$", fontsize=9.5, pad=3)

    ax = axes[1][1]
    axis(ax, (-3.3, 3.3), (-0.3, 2.5), xlabel="t", xat=0)
    ax.plot(t, f(-t), color=RED, lw=1.7)
    ticks(ax, xs=[-2, -1, 1, 2], ys=[1, 2], xat=0)
    ax.axvline(0, color=GREEN, lw=1.1, ls="--", ymax=0.95, zorder=0)
    ax.set_title("(2) 反褶：$f(-t)$（关于纵轴镜像）", fontsize=9.5, pad=3)

    # 行3：尺度
    ax = axes[2][0]
    axis(ax, (-3.3, 3.3), (-0.3, 2.5), xlabel="t", xat=0)
    ax.plot(t, f(t), color=BLUE, lw=1.7)
    ticks(ax, xs=[-2, -1, 1, 2], ys=[1, 2], xat=0)
    ax.set_title("$f(t)$", fontsize=9.5, pad=3)

    ax = axes[2][1]
    axis(ax, (-3.3, 3.3), (-0.3, 2.5), xlabel="t", xat=0)
    ax.plot(t, f(2 * t), color=RED, lw=1.7)
    ax.plot(t, f(t / 2), color=GREEN, lw=1.4, ls="--")
    ticks(ax, xs=[-2, -1, 1, 2], ys=[1, 2], xat=0)
    ax.legend(["$f(2t)$ 压缩", "$f(t/2)$ 扩展"], fontsize=7.6,
              loc="upper left", frameon=False, handlelength=1.6)
    ax.set_title("(3) 尺度变换：$f(at)$", fontsize=9.5, pad=3)

    fig.tight_layout(h_pad=1.0, w_pad=1.4)
    save(fig, "ch1-1.3-三种基本运算.png")


# ---------------------------------------------------------------- 1.3 f(-2t+1)
def fig_combined():
    def f(tt):
        y = np.zeros_like(tt)
        m1 = (tt >= -2) & (tt < 0)
        y[m1] = 2.0
        m2 = (tt >= 0) & (tt <= 2)
        y[m2] = 2 + 0.5 * tt[m2]
        return y

    fig, axes = plt.subplots(1, 4, figsize=(11.0, 3.0))
    specs = [("$f(t)$", lambda tt: f(tt), BLUE, "原信号"),
             ("$f(-t)$", lambda tt: f(-tt), RED, "(1) 反折"),
             ("$f(-2t)$", lambda tt: f(-2 * tt), RED, "(2) 尺度变换"),
             ("$f(-2t\\!+\\!1)$", lambda tt: f(-2 * tt + 1), RED, "(3) 时移")]
    t = np.linspace(-3.4, 3.4, 4000)
    for ax, (ttl, g, c, sub) in zip(axes, specs):
        axis(ax, (-3.4, 3.4), (-0.5, 3.6), xlabel="t", xat=0)
        ax.plot(t, g(t), color=c, lw=1.8)
        ticks(ax, xs=[-2, -1, 1, 2], ys=[2, 3], xat=0, fs=7.5)
        ax.axhline(2, color=GREY, lw=0.6, ls=":", zorder=0)
        ax.axhline(3, color=GREY, lw=0.6, ls=":", zorder=0)
        ax.set_title(ttl, fontsize=10, pad=2)
        ax.text(0.5, -0.22, sub, transform=ax.transAxes, ha="center",
                va="top", fontsize=8.2, color="#555555")
    axes[3].annotate("", xy=(2.45, 0.62), xytext=(1.55, 0.62),
                     arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.5,
                                     mutation_scale=11))
    axes[3].text(2.0, 0.74, "右移 1/2", fontsize=8.5, color=GREEN, ha="center")
    fig.tight_layout(w_pad=0.9)
    save(fig, "ch1-1.3-综合变换.png")


# ---------------------------------------------------------------- 1.3 微分与积分
def fig_diff_int():
    fig, axes = plt.subplots(2, 2, figsize=(7.4, 4.4))

    # 上：微分
    ax = axes[0][0]
    axis(ax, (-0.6, 6.0), (-0.6, 3.0), xlabel="t", xat=0)
    t = np.linspace(0, 5.0, 1200)
    y = np.piecewise(t, [t < 1, (t >= 1) & (t < 4), t >= 4],
                     [lambda v: 2 * v, 2.0, lambda v: 2 * (5 - v)])
    ax.plot(t, y, color=BLUE, lw=1.7)
    ax.plot([5.0, 5.7], [0, 0], color=BLUE, lw=1.7)
    ticks(ax, xs=[1, 4, 5], ys=[2], xat=0)
    ax.set_title("$f(t)$：含突变与平直段", fontsize=9, pad=3)

    ax = axes[0][1]
    axis(ax, (-0.6, 6.0), (-3.0, 3.0), xlabel="t", xat=0)
    ax.plot([0, 1], [2, 2], color=RED, lw=2.0)
    ax.plot([1, 4], [0, 0], color=RED, lw=2.0)
    ax.plot([4, 5], [-2, -2], color=RED, lw=2.0)
    ax.plot([0, 0], [0, 2], color=RED, lw=1.4, ls=":")
    ax.plot([5, 5], [-2, 0], color=RED, lw=1.4, ls=":")
    ticks(ax, xs=[1, 4, 5], ys=[2, -2], xat=0)
    ax.set_title(r"$\dfrac{df(t)}{dt}$：只留下变化段", fontsize=9, pad=3)

    # 下：积分
    ax = axes[1][0]
    axis(ax, (-1.2, 3.4), (-0.5, 1.9), xlabel="t", xat=0)
    ax.plot([-1.1, 0, 0, 3.2], [0, 0, 1, 1], color=BLUE, lw=1.7)
    ticks(ax, xs=[1, 2, 3], ys=[1], xat=0)
    ax.annotate("跳变", xy=(0.02, 0.55), xytext=(0.75, 1.15),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.2, mutation_scale=10),
                fontsize=8.5, color=GREEN, ha="center")
    ax.set_title("$f(t)$：$t=0$ 处突变", fontsize=9, pad=3)

    ax = axes[1][1]
    axis(ax, (-1.2, 3.4), (-0.5, 1.9), xlabel="t", xat=0)
    t = np.linspace(-1.1, 3.2, 900)
    y = np.piecewise(t, [t < 0, (t >= 0) & (t <= 1), t > 1],
                     [0.0, lambda v: v, 1.0])
    ax.plot(t, y, color=RED, lw=1.7)
    ax.axhline(1, color=GREY, lw=0.8, ls=":")
    ticks(ax, xs=[1, 2, 3], ys=[1], xat=0)
    ax.set_title(r"$\int_{-\infty}^{t} f(\tau)\,d\tau$：突变被平滑", fontsize=9, pad=3)

    fig.tight_layout(h_pad=1.6, w_pad=1.8)
    save(fig, "ch1-1.3-微分与积分.png")


# ---------------------------------------------------------------- 1.4 斜变信号
def fig_ramp():
    fig, axes = plt.subplots(1, 3, figsize=(8.2, 2.3))
    t = np.linspace(-1.2, 3.2, 1200)

    ax = axes[0]
    axis(ax, (-1.3, 3.4), (-0.35, 2.6), xlabel="t", xat=0)
    ax.plot(t, np.where(t >= 0, t, 0), color=BLUE, lw=1.7)
    ticks(ax, xs=[1, 2, 3], xat=0)
    ax.set_title("单位斜变 $R(t)$", fontsize=9, pad=3)

    ax = axes[1]
    axis(ax, (-1.3, 3.4), (-0.35, 2.6), xlabel="t", xat=0)
    ax.plot(t, np.where(t < 2, t, 2.0) * (t >= 0), color=BLUE, lw=1.7)
    ax.plot([2, 2], [0, 2], color=GREY, lw=0.8, ls=":")
    ticks(ax, xs=[1, 2, 3], ys=[2], xat=0)
    ax.text(2.1, -0.28, "$T$", fontsize=8.5)
    ax.text(0.15, 2.2, "$k$", fontsize=8.5)
    ax.set_title("截平的斜变 $f_1(t)$", fontsize=9, pad=3)

    ax = axes[2]
    axis(ax, (-1.3, 3.4), (-0.35, 2.6), xlabel="t", xat=0)
    ax.plot(t, np.where((t >= 0) & (t <= 2), t, 0), color=BLUE, lw=1.7)
    ax.plot([2, 2], [0, 2], color=GREY, lw=0.8, ls=":")
    ticks(ax, xs=[1, 2, 3], ys=[2], xat=0)
    ax.text(2.1, -0.28, "$T$", fontsize=8.5)
    ax.set_title("三角形脉冲 $f_2(t)$", fontsize=9, pad=3)

    fig.tight_layout(w_pad=0.7)
    save(fig, "ch1-1.4-斜变信号.png")


# ---------------------------------------------------------------- 1.4 阶跃与矩形脉冲
def fig_step_rect():
    fig, axes = plt.subplots(1, 3, figsize=(8.2, 2.3))
    t = np.linspace(-1.3, 3.2, 1200)

    ax = axes[0]
    axis(ax, (-1.3, 3.4), (-0.4, 1.7), xlabel="t", xat=0)
    ax.plot([-1.2, 0, 0, 3.2], [0, 0, 1, 1], color=BLUE, lw=1.7)
    ax.plot([0], [0.5], marker="o", ms=3.6, mfc="white", mec=BLUE, mew=1.4)
    ax.plot([0], [0], marker="o", ms=3.2, color=BLUE)
    ticks(ax, ys=[1], xat=0)
    ax.text(0.12, 0.42, "$1/2$", fontsize=8)
    ax.set_title("单位阶跃 $u(t)$", fontsize=9, pad=3)

    ax = axes[1]
    axis(ax, (-1.3, 3.4), (-0.4, 1.7), xlabel="t", xat=0)
    ax.plot([-1.2, 0, 0, 2, 2, 3.2], [0, 0, 1, 1, 0, 0], color=BLUE, lw=1.7)
    ticks(ax, xs=[2], ys=[1], xat=0)
    ax.text(1.0, -0.33, "$T$", fontsize=8.5)
    ax.set_title("矩形脉冲 $R_T(t)=u(t)-u(t-T)$", fontsize=9, pad=3)

    ax = axes[2]
    axis(ax, (-1.3, 3.4), (-0.4, 1.7), xlabel="t", xat=0)
    ax.plot([-1.2, 0.6, 0.6, 2.6, 2.6, 3.2], [0, 0, 1, 1, 0, 0], color=BLUE, lw=1.7)
    ticks(ax, ys=[1], xat=0)
    ax.text(1.6, -0.33, "$T$", fontsize=8.5, ha="center")
    ax.annotate("", xy=(0.6, 0.45), xytext=(2.6, 0.45),
                arrowprops=dict(arrowstyle="<|-|>", color=GREEN, lw=1.0, mutation_scale=9))
    ax.text(1.6, 0.52, "宽度", fontsize=8, color=GREEN, ha="center")
    ax.set_title("对称矩形脉冲 $G_T(t)$", fontsize=9, pad=3)

    fig.tight_layout(w_pad=0.7)
    save(fig, "ch1-1.4-阶跃与矩形脉冲.png")


# ---------------------------------------------------------------- 1.4 接入特性
def fig_access():
    fig, axes = plt.subplots(1, 3, figsize=(8.4, 2.3))

    ax = axes[0]
    t = np.linspace(-1.4, 6.6, 2000)
    axis(ax, (-1.5, 7.0), (-1.5, 1.6), xlabel="t", xat=0)
    ax.plot(t, np.where(t >= 0, np.sin(t), 0), color=BLUE, lw=1.7)
    ticks(ax, ys=[1, -1], xat=0)
    ax.text(2.6, 1.15, r"$f_1(t)=\sin t\cdot u(t)$", fontsize=8.5, ha="center")
    ax.set_title("正弦信号接入", fontsize=9, pad=3)

    ax = axes[1]
    t = np.linspace(-0.6, 4.2, 1200)
    axis(ax, (-0.7, 4.5), (-0.35, 1.5), xlabel="t", xat=0)
    y = np.where(t >= 0, np.exp(-t) * ((t <= 2.6).astype(float)), 0)
    ax.plot(t, y, color=BLUE, lw=1.7)
    ax.plot([2.6, 2.6], [0, np.exp(-2.6)], color=GREY, lw=0.8, ls=":")
    ticks(ax, ys=[1], xat=0)
    ax.text(2.75, -0.26, "$t_0$", fontsize=8.5)
    ax.text(2.0, 1.15, r"$f_2(t)=e^{-t}[u(t)-u(t-t_0)]$", fontsize=8.0, ha="center")
    ax.set_title("指数脉冲", fontsize=9, pad=3)

    ax = axes[2]
    t = np.linspace(-0.6, 5.6, 3000)
    axis(ax, (-0.7, 5.9), (-0.65, 1.85), xlabel="t", xat=0)
    T, tau, E = 1.5, 0.55, 1.0
    y = np.zeros_like(t)
    for n in range(4):
        y += E * (((t >= n * T) & (t < n * T + tau)).astype(float))
    ax.plot(t, y, color=BLUE, lw=1.7)
    ax.plot([5.5, 5.9], [1, 1], color=BLUE, lw=1.7, ls="--")
    ticks(ax, ys=[1], xat=0)
    ax.annotate("", xy=(0, -0.26), xytext=(0.55, -0.26),
                arrowprops=dict(arrowstyle="<|-|>", color=GREEN, lw=0.9, mutation_scale=8))
    ax.text(0.28, -0.45, "$\\tau$", fontsize=8.5, color=GREEN, ha="center")
    ax.annotate("", xy=(0, 1.34), xytext=(1.5, 1.34),
                arrowprops=dict(arrowstyle="<|-|>", color=GREEN, lw=0.9, mutation_scale=8))
    ax.text(0.75, 1.42, "$T$", fontsize=8.5, color=GREEN, ha="center")
    ax.set_title("周期脉冲串 $f_3(t)$", fontsize=9, pad=3)

    fig.tight_layout(w_pad=0.8)
    save(fig, "ch1-1.4-阶跃的接入特性.png")


# ---------------------------------------------------------------- 1.4 冲激的广义极限
def fig_dirac_limit():
    fig, axes = plt.subplots(1, 3, figsize=(8.2, 2.3))
    for k, tau in enumerate([1.0, 0.45]):
        ax = axes[k]
        axis(ax, (-1.5, 1.5), (-0.4, 3.2), xlabel="t", xat=0)
        h = 1.0 / tau
        ax.plot([-tau / 2, -tau / 2, tau / 2, tau / 2, tau / 2],
                [0, h, h, 0, 0], color=BLUE, lw=1.7)
        ax.fill_between([-tau / 2, tau / 2], 0, h, color=BLUE, alpha=0.13)
        ax.axhline(1 / tau, color=GREY, lw=0.8, ls=":")
        ax.text(-1.42, 1 / tau + 0.1, f"$1/\\tau={1/tau:.2f}$", fontsize=8)
        ax.text(0, -0.32, f"宽度 $\\tau={tau}$", fontsize=8.5, ha="center")
        ax.set_title(f"$\\tau={tau}$，面积恒为 1", fontsize=9, pad=3)
        if k == 0:
            ax.annotate("", xy=(1.32, 1.6), xytext=(0.75, 1.6),
                        arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.4,
                                        mutation_scale=11))
            ax.text(1.05, 1.7, "$\\tau\\to 0$", fontsize=8.5, color=GREEN, ha="center")

    ax = axes[2]
    axis(ax, (-1.5, 1.5), (-0.4, 3.2), xlabel="t", xat=0)
    impulse(ax, 0, 2.6, color=RED, label="$1$")
    ax.text(0.12, 1.3, "$\\delta(t)$", fontsize=10, color=RED)
    ax.text(0.62, 0.35, "冲激强度", fontsize=8, color=RED)
    ax.set_title("$\\tau\\to 0$ 的极限：单位冲激", fontsize=9, pad=3)

    fig.tight_layout(w_pad=0.8)
    save(fig, "ch1-1.4-冲激的广义极限定义.png")


# ---------------------------------------------------------------- 1.4 冲激偶推导
def fig_doublet():
    fig, axes = plt.subplots(1, 3, figsize=(8.8, 2.9))

    # (a) 三角脉冲
    ax = axes[0]
    t = np.linspace(-1.4, 1.4, 1200)
    tau, h = 1.0, 1.0
    y = np.where(np.abs(t) <= tau, 1 - np.abs(t) / tau, 0) * h
    axis(ax, (-1.5, 1.5), (-0.4, 1.9), xlabel="t", xat=0)
    ax.plot(t, y, color=BLUE, lw=1.7)
    ax.fill_between(t, 0, y, color=BLUE, alpha=0.12)
    ticks(ax, ys=[1], xat=0)
    ax.text(-1.5, 1.42, "底宽 $2\\tau$，高 $1/\\tau$", fontsize=8.2)
    ax.set_title("(a) 三角形脉冲 $s(t)$", fontsize=9, pad=3)

    # (b) 求导
    ax = axes[1]
    axis(ax, (-1.5, 1.5), (-2.0, 2.0), xlabel="t", xat=0)
    ax.plot([-tau, -tau], [0, h / tau], color=RED, lw=2.0)
    ax.plot([-tau, 0], [h / tau, h / tau], color=RED, lw=2.0)
    ax.plot([0, 0], [h / tau, -h / tau], color=RED, lw=2.0)
    ax.plot([0, tau], [-h / tau, -h / tau], color=RED, lw=2.0)
    ax.plot([tau, tau], [-h / tau, 0], color=RED, lw=2.0)
    ticks(ax, ys=[1, -1], xat=0)
    ax.set_title("(b) 求导 $\\dfrac{ds(t)}{dt}$", fontsize=9, pad=3)

    # (c) 取极限 → 冲激偶
    ax = axes[2]
    axis(ax, (-1.6, 1.6), (-2.0, 2.0), xlabel="t", xat=0)
    impulse(ax, 0, 1.6, color=RED)
    impulse(ax, 0, -1.6, color=RED)
    ax.text(0.16, 1.05, "$\\delta'(t)$", fontsize=11, color=RED)
    ax.text(0.16, -1.05, "$\\int\\delta'(t)\\,dt=0$", fontsize=8.5, color="#555555")
    ax.set_title("(c) $\\tau\\to 0$ 的极限：冲激偶（doublet）", fontsize=9, pad=3)

    for ax in axes:
        ax.set_ylim(-2.0, 2.1)
    fig.tight_layout(w_pad=0.8)
    save(fig, "ch1-1.4-冲激偶的推导.png")


# ---------------------------------------------------------------- 1.5 直流与交流
def fig_dc_ac():
    fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.3))
    t = np.linspace(-1.4, 3.4, 1500)

    ax = axes[0]
    axis(ax, (-1.5, 3.7), (-1.8, 2.0), xlabel="t", xat=0)
    f = 1 + 0.75 * np.sin(2 * np.pi * 0.55 * t)
    ax.plot(t, f, color=BLUE, lw=1.6)
    ax.axhline(1, color=GREEN, lw=1.4)
    ax.text(0.15, 1.12, "$f_D$：直流分量（平均值）", fontsize=8.2, color=GREEN)
    ticks(ax, ys=[1], xat=0)
    ax.set_title("$f(t)=f_D+f_A(t)$", fontsize=9.5, pad=3)

    ax = axes[1]
    axis(ax, (-1.5, 3.7), (-1.8, 2.0), xlabel="t", xat=0)
    ax.plot(t, 0.75 * np.sin(2 * np.pi * 0.55 * t), color=RED, lw=1.6)
    ax.text(0.15, 1.5, "$f_A(t)$：交流分量", fontsize=8.2, color=RED)
    ticks(ax, xat=0)
    ax.set_title("去掉平均值后的部分", fontsize=9.5, pad=3)

    fig.tight_layout(w_pad=1.2)
    save(fig, "ch1-1.5-直流与交流分量.png")


# ---------------------------------------------------------------- 1.5 偶分量与奇分量
def fig_even_odd():
    fig, axes = plt.subplots(1, 3, figsize=(8.4, 2.3))
    t = np.linspace(-1.6, 1.6, 2000)
    ax = axes[0]
    axis(ax, (-1.7, 1.7), (-1.6, 2.6), xlabel="t", xat=0)
    ax.plot(t, np.where((t >= -1) & (t <= 1), 1 + t, 0), color=BLUE, lw=1.8)
    ticks(ax, xs=[-1, 1], ys=[1, 2], xat=0)
    ax.set_title("$f(t)$,　$-1\\leq t\\leq 1$", fontsize=9.5, pad=3)

    ax = axes[1]
    axis(ax, (-1.7, 1.7), (-1.6, 2.6), xlabel="t", xat=0)
    ax.plot([-1, 1], [1, 1], color=RED, lw=2.2)
    ticks(ax, xs=[-1, 1], ys=[1], xat=0)
    ax.text(-1.55, 2.3, "$f_e(t)=\\frac{1}{2}[f(t)+f(-t)]$", fontsize=8.5)
    ax.text(0, -1.15, "偶分量：关于纵轴对称", fontsize=8.2, color=RED, ha="center")
    ax.set_title("$f_e(t)$", fontsize=9.5, pad=3)

    ax = axes[2]
    axis(ax, (-1.7, 1.7), (-1.6, 2.6), xlabel="t", xat=0)
    ax.plot(t, np.where(np.abs(t) <= 1, t, 0), color=RED, lw=2.0)
    ticks(ax, xs=[-1, 1], ys=[1, -1], xat=0)
    ax.text(-1.55, 2.3, "$f_o(t)=\\frac{1}{2}[f(t)-f(-t)]$", fontsize=8.5)
    ax.text(0, -1.15, "奇分量：关于原点对称", fontsize=8.2, color=RED, ha="center")
    ax.set_title("$f_o(t)$", fontsize=9.5, pad=3)

    fig.tight_layout(w_pad=0.8)
    save(fig, "ch1-1.5-偶分量与奇分量.png")


if __name__ == "__main__":
    print("输出目录:", OUT)
    fig_time_freq()
    fig_four_types()
    fig_exp_signals()
    fig_sa()
    fig_ops()
    fig_combined()
    fig_diff_int()
    fig_ramp()
    fig_step_rect()
    fig_access()
    fig_dirac_limit()
    fig_doublet()
    fig_dc_ac()
    fig_even_odd()
    print("全部完成")
