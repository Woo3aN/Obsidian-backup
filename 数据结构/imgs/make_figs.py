# -*- coding: utf-8 -*-
"""生成《数据结构》第 3、4 章配图。

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


if __name__ == "__main__":
    fig_seq_stack()
    fig_stack_states()
    fig_link_stack()
    fig_circular_queue()
    fig_false_overflow()
    fig_string_storage()
    print("figures written to", OUT)
