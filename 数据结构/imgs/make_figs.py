# -*- coding: utf-8 -*-
"""生成《数据结构》第 3、4、5 章配图。

命名规则：ch{章}-{节}-{描述}.png，与笔记正文的 ![](imgs/xxx.png) 一一对应。
本脚本只负责"需要统一风格 / 合成对照图"的那几张；其余一律不画。

用法：python make_figs.py
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

OUT = os.path.dirname(os.path.abspath(__file__))

C_LINE = "#3c4a5a"
C_FILL = "#dce9f7"
C_FILL2 = "#fbeee0"
C_TOP = "#b03a2e"
C_BASE = "#23689b"
C_TEXT = "#22303c"
C_TXT2 = "#7a8899"
C_EMP = "#fafbfc"
C_GRN = "#2e8b57"


def _slot(ax, x, y, w, h, text="", fc="none", lw=1.2, fs=10.5):
    ax.add_patch(Rectangle((x, y), w, h, fc=fc, ec=C_LINE, lw=lw))
    if text:
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
                fontsize=fs, color=C_TEXT)


def _arrow(ax, p1, p2, color=C_LINE, lw=1.4, ms=11):
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=ms,
                                 color=color, lw=lw, shrinkA=0, shrinkB=0))


# ---------------------------------------------------------------- 图 1 顺序栈
def fig_seq_stack():
    fig, ax = plt.subplots(figsize=(7.4, 4.3), dpi=150)
    ax.set_xlim(0, 11.4)
    ax.set_ylim(0, 6)
    ax.axis("off")

    x0, w, h = 2.0, 2.4, 0.74
    n = 6
    for i in range(n):
        _slot(ax, x0, 0.45 + i * h, w, h, fc=C_EMP)
    for i, e in enumerate(["$a_1$", "$a_2$", "$a_3$"]):
        _slot(ax, x0, 0.45 + i * h, w, h, text=e, fc=C_FILL)

    _arrow(ax, (1.75, 0.82), (x0 + 0.02, 0.82), C_BASE)
    ax.text(x0 - 1.4, 0.82, "base", ha="left", va="center", fontsize=11,
            color=C_BASE, weight="bold")
    ax.text(x0 - 1.4, 0.40, "栈底（固定）", ha="left", va="center",
            fontsize=9, color=C_TXT2)

    y_top = 0.45 + 3 * h + h / 2
    _arrow(ax, (1.75, y_top), (x0 + 0.02, y_top), C_TOP)
    ax.text(x0 - 1.4, y_top + 0.30, "top", ha="left", va="center", fontsize=11,
            color=C_TOP, weight="bold")
    ax.text(x0 - 1.4, y_top - 0.16, "栈顶（随操作变化）", ha="left", va="center",
            fontsize=9, color=C_TXT2)

    ax.annotate("", xy=(x0 + w / 2, 0.45 + 5 * h), xytext=(x0 + w / 2, 0.45 + 3 * h),
                arrowprops=dict(arrowstyle="-|>", color=C_GRN, lw=1.6))
    ax.text(x0 + w / 2 + 0.15, 0.45 + 4.1 * h, "进栈 push", fontsize=10,
            color=C_GRN, va="center")
    ax.annotate("", xy=(x0 + w + 0.75, 0.45 + 2.5 * h),
                xytext=(x0 + w + 0.75, 0.45 + 0.6 * h),
                arrowprops=dict(arrowstyle="-|>", color="#a0522d", lw=1.6))
    ax.text(x0 + w + 0.92, 0.45 + 1.55 * h, "出栈 pop", fontsize=10,
            color="#a0522d", va="center")

    tx = 7.35
    ax.text(tx, 5.5, "约定：top 指向栈顶元素的下一个位置", fontsize=10.5,
            color=C_TEXT, weight="bold")
    ax.text(tx, 4.92, "即 top 所指单元是空的，写入后才上移", fontsize=9.5, color=C_TXT2)

    ax.text(tx, 4.30, "进栈", fontsize=10.5, color=C_GRN, weight="bold")
    ax.text(tx, 3.92, "①  将 e 写入 top 所指位置", fontsize=9.5, color=C_TEXT)
    ax.text(tx, 3.58, "②  top 上移一位（top++）", fontsize=9.5, color=C_TEXT)
    ax.text(tx + 0.35, 3.20, "*S.top++ = e;", fontsize=9.5, color=C_GRN,
            family="monospace")

    ax.text(tx, 2.55, "出栈", fontsize=10.5, color="#a0522d", weight="bold")
    ax.text(tx, 2.17, "①  top 下移一位（top--）", fontsize=9.5, color=C_TEXT)
    ax.text(tx, 1.83, "②  再取出该位置的元素", fontsize=9.5, color=C_TEXT)
    ax.text(tx + 0.35, 1.45, "e = *--S.top;", fontsize=9.5, color="#a0522d",
            family="monospace")

    ax.add_patch(Rectangle((tx - 0.2, 0.42), 3.95, 0.72, fc=C_FILL2,
                           ec="#d9b382", lw=1))
    ax.text(tx, 0.78, "空栈：top == base    栈满：top - base ≥ stacksize",
            fontsize=9.5, color=C_TEXT, va="center")

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "ch3-1-1-顺序栈与进出栈.png"),
                bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------ 图 2 栈的状态变化
def fig_stack_states():
    states = [
        ("空栈", []),
        ("$a$ 进栈", ["a"]),
        ("$b$、$c$ 进栈", ["a", "b", "c"]),
        ("$c$ 退栈", ["a", "b"]),
    ]
    fig, axes = plt.subplots(1, 4, figsize=(8.2, 3.5), dpi=150)
    x0, w, h, n = 0.9, 1.7, 0.62, 5
    for ax, (title, elems) in zip(axes, states):
        ax.set_xlim(0, 3.4)
        ax.set_ylim(0, 4.9)
        ax.axis("off")
        for i in range(n):
            _slot(ax, x0, 0.55 + i * h, w, h, fc=C_EMP)
        for i, e in enumerate(elems):
            _slot(ax, x0, 0.55 + i * h, w, h, text=e, fc=C_FILL)
        y_top = 0.55 + len(elems) * h + h / 2
        if not elems:
            # 空栈：base 与 top 重合，只画一个指针
            _arrow(ax, (0.82, 0.86), (x0 + 0.02, 0.86), C_BASE, ms=9)
            ax.text(0.74, 0.86, "base = top", ha="right", va="center",
                    fontsize=9, color=C_BASE, weight="bold")
        else:
            _arrow(ax, (0.82, y_top), (x0 + 0.02, y_top), C_TOP, ms=9)
            ax.text(0.74, y_top, "top", ha="right", va="center", fontsize=9,
                    color=C_TOP, weight="bold")
            _arrow(ax, (0.82, 0.86), (x0 + 0.02, 0.86), C_BASE, ms=9)
            ax.text(0.74, 0.86, "base", ha="right", va="center", fontsize=9,
                    color=C_BASE, weight="bold")
        ax.set_title(title, fontsize=11.5, color=C_TEXT, pad=6)
    fig.suptitle("顺序栈的动态变化（top 始终指向下一个可写入位置）",
                 fontsize=11.5, color=C_TEXT, y=1.02)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "ch3-1-2-栈的状态变化.png"),
                bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3 链栈
def fig_link_stack():
    fig, ax = plt.subplots(figsize=(7.4, 2.8), dpi=150)
    ax.set_xlim(0, 11.4)
    ax.set_ylim(0, 3.6)
    ax.axis("off")

    def node(x, y, data, has_next=True, w=1.45, h=0.72):
        ax.add_patch(Rectangle((x, y), w * 0.58, h, fc=C_FILL, ec=C_LINE, lw=1.2))
        ax.add_patch(Rectangle((x + w * 0.58, y), w * 0.42, h, fc="white",
                               ec=C_LINE, lw=1.2))
        ax.text(x + w * 0.29, y + h / 2, data, ha="center", va="center",
                fontsize=11, color=C_TEXT)
        if not has_next:
            ax.text(x + w * 0.79, y + h / 2, "∧", ha="center", va="center",
                    fontsize=12, color=C_TEXT)

    y1 = 2.05
    ax.text(0.30, y1 + 1.00, "非空栈", fontsize=10.5, color=C_TEXT, weight="bold")
    xs = [2.05, 3.9, 5.75, 7.6]
    for k, (x, d) in enumerate(zip(xs, ["$a_4$", "$a_3$", "$a_2$", "$a_1$"])):
        node(x, y1, d, has_next=(k != len(xs) - 1))
        if k != len(xs) - 1:
            _arrow(ax, (x + 1.45, y1 + 0.36), (xs[k + 1] - 0.02, y1 + 0.36), ms=10)
    _arrow(ax, (1.62, y1 + 0.36), (xs[0] - 0.02, y1 + 0.36), C_TOP, lw=1.5)
    ax.text(1.55, y1 + 0.36, "top", fontsize=10.5, color=C_TOP,
            weight="bold", ha="right", va="center")
    ax.text(0.30, y1 - 0.30, "栈顶在表头，top 即头指针", fontsize=9, color=C_TXT2)

    y2 = 0.70
    ax.text(0.30, y2 - 0.02, "空栈", fontsize=10.5, color=C_TEXT, weight="bold")
    _arrow(ax, (1.24, y2 + 0.36), (1.78, y2 + 0.36), C_TOP, lw=1.5)
    ax.text(1.18, y2 + 0.36, "top", fontsize=10.5, color=C_TOP,
            weight="bold", ha="right", va="center")
    ax.text(1.86, y2 + 0.36, "∧", fontsize=13, color=C_TEXT, va="center")

    ax.text(5.4, y2 + 0.60, "插入 / 删除都固定在表头进行，因此不必附加头结点",
            fontsize=9.5, color=C_TEXT, va="center")

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "ch3-1-3-链栈.png"),
                bbox_inches="tight", facecolor="white")
    plt.close(fig)


# -------------------------------------------------------------- 图 4 循环队列
def _draw_ring(ax, cx, cy, r, front, rear, filled, title, note):
    n = 6
    ax.add_patch(Circle((cx, cy), r, fill=False, ec=C_LINE, lw=1.5))
    for i in range(n):
        a = np.deg2rad(90 - i * 60)
        ax.plot([cx, cx + r * np.cos(a)], [cy, cy + r * np.sin(a)],
                color=C_LINE, lw=1.1)
    for i in range(n):
        a = np.deg2rad(90 - i * 60 - 30)
        x, y = cx + 0.68 * r * np.cos(a), cy + 0.68 * r * np.sin(a)
        ax.text(x, y + 0.085, str(i), ha="center", va="center", fontsize=9,
                color=C_TXT2)
        ax.text(x, y - 0.115, "有元素" if i in filled else "空",
                ha="center", va="center", fontsize=8.5,
                color=C_GRN if i in filled else C_TXT2)

    def mark(idx, color, label, dxy=(0, 0), r_out=1.30, r_in=1.06):
        a = np.deg2rad(90 - idx * 60 - 30)
        ux, uy = np.cos(a), np.sin(a)
        x, y = cx + r_out * r * ux, cy + r_out * r * uy
        _arrow(ax, (x, y), (cx + r_in * r * ux, cy + r_in * r * uy), color, lw=1.5, ms=10)
        ax.text(x + dxy[0], y + dxy[1], label, ha="center", va="center",
                fontsize=10.5, color=color, weight="bold")

    if rear == front:
        # 空队：front 与 rear 指向同一格，画一支箭头、两个标签即可
        a = np.deg2rad(90 - front * 60 - 30)
        ux, uy = np.cos(a), np.sin(a)
        x, y = cx + 1.30 * r * ux, cy + 1.30 * r * uy
        _arrow(ax, (x, y), (cx + 1.06 * r * ux, cy + 1.06 * r * uy),
               C_BASE, lw=1.5, ms=10)
        ax.text(x - 0.04, y + 0.24, "front", ha="center", va="center",
                fontsize=10.5, color=C_BASE, weight="bold")
        ax.text(x + 0.66, y + 0.00, "rear", ha="center", va="center",
                fontsize=10.5, color=C_TOP, weight="bold")
    else:
        mark(front, C_BASE, "front")
        mark(rear, C_TOP, "rear")
    ax.set_title(title, fontsize=11.5, color=C_TEXT, pad=2)
    ax.text(cx, cy - r - 0.44, note, ha="center", va="center", fontsize=9.5,
            color=C_TEXT)


def fig_circular_queue():
    fig, axes = plt.subplots(1, 2, figsize=(7.6, 3.9), dpi=150)
    for ax in axes:
        ax.set_xlim(-2.2, 2.2)
        ax.set_ylim(-2.5, 2.15)
        ax.axis("off")
        ax.set_aspect("equal")

    _draw_ring(axes[0], 0, 0, 1.05, front=0, rear=0, filled=set(),
               title="队空", note="front == rear")
    _draw_ring(axes[1], 0, 0, 1.05, front=0, rear=5, filled={0, 1, 2, 3, 4},
               title="队满", note="(rear + 1) % MAXQSIZE == front")

    fig.suptitle("循环队列：牺牲一个单元，用来区分「空」与「满」",
                 fontsize=11.5, color=C_TEXT, y=1.0)
    fig.text(0.5, -0.08,
             "加 1 后取模使指针到达数组尾部时自动折回起点；"
             "队满时实际只存 MAXQSIZE − 1 个元素。",
             ha="center", fontsize=9.5, color=C_TXT2)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "ch3-4-1-循环队列.png"),
                bbox_inches="tight", facecolor="white")
    plt.close(fig)


# -------------------------------------------------------------- 图 5 假溢出
def fig_false_overflow():
    n = 5                                   # 教材例子：数组大小为 5
    panels = [
        ("(a) 空队列", [], 0, 0),
        (r"(b) 入队 $a_1\ a_2\ a_3$", ["$a_1$", "$a_2$", "$a_3$"], 0, 3),
        (r"(c) 出队 $a_1\ a_2\ a_3$", [], 3, 3),
        (r"(d) 再入队 $a_4\ a_5$", ["$a_4$", "$a_5$"], 3, 5),
    ]
    fig, axes = plt.subplots(4, 1, figsize=(7.2, 5.8), dpi=150)
    x0, w, h, y0 = 2.75, 1.28, 0.66, 0.95
    for ax, (title, elems, front, rear) in zip(axes, panels):
        ax.set_xlim(0, 11.0)
        ax.set_ylim(0, 2.5)
        ax.axis("off")
        ax.text(0.12, 1.30, title, fontsize=10.5, color=C_TEXT,
                weight="bold", va="center")
        for i in range(n):
            _slot(ax, x0 + i * w, y0, w, h, fc=C_EMP)
            ax.text(x0 + i * w + w / 2, y0 + h + 0.14, str(i), ha="center",
                    va="center", fontsize=8.5, color=C_TXT2)
        for i, e in enumerate(elems):
            _slot(ax, x0 + (front + i) * w, y0, w, h, text=e, fc=C_FILL)

        same = (front == rear)
        for pos, color, label in ((front, C_BASE, "front"), (rear, C_TOP, "rear")):
            # 箭头统一高度，只有文字在下标重合时错开一行
            dy = -0.32 if (same and color == C_TOP) else 0.0
            if pos >= n:                    # 指针已越出数组上界
                ax.annotate("", xy=(x0 + n * w - 0.06, y0 - 0.05),
                            xytext=(x0 + n * w + 0.55, 0.14),
                            arrowprops=dict(arrowstyle="-|>", color=color, lw=1.5))
                ax.text(x0 + n * w + 0.65, 0.08, label + "（越界）", fontsize=9.5,
                        color=color, weight="bold", va="center")
            else:
                _arrow(ax, (x0 + pos * w + w / 2, y0 - 0.09),
                       (x0 + pos * w + w / 2, y0 - 0.01), color, lw=1.5, ms=10)
                ax.text(x0 + pos * w + w / 2, y0 - 0.50 + dy, label,
                        ha="center", fontsize=9.5, color=color, weight="bold")
        if rear >= n:
            ax.add_patch(Rectangle((x0, 0.10), 3 * w, 0.38, fc=C_FILL2,
                                   ec="#d9b382", lw=1))
            ax.text(x0 + 1.5 * w, 0.29, "空间已空出却回不去", ha="center",
                    va="center", fontsize=9, color="#8d6a3f")
    fig.suptitle("顺序队列的假溢出：头尾指针只增不减，前面的空间被白白浪费",
                 fontsize=11.5, color=C_TEXT, y=1.0)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "ch3-4-2-假溢出现象.png"),
                bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------- 图 6 串的三种存储
def fig_string_storage():
    fig, axes = plt.subplots(3, 1, figsize=(7.8, 5.8), dpi=150)
    for ax in axes:
        ax.set_xlim(0, 11.0)
        ax.set_ylim(0, 2.0)
        ax.axis("off")

    w, h, y0 = 0.72, 0.62, 0.62

    # (1) 定长顺序存储
    ax = axes[0]
    ax.text(0.20, 1.80, "定长顺序存储", fontsize=11, color=C_TEXT, weight="bold")
    ax.text(0.20, 1.48, "数组上界在编译时确定，0 号下标用来存串长",
            fontsize=9.5, color=C_TXT2)
    x = 0.90
    _slot(ax, x, y0, w, h, text="5", fc=C_FILL2)
    for i, c in enumerate("Hello"):
        _slot(ax, x + (i + 1) * w, y0, w, h, text=c, fc=C_FILL)
    for i in range(6, 8):
        _slot(ax, x + i * w, y0, w, h, fc=C_EMP)
    ax.text(x + w / 2, y0 - 0.20, "串长", ha="center", va="center",
            fontsize=9, color="#b07d2a")
    ax.text(x + 3.5 * w, y0 - 0.20, "串值", ha="center", va="center",
            fontsize=9, color=C_TXT2)
    ax.text(x + 7 * w, y0 + h / 2, "未用", fontsize=9, color=C_TXT2, va="center")
    ax.text(0.20, 0.18, "typedef unsigned char SString[MAXSTRLEN + 1];",
            fontsize=9, color=C_TXT2, family="monospace")

    # (2) 堆分配存储
    ax = axes[1]
    ax.text(0.20, 1.80, "堆分配存储", fontsize=11, color=C_TEXT, weight="bold")
    ax.text(0.20, 1.48, "运行时按串的实际长度动态分配，用 malloc / free 管理",
            fontsize=9.5, color=C_TXT2)
    bx, bw = 0.90, 2.30
    ax.add_patch(Rectangle((bx, y0), bw, h, fc="white", ec=C_LINE, lw=1.2))
    ax.plot([bx, bx + bw], [y0 + h / 2, y0 + h / 2], color=C_LINE, lw=1.2)
    ax.plot([bx + 1.0, bx + 1.0], [y0, y0 + h], color=C_LINE, lw=1.2)
    ax.text(bx + 0.5, y0 + 0.75 * h, "length", ha="center", va="center",
            fontsize=9.5, color=C_TEXT)
    ax.text(bx + 1.65, y0 + 0.75 * h, "5", ha="center", va="center",
            fontsize=9.5, color=C_TEXT)
    ax.text(bx + 0.5, y0 + 0.25 * h, "ch", ha="center", va="center",
            fontsize=9.5, color=C_TEXT)
    ax.text(bx + 1.65, y0 + 0.25 * h, "●", ha="center", va="center",
            fontsize=11, color=C_TOP)
    _arrow(ax, (bx + bw + 0.03, y0 + h / 2), (bx + bw + 0.55, y0 + h / 2),
           C_TOP, lw=1.5)
    hx = bx + bw + 0.65
    for i, c in enumerate("Hello"):
        _slot(ax, hx + i * w, y0, w, h, text=c, fc=C_FILL)
    ax.text(hx + 2.5 * w, y0 - 0.20, "堆区", ha="center", va="center",
            fontsize=9, color=C_TXT2)

    # (3) 块链存储
    ax = axes[2]
    ax.text(0.20, 1.80, "块链存储", fontsize=11, color=C_TEXT, weight="bold")
    ax.text(0.20, 1.48, "每个结点存放若干字符（结点大小 CHUNKSIZE），避免指针域过多",
            fontsize=9.5, color=C_TXT2)
    cx = 0.90
    sw, gap = 0.62, 0.30
    for k, chunk in enumerate([("a", "b", "c"), ("e", "p", "c"), ("g", "@", "@")]):
        x = cx + k * (3 * sw + 0.50 + gap)
        for i, ch in enumerate(chunk):
            _slot(ax, x + i * sw, y0, sw, h, text=ch,
                  fc=C_FILL2 if ch == "@" else C_FILL)
        _slot(ax, x + 3 * sw, y0, 0.50, h, fc="white")
        if k != 2:
            _arrow(ax, (x + 3 * sw + 0.52, y0 + h / 2),
                   (x + 3 * sw + 0.50 + gap + 0.02, y0 + h / 2), ms=10)
        else:
            ax.text(x + 3 * sw + 0.25, y0 + h / 2, "∧", fontsize=12,
                    color=C_TEXT, va="center", ha="center")
    ax.text(cx, 0.40, "@ 为块内填补的特殊字符，用以表示串的终结",
            fontsize=9, color="#b07d2a")
    ax.text(cx, 0.14, "LString{ head, tail, curlen }；"
            "插入 / 删除时通常需要在块间移动字符",
            fontsize=9, color=C_TXT2)

    fig.tight_layout(h_pad=1.6)
    fig.savefig(os.path.join(OUT, "ch4-2-1-串的三种存储结构.png"),
                bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ------------------------------------------------ 图 7 KMP 失配后的滑动
def fig_kmp_shift():
    """S 与 T 在 j=6 失配：i 不动，T 右滑 3 位后前两个字符天然相等。"""
    fig, ax = plt.subplots(figsize=(7.8, 4.0), dpi=150)
    ax.set_xlim(0, 8.6)
    ax.set_ylim(0, 4.0)
    ax.axis("off")

    S = list("abaababcabc")        # S[1..11]
    T = list("abaabcac")           # T[1..8]
    w, h = 0.62, 0.46
    x0 = 1.15

    def col(i):                    # 第 i 列（1 起点）的左边界
        return x0 + (i - 1) * w

    y_s, y_t1, y_t2 = 3.15, 2.20, 1.30

    ax.text(x0 - 0.20, y_s + h / 2, "S", ha="right", va="center",
            fontsize=10.5, color=C_BASE, weight="bold")
    for i, ch in enumerate(S, start=1):
        fc = C_FILL if i <= 5 else C_EMP
        if i == 6:
            fc = "#f6d5d0"
        _slot(ax, col(i), y_s, w, h, ch, fc=fc)

    ax.text(x0 - 0.20, y_t1 + h / 2, "T", ha="right", va="center",
            fontsize=10.5, color=C_TOP, weight="bold")
    for j, ch in enumerate(T, start=1):
        fc = C_FILL if j <= 5 else C_EMP
        if j == 6:
            fc = "#f6d5d0"
        _slot(ax, col(j), y_t1, w, h, ch, fc=fc)

    ax.text(x0 - 0.20, y_t2 + h / 2, "T'", ha="right", va="center",
            fontsize=10.5, color=C_GRN, weight="bold")
    for j, ch in enumerate(T, start=1):
        fc = "#d9f0e2" if j <= 2 else C_EMP
        _slot(ax, col(j + 3), y_t2, w, h, ch, fc=fc)

    xm = col(6) + w / 2
    ax.plot([xm, xm], [y_t2 - 0.12, y_s + h + 0.16], ls=(0, (4, 3)),
            color=C_TOP, lw=1.3)
    ax.text(xm, y_s + h + 0.24, "失配处：i 不动", ha="center", va="bottom",
            fontsize=9.5, color=C_TOP, weight="bold")
    ax.text(xm - 0.06, y_t1 + h + 0.06, "j = 6", ha="right", va="bottom",
            fontsize=9.5, color=C_TOP, weight="bold",
            bbox=dict(fc="white", ec="none", pad=1.2))
    ax.text(col(3) + w / 2, y_t2 - 0.10, "j = next[6] = 3", ha="center",
            va="top", fontsize=9.5, color=C_GRN, weight="bold")

    ax.add_patch(Rectangle((col(4), y_t2 - 0.03), 2 * w,
                           (y_s + h) - y_t2 + 0.06, fc="none", ec=C_GRN,
                           lw=1.5, ls="--"))
    ax.text(col(5) + w / 2, y_t2 - 0.50,
            "右滑 3 位后，这两个字符必相等（next 已保证）",
            ha="center", va="top", fontsize=9.5, color=C_GRN)

    ax.text(x0 - 0.20, 0.20,
            "主串指针 i 不回溯；模式串整体右滑，j 由 6 退到 next[6] = 3",
            ha="left", va="center", fontsize=9.5, color=C_TXT2)

    fig.savefig(os.path.join(OUT, "ch4-3-2-KMP失配后的滑动.png"),
                bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ------------------------------------------ 图 8 next 的本质：前缀 = 后缀
def fig_next_meaning():
    """以 T = "abaabc" 求 next[6] 为例，说明"前缀等于后缀的最长不重叠子串"。"""
    fig, ax = plt.subplots(figsize=(7.2, 3.0), dpi=150)
    ax.set_xlim(0, 7.0)
    ax.set_ylim(0, 2.9)
    ax.axis("off")

    T = list("abaab")
    w, h = 0.68, 0.54
    x0 = 1.30
    y = 1.62

    for i, ch in enumerate(T, start=1):
        if i <= 2:
            fc = C_FILL
        elif i >= 4:
            fc = C_FILL2
        else:
            fc = C_EMP
        _slot(ax, x0 + (i - 1) * w, y, w, h, ch, fc=fc)

    ax.annotate("", xy=(x0, y + h + 0.12), xytext=(x0 + 2 * w, y + h + 0.12),
                arrowprops=dict(arrowstyle="<->", color=C_BASE, lw=1.3))
    ax.text(x0 + w, y + h + 0.20, '前缀 "ab"', ha="center", va="bottom",
            fontsize=10, color=C_BASE, weight="bold")

    ax.annotate("", xy=(x0 + 3 * w, y - 0.12), xytext=(x0 + 5 * w, y - 0.12),
                arrowprops=dict(arrowstyle="<->", color="#b07d2a", lw=1.3))
    ax.text(x0 + 4 * w, y - 0.20, '后缀 "ab"', ha="center", va="top",
            fontsize=10, color="#b07d2a", weight="bold")

    ax.text(x0 - 0.24, y + h / 2, "前 j-1 个字符", ha="right", va="center",
            fontsize=10, color=C_TEXT)

    ax.text(x0 - 0.24, 0.46,
            'T = "abaabc"，求 next[6]：前 5 个字符里最长的「前缀 = 后缀」是 "ab"\n'
            "（长 2，前后缀不能完全重叠）→ k = 2（0 起点），课本 1 起点记作 next[6] = 3",
            ha="left", va="center", fontsize=9.5, color=C_TXT2, linespacing=1.8)

    fig.savefig(os.path.join(OUT, "ch4-3-2-next的本质.png"),
                bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ------------------------------------------------- 图 9 快速转置的 num/cpot
def fig_fast_transpose():
    fig, ax = plt.subplots(figsize=(10.0, 5.4), dpi=150)
    ax.set_xlim(0, 15.0)
    ax.set_ylim(-1.2, 9.4)
    ax.axis("off")

    ax.text(0.1, 9.0, "快速转置：先数每列几个元素，再算出每列该填到哪",
            ha="left", va="center", fontsize=12.5, color=C_TEXT)

    # 左：M 的三元组表（8 行，自顶向下）
    ax.text(0.35, 8.25, "M.data（行序）", ha="left", va="center",
            fontsize=10.5, color=C_BASE)
    rows = [("1", "2", "12"), ("1", "3", "9"), ("3", "1", "-3"),
            ("3", "6", "14"), ("4", "3", "24"), ("5", "2", "18"),
            ("6", "1", "15"), ("6", "4", "-7")]
    x0, w, h = 0.35, 1.0, 0.5
    top = 7.9
    for r, (i, j, v) in enumerate(rows):
        y = top - (r + 1) * h
        for c, val in enumerate([i, j, v]):
            fc = C_FILL if c == 1 else C_EMP
            _slot(ax, x0 + c * w, y, w, h, val, fc=fc, fs=10)
        if j == "1":
            ax.add_patch(Rectangle((x0 + w, y), w, h, fc="none",
                                   ec=C_TOP, lw=1.8))
    ax.text(x0, top - 8 * h - 0.42,
            "红框 = M 中所有第 1 列的元组\n（它们转置后就是 T 的第 1 行）",
            ha="left", va="top", fontsize=9.5, color=C_TXT2, linespacing=1.7)

    # 右：说明
    xr = 5.3
    ax.text(xr, 8.25, "① 数 M 的每一列（不是行！）有几个非零元  →  num[col]",
            ha="left", va="center", fontsize=10.3, color=C_TXT2)
    ax.text(xr, 7.73, "② 从第 1 列起累加  →  每列的起始位置 cpot[col]",
            ha="left", va="center", fontsize=10.3, color=C_TXT2)
    ax.text(xr, 7.21, "③ 依次扫 M.data，用 cpot 落到 T.data 的位置，落一个 +1",
            ha="left", va="center", fontsize=10.3, color=C_TXT2)
    ax.text(xr, 6.5, "M 的列  =  T 的行  →  「按列抄 M」就是「按行填 T」",
            ha="left", va="center", fontsize=11, color=C_BASE)

    # 右下：num / cpot 表
    cols = ["col", "1", "2", "3", "4", "5", "6", "7"]
    num = ["num", "2", "2", "2", "1", "0", "1", "0"]
    cpot = ["cpot", "1", "3", "5", "7", "8", "8", "9"]
    tx, tw, th = xr, 0.95, 0.5
    ttop = 5.35
    ax.text(tx, ttop + 0.32, "num / cpot 对照表", ha="left", va="center",
            fontsize=10.5, color=C_BASE)
    for r, data in enumerate([cols, num, cpot]):
        y = ttop - (r + 1) * th
        for c, val in enumerate(data):
            fc = C_FILL2 if (r == 0 or c == 0) else C_EMP
            _slot(ax, tx + c * tw, y, tw, th, val, fc=fc, fs=10)
    ybot = ttop - 3 * th
    ax.text(tx, ybot - 0.42,
            "cpot[col] = cpot[col-1] + num[col-1]   （cpot[1] = 1）",
            ha="left", va="top", fontsize=10.3, color=C_TOP)
    ax.text(tx, ybot - 1.06,
            "填一个元素就 ++cpot[col]，否则同一列的多个元素会互相覆盖",
            ha="left", va="top", fontsize=10, color=C_TXT2)

    fig.savefig(os.path.join(OUT, "ch5-3-2-快速转置的num和cpot.png"),
                bbox_inches="tight", facecolor="white")
    plt.close(fig)


# --------------------------------------------- 图 10 广义表两种存储结构对照
def fig_glist_two_storage():
    """广义表 E = (a, (b, (c, d)), (e)) 的两种存储结构对照。

    上排：头尾链表（每个原子占两层结点）
    下排：同层结点链表（有头结点，原子占一个结点）
    两排各自用独立的格点坐标，避免连线交叉。
    """
    fig, ax = plt.subplots(figsize=(11.0, 7.6), dpi=150)
    ax.set_xlim(0, 22.0)
    ax.set_ylim(-9.6, 4.6)
    ax.axis("off")

    W, H = 1.12, 0.62      # 单个格子的宽高

    def cells(x, y, vals, fc=C_EMP, fs=10.5, hi=None):
        """在 (x, y) 起画一排格子；hi 为需要高亮的列号集合。"""
        for k, v in enumerate(vals):
            f = C_FILL2 if (hi and k in hi) else fc
            _slot(ax, x + k * W, y, W, H, v, fc=f, fs=fs)
        return x + len(vals) * W

    def top(x, y, n):
        return (x + n * W, y + H)

    # =============================================== 上：头尾链表
    ax.text(0.2, 4.1, "（a）头尾链表：每个原子对应两层结点（外层还包一层表结点）",
            ha="left", va="center", fontsize=12, color=C_BASE)

    # 顶层 E 的 tp 链：三个表结点 (hp 指向元素)
    yA = 2.95
    xa = cells(1.5, yA, ["1", "", ""], fc=C_FILL)
    _arrow(ax, (xa, yA + H / 2), (xa + 0.25, yA + H / 2))
    xb = cells(xa + 0.25, yA, ["1", "", ""], fc=C_FILL)
    _arrow(ax, (xb, yA + H / 2), (xb + 0.25, yA + H / 2))
    xc = cells(xb + 0.25, yA, ["1", "∧"], fc=C_FILL)
    ax.text(0.9, yA + H / 2, "E", ha="left", va="center", fontsize=11,
            color=C_TEXT)

    # 元素 a：hp 表结点 → 原子结点
    y1 = 1.55
    a1 = cells(1.5, y1, ["1", "", "∧"], fc=C_FILL)
    y2 = 0.35
    a2 = cells(1.5, y2, ["0", "a", "∧"], fc=C_FILL2)
    _arrow(ax, (1.5 + W / 2, yA), (1.5 + W / 2, y1 + H))
    _arrow(ax, (1.5 + W / 2, y1), (1.5 + W / 2, y2 + H))

    # 元素 (b, (c, d))：hp 表结点 → [b / (c,d)]
    x2 = xa + W     # 第二个顶层表结点的 hp 格
    b1 = cells(x2, y1, ["1", "", ""], fc=C_FILL)
    _arrow(ax, (x2 + W / 2, yA), (x2 + W / 2, y1 + H))
    # 这一层里 b 与 (c,d) 并排
    y3 = 0.35
    b2 = cells(x2, y3, ["0", "b", "∧"], fc=C_FILL2)
    _arrow(ax, (x2 + W / 2, y1), (x2 + W / 2, y3 + H))
    x3 = b2 + 0.35
    c1 = cells(x3, y3, ["1", "", ""], fc=C_FILL)
    _arrow(ax, (b2 + W / 2, y1), (b2 + W / 2, y3 + H)) if False else None
    _arrow(ax, (x3 + W / 2, y1), (x3 + W / 2, y3 + H))
    y4 = -0.85
    c2 = cells(x3, y4, ["0", "c", "∧"], fc=C_FILL2)
    _arrow(ax, (x3 + W / 2, y3), (x3 + W / 2, y4 + H))
    x4 = c2 + 0.35
    d1 = cells(x4, y4, ["0", "d", "∧"], fc=C_FILL2)
    _arrow(ax, (c2, y4 + H / 2), (x4, y4 + H / 2))

    # 元素 (e)：hp 表结点 → 原子结点
    y5 = 1.55
    e1 = cells(xb + W, y5, ["1", "∧"], fc=C_FILL)
    _arrow(ax, (xb + W + W / 2, yA), (xb + W + W / 2, y5 + H))
    y6 = 0.35
    e2 = cells(xb + W, y6, ["0", "e", "∧"], fc=C_FILL2)
    _arrow(ax, (xb + W + W / 2, y5), (xb + W + W / 2, y6 + H))

    ax.text(0.2, -1.75,
            "关键：原子 a 下面挂的是「表结点 → 原子结点」两级；\n"
            "空格是没用到/指向别处的域，∧ 表示空指针。",
            ha="left", va="center", fontsize=10, color=C_TXT2,
            linespacing=1.8)

    # =============================================== 下：同层结点链表
    ax.text(0.2, -2.85,
            "（b）同层结点链表：有头结点，原子结点的值填到中间域，每个原子只占一个结点",
            ha="left", va="center", fontsize=12, color=C_BASE)

    # 用固定列坐标排布：第 n 列的 x
    COL = {1: 1.5, 2: 4.2, 3: 6.9, 4: 9.6, 5: 12.3, 6: 15.0, 7: 17.7}

    yB = -4.0
    cells(COL[1], yB, ["1", "∧"], fc=C_FILL)                    # 头结点
    ax.text(0.9, yB + H / 2, "E", ha="left", va="center", fontsize=11,
            color=C_TEXT)

    y7 = -5.2
    e1 = cells(COL[1], y7, ["0", "a", ""], fc=C_FILL2)          # 原子 a
    _arrow(ax, (COL[1] + W / 2, yB), (COL[1] + W / 2, y7 + H))
    _arrow(ax, (e1, y7 + H / 2), (COL[2], y7 + H / 2))
    e2 = cells(COL[2], y7, ["1", "", ""], fc=C_FILL)            # (b,(c,d)) 容器
    _arrow(ax, (e2, y7 + H / 2), (e2 + 0.55, y7 + H / 2))
    _arrow(ax, (e2 + 0.55, y7 + H / 2), (COL[5], y7 + H / 2))
    e3 = cells(COL[5], y7, ["1", "∧"], fc=C_FILL)               # (e) 容器

    y8 = -6.4
    f1 = cells(COL[2], y8, ["0", "b", ""], fc=C_FILL2)          # 原子 b
    _arrow(ax, (COL[2] + W / 2, y7), (COL[2] + W / 2, y8 + H))
    _arrow(ax, (f1, y8 + H / 2), (COL[3], y8 + H / 2))
    f2 = cells(COL[3], y8, ["1", "∧"], fc=C_FILL)               # (c,d) 容器
    g3 = cells(COL[5], y8, ["0", "e", "∧"], fc=C_FILL2)         # 原子 e
    _arrow(ax, (COL[5] + W / 2, y7), (COL[5] + W / 2, y8 + H))

    y9 = -7.6
    h1 = cells(COL[4], y9, ["0", "c", ""], fc=C_FILL2)          # 原子 c
    _arrow(ax, (COL[3] + W / 2, y8), (COL[4] + W / 2, y9 + H))
    _arrow(ax, (h1, y9 + H / 2), (COL[5], y9 + H / 2))
    h2 = cells(COL[5], y9, ["0", "d", "∧"], fc=C_FILL2)         # 原子 d

    ax.text(0.2, -8.8,
            "对照：同一层里 (b,(c,d)) 与 (e) 是兄弟，所以它们的原子结点也都排在下一层；\n"
            "实际使用中每一层都会有头结点（此处只画了 E 指向的那个）。",
            ha="left", va="center", fontsize=10, color=C_TXT2,
            linespacing=1.8)

    fig.savefig(os.path.join(OUT, "ch5-5-广义表两种存储结构.png"),
                bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ------------------------------------------- 图 11 树的基本术语（树的定义和术语）
def fig_tree_terms():
    fig, ax = plt.subplots(figsize=(10.6, 6.0), dpi=150)
    ax.set_xlim(-3.0, 22.4)
    ax.set_ylim(0.3, 6.9)
    ax.axis("off")

    R = 0.36

    def nd(x, y, s, fc=C_FILL, fs=10.5):
        ax.add_patch(Circle((x, y), R, fc=fc, ec=C_LINE, lw=1.3, zorder=3))
        ax.text(x, y, s, ha="center", va="center", fontsize=fs,
                color=C_TEXT, zorder=4)

    def lk(a, b):
        ax.plot([a[0], b[0]], [a[1], b[1]], color=C_LINE, lw=1.15,
                zorder=1, solid_capstyle="round")

    # 课件 P4 的树：A(B(E(K,L),F), C(G(M,N)), D(H,I,J))
    P = {
        "A": (8.0, 5.5),
        "B": (4.4, 4.1), "C": (8.0, 4.1), "D": (12.4, 4.1),
        "E": (2.9, 2.7), "F": (6.1, 2.7), "G": (8.0, 2.7),
        "H": (11.2, 2.7), "I": (13.4, 2.7), "J": (15.6, 2.7),
        "K": (1.9, 1.3), "L": (3.9, 1.3), "M": (7.1, 1.3), "N": (9.1, 1.3),
    }
    for a, b in [("A", "B"), ("A", "C"), ("A", "D"),
                 ("B", "E"), ("B", "F"), ("C", "G"),
                 ("D", "H"), ("D", "I"), ("D", "J"),
                 ("E", "K"), ("E", "L"), ("G", "M"), ("G", "N")]:
        lk(P[a], P[b])
    for k, v in P.items():
        nd(v[0], v[1], k)

    # 左侧层次标注
    for lvl, y in [(1, 5.5), (2, 4.1), (3, 2.7), (4, 1.3)]:
        ax.text(-0.55, y, f"第 {lvl} 层", ha="right", va="center",
                fontsize=10, color=C_TXT2)

    ax.text(8.0, 6.45, "根（root）", ha="center", va="center",
            fontsize=10.5, color=C_TOP)
    ax.annotate("", xy=(8.0, 5.88), xytext=(8.0, 6.26),
                arrowprops=dict(arrowstyle="-|>", color=C_TOP, lw=1.3))

    # 右侧说明
    ax.text(17.2, 6.35, "基本术语速查", ha="left", va="center",
            fontsize=11.5, color=C_BASE)
    ax.text(17.2, 3.85,
            "· 结点的度 = 往下长出的子树棵数\n"
            "  A 的度 = 3，B 的度 = 2\n"
            "  树的度 = 各结点度的最大值 = 3\n\n"
            "· 度 = 0 的结点叫叶子（终端结点）\n"
            "  H、I、J、K、L、M、N 都是叶子\n\n"
            "· B、C、D 是 A 的孩子，A 是它们的双亲\n"
            "  B、C、D 互称兄弟\n\n"
            "· 双亲同在一层的结点互称堂兄弟\n"
            "  E、F、G、H、I、J 是堂兄弟\n\n"
            "· 树的深度（高度）= 最大层次值 = 4",
            ha="left", va="center", fontsize=10, color=C_TXT2,
            linespacing=1.7)

    ax.text(-3.0, 0.55,
            "说明：结点的度只数「向下长出去几条枝」，连到双亲的那一根不算；"
            "从根到任一结点的路径有且只有一条。",
            ha="left", va="center", fontsize=9.8, color=C_TXT2)

    fig.savefig(os.path.join(OUT, "ch6-1-树的基本术语.png"),
                bbox_inches="tight", facecolor="white")
    plt.close(fig)


# -------------------------------- 图 12 满二叉树 / 完全二叉树 / 非完全二叉树
def fig_full_vs_complete():
    fig, ax = plt.subplots(figsize=(11.4, 4.9), dpi=150)
    ax.set_xlim(0, 30.4)
    ax.set_ylim(-1.3, 6.9)
    ax.axis("off")

    R = 0.30
    DX, DY, Y0 = 0.72, 1.15, 0.9

    def build(x0, drop4=()):
        """返回 (结点坐标字典, 边列表, 被抹掉的底层序号)。"""
        lv4 = [(x0 + i * DX, Y0) for i in range(8)]
        lv3 = [((lv4[2 * i][0] + lv4[2 * i + 1][0]) / 2, Y0 + DY)
               for i in range(4)]
        lv2 = [((lv3[2 * i][0] + lv3[2 * i + 1][0]) / 2, Y0 + 2 * DY)
               for i in range(2)]
        lv1 = [((lv2[0][0] + lv2[1][0]) / 2, Y0 + 3 * DY)]

        nodes, edges = {}, []
        nodes[1] = lv1
        nodes[2] = lv2
        nodes[3] = lv3
        nodes[4] = lv4
        for i in range(2):
            edges.append((lv1[0], lv2[i]))
        for i in range(4):
            edges.append((lv2[i // 2], lv3[i]))
        for i in range(8):
            if i in drop4:
                continue
            edges.append((lv3[i // 2], lv4[i]))
        return nodes, edges, drop4

    def panel(x0, title, sub, drop4=()):
        nodes, edges, d4 = build(x0, drop4=drop4)
        for a, b in edges:
            ax.plot([a[0], b[0]], [a[1], b[1]], color=C_LINE, lw=1.05,
                    zorder=1, solid_capstyle="round")
        for lvl, pts in nodes.items():
            for i, (x, y) in enumerate(pts):
                if lvl == 4 and i in d4:
                    continue
                fc = C_FILL2 if lvl == 4 else C_FILL
                ax.add_patch(Circle((x, y), R, fc=fc, ec=C_LINE,
                                    lw=1.1, zorder=3))
        cx = (nodes[4][0][0] + nodes[4][7][0]) / 2
        ax.text(cx, 6.35, title, ha="center", va="center", fontsize=11.5,
                color=C_BASE)
        ax.text(cx, 5.85, sub, ha="center", va="center", fontsize=10,
                color=C_TXT2)

    panel(1.6, "满二叉树（k = 4）", "每层都挂满 → 共 15 个结点（$2^4-1$）")
    panel(11.6, "完全二叉树", "抹掉编号 15 → 前 14 个结点一一对应", drop4=(7,))
    panel(21.6, "非完全二叉树", "抹掉的是中间某个 → 编号不连续", drop4=(5,))

    ax.text(0.1, -0.85,
            "完全二叉树 = 在满二叉树上「从最后一个结点往前挨着抹」抹出来的任意一棵；"
            "逆序抹、跳着抹出来的都不是。",
            ha="left", va="center", fontsize=10, color=C_TXT2)

    fig.savefig(os.path.join(OUT, "ch6-2-满二叉树与完全二叉树.png"),
                bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ------------------------------------------- 图 13 编号（1 起）vs 下标（0 起）
def fig_index_vs_number():
    fig, ax = plt.subplots(figsize=(12.0, 5.4), dpi=150)
    ax.set_xlim(0, 12.0)
    ax.set_ylim(0.2, 6.5)
    ax.axis("off")

    R = 0.38
    rel = {"A": (2.5, 4.7), "B": (1.3, 3.3), "C": (3.7, 3.3),
           "D": (0.7, 1.9), "E": (1.9, 1.9), "F": (3.1, 1.9)}
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), ("C", "F")]
    num = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6}

    def panel(x0, title, color, offset, above):
        pts = {k: (v[0] + x0, v[1]) for k, v in rel.items()}
        for a, b in edges:
            ax.plot([pts[a][0], pts[b][0]], [pts[a][1], pts[b][1]],
                    color=C_LINE, lw=1.05, zorder=1, solid_capstyle="round")
        for k, (x, y) in pts.items():
            ax.add_patch(Circle((x, y), R, fc=C_FILL, ec=C_LINE,
                                lw=1.1, zorder=3))
            ax.text(x, y, k, ha="center", va="center", fontsize=11,
                    color=C_TEXT, zorder=4)
            dy = (R + 0.32) if above else -(R + 0.32)
            label = str(num[k] + offset) if above else "[%d]" % (num[k] + offset)
            ax.text(x, y + dy, label, ha="center", va="center",
                    fontsize=10.5 if above else 9.5, color=color,
                    fontweight="bold", zorder=4)
        ax.text(x0 + 2.2, 6.05, title, ha="center", va="center",
                fontsize=11.5, color=C_BASE)

    panel(0.3, "编号：从 1 起（性质 5 用这套）", C_TOP, 0, True)
    panel(6.3, "数组下标：从 0 起（存进数组用这套）", C_BASE, -1, False)

    ax.text(6.0, 6.45, "同一棵完全二叉树：两套数字，永远差 1",
            ha="center", va="center", fontsize=13, color=C_TEXT)
    ax.text(0.3, 0.62,
            "编号 i 的结点 → 下标 i-1；所以孩子公式 2i / 2i+1 落到数组上要写成 2i+1 / 2i+2。",
            ha="left", va="center", fontsize=10, color=C_TXT2)

    fig.savefig(os.path.join(OUT, "ch6-2-3-编号与下标.png"),
                bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ------------------------------------------------ 图 14 中序线索化的示意
def fig_thread_demo():
    import math

    fig, ax = plt.subplots(figsize=(8.2, 5.4), dpi=150)
    ax.set_xlim(0, 10)
    ax.set_ylim(0.55, 7.25)
    ax.axis("off")

    R = 0.44
    A, B, C = (5.0, 5.25), (3.5, 3.6), (6.5, 3.6)

    for p, q in [(A, B), (A, C)]:
        ax.plot([p[0], q[0]], [p[1], q[1]], color=C_LINE, lw=1.5,
                zorder=1, solid_capstyle="round")

    for (x, y), name in [(A, "A"), (B, "B"), (C, "C")]:
        ax.add_patch(Circle((x, y), R, fc=C_FILL, ec=C_LINE, lw=1.2, zorder=3))
        ax.text(x, y, name, ha="center", va="center", fontsize=12,
                color=C_TEXT, zorder=4)

    def seg(a, b, r=R + 0.05):
        dx, dy = b[0] - a[0], b[1] - a[1]
        d = math.hypot(dx, dy)
        ux, uy = dx / d, dy / d
        return ((a[0] + ux * r, a[1] + uy * r),
                (b[0] - ux * (r + 0.07), b[1] - uy * (r + 0.07)))

    p1, p2 = seg(B, A)
    ax.add_patch(FancyArrowPatch(
        p1, p2, arrowstyle="-|>", mutation_scale=12, color=C_GRN, lw=1.6,
        linestyle=(0, (4, 3)), connectionstyle="arc3,rad=-0.55",
        shrinkA=0, shrinkB=0, zorder=2))

    p1, p2 = seg(C, A)
    ax.add_patch(FancyArrowPatch(
        p1, p2, arrowstyle="-|>", mutation_scale=12, color="#d9822b", lw=1.6,
        linestyle=(0, (4, 3)), connectionstyle="arc3,rad=0.42",
        shrinkA=0, shrinkB=0, zorder=2))

    ax.text(2.15, 2.72, "rchild 空 → 指向后继 A", ha="left", va="center",
            fontsize=10, color=C_GRN)
    ax.text(7.85, 2.72, "lchild 空 → 指向前驱 A", ha="right", va="center",
            fontsize=10, color="#d9822b")

    ax.text(5.0, 6.95, "中序序列 B → A → C：只把「空着的」指针改成线索",
            ha="center", va="center", fontsize=12.5, color=C_TEXT)
    ax.text(0.15, 1.45,
            "实线 = 孩子指针（Tag = 0）      橙虚线 = 前驱线索      绿虚线 = 后继线索",
            ha="left", va="center", fontsize=10, color=C_TXT2)
    ax.text(0.15, 0.95,
            "A 的左右孩子都在，两根指针原样不动 —— 线索只补空指针。",
            ha="left", va="center", fontsize=10, color=C_TXT2)

    fig.savefig(os.path.join(OUT, "ch6-3-2-中序线索示意.png"),
                bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig_seq_stack()
    fig_stack_states()
    fig_link_stack()
    fig_circular_queue()
    fig_false_overflow()
    fig_string_storage()
    fig_kmp_shift()
    fig_next_meaning()
    fig_fast_transpose()
    fig_glist_two_storage()
    fig_tree_terms()
    fig_full_vs_complete()
    fig_index_vs_number()
    fig_thread_demo()
    print("figures written to", OUT)
