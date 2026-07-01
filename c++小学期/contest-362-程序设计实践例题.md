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

- 入门题，直接 `cin >> a >> b` 读取，`cout << a + b` 输出即可。
- 数据范围 0~10⁸，和最大 2×10⁸，用 `int` 足够（32 位上限约 2.1×10⁹）。

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

- **四重循环枚举**：N ≤ 100，四重循环最多约 100⁴/6 ≈ 1.6×10⁷ 次，在时限内可行。
- **剪枝优化**：预先计算 `a3 = a³` 避免在内层循环中重复计算。
- **有序枚举**：令 b ≤ c ≤ d，循环范围分别从上一个变量的值开始（`c = b`, `d = c`），既满足条件又避免重复组合。
- **注意**：所有变量从 2 开始（大于 1），都不超过 N。

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

- **中国剩余定理 / 逐步试探法**：目标是找到最小的 k > d，使得 `(k-p)%23==0`、`(k-e)%28==0`、`(k-i)%33==0` 同时成立。
- **三步跳跃法**：
  1. 先从 `d+1` 开始，每次 `+1`，找到第一个满足体力周期 `(k-p)%23==0` 的 k。
  2. 然后每次 `+23`（保证体力周期始终满足），找到同时满足感情周期 `(k-e)%28==0` 的 k。
  3. 最后每次 `+23×28=644`（保证体力、感情周期始终满足），找到同时满足智力周期 `(k-i)%33==0` 的 k。
- 这样最坏约 21252/644 ≈ 33 次即可收敛，远优于逐一枚举 21252 天。
- **多组输入**：用 `while (cin >> ... && p != -1)` 读取，以 `-1 -1 -1 -1` 结束。
- **caseNumber 计数器**：每组数据编号从 1 递增。

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

- **多组数据处理**：`while (T--)` 遍历每组测试数据。
- **vector + sort**：用 `vector<int>` 存储每组数据，`sort()` 默认升序。
- **输出格式**：行末无多余空格，用 `if (i > 0) cout << " "` 控制。
- 注意每组 N 最大可达 1000000，用 `vector` 动态扩容，不需要预分配。

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

- **DFS 回溯**：逐行放置皇后，`res[row] = col` 记录每行皇后所在的列。
- **冲突检测**：同一列 `res[k] == i`，同一对角线 `abs(res[k] - i) == abs(k - n)`（即行差 = 列差）。
- **递归终止**：`n == N` 时输出当前排列，`res` 中的数字拼接为长度为 N 的整数串。
- 时间复杂度 O(N!)，N ≤ 13 可接受。

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

- **预计算 + 查表**：提前 DFS 生成全部 92 种解存入 `res[92][8]`，查询时 O(1) 输出。
- DFS 使用回溯（同 LinK13），字典序恰好对应整数从小到大的顺序。
- **多组查询**：`while (T--)` 处理，直接 `res[n-1]` 索引第 n 个解（n 从 1 开始）。
- 固定 8 皇后，计算量很小。

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

- **标准 N 皇后模板**：DFS + 布尔数组回溯。
- **对角线映射**：
  - 主对角线（左上→右下）：`dg[u + i]`，同一对角线上 `row + col` 为常数。
  - 副对角线（右上→左下）：`udg[n - u + i]`，同一对角线上 `row - col` 为常数，加上偏移 n 避免负索引。
- `puts(g[i])` 直接输出 c-string 的一行。
- 递归完一整行 `u` 后输出棋盘，再输出空行分隔方案。

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

- **经典整数划分问题**：设 `f(m, n)` 为 m 个苹果放入 n 个盘子的方案数。
- **递推关系**：
  - 若 `m < n`：必有空盘，等价于 `f(m, m)`。
  - 若 `m == 0`：只有一种方法（全空），返回 1。
  - 若 `n == 0`：无盘子，返回 0。
  - 一般情况 `f(m, n) = f(m, n-1) + f(m-n, n)`：
    - `f(m, n-1)`：至少有一个空盘子，等价于只用 n-1 个盘子。
    - `f(m-n, n)`：每个盘子至少放 1 个，等价于每个盘子先放一个，然后分配剩余的 m-n 个。
- 数据范围小（M, N ≤ 10），递归无性能问题。

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

- **子集枚举 DFS**：每个数有两种选择——选或不选。
  - `st[u] = true`：选当前数 u，然后递归处理 u+1。
  - `st[u] = false`：不选当前数 u，递归处理 u+1。
- **递归终止**：`u > n` 时遍历 `st[1..n]`，被标记为 `true` 的输出。
- 由于 DFS 按数值从小到大决策，输出天然保持升序。
- N ≤ 15，共 2¹⁵ = 32768 种方案，完全可行。
- **注意**："不选任何数"的方案输出空行（样例第一行就是空的）。
