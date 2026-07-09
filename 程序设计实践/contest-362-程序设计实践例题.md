# 2026年程序设计实践例题 — 实验笔记

> 实验：2026年程序设计实践例题(05李胜睿班)  
> 题型：OI  
> 语言：C++

---

## 目录

1. [LinK01 A+B](#link01-ab)
2. [LinK02 完美立方](#link02-完美立方)
3. [LinK03 人的周期](#link03-人的周期)
4. [LinK04 排序考试](#link04-排序考试)
5. [LinK13 输出N皇后的全部摆法](#link13-输出n皇后的全部摆法)
6. [LinK14 求八皇后的第n种解](#link14-求八皇后的第n种解)
7. [LinK14.5 DFS试炼之n皇后问题](#link145-dfs试炼之n皇后问题)
8. [LinK16 放苹果](#link16-放苹果)
9. [LinK19 递归实现指数型枚举](#link19-递归实现指数型枚举)
10. [LinK05 假币问题](#link05-假币问题)
11. [LinK09 汉诺塔I](#link09-汉诺塔i)
12. [LinK10 汉诺塔II](#link10-汉诺塔ii)
13. [LinK15 爬天梯](#link15-爬天梯)
14. [LinK20 递归实现组合型枚举](#link20-递归实现组合型枚举)
15. [LinK21 递归实现排列型枚举](#link21-递归实现排列型枚举)
16. [LinK27 大数排序](#link27-大数排序)
17. [LinK30 归并排序](#link30-归并排序)
18. [LinK31 求排列的逆序数](#link31-求排列的逆序数)
19. [LinK38 林克的命运之阵](#link38-林克的命运之阵)
20. [LinK39 净化迷雾森林](#link39-净化迷雾森林)
21. [LinK43 求二进制中1的个数](#link43-求二进制中1的个数)
22. [LinK44 二进制中1的最低位位置](#link44-二进制中1的最低位位置)
23. [LinK45 真假记忆碎片](#link45-真假记忆碎片)
24. [LinK46 寻找林克的回忆(1)](#link46-寻找林克的回忆1)
25. [LinK47 寻找林克的回忆(2)](#link47-寻找林克的回忆2)
26. [LinK48 寻找林克的回忆(3)](#link48-寻找林克的回忆3)
27. [LinK51 净化迷雾森林(广搜)](#link51-净化迷雾森林广搜)
28. [LinK52 波克布林的巡逻范围](#link52-波克布林的巡逻范围)
29. [LinK53 加农的入侵](#link53-加农的入侵)
30. [LinK57 Dijkstra求最短路(1)](#link57-dijkstra求最短路1)

---

## LinK01 A+B

### 题目描述

输入两个整数，求这两个整数的和是多少。

### 输入

输入两个整数 A, B，用空格隔开，0 ≤ A, B ≤ 10⁸。

### 输出

输出一个整数，表示这两个数的和。

### 样例

**输入：**
```
7 7
```

**输出：**
```
14
```

### 我的代码

```cpp
#include <iostream>
using namespace std;

int main()
{
    int a, b, c;
    cin >> a >> b;
    c = a + b;
    cout << c;
}
```

### 思路要点

- **题目本质**：这是 OI 竞赛的"Hello World"，考察最基本的输入输出语法，没有任何算法难度。
- **输入方式**：使用 `cin >> a >> b` 从标准输入读取两个整数。`cin` 会自动跳过空白字符（空格、换行），所以输入中的空格分隔不是问题。
- **输出方式**：使用 `cout << a + b` 直接输出结果。也可以用 `cout << c` 先存到变量 `c` 中再输出，效果相同。
- **数据类型选择**：题目数据范围是 0 ≤ A, B ≤ 10⁸，两数之和最大为 2×10⁸。C++ 中 `int` 类型在 32 位系统上能表示的范围约为 -2.1×10⁹ ~ 2.1×10⁹（即 -2³¹ ~ 2³¹-1），因此用 `int` 完全足够，不会溢出。如果想要更安全，也可以用 `long long`，但本题不需要。
- **易错点**：
  - 不要忘记 `#include <iostream>` 和 `using namespace std;`（或 `std::cin` / `std::cout`）。
  - OJ 判题时只比对输出内容，多余的提示文字（如 `"Please input:"`）会导致 Wrong Answer。

---

## LinK02 完美立方

### 题目描述

形如 a³ = b³ + c³ + d³ 的等式被称为完美立方等式。例如 12³ = 6³ + 8³ + 10³。编写一个程序，对任给的正整数 N (N ≤ 100)，寻找所有的四元组 (a, b, c, d)，使得 a³ = b³ + c³ + d³，其中 a, b, c, d 大于 1，小于等于 N，且 b ≤ c ≤ d。

### 输入

一个正整数 N（N ≤ 100）。

### 输出

每行输出一个完美立方。格式为：

```
Cube = a, Triple = (b,c,d)
```

请按照 a 的值从小到大依次输出。当 a 相同时，b 值小的优先输出；b 相同时 c 值小的优先；c 相同时 d 值小的优先。

### 样例

**输入：**
```
24
```

**输出：**
```
Cube = 6, Triple = (3,4,5)
Cube = 12, Triple = (6,8,10)
Cube = 18, Triple = (2,12,16)
Cube = 18, Triple = (9,12,15)
Cube = 19, Triple = (3,10,18)
Cube = 20, Triple = (7,14,17)
Cube = 24, Triple = (12,16,20)
```

### 我的代码

```cpp
#include <iostream>
using namespace std;

int main()
{
    int a, b, c, d;
    int N;
    cin >> N;
    for (a = 2; a <= N; a++)
    {
        int a3 = a * a * a;
        for (b = 2; b < N; b++)
        {
            for (c = b; c < N; c++)
            {
                for (d = c; d < N; d++)
                {
                    if (a3 == b * b * b + c * c * c + d * d * d)
                    {
                        cout << "Cube = " << a << ", "
                             << "Triple = "
                             << "(" << b << "," << c << "," << d << ")"
                             << endl;
                    }
                }
            }
        }
    }
    return 0;
}
```

### 思路要点

- **题目本质**：在给定范围内枚举所有可能的四元组 (a, b, c, d)，找出满足 a³ = b³ + c³ + d³ 的组合。由于限制了 b ≤ c ≤ d，可以避免重复枚举同一组合的不同排列。
- **为什么四重循环可行**：N ≤ 100，四重循环的枚举量大约是 N⁴ / 6（因为有 b ≤ c ≤ d 的约束，组合数约为 C(N,3) 量级），实际计算次数约 1.6×10⁷（一千六百万），在 OJ 的 1 秒时限内完全可行。现代 CPU 每秒可执行数亿次简单运算。
- **剪枝优化——预计算 a³**：`int a3 = a * a * a;` 放在最外层循环，避免在内层 b、c、d 的每一次迭代中都重新计算 a³。如果不这样做，`a * a * a` 会在最内层被计算 O(N³) 次，虽然编译器可能会优化，但手动提出来是好习惯。
- **有序枚举避免重复**：令 `b` 从 2 开始，`c` 从 `b` 开始，`d` 从 `c` 开始。这样天然保证 b ≤ c ≤ d，同时避免产生如 (3,4,5) 和 (4,3,5) 这种实际上等价的重复组合。注意题目要求 "b ≤ c ≤ d"，所以这个顺序也是题目规定的输出顺序。
- **起点的选择**：所有变量从 2 开始而非 1，因为题目明确说 "大于 1"。如果误从 1 开始，会多出一些不满足题目要求的组合（如 a=3, b=1, c=1, d=1 这种 1³+1³+1³ = 3 ≠ 27，实际上也不会成立，但边界条件要严格遵循题意）。
- **复杂度分析**：时间复杂度 O(N⁴/6)，空间复杂度 O(1)。N=100 时可以在 1 秒内完成。
- **易错点**：
  - 内层循环的终止条件写成了 `b < N` 而不是 `b <= N`——看起来像是 bug，但因为 c 和 d 都从更大的值开始，且 a³ = b³ + c³ + d³ 意味着 b、c、d 都小于 a，而 a ≤ N，所以 b < N 实际上不会漏解。不过严格来说写 `b <= N` 更安全、更符合题意。
  - 输出格式要严格匹配 `Cube = a, Triple = (b,c,d)`，包括空格和括号，否则 OJ 判错。

---

## LinK03 人的周期

### 题目描述

据说人生来就有三个生理周期，分别为体力周期、感情周期和智力周期，它们的周期长度分别为 **23 天**、**28 天**和 **33 天**。每一个周期中有一天是高峰。因为三个周期的长度不同，通常三个周期的高峰不会落在同一天。

对于每个周期，会给出从当前年份的第一天开始，到出现高峰的天数（不一定是第一次高峰出现的时间）。给定一个从当年第一天开始的天数 d，任务是输出从给定时间开始（**不包括**给定时间），下一次三个高峰落在同一天的时间（距给定时间的天数）。

例如：给定时间为 10，下次出现三个高峰同一天的时间是 12，则输出 2（注意这里不是 3）。

### 输入

输入包含多组数据，每一组数据由四个整数组成，数据以 `-1 -1 -1 -1` 结束。

对于每一行的四个整数 p, e, i 和 d：
- p, e, i 分别表示体力、情感和智力高峰出现的时间（从当年第一天开始计算）
- d 是给定的时间，可能小于 p, e 或 i

所有给定时间是非负的且 ≤ 365，所求的时间 ≤ 21252。

### 输出

从给定时间起，下一次三个高峰同一天的时间（距离给定时间的天数）。

### 样例

**输入：**
```
0 0 0 0
0 0 0 100
5 20 34 325
4 5 6 7
283 102 23 320
203 301 203 40
-1 -1 -1 -1
```

**输出：**
```
Case 1: the next triple peak occurs in 21252 days.
Case 2: the next triple peak occurs in 21152 days.
Case 3: the next triple peak occurs in 19575 days.
Case 4: the next triple peak occurs in 16994 days.
Case 5: the next triple peak occurs in 8910 days.
Case 6: the next triple peak occurs in 10789 days.
```

### 我的代码

```cpp
#include <iostream>
using namespace std;

int main()
{
    int p, e, i, d, caseNumber = 0;

    while (cin >> p >> e >> i >> d && p != -1)
    {
        ++caseNumber;
        int k;
        for (k = d + 1; (k - p) % 23; ++k);
        for (; (k - e) % 28; k += 23);
        for (; (k - i) % 33; k += 23 * 28);
        cout << "Case " << caseNumber
             << ": the next triple peak occurs in "
             << k - d << " days." << endl;
    }

    return 0;
}
```

### 思路要点

- **题目本质**：给定三个周期（23、28、33）的起始偏移 p、e、i，以及一个参考日期 d，求大于 d 的最小整数 k，使得 k 与 p 的差能被 23 整除、k 与 e 的差能被 28 整除、k 与 i 的差能被 33 整除。这是中国剩余定理（CRT）的一个特例，但代码中采用的是更直观的「逐步试探 / 步长加速法」，不需要 CRT 的模逆元计算。

- **数学表达**：求解同余方程组：
  ```
  k ≡ p (mod 23)
  k ≡ e (mod 28)
  k ≡ i (mod 33)
  ```
  且 k > d。等价于找最小的 k > d 使得 `(k-p)%23 == 0 && (k-e)%28 == 0 && (k-i)%33 == 0`。

- **三步跳跃法详解**（核心技巧）：

  1. **第一步——满足体力周期**：从 `k = d+1` 开始，每次 `k++`，找到第一个满足 `(k-p) % 23 == 0` 的 k。这一步最多走 23 步就能找到（因为模 23 的余数在连续 23 个整数中必然覆盖 0~22 各一次）。

  2. **第二步——同时满足体力和感情**：从上一步找到的 k 开始，每次让 `k += 23`，继续判断 `(k-e) % 28 == 0`。这里的关键是：k 增加 23 的倍数不会改变 `(k-p) % 23` 的值（因为 `(k+23t - p) % 23 == (k-p) % 23`），所以体力周期的条件始终满足。这一步最多走 28 次（因为 23 和 28 互质，对模 28 来说 +23 可以遍历所有余数）。

  3. **第三步——同时满足三个周期**：从上一步找到的 k 开始，每次让 `k += 23×28 = 644`，判断 `(k-i) % 33 == 0`。同理，+644 不会改变 `(k-p) % 23` 和 `(k-e) % 28` 的值（因为 644 是 23 和 28 的公倍数）。这一步最多走 33 次。三个模数 23、28、33 两两互质，它们的乘积 21252 就是所有三个条件同时满足的周期（即答案不会超过 21252）。

  综上，最坏情况下需要约 23 + 28 + 33 = 84 次循环就能找到答案，远优于从 d+1 到 21252 逐一枚举的 20000+ 次。

- **逐枚 vs 跳跃的直观理解**：想象你每 23 天去一次健身房（体力周期），每 28 天去一次图书馆（感情周期）。如果你想找一天同时去两个地方，不需要一天一天翻日历——只需要在每次去健身房的那天检查是否也要去图书馆即可。三个周期同理，层层叠加。

- **多组输入处理**：`while (cin >> p >> e >> i >> d && p != -1)` 在读取四个整数的同时判断 p 是否为 -1。`cin >> p` 的返回值是 `cin` 对象本身，可以用作布尔判断（读取成功为 true，失败或 EOF 为 false）。题目约定以 `-1 -1 -1 -1` 结束，但只检查 p != -1 就够了。

- **caseNumber 计数器**：每组数据的输出需要标注是第几个 Case，用 `++caseNumber` 从 1 开始递增。

- **复杂度分析**：每组数据最多约 23 + 28 + 33 ≈ 84 次循环，总复杂度 O(每组常数) × T。空间复杂度 O(1)。

- **易错点**：
  - 题目要求输出的是"距离给定时间的天数"即 `k - d`，而不是 k 本身。样例中给定 10，答案是 12，输出 2（因为 12-10=2，"不包括给定时间"）。代码中的 `for (k = d + 1; ...)` 从 d+1 开始正是这个原因。
  - 答案不会超过 21252（23×28×33），在 `int` 范围内。

---

## LinK04 排序考试

### 题目描述

给定任意 T 组整数，每组整数都要按升序输出。

### 输入

第一行是整数 T，表示一共有 T 组数据。接下来 T 行，每行有 N+1 个数，第一个整数表示该行有 N 个待排序的数字。

T（1 ≤ T ≤ 100），N（1 ≤ N ≤ 1000000）。

### 输出

对于每组整数，按照升序输出排序结果，每个结果占一行。

### 样例

**输入：**
```
3
4 412 120 5560 3760
5 576 66 35 99 88
4 127 100 510 380
```

**输出：**
```
120 412 3760 5560
35 66 88 99 576
100 127 380 510
```

### 我的代码

```cpp
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, value;
        cin >> N;
        vector<int> numbers;
        for (int i = 0; i < N; ++i)
        {
            cin >> value;
            numbers.push_back(value);
        }
        sort(numbers.begin(), numbers.end());
        for (int i = 0; i < N; ++i)
        {
            if (i > 0) cout << " ";
            cout << numbers[i];
        }
        cout << endl;
    }
    return 0;
}
```

### 思路要点

- **题目本质**：多组数据的排序问题。考察标准库 `std::sort` 的使用、动态数组 `vector` 的使用、多组输入的处理方式以及输出格式控制。

- **多组数据框架**：先读入 `T`（组数），然后用 `while (T--)` 循环 T 次。每组先读一个整数 N（该组有多少个数），再读入 N 个整数。

- **为什么用 `vector`**：题目中 N 最大可达 1,000,000（一百万）。如果使用固定大小的数组（如 `int arr[1000000]`），需要在编译时确定大小，而且栈空间通常只有几 MB，存不下这么大的数组（一百万 int ≈ 4MB，可能接近栈限制）。`vector` 在堆上动态分配内存，没有这个限制，而且可以根据需要自动扩容。也可以写成 `vector<int> numbers(N)` 预分配大小后再用下标访问，但 `push_back` 的写法更通用。

- **排序**：`sort(numbers.begin(), numbers.end())` 是 C++ STL 中最常用的排序函数，底层实现是快速排序 + 插入排序 + 堆排序的混合算法（内省排序），时间复杂度 O(N log N)，对一百万元素也足够快。

- **输出格式控制**：每一行的数字之间用空格隔开，但行末不能有多余空格（有些 OJ 对此很严格，会导致 Presentation Error 或 Wrong Answer）。代码用 `if (i > 0) cout << " "` 的技巧：除了第一个数字外，每个数字前先输出一个空格，这样最后一个数字后面就不会有空格。也可以用更简洁的方式：先输出第一个元素，然后循环输出 `" " << numbers[i]`。

- **复杂度分析**：每组排序 O(N log N)，总复杂度 O(Σ N log N)。空间复杂度 O(N)（每组存储 vector）。

- **易错点**：
  - 题目输入格式是每行第一个数表示该行有多少个待排序的数字，读入时容易搞混——第一个数 N 是数量，不能也参与排序。
  - 各组的 N 不同，每轮循环都要重新声明 `vector<int> numbers`（或用 `clear()` 清空），不能把上一组的数据混进来。
  - 需要引入 `<algorithm>`（sort）和 `<vector>`（vector）两个头文件。

---

## LinK13 输出N皇后的全部摆法

### 题目描述

输入一个正整数 N，输出 N 皇后问题的全部摆法。输出结果里的每一行都代表一种摆法，行里的第 i 个数字如果是 n，就代表第 i 行的皇后应该放在第 n 列。皇后的行、列编号都从 1 开始算。

### 输入

皇后的个数 n（n ≤ 13）。

### 输出

输出长度为 n 的正整数，每行一种摆法。

### 样例

**输入：**
```
4
```

**输出：**
```
2413
3142
```

### 我的代码

```cpp
#include <iostream>
#include <vector>
using namespace std;

int N;
vector<int> res;

void dfs(int n)
{
    if (n == N)
    {
        for (auto x : res) cout << x;
        cout << endl;
        return;
    }

    for (int i = 1; i <= N; i++)
    {
        int k;
        for (k = 0; k < n; k++)
        {
            if (res[k] == i || abs(res[k] - i) == abs(k - n))
                break;
        }
        if (k == n)
        {
            res[n] = i;
            dfs(n + 1);
        }
    }
}

int main()
{
    cin >> N;
    res.resize(N);
    dfs(0);
    return 0;
}
```

### 思路要点

- **题目本质**：经典 N 皇后问题——在 N×N 的棋盘上放置 N 个皇后，使得它们互不攻击（任意两个不在同一行、同一列、同一对角线）。这里要求输出所有解，每行解用一个 N 位数字表示，第 i 位表示第 i 行的皇后放在第几列。

- **DFS 回溯框架**：
  - 逐行放置皇后（`n` 表示当前处理到第几行，从 0 开始），每行尝试 1~N 的每一列。
  - `res[n] = i` 表示第 n 行的皇后放在第 i 列。
  - 放置前先做**冲突检测**（见下），通过后才递归进入下一行。
  - 当 `n == N` 时，说明 N 个皇后全部放置成功，此时 `res[0..N-1]` 保存了一组完整解，直接输出。由于递归会自然回溯（返回上一层尝试下一列），不需要显式的"撤销"操作——`res[n]` 在下一轮循环中会被覆盖。

- **冲突检测详解**（`for (k = 0; k < n; k++)` 检查当前行 n 的候选列 i 与已放置的 0~n-1 行是否冲突）：
  - **同一列**：`res[k] == i` —— 之前某行的皇后已经放在第 i 列了。
  - **同一对角线**：`abs(res[k] - i) == abs(k - n)` —— 如果行差等于列差的绝对值，说明两个皇后在一条斜线上。这是因为在 N×N 棋盘中，45° 斜线上所有格子的 `行 - 列` 为常数，135° 斜线上所有格子的 `行 + 列` 为常数。`|行1 - 行2| == |列1 - 列2|` 同时覆盖了两种情况。
  - 如果内层循环完整结束（`k == n`），说明没有任何冲突，该位置合法。

- **为什么不用布尔数组优化**：LinK14.5 中使用了 `col[]`, `dg[]`, `udg[]` 三个布尔数组 O(1) 判断冲突，这里用的是 O(n) 遍历检查。两种方法在这个数据范围（N ≤ 13）下都可以。遍历检查代码更短，容易理解和记忆；布尔数组版本更高效但需要处理对角线映射的细节。

- **输出格式**：`for (auto x : res) cout << x;` —— `res` 中的每个数字（列号从 1 开始）直接连接在一起组成一个整数串，符合题目要求的格式。注意与 LinK14.5 的输出格式完全不同（那个要求输出棋盘图案）。

- **复杂度分析**：N 皇后在已知所有解的情况下最坏时间复杂度约为 O(N!)，因为第一行有 N 种选择，第二行约 N-2 种……实际搜索树会被剪枝大幅缩小。N=13 时解数为 73712 个，在可接受范围内。

- **易错点**：
  - `res` 的索引从 0 开始，但输出的列号要从 1 开始（i 的范围是 1~N 而非 0~N-1）。
  - `res.resize(N)` 一定要在调用 dfs 之前执行，否则 `res[n] = i` 会出现越界访问（未分配空间）。

---

## LinK14 求八皇后的第n种解

### 题目描述

八皇后问题一共有 92 组解，每组解用一个皇后串表示：`a = b₁b₂...b₈`，其中 bᵢ 为第 i 行皇后所处的列数。皇后串的比较：将串视为整数，整数小的排前面。输入一个数 n，要求输出八皇后问题的第 n 个解。

### 输入

第 1 行是测试数据的组数 T，后面跟着 T 行输入。每组测试数据包含一个正整数 n (1 ≤ n ≤ 92)。

### 输出

输出有 T 行，每行输出第 n 个八皇后串。

### 样例

**输入：**
```
2
1
92
```

**输出：**
```
15863724
84136275
```

### 我的代码

```cpp
#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

int res[92][8];
int path[8];
int count = 0;

void dfs(int n)
{
    if (n > 7)
    {
        for (int k = 0; k < n; k++)
            res[count][k] = path[k];
        count++;
        return;
    }

    for (int i = 1; i <= 8; i++)
    {
        int k;
        for (k = 0; k < n; k++)
        {
            if (path[k] == i || abs(path[k] - i) == abs(k - n))
                break;
        }
        if (k == n)
        {
            path[n] = i;
            dfs(n + 1);
        }
    }
}

int main()
{
    int T, n;
    memset(path, 0, sizeof(path));
    dfs(0);

    cin >> T;
    while (T--)
    {
        cin >> n;
        for (int i = 0; i < 8; i++)
            cout << res[n - 1][i];
        cout << endl;
    }
    return 0;
}
```

### 思路要点

- **题目本质**：与 LinK13 思路一致，但不需要输出所有解，而是支持"按编号查询第 n 个解"。8 皇后的解总数固定为 92 个，所以最适合的策略是**预计算 + 查表**：一次性生成全部解存入二维数组，之后每次查询 O(1) 直接输出。

- **预计算（打表）策略**：
  - 用 `res[92][8]` 存储所有解：92 行（每种解一行），8 列（8 个皇后的列号）。
  - `path[8]` 作为临时数组，在 DFS 过程中记录当前路径。
  - 全局计数器 `count` 从 0 开始，每找到一组完整解就把它拷贝进 `res[count]` 然后 `count++`。
  - DFS 回溯的过程与 LinK13 完全一致：逐行放置，`path[n] = i`，冲突检测，递归。

- **为什么 DFS 顺序天然对应字典序**：DFS 从第 0 行开始，每行从小到大（1→8）尝试列号。这样先找到的解，第 0 行的列号更小（或相等时看第 1 行……依次类推），把皇后串看作 8 位整数的话，先找到的就是较小的——恰好符合题目要求的"整数小的排前面"。

- **查询**：`while (T--)` 读入 n，直接 `res[n-1]` 索引到第 n 个解（数组下标从 0 开始，题目 n 从 1 开始，所以要 -1），遍历 8 列输出即可。

- **时间复杂度**：预计算阶段 O(8!) ≈ 40320 种尝试（实际更少因为剪枝），固定常数。每次查询 O(1)（只是读数组 + 输出 8 个数字）。总复杂度 O(T)。

- **一个有趣的点——为什么是 92**：8 皇后问题共有 92 个解（如果不考虑旋转和镜像对称，只算本质不同的解是 12 个）。这个数字是固定的，可以上网查证。如果 DFS 跑出来的不是 92，说明代码有 bug。

- **易错点**：
  - `memset(path, 0, sizeof(path))` 需要 `<cstring>` 头文件（代码中引入了但实际可以省略，因为 `path` 是全局数组会被零初始化）。
  - `dfs(0)` 从第 0 行开始（而非第 1 行），递归终止条件是 `n > 7`（即已经放置了第 0~7 行共 8 个皇后）。也可以写 `n == 8` 但 `n > 7` 更安全（防御性编程）。
  - 如果忘记给 `res` 赋值而直接 `res[count][k] = path[k]` 语法正确，但必须确保 `count` 不越界（92 在范围内）。

---

## LinK14.5 DFS试炼之n皇后问题

### 题目描述

n-皇后问题是指将 n 个皇后放在 n×n 的国际象棋棋盘上，使得皇后不能相互攻击到，即任意两个皇后都不能处于同一行、同一列或同一斜线上。

### 输入

共一行，包含整数 n（1 ≤ n ≤ 12）。

### 输出

每个解决方案占 n 行，每行输出一个长度为 n 的字符串表示棋盘状态：`.` 表示空位，`Q` 表示皇后。每个方案输出完成后，输出一个空行。

### 样例

**输入：**
```
4
```

**输出：**
```
.Q..
...Q
Q...
..Q.

..Q.
Q...
...Q
.Q..
```

### 我的代码

```cpp
#include <iostream>
using namespace std;

const int N = 20;
int n;
char g[N][N];
bool col[N], dg[N], udg[N];

void dfs(int u)
{
    if (u == n)
    {
        for (int i = 0; i < n; i++) puts(g[i]);
        puts("");
        return;
    }

    for (int i = 0; i < n; i++)
        if (!col[i] && !dg[u + i] && !udg[n - u + i])
        {
            g[u][i] = 'Q';
            col[i] = dg[u + i] = udg[n - u + i] = true;
            dfs(u + 1);
            col[i] = dg[u + i] = udg[n - u + i] = false;
            g[u][i] = '.';
        }
}

int main()
{
    cin >> n;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            g[i][j] = '.';
    dfs(0);
    return 0;
}
```

### 思路要点

- **题目本质**：与 LinK13 一样是 N 皇后问题，但输出格式不同——需要输出完整的棋盘图案（`.` 和 `Q`），每个方案间用空行分隔。此外，这题使用了布尔数组优化冲突检测，是更标准的"N 皇后模板"写法。

- **布尔数组优化冲突检测（模板级写法）**：
  - `col[i]`：第 i 列是否已被占用。`true` 表示已有皇后。
  - `dg[u + i]`：主对角线（左上→右下方向）是否被占用。数学推导：在同一条主对角线上的格子，它们的 `行号 + 列号` 是定值。对于第 u 行第 i 列的格子，这个值是 `u + i`。所以用 `dg[u + i]` 就能标记/查询这条对角线。
  - `udg[n - u + i]`：副对角线（右上→左下方向）是否被占用。数学推导：在同一条副对角线上的格子，它们的 `行号 - 列号` 是定值。直接用 `u - i` 会有负数（当 i > u 时），所以统一偏移 n 得到 `n - u + i`（也可以用 `u - i + n`，效果相同，都保证非负）。
  - 三个数组的容量设计：`col[N]` 需要覆盖 0~n-1 列，`dg[N]` 和 `udg[N]` 需要覆盖 `u+i` 的范围（最大约 n+n=2n），所以 `const int N = 20` 对于 n ≤ 12 绰绰有余。

- **回溯三部曲**——放置一个皇后要做三件事：
  1. **做选择**：`g[u][i] = 'Q'`，标记三个数组 `col[i] = dg[u+i] = udg[n-u+i] = true`。
  2. **递归**：`dfs(u + 1)` 进入下一行。
  3. **撤销选择（回溯）**：`col[i] = dg[u+i] = udg[n-u+i] = false`，`g[u][i] = '.'` 恢复为空位。撤销是关键——只有这样，for 循环尝试下一列时，棋盘和标记数组才能回到"没放过"的状态。

- **棋盘初始化**：所有格子初始化为 `'.'`（用双重循环填充）。只有放置皇后时才改为 `'Q'`，回溯时恢复为 `'.'`。

- **输出**：`puts(g[i])` 直接输出 c-string 的一行（`g[i]` 是 `char[N]`，以 `\0` 结尾）。`puts("")` 输出一个空行，用于分隔不同方案。

- **与 LinK13 的对比**：

  | 方面 | LinK13 | LinK14.5 |
  |------|--------|----------|
  | 冲突检测 | O(n) 遍历 | O(1) 布尔数组 |
  | 输出格式 | 数字串（2413） | 棋盘图案（Q / .） |
  | 方案分隔 | 无 | 空行分隔 |
  | 回溯方式 | 隐式（循环覆盖） | 显式（设为 false / '.'） |
  | 代码复杂度 | 更简短 | 更高效、更规范 |

- **复杂度分析**：与 LinK13 相同，O(N!) 级别，但常数更小（布尔数组 O(1) vs 遍历 O(n)）。N ≤ 12 完全可以接受。

- **易错点**：
  - 对角线索引的偏移方式不是唯一的：`dg[u+i]` 和 `udg[n-u+i]` 换成 `udg[u-i+n-1]` 也能工作，只要保证索引不越界、映射关系正确即可。理解原理比死记下标公式更重要。
  - 三个布尔数组一定要记得回溯（恢复为 false），否则后续搜索会错误地认为某些列/对角线已被占用。
  - 输出需要 `#include <cstdio>`（或使用 `printf/puts`），代码中没有显式引入但可能通过 iostream 间接可用。严格来说建议加上 `<cstdio>`。

---

## LinK16 放苹果

### 题目描述

把 M 个同样的苹果放在 N 个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的放法？注意：5,1,1 和 1,5,1 是同一种放法（盘子相同、苹果相同）。

### 输入

第一行是测试数据的数目 t（0 ≤ t ≤ 20）。以下每行均包含二个整数 M 和 N，以空格分开。0 ≤ M, N ≤ 10。

### 输出

对输入的每组数据 M 和 N，用一行输出相应的 K（正整数，代表共有几种放法）。

### 样例

**输入：**
```
1
7 3
```

**输出：**
```
8
```

### 我的代码

```cpp
#include <iostream>
using namespace std;

int f(int x, int y)
{
    if (x < y)
        return f(x, x);

    if (x == 0)
        return 1;

    if (y <= 0)
        return 0;

    return f(x, y - 1) + f(x - y, y);
}

int main()
{
    int t, x, y;
    cin >> t;

    while (t--)
    {
        cin >> x >> y;
        cout << f(x, y) << endl;
    }
    return 0;
}
```

### 思路要点

- **题目本质**：经典的"整数划分"问题（也叫"放苹果"问题）——把 M 个不可区分的物品放入 N 个不可区分的容器，允许容器为空。由于苹果相同、盘子相同，方案只取决于每个盘子里有几个苹果（不考虑盘子的排列顺序）。

- **状态定义**：`f(m, n)` 表示把 m 个相同的苹果放入 n 个相同的盘子的方案总数。注意盘子和苹果都是"同样的"（不可区分），所以 5,1,1 和 1,5,1 算同一种——我们只关心每个盘子的苹果数量组成的多重集。

- **递推关系推导**（核心）：
  - **情况 1：m < n（苹果比盘子少）**——即使每个盘子最多放 1 个苹果，也会有 n-m 个盘子空着。空着的盘子不影响计数（盘子不可区分），所以问题退化为 `f(m, m)`（用 m 个盘子装 m 个苹果），多余的盘子直接忽略。
  - **情况 2：m == 0（没有苹果）**——所有盘子都空着，只有 1 种方案。这是递推的边界（base case）。
  - **情况 3：n <= 0（没有盘子）**——有苹果但没盘子，不可能，返回 0。也是边界条件。
  - **情况 4：一般情况 m ≥ n > 0**——递推核心：`f(m, n) = f(m, n-1) + f(m-n, n)`。
    - **第一项 `f(m, n-1)`**：至少有一个盘子是空的。既然有一个空盘，问题等价于把 m 个苹果放入 n-1 个盘子（那个空盘子不影响结果）。这一项覆盖了所有"有空盘子"的方案。
    - **第二项 `f(m-n, n)`**：所有盘子都至少放 1 个苹果。既然每个盘子至少 1 个，我们可以先从 m 个苹果中拿出 n 个，每个盘子预先放 1 个，然后把剩下的 m-n 个苹果任意分配到 n 个盘子中。由于每个盘子已经"非空"了，剩下的分配可以有空盘也可以没有。
    - 这两项**不重不漏**：任何方案要么有空盘（第一项覆盖），要么完全没有空盘（第二项覆盖）。两者互斥且完备。

- **递推过程示例**（M=7, N=3）：
  ```
  f(7, 3) = f(7, 2) + f(4, 3)
  f(7, 2) = f(7, 1) + f(5, 2)
  f(7, 1) = f(7, 0) + f(6, 1) = 0 + ... → 最终 1
  ...
  → f(7, 3) = 8
  ```
  7 个苹果 3 个盘子的 8 种分法是：(7,0,0), (6,1,0), (5,2,0), (5,1,1), (4,3,0), (4,2,1), (3,3,1), (3,2,2)。

- **递归 vs DP**：代码使用的是带记忆化的递归（虽然这里没有显式 memo），数据范围 M, N ≤ 10 非常小，纯递归的计算量也很有限。如果数据范围增大（如 M, N ≤ 100），就需要改用 DP 或加记忆化数组避免重复计算，状态数 O(M×N)。

- **复杂度分析**：纯递归最坏约 O(2^(M+N)) 但实际因为分支中 m 或 n 递减，远小于此。M, N 都不超过 10，完全可以接受。

- **易错点**：
  - 递归边界条件的顺序很重要：`m < n` 的判定必须放在 `n <= 0` 之前，因为当 m < n 时直接归约到 `f(m, m)`，m 可能为 0，最终会被 `m == 0` 捕获返回 1。如果先判断 `n <= 0`，会导致某些情况错误返回 0。
  - 不要忘记处理"全空"方案（m=0），这是一种合法方案（对应题目中"允许有的盘子空着不放"）。
  - 多组输入用 `while (t--)` 处理，cin 读入后立即调用 `f(x, y)`。

---

## LinK19 递归实现指数型枚举

### 题目描述

从 1∼n 这 n 个整数中随机选取任意多个，输出所有可能的选择方案。

### 输入

输入一个整数 n（1 ≤ n ≤ 15）。

### 输出

每行输出一种方案。同一行内的数必须升序排列，相邻两个数用恰好 1 个空格隔开。对于没有选任何数的方案，输出空行。各行（不同方案）之间的顺序任意（本题有 SPJ）。

### 样例

**输入：**
```
3
```

**输出：**
```

3
2
2 3
1
1 3
1 2
1 2 3
```

### 我的代码

```cpp
#include <iostream>
using namespace std;

const int N = 29;
int n;
bool st[N];

void dfs(int u)
{
    if (u > n)
    {
        for (int i = 1; i <= n; i++)
            if (st[i])
                cout << i << " ";
        cout << endl;
        return;
    }

    st[u] = true;
    dfs(u + 1);

    st[u] = false;
    dfs(u + 1);
}

int main()
{
    cin >> n;
    dfs(1);
    return 0;
}
```

### 思路要点

- **题目本质**：生成集合 {1, 2, ..., n} 的所有子集（幂集）。每个元素要么选、要么不选，共 2ⁿ 种可能。这是指数型枚举（与排列组合型枚举不同，排列是 n! 级别）。

- **DFS 决策树**：把问题看作一棵二叉树——
  - 从 u=1 开始，每层决策一个数：选还是不选。
  - 左分支：`st[u] = true`（选），递归 `dfs(u+1)`。
  - 右分支：`st[u] = false`（不选），递归 `dfs(u+1)`。
  - 当 `u > n` 时（即 n 个数的决策都已完成），到达叶子节点，输出当前选择的子集。

- **为什么输出天然升序**：因为 DFS 按照 1 → 2 → ... → n 的顺序决策，遍历 `st[1..n]` 时也是从小到大检查，所以输出的每个方案内数字必然是升序的。这也符合题目要求"同一行内的数必须升序排列"。

- **状态数组 st[] 的设计**：
  - `st[i] = true` 表示数字 i 被选入当前子集。
  - `st[i] = false` 表示不选。
  - 注意这里没有显式的"回溯撤销"——因为每一层在 `st[u]=true` 递归返回后，紧接着就执行 `st[u]=false` 并再次递归，两次递归的路径互不干扰。第一次递归返回时 `st[u]` 可能还是 true，但第二段会把它覆盖为 false。对于本层而言已经完成了所有子节点，本层返回后上一层的 `st[u-1]` 仍然是上一层的值，没有问题。

- **递归树结构示例（n=3）**：
  ```
                    []
            /              \
        选1: [1]          不选1: []
       /    \             /     \
  选2:[1,2] 不选2:[1] 选2:[2] 不选2:[]
    /  \      /  \      /  \     /  \
  ...（共 8 个叶子）
  ```
  每个叶子对应一个子集，正好 2³ = 8 个。

- **空子集的处理**：`st[1..n]` 全为 false 时，遍历不会输出任何数字，只输出一个 `endl`（空行）。这是合法的方案（"选了 0 个数字"），样例的第一行就是空的。

- **复杂度分析**：方案总数为 2ⁿ，n ≤ 15 时最多 32768 种方案。每个方案输出最多 n 个数字，总输出量约 2ⁿ × n ≈ 5×10⁵ 个数字，完全可行。时间复杂度 O(n·2ⁿ)，空间复杂度 O(n)（递归栈 + st 数组）。

- **扩展思考——位运算替代法**：这题也可以不用 DFS，直接用一个整数从 0 到 2ⁿ-1 循环，整数的二进制第 i 位为 1 表示选 i。这种方法代码更短，且方案按字典序排列。例如 n=3：
  ```
  for (int mask = 0; mask < (1 << n); mask++) {
      for (int i = 1; i <= n; i++)
          if (mask >> (i-1) & 1)
              cout << i << " ";
      cout << endl;
  }
  ```
  DFS 和位运算两种写法都应该掌握，DFS 更直观，位运算更简洁。

- **易错点**：
  - 数组索引：`st[u]` 中 u 的范围是 1~n，所以数组大小需要 ≥ n+1（代码中 N=29 是够的）。不要从 0 开始。
  - 输出时每个数字后有一个空格，包括最后一个数字后也有（代码写的是 `cout << i << " "`）。虽然 OJ 使用了 SPJ（Special Judge），行末有多余空格通常也能通过，但在非 SPJ 的题目中这可能被判错。
  - 这题有 SPJ（Special Judge），意味着方案的排列顺序任意，不用担心 DFS 顺序是否"正确"——只要所有方案都输出且每种恰好一次即可。

---

## LinK05 假币问题

### 题目描述

林克有 12 枚银币（A-L），其中 11 枚真币和 1 枚假币。假币重量不同但不知道是轻还是重。天平称了三次，给定三次称量结果，找出假币并判断轻重。

### 输入

第一行 n 表示测试组数。每组三行，每行格式：`左边硬币 右边硬币 结果`（结果：`even`/`up`/`down`）。

### 样例

**输入：**
```
1
ABCD EFGH even
ABCI EFJK up
ABIJ EFGH even
```

**输出：**
```
K is the counterfeit coin and it is light.
```

### 我的代码

```cpp
#include <iostream>
#include <cstring>
using namespace std;

string Left[3], Right[3], result[3];

bool isfeitcoin(char icoin, bool islight)
{
    string c;
    c.push_back(icoin);
    for (int i = 0; i < 3; i++)
    {
        string l = Left[i], r = Right[i];
        if (!islight) swap(l, r);
        switch (result[i][0])
        {
            case 'e':
                if (l.find(c) != string::npos || r.find(c) != string::npos)
                    return false;
                break;
            case 'u':
                if (r.find(c) == string::npos) return false;
                break;
            case 'd':
                if (l.find(c) == string::npos) return false;
                break;
        }
    }
    return true;
}

int main()
{
    int t; cin >> t;
    while (t--)
    {
        for (int i = 0; i < 3; ++i)
            cin >> Left[i] >> Right[i] >> result[i];
        for (char icoin = 'A'; icoin <= 'L'; icoin++)
        {
            if (isfeitcoin(icoin, true))
            { cout << icoin << " is the counterfeit coin and it is light." << endl; break; }
            else if (isfeitcoin(icoin, false))
            { cout << icoin << " is the counterfeit coin and it is heavy." << endl; break; }
        }
    }
    return 0;
}
```

### 思路要点

- **枚举报枚 + 假设检验**：对 A-L 共 12 枚币逐一假设为假币，再分别假设轻或重，代入三次称量结果验证是否一致。
- 如果假设假币轻(`islight=true`)：天平右边高(`up`)时假币应出现在右边，右边低(`down`)时假币应在左边。
- 反之假币重时左右交换。用 swap(l, r) 统一处理两种假设。
- O(12×2×3) 常数时间。

---

## LinK09 汉诺塔I

### 题目描述

三根杆 A、B、C，A 有 N 个穿孔圆盘（由下到上变小）。移到 C 杆，每次只能移一个，大盘不能叠小盘。输出移动步骤。

### 样例

**输入：** `3`
**输出：** `A->C / A->B / C->B / A->C / B->A / B->C / A->C`

### 我的代码

```cpp
#include <iostream>
using namespace std;

void move(char start, char target) { cout << start << "->" << target << endl; }

void hanoi(int n, char start, char other, char target)
{
    if (n == 1) { move(start, target); return; }
    hanoi(n - 1, start, target, other);
    move(start, target);
    hanoi(n - 1, other, start, target);
}

int main() { int n; cin >> n; hanoi(n, 'A', 'B', 'C'); return 0; }
```

### 思路要点

- **经典递归**：将 N-1 个盘借助 target 移到 other → 最大盘从 start 移到 target → N-1 个盘从 other 借助 start 移到 target。
- 递推关系：移动次数 T(n) = 2T(n-1) + 1 = 2ⁿ - 1。
- 递归终止：n==1 时直接移动。

---

## LinK10 汉诺塔II

### 题目描述

与 I 相同，但输入包含杆子编号（如 `3 a b c`），输出格式为 `盘号:起始->目标`（如 `1:a->c`）。

### 样例

**输入：** `3 a b c`

**输出：**
```
1:a->c
2:a->b
1:c->b
3:a->c
1:b->a
2:b->c
1:a->c
```

### 我的代码

```cpp
#include <iostream>
using namespace std;

void move(int id, char start, char target) { cout << id << ":" << start << "->" << target << endl; }

void hanoi(int n, int id, char start, char other, char target)
{
    if (n == 1) { move(id, start, target); return; }
    hanoi(n - 1, id, start, target, other);
    int newid = id + n - 1;
    move(newid, start, target);
    hanoi(n - 1, id, other, start, target);
}

int main()
{
    char a, b, c; int n;
    cin >> n >> a >> b >> c;
    hanoi(n, 1, a, b, c);
}
```

### 思路要点

- 在汉诺塔 I 的基础上增加**盘号追踪**。底部 N 个盘中，最顶的盘从 id 开始。递归时最大盘的编号 = id+n-1（因为上面有 n-1 个更小的盘）。

---

## LinK15 爬天梯

### 题目描述

天梯 N 阶，每次可以走 1 阶或 2 阶，求总共有多少种不同走法。

### 样例

**输入：** `3` → **输出：** `3`

### 我的代码

```cpp
#include <iostream>
using namespace std;
const int mod = 1000000007;

int stairs(int n)
{
    if (n <= 1) return 1;
    return (stairs(n - 1) + stairs(n - 2)) % mod;
}

int main() { int N; cin >> N; cout << stairs(N) << endl; return 0; }
```

### 思路要点

- **斐波那契数列**：f(n) = f(n-1) + f(n-2)，f(0)=f(1)=1。
- 注意答案取模 1000000007。N ≤ 46，递归+备忘或直接递归都可以（代码中的纯递归会重复计算，但 N 小可接受）。

---

## LinK20 递归实现组合型枚举

### 题目描述

从 1∼n 中随机选出 m 个，输出所有可能的组合方案。行内升序，行间字典序。

### 样例

**输入：** `5 3` → 输出 C(5,3) = 10 种组合。

### 我的代码

```cpp
#include <iostream>
using namespace std;

const int N = 30;
int n, m, path[N];

void dfs(int u, int start)
{
    if (u > m)
    {
        for (int i = 1; i <= m; i++) cout << path[i] << " ";
        cout << endl;
    }
    else
    {
        for (int i = start; i <= n; i++)
        { path[u] = i; dfs(u + 1, i + 1); }
    }
}

int main() { cin >> n >> m; dfs(1, 1); return 0; }
```

### 思路要点

- **组合枚举 DFS**：每次从 start 到 n 选一个数，下一个递归从 i+1 开始（保证升序不重复）。
- 与子集枚举不同：这里是选固定 m 个，递归深度固定 m 层，叶子数 C(n,m)。

---

## LinK21 递归实现排列型枚举

### 题目描述

输出 1∼n 的所有排列，按字典序从小到大。

### 样例

**输入：** `3` → 输出 123、132、213、231、312、321。

### 我的代码

```cpp
#include <iostream>
using namespace std;

const int N = 15;
int n, path[N];
bool st[N];

void dfs(int u)
{
    if (u > n)
    {
        for (int i = 1; i <= n; i++) cout << path[i] << " ";
        cout << endl;
    }
    else
    {
        for (int i = 1; i <= n; i++)
            if (!st[i])
            { path[u] = i; st[i] = true; dfs(u + 1); st[i] = false; }
    }
}

int main() { cin >> n; dfs(1); return 0; }
```

### 思路要点

- **排列枚举 DFS**：每位从 1 到 n 选未被标记的数，使用 `st[]` 标记使用状态，回溯时恢复。
- 与组合的区别：排列中每个位置都可以选任何未被使用的数，顺序敏感。

---

## LinK27 大数排序

### 题目描述

给定长度为 n（≤ 100000）的数列，用快速排序按升序输出。

### 样例

**输入：** `12` + 12个大整数 → 输出排序后序列。

### 我的代码

```cpp
#include <iostream>
using namespace std;

const int N = 1000010;
int q[N];

void quick_sort(int q[], int l, int r)
{
    if (l >= r) return;
    int i = l - 1, j = r + 1, x = q[l + r >> 1];
    while (i < j)
    {
        do i++; while (q[i] < x);
        do j--; while (q[j] > x);
        if (i < j) swap(q[i], q[j]);
    }
    quick_sort(q, l, j);
    quick_sort(q, j + 1, r);
}

int main()
{
    int n; scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &q[i]);
    quick_sort(q, 0, n - 1);
    for (int i = 0; i < n; i++) printf("%d ", q[i]);
    return 0;
}
```

### 思路要点

- **快速排序模板**：双指针 partition，选取中间值为 pivot。`i = l-1, j = r+1` 保证首轮 do-while 正确。递归处理左右区间。

---

## LinK30 归并排序

### 题目描述

使用归并排序对数组排序，N ≤ 100000。

### 样例

输入 `3 1 2 4 5`，输出 `1 2 3 4 5`。

### 我的代码

```cpp
#include <iostream>
using namespace std;

const int N = 100007;
int numbers[N], tmp[N];

void mergesort(int nums[], int left, int right)
{
    if (left >= right) return;
    int mid = left + right >> 1;
    mergesort(nums, left, mid), mergesort(nums, mid + 1, right);
    int k = 0, p = left, q = mid + 1;
    while (p <= mid && q <= right)
        tmp[k++] = nums[p] <= nums[q] ? nums[p++] : nums[q++];
    while (p <= mid) tmp[k++] = nums[p++];
    while (q <= right) tmp[k++] = nums[q++];
    for (int i = left, k = 0; i <= right; i++, k++) nums[i] = tmp[k];
}

int main()
{
    int n; scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &numbers[i]);
    mergesort(numbers, 0, n - 1);
    for (int i = 0; i < n; i++) printf("%d ", numbers[i]);
    return 0;
}
```

### 思路要点

- **归并排序模板**：分治递归 → 两路归并 → 复制回原数组。O(N log N)，稳定排序。

---

## LinK31 求排列的逆序数

### 题目描述

给定 n 个数的排列，求其逆序对数量（i < j 且 a_i > a_j）。n ≤ 100000。

### 样例

输入 `2 6 3 4 5 1`，输出 `8`。

### 我的代码

```cpp
#include <iostream>
using namespace std;

const int N = 100007;
int numbers[N], tmp[N];

long long mergesort(int nums[], int left, int right)
{
    if (left >= right) return 0;
    int mid = left + right >> 1;
    long long result = mergesort(nums, left, mid) + mergesort(nums, mid + 1, right);
    int k = 0, p = left, q = mid + 1;
    while (p <= mid && q <= right)
    {
        if (nums[p] <= nums[q]) tmp[k++] = nums[p++];
        else { result += mid - p + 1; tmp[k++] = nums[q++]; }
    }
    while (p <= mid) tmp[k++] = nums[p++];
    while (q <= right) tmp[k++] = nums[q++];
    for (int i = left, k = 0; i <= right; i++, k++) nums[i] = tmp[k];
    return result;
}

int main()
{
    int n; scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &numbers[i]);
    cout << mergesort(numbers, 0, n - 1);
    return 0;
}
```

### 思路要点

- **归并排序求逆序对**：归并过程中，当右半元素 `nums[q]` 小于左半元素 `nums[p]` 时，左半从 p 到 mid 的所有元素都大于 `nums[q]`，贡献 mid-p+1 个逆序对。
- 答案可能超过 int 范围（n=100000 时最坏约 5×10⁹），使用 `long long`。

---

## LinK38 林克的命运之阵

### 题目描述

在方格矩阵中从任意位置出发，只能向下/左/右走，不能重复访问。求走 n 步的不同路径数。n ≤ 20。

### 样例

n=2 → 7 种；n=20 → 54608393。

### 我的代码

```cpp
#include <iostream>
#include <cstring>
using namespace std;

const int N = 70;
int fates[N][N];
int dx[3] = {0, 0, 1}, dy[3] = {-1, 1, 0};

long long dfs(int i, int j, int n)
{
    if (n == 0) return 1;
    long long res = 0;
    fates[i][j] = 1;
    for (int k = 0; k < 3; k++)
    {
        int x = i + dx[k], y = j + dy[k];
        if (fates[x][y] == 0) res += dfs(x, y, n - 1);
    }
    fates[i][j] = 0;
    return res;
}

int main()
{
    int n; cin >> n;
    cout << dfs(0, N / 2, n) << endl;
    return 0;
}
```

### 思路要点

- **DFS 回溯 + 网格标记**：从中心位置出发，向三个方向（下、左、右）递归探索，不走回头路。`fates[][]` 标记已访问位置，回溯恢复。时间复杂度 O(3ⁿ)，n≤20 可接受。

---

## LinK39 净化迷雾森林

### 题目描述

W×H 网格，`.`表示可走，`#`表示墙，`@`表示起点。从起点走四方向可达的 `.` 区域数量（Flood Fill）。

### 样例

6×9 地图，输出 45。

### 我的代码

```cpp
#include <iostream>
using namespace std;

int w, h;
char fogforest[27][27];

int dfs(int i, int j)
{
    int res = 1;
    fogforest[i][j] = '#';
    int dx[4] = {0, -1, 0, 1}, dy[4] = {1, 0, -1, 0};
    for (int k = 0; k < 4; k++)
    {
        int x = i + dx[k], y = j + dy[k];
        if (x >= 0 && y >= 0 && x < h && y < w && fogforest[x][y] == '.')
            res += dfs(x, y);
    }
    return res;
}

int main()
{
    while (cin >> w >> h, w || h)
    {
        int startx, starty;
        for (int i = 0; i < h; i++)
            for (int j = 0; j < w; j++)
            {
                cin >> fogforest[i][j];
                if (fogforest[i][j] == '@') { startx = i; starty = j; }
            }
        cout << dfs(startx, starty) << endl;
    }
}
```

### 思路要点

- **DFS Flood Fill（种子填充）**：从起点递归访问所有可达的 `.` 格，访问后改为 `#` 避免重复。

---

## LinK43 求二进制中1的个数

### 题目描述

输入 32 位整数（可为负，采用补码表示），用 lowbit 求其二进制中 1 的个数。

### 样例

输入 `9` → `2`；输入 `-2` → `31`。

### 我的代码

```cpp
int lowbit(int n) { return n & -n; }

int NumberOf1(int n)
{
    int res = 0;
    while (n) { n -= lowbit(n); res++; }
    return res;
}
```

### 思路要点

- **lowbit 技巧**：`n & -n` 能取出 n 二进制表示中最低位的 1。每次减去 lowbit 消除一个 1，同时计数器 +1，直到 n=0。

---

## LinK44 二进制中1的最低位位置

### 题目描述

给定 16 位数，求其二进制最低位 1 的位置。用打表法 + lowbit。

### 样例

`9` → `0`（二进制 1001，最低位 1 在第 0 位）；`8` → `3`。

### 我的代码

```cpp
#include <iostream>
using namespace std;

#define N 17
int log[1 << N];

void BuildLogTable(int n) { for (int i = 0; i < n; i++) log[1 << i] = i; }

inline int lowbit(int n) { return n & -n; }

int main()
{
    BuildLogTable(N);
    int n; cin >> n;
    cout << log[lowbit(n)];
    return 0;
}
```

### 思路要点

- **打表法**：预处理 `log[1<<i] = i`，即 2ⁱ → i 的映射。`lowbit(n)` 取出最低位 1 的值（必然是 2 的幂），查表 O(1) 得到位置。

---

## LinK45 真假记忆碎片

### 题目描述

给定初始 9×9 数独矩阵（含 0 表示空位）和一份声称是解的 9×9 矩阵，判断该解是否合法（与初始矩阵的非零格一致，且满足数独规则）。

### 样例

合法解 → `Yes`；不合法 → `No`。

### 我的代码

```cpp
#include <iostream>
#include <cstring>
using namespace std;

const int N = 9, M = 3;
string memory[N] = {{"530070000"}, {"600195000"}, {"098000060"},
                    {"800060003"}, {"400803001"}, {"700020006"},
                    {"060000280"}, {"000419005"}, {"000080079"}};
int a[N][N], b[N][N];
bool st[N + 1];

bool check_input() { /* 检查每行长度=9且数字与初始矩阵一致 */ }
bool check_row()   { /* 每行1-9不重复 */ }
bool check_col()   { /* 每列1-9不重复 */ }
bool check_block() { /* 每个3x3块1-9不重复 */ }

int main()
{
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            a[i][j] = memory[i][j] - '0';
    if (check_input() && check_row() && check_col() && check_block())
        cout << "Yes" << endl;
    else cout << "No" << endl;
    return 0;
}
```

### 思路要点

- **数独验证四步**：检查输入格式、每行、每列、每个 3×3 九宫格内数字 1~9 是否恰好各出现一次。用 `st[]` 布尔数组判重。
