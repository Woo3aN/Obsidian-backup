# 2026年程序设计实践例题 — 题解集

> 实验：2026年程序设计实践例题(05李胜睿班)  
> 每题三要素：思路 → 关键代码 → 总结  
> 共 44 题，按专题分组

---

## 目录

### 基础入门
1. [[#LinK01 A+B|LinK01 A+B]]
2. [[#LinK02 完美立方|LinK02 完美立方]]
3. [[#LinK03 人的周期|LinK03 人的周期]]
4. [[#LinK04 排序考试|LinK04 排序考试]]
5. [[#LinK05 假币问题|LinK05 假币问题]]

### 递归与分治
6. [[#LinK09 汉诺塔I|LinK09 汉诺塔I]]
7. [[#LinK10 汉诺塔II|LinK10 汉诺塔II]]
8. [[#LinK15 爬天梯|LinK15 爬天梯]]
9. [[#LinK16 放苹果|LinK16 放苹果]]

### 枚举
10. [[#LinK19 递归实现指数型枚举|LinK19 指数型枚举]]
11. [[#LinK20 递归实现组合型枚举|LinK20 组合型枚举]]
12. [[#LinK21 递归实现排列型枚举|LinK21 排列型枚举]]

### 排序
13. [[#LinK27 大数排序|LinK27 大数排序（快排）]]
14. [[#LinK30 归并排序|LinK30 归并排序]]
15. [[#LinK31 求排列的逆序数|LinK31 逆序数]]

### DFS 搜索
16. [[#LinK13 输出N皇后的全部摆法|LinK13 N皇后（输出全部）]]
17. [[#LinK14 求八皇后的第n种解|LinK14 八皇后（查表）]]
18. [[#LinK14.5 DFS试炼之n皇后问题|LinK14.5 N皇后（棋盘输出）]]
19. [[#LinK38 林克的命运之阵|LinK38 命运之阵]]

### BFS & 图论
20. [[#LinK39 净化迷雾森林|LinK39 净化迷雾森林（DFS）]]
21. [[#LinK51 净化迷雾森林(广搜)|LinK51 净化迷雾森林（BFS）]]
22. [[#LinK52 波克布林的巡逻范围|LinK52 巡逻范围]]
23. [[#LinK53 加农的入侵|LinK53 加农的入侵]]
24. [[#LinK57 Dijkstra求最短路(1)|LinK57 Dijkstra]]

### 位运算
25. [[#LinK43 求二进制中1的个数|LinK43 二进制中1的个数]]
26. [[#LinK44 二进制中1的最低位位置|LinK44 最低位1位置]]

### 数独系列
27. [[#LinK45 真假记忆碎片|LinK45 数独验证]]
28. [[#LinK46 寻找林克的回忆(1)|LinK46 数独求解 I]]
29. [[#LinK47 寻找林克的回忆(2)|LinK47 数独求解 II（位运算）]]
30. [[#LinK48 寻找林克的回忆(3)|LinK48 靶形数独]]

### 动态规划 — 入门
31. [[#LinK62 数字三角形|LinK62 数字三角形]]
32. [[#LinK69 摘花生|LinK69 摘花生]]
33. [[#LinK70 最低通行费|LinK70 最低通行费]]

### 动态规划 — 背包
34. [[#LinK63 林克的01背包|LinK63 01背包]]
35. [[#LinK64 林克的完全背包|LinK64 完全背包]]
36. [[#LinK65 多重背包问题(1)|LinK65 多重背包（朴素）]]
37. [[#LinK66 多重背包问题(2)|LinK66 多重背包（二进制优化）]]
38. [[#LinK67 分组背包问题|LinK67 分组背包]]
39. [[#LinK68 混合背包问题|LinK68 混合背包]]

### 动态规划 — LIS/LCS
40. [[#LinK71 最长上升子序列|LinK71 LIS（朴素）]]
41. [[#LinK72 最长上升子序列(2)|LinK72 LIS（贪心+二分）]]
42. [[#LinK73 拦截导弹|LinK73 拦截导弹]]
43. [[#LinK75 最长公共子序列|LinK75 LCS]]

### 动态规划 — 区间DP
44. [[#LinK76 石子合并|LinK76 石子合并]]

---

## 基础入门

### LinK01 A+B

**思路**：OI 的 Hello World，考察 `cin >> a >> b` 输入和 `cout << a + b` 输出，注意不要输出多余提示文字。

**关键代码**：
```cpp
int a, b;
cin >> a >> b;          // cin 自动跳过空白字符
cout << a + b << endl;  // 直接输出和，无需多余提示
```

**总结**：OJ 判题只看输出内容，多余提示（如 "Please input:"）会导致 Wrong Answer。数据范围 $0 \le A,B \le 10^8$，用 `int` 足够。

---

### LinK02 完美立方

**思路**：四重循环枚举 a,b,c,d（b≤c≤d 去重），检查 $a^3 = b^3 + c^3 + d^3$，N≤100 时约 $1.6\times 10^7$ 次运算可过。

**关键代码**：
```cpp
for (a = 2; a <= N; a++) {
    int a3 = a * a * a;              // 预计算 a³，避免内层重复计算
    for (b = 2; b < N; b++)
        for (c = b; c < N; c++)      // b≤c≤d 天然有序，避免重复排列
            for (d = c; d < N; d++)
                if (a3 == b*b*b + c*c*c + d*d*d)
                    cout << "Cube = " << a << ", Triple = (" << b << "," << c << "," << d << ")" << endl;
}
```

**总结**：枚举时利用有序约束（b≤c≤d）能避免同一组合的重复排列。`a*a*a` 提到最外层是常数优化好习惯。

---

### LinK03 人的周期

**思路**：找 > d 的最小 k 同时满足 `(k-p)%23==0`、`(k-e)%28==0`、`(k-i)%33==0`。用"三步跳跃法"：先满足第一个条件（步长 1），再满足第二个（步长 23），最后满足第三个（步长 23×28=644），最坏约 23+28+33=84 次循环。

**关键代码**：
```cpp
int k;
for (k = d + 1; (k - p) % 23; ++k);       // 从 d+1 开始，找到第一个满足体力周期的
for (; (k - e) % 28; k += 23);            // 保持体力周期满足，步长 23
for (; (k - i) % 33; k += 23 * 28);       // 保持前两个满足，步长 644
cout << "Case " << caseNumber << ": the next triple peak occurs in " << k - d << " days." << endl;
```

**总结**：逐步缩小搜索步长的"跳跃法"是解决多条件同余问题的利器——步长 = 已满足条件的模数之积。答案不超过 21252（23×28×33）。

---

### LinK04 排序考试

**思路**：多组数据排序，用 `vector` 动态存数据，`sort()` 直接排序。N 最大 $10^6$，`vector` 在堆上分配避免栈溢出。

**关键代码**：
```cpp
int T; cin >> T;
while (T--) {
    int N; cin >> N;
    vector<int> v(N);
    for (int i = 0; i < N; i++) cin >> v[i];
    sort(v.begin(), v.end());               // STL 排序 O(N log N)
    for (int i = 0; i < N; i++) {
        if (i > 0) cout << " ";             // 控制空格，行末无多余空格
        cout << v[i];
    }
    cout << endl;
}
```

**总结**：大数组（>10⁵）用 `vector` 而不用定长栈数组，避免栈溢出。输出格式"数字间空格分隔、行末无空格"是 OJ 常见要求。

---

### LinK05 假币问题

**思路**：12 枚硬币枚举 24 种假设（每枚轻/重），用三次称量结果验证。关键是 swap 技巧——假币重时交换左右，统一用"轻假币"逻辑处理。

**关键代码**：
```cpp
bool isFake(char coin, bool isLight) {
    string c; c.push_back(coin);
    for (int i = 0; i < 3; i++) {
        string l = Left[i], r = Right[i];
        if (!isLight) swap(l, r);              // 重假币 → 交换左右，统一按轻假币处理
        switch (result[i][0]) {
            case 'e': if (l.find(c)!=npos || r.find(c)!=npos) return false; break;
            case 'u': if (r.find(c) == npos) return false; break;  // 右边翘=轻的在右
            case 'd': if (l.find(c) == npos) return false; break;  // 右边沉=轻的在左
        }
    }
    return true;
}
```

**总结**：小范围枚举（24 种）验证是处理逻辑推理题的通用方法。`swap` 将对称情况统一处理的技巧很巧妙。

---

## 递归与分治

### LinK09 汉诺塔I

**思路**：递归三步骤——① 把上面 n-1 个从 A 移到 B（借助 C）；② 把最大的从 A 移到 C；③ 把 n-1 个从 B 移到 C（借助 A）。

**关键代码**：
```cpp
void hanoi(int n, char start, char other, char target) {
    if (n == 1) { cout << start << "->" << target << endl; return; }
    hanoi(n - 1, start, target, other);    // ① n-1: start → other (借助 target)
    cout << start << "->" << target << endl; // ② 最大盘: start → target
    hanoi(n - 1, other, start, target);    // ③ n-1: other → target (借助 start)
}
```

**总结**：汉诺塔是递归思想的典范——把大问题分解为"移动上面 n-1 个"和"移动最底下 1 个"两个子问题。移动次数 = $2^n - 1$。

---

### LinK10 汉诺塔II

**思路**：与 I 相同，但输入自定义杆名、输出带盘号和自定义杆名。盘号追踪：一组 n 个盘中最大盘编号 = `id + n - 1`。

**关键代码**：
```cpp
void hanoi(int n, int id, char start, char other, char target) {
    if (n == 1) { cout << id << ":" << start << "->" << target << endl; return; }
    hanoi(n - 1, id, start, target, other);          // 上面 n-1 个编号从 id 开始
    cout << id + n - 1 << ":" << start << "->" << target << endl;  // 最大盘编号 = id+n-1
    hanoi(n - 1, id, other, start, target);
}
```

**总结**：盘号追踪——上面 n-1 个盘的最小编号是 `id`，最大盘编号是 `id + n - 1`。

---

### LinK15 爬天梯

**思路**：斐波那契数列：`f(n) = f(n-1) + f(n-2)`，最后一步要么从 n-1 走 1 阶、要么从 n-2 走 2 阶。注意对 `1000000007` 取模。

**关键代码**：
```cpp
int stairs(int n) {
    if (n <= 1) return 1;
    return (stairs(n - 1) + stairs(n - 2)) % 1000000007;  // 斐波那契，取模防溢出
}
```

**总结**：纯递归 O($2^n$) 易超时，N 大时应改用迭代 DP `for (i=2; i<=N; i++) dp[i] = (dp[i-1] + dp[i-2]) % mod`。取模要在加法之后立即做。

---

### LinK16 放苹果

**思路**：整数划分问题。`f(m,n)` = m 个苹果放 n 个盘子。递推：`f(m,n) = f(m,n-1) + f(m-n,n)`（至少空一盘 / 全不空各放一个）。

**关键代码**：
```cpp
int f(int m, int n) {
    if (m < n) return f(m, m);          // 苹果比盘子少，多余盘子忽略
    if (m == 0) return 1;               // 没有苹果，全空，1 种方案
    if (n <= 0) return 0;               // 有苹果没盘子，0 种
    return f(m, n - 1) + f(m - n, n);   // 空一盘 + 每盘至少一个
}
```

**总结**：**不重不漏**的关键：将方案按"是否有空盘"二分——`f(m, n-1)` 覆盖有空盘、`f(m-n, n)` 覆盖全不空。

---

## 枚举

### LinK19 递归实现指数型枚举

**思路**：每个数选/不选，递归深度 = n，叶子共 $2^n$ 个。`st[i]` 标记是否选。位运算替代法：`for (mask = 0; mask < (1<<n); mask++)` 更简洁。

**关键代码**：
```cpp
void dfs(int u) {
    if (u > n) {
        for (int i = 1; i <= n; i++)
            if (st[i]) cout << i << " ";  // 选了才输出
        cout << endl; return;
    }
    st[u] = true;  dfs(u + 1);           // 选 u
    st[u] = false; dfs(u + 1);           // 不选 u
}
```

**总结**：子集枚举三种写法：① DFS 决策树（直观）② 位运算（简洁）③ `next_permutation`（不适用）。输出天然升序因为按 1→n 遍历。

---

### LinK20 递归实现组合型枚举

**思路**：从 n 个选 m 个，用 `start` 参数强制升序避免重复（{1,3} 和 {3,1} 只输出一次）。递归深度 = m，叶子 = $C(n,m)$。与子集不同的是不固定选或不选，而是用 for 循环选"下一个数"。

**关键代码**：
```cpp
void dfs(int u, int start) {
    if (u > m) {                          // 选满了 m 个
        for (int i = 1; i <= m; i++) cout << path[i] << " ";
        cout << endl; return;
    }
    for (int i = start; i <= n; i++) {    // 从 start 开始，保证升序
        path[u] = i;
        dfs(u + 1, i + 1);                // 下一个从 i+1 开始，杜绝重复
    }
}
```

**总结**：组合 vs 排列的核心区别：组合用 `start` 参数强制升序去重，排列用 `st[]` 布尔数组标记已用元素。

---

### LinK21 递归实现排列型枚举

**思路**：n 个元素全排列共 $n!$ 种。每层从 1~n 中选一个未使用的数，用 `st[i]` 标记，递归后**必须回溯恢复**。

**关键代码**：
```cpp
void dfs(int u) {
    if (u > n) {
        for (int i = 1; i <= n; i++) cout << path[i] << " "; cout << endl; return;
    }
    for (int i = 1; i <= n; i++)
        if (!st[i]) {                     // 只选未使用的数字
            path[u] = i; st[i] = true;
            dfs(u + 1);
            st[i] = false;                // ★ 回溯恢复！忘记会大量漏解
        }
}
```

**总结**：排列的回溯恢复是必须的——不同于组合的 `start` 隐式排除，排列不恢复 `st[i]` 会导致其他分支无法使用该数字。

---

## 排序

### LinK27 大数排序（快排）

**思路**：手动实现快速排序。双指针 partition——选中间值为 pivot，`do-while` 两个指针移动，交错后递归左右。

**关键代码**：
```cpp
void quick_sort(int q[], int l, int r) {
    if (l >= r) return;
    int i = l - 1, j = r + 1, x = q[l + r >> 1];  // 中间值为 pivot
    while (i < j) {
        do i++; while (q[i] < x);                   // 找左边 ≥ pivot 的
        do j--; while (q[j] > x);                   // 找右边 ≤ pivot 的
        if (i < j) swap(q[i], q[j]);                // 交换
    }
    quick_sort(q, l, j); quick_sort(q, j + 1, r);  // 递归左右（用 j 分界）
}
```

**总结**：Y 总模板核心——pivot 取 `l+r>>1` 配 `(l,j)(j+1,r)` 递归。取 `l+r+1>>1` 则配 `(l,i-1)(i,r)`。两套不能混用，否则死循环。

---

### LinK30 归并排序

**思路**：先递归到底（分），再合并两个有序区间（治）。双指针比较 `nums[p]` 和 `nums[q]`，小的进 tmp。$O(N\log N)$，稳定。

**关键代码**：
```cpp
void mergesort(int nums[], int left, int right) {
    if (left >= right) return;
    int mid = left + right >> 1;
    mergesort(nums, left, mid); mergesort(nums, mid + 1, right);
    int k = 0, p = left, q = mid + 1;
    while (p <= mid && q <= right)
        tmp[k++] = nums[p] <= nums[q] ? nums[p++] : nums[q++]; // ≤ 保证稳定
    while (p <= mid) tmp[k++] = nums[p++];      // 左边剩余
    while (q <= right) tmp[k++] = nums[q++];    // 右边剩余
    for (int i = left, k = 0; i <= right; ) nums[i++] = tmp[k++]; // 拷回原数组
}
```

**总结**：快排 vs 归并——快排先分后排（不稳定），归并先递归再合并（稳定，需 O(N) 临时空间）。`<=` 保证了稳定性。

---

### LinK31 求排列的逆序数

**思路**：在归并排序的合并过程中统计逆序对：当 `nums[q] < nums[p]` 时，左半 [p..mid] 都大于 `nums[q]`，贡献 `mid - p + 1` 个逆序对。

**关键代码**：
```cpp
long long mergesort(int nums[], int left, int right) {
    if (left >= right) return 0;
    int mid = left + right >> 1;
    long long res = mergesort(nums, left, mid) + mergesort(nums, mid + 1, right);
    // ... 归并过程 ...
    if (nums[p] <= nums[q]) tmp[k++] = nums[p++];
    else {
        res += mid - p + 1;    // ★ nums[q] 比左半 [p..mid] 都小，形成逆序对
        tmp[k++] = nums[q++];
    }
    return res;  // 用 long long，逆序数可能超 int（最大 ~5×10⁹）
}
```

**总结**：归并排序求逆序对的精髓——合并时一个元素归入，就能统计跨区间的所有逆序对。返回值用 `long long` 防溢出。

---

## DFS 搜索

### LinK13 输出N皇后的全部摆法

**思路**：DFS 逐行放皇后，每行尝试 1~N 列，O(n) 遍历检查冲突（同列/同对角线 `abs(row1-row2) == abs(col1-col2)`）。

**关键代码**：
```cpp
void dfs(int row) {
    if (row == N) {
        for (auto x : res) cout << x; cout << endl; return;
    }
    for (int col = 1; col <= N; col++) {
        int k;
        for (k = 0; k < row; k++)
            if (res[k] == col || abs(res[k] - col) == abs(k - row)) break; // 同列或同对角线
        if (k == row) { res[row] = col; dfs(row + 1); }  // 无冲突，递归下一行
    }
}
```

**总结**：对角线判断 `abs(col1-col2) == abs(row1-row2)` 覆盖主副对角线。N≤13 时 O(n) 遍历冲突检查足够，更大时需布尔数组 O(1) 优化。

---

### LinK14 求八皇后的第n种解

**思路**：预计算全部 92 组解存入 `res[92][8]`，每次查询 O(1) 输出。DFS 从小到大试列号天然保证字典序。

**关键代码**：
```cpp
void dfs(int row) {
    if (row > 7) {
        for (int k = 0; k < 8; k++) res[count][k] = path[k];  // 存解
        count++; return;
    }
    for (int col = 1; col <= 8; col++) {
        // ... 冲突检测 ...
        path[row] = col; dfs(row + 1);
    }
}
// 查询: for (int i = 0; i < 8; i++) cout << res[n - 1][i];  // n 从 1 开始，下标 -1
```

**总结**：打表法——答案数量固定（92 个）时，一次性生成全部解，查询 O(1)。DFS 从 1→8 列枚举天然按字典序生成。

---

### LinK14.5 DFS试炼之n皇后问题

**思路**：N 皇后标准模板，用 `col[N]`、`dg[2N]`、`udg[2N]` 三个布尔数组 O(1) 判冲突。输出棋盘图案（`Q` 和 `.`）。

**关键代码**：
```cpp
void dfs(int u) {
    if (u == n) {
        for (int i = 0; i < n; i++) puts(g[i]); puts(""); return;
    }
    for (int i = 0; i < n; i++)
        if (!col[i] && !dg[u + i] && !udg[n - u + i]) {   // O(1) 三数组判冲突
            g[u][i] = 'Q'; col[i] = dg[u + i] = udg[n - u + i] = true;
            dfs(u + 1);
            g[u][i] = '.'; col[i] = dg[u + i] = udg[n - u + i] = false; // 回溯
        }
}
```

**总结**：对角线映射：主对角线 `u+i` 为定值，副对角线 `n-u+i`（偏移防负）。三个布尔数组 O(1) 判冲突是 N 皇后最优写法。

---

### LinK38 林克的命运之阵

**思路**：网格中只能向下/左/右走，不能重复访问。DFS+回溯标记已访问格子，统计走 n 步的不同路径。虽有 3 个方向但大量剪枝，$3^{20} \approx 3.5\times 10^9$ 实际只约 $5.4\times 10^7$。

**关键代码**：
```cpp
long long dfs(int i, int j, int n) {
    if (n == 0) return 1;
    long long res = 0;
    fates[i][j] = 1;                         // 标记已访问
    for (int k = 0; k < 3; k++) {            // 下、左、右
        int x = i + dx[k], y = j + dy[k];
        if (fates[x][y] == 0) res += dfs(x, y, n - 1);
    }
    fates[i][j] = 0;                         // ★ 回溯恢复
    return res;
}
```

**总结**：求路径数必须回溯恢复标记（不同于求连通块大小）。结果用 `long long`（n=20 时约 $5\times 10^7$）。

---

## BFS & 图论

### LinK39 净化迷雾森林（DFS）

**思路**：Flood Fill——从 `@` 开始 DFS 四方向找 `.`，访问后改为 `#`（不恢复）。求连通区域大小。

**关键代码**：
```cpp
int dfs(int i, int j) {
    int res = 1;
    fogforest[i][j] = '#';                   // 标记为已访问（不恢复！这是连通块统计）
    for (int k = 0; k < 4; k++) {
        int x = i + dx[k], y = j + dy[k];
        if (x>=0 && y>=0 && x<h && y<w && fogforest[x][y] == '.')
            res += dfs(x, y);
    }
    return res;
}
```

**总结**：Flood Fill 不需要回溯（与 LinK38 求路径数不同）——统计"去过多少格"，标记后不再使用。DFS 递归深度 ≤ W×H ≤ 400。

---

### LinK51 净化迷雾森林（BFS）

**思路**：与 LinK39 相同但用 BFS 实现。入队前标记为 `#` 避免重复入队。

**关键代码**：
```cpp
int bfs(int sx, int sy) {
    queue<PII> q; q.push({sx, sy}); g[sx][sy] = '#';
    int res = 0;
    while (q.size()) {
        auto t = q.front(); q.pop(); res++;
        for (int i = 0; i < 4; i++) {
            int x = t.first + dx[i], y = t.second + dy[i];
            if (x<0||x>=n||y<0||y>=m||g[x][y]!='.') continue;
            g[x][y] = '#'; q.push({x, y});   // ★ 入队前标记，防重复入队
        }
    }
    return res;
}
```

**总结**：BFS 关键技巧——**入队时立即标记**已访问（而非出队时），防止同一节点被重复入队导致队列膨胀。

---

### LinK52 波克布林的巡逻范围

**思路**：BFS 从 (0,0) 出发，约束是行列坐标数位和 ≤ k。注意只有在出队时判断约束（不是入队前）可以简化代码。

**关键代码**：
```cpp
int getSum(int x) { int s = 0; while (x) s += x % 10, x /= 10; return s; }

// BFS 中:
auto t = q.front(); q.pop();
if (st[t.first][t.second] || getSum(t.first)+getSum(t.second) > k) continue; // 出队检查
res++; st[t.first][t.second] = true;
for (int i = 0; i < 4; i++) { /* 四方向扩展 */ }
```

**总结**：数位和问题——用 `while(x) s+=x%10, x/=10` 计算。坐标从 (0,0) 开始，(35,37) 的数位和 = 3+5+3+7=18。

---

### LinK53 加农的入侵

**思路**：8 方向 BFS（含对角线），`dist` 数组记录步数，最远距离 = 所需天数。注意坐标系转换——题目左下角 (1,1)，数组左上角 (0,0)。

**关键代码**：
```cpp
int bfs() {
    memset(dist, -1, sizeof(dist));
    queue<PII> q; q.push(start); dist[start.first][start.second] = 0;
    int res = 0;
    while (q.size()) {
        auto t = q.front(); q.pop();
        for (int i = 0; i < 8; i++) {             // 8 方向
            int x = t.first + dx[i], y = t.second + dy[i];
            if (x<1||x>n||y<1||y>m||g[x][y]=='*'||dist[x][y]!=-1) continue;
            dist[x][y] = dist[t.first][t.second] + 1;
            res = max(res, dist[x][y]);            // 最大步数 = 所需天数
            q.push({x, y});
        }
    }
    return res;
}
```

**总结**：坐标系转换——题目 (Mx, My) 中 My 是从下往上数，需 `n+1-My` 转为数组下标。8 方向 BFS 需 8 个偏移量。

---

### LinK57 Dijkstra求最短路(1)

**思路**：朴素 Dijkstra O(N²)——每次选未确定点中 dist 最小的，标记后松弛所有邻接点。适合稠密图（N≤500）。

**关键代码**：
```cpp
int dijkstra() {
    memset(dist, 0x3f, sizeof(dist)); dist[1] = 0;
    for (int i = 0; i < n - 1; i++) {
        int t = -1;
        for (int j = 1; j <= n; j++)
            if (!st[j] && (t == -1 || dist[t] > dist[j])) t = j;  // 选最小 dist
        for (int j = 1; j <= n; j++)
            dist[j] = min(dist[j], dist[t] + g[t][j]);            // 松弛
        st[t] = true;
    }
    return dist[n] == 0x3f3f3f3f ? -1 : dist[n];
}
```

**总结**：`0x3f3f3f3f` ≈ $1.06\times 10^9$ 是经典 INF——够大且 `0x3f3f3f3f + 0x3f3f3f3f` 不溢出 int。重边处理：`g[a][b] = min(g[a][b], c)`。

---

## 位运算

### LinK43 求二进制中1的个数

**思路**：`n & -n`（lowbit）每次提取最低位 1，然后 `n -= lowbit(n)` 消去它，循环次数 = 1 的个数。

**关键代码**：
```cpp
int lowbit(int n) { return n & -n; }   // 提取最低位 1，如 12(1100) → 4(0100)

int NumberOf1(int n) {
    int res = 0;
    while (n) { n -= lowbit(n); res++; }  // 每次消去最低位 1
    return res;
}
```

**总结**：lowbit 原理——`n & -n` 在补码下提取最低位 1。对于稀疏的 1（如只有几个位为 1），这比移位法（固定 32 次）更高效。

---

### LinK44 二进制中1的最低位位置

**思路**：lowbit 提取权值 → 打表查位置。`log[1<<i] = i` 预建 2 的幂到指数的映射。

**关键代码**：
```cpp
void BuildLogTable(int n) {
    for (int i = 0; i < n; i++) log[1 << i] = i;  // log[1]=0, log[2]=1, log[4]=2...
}
inline int lowbit(int n) { return n & -n; }

// 查询:
int n; cin >> n;
cout << log[lowbit(n)];  // lowbit 提取权值 → log 查表得位置
```

**总结**：打表法——结果范围有限（16 位，$2^{17}$=131072）时预计算所有可能答案，O(1) 查询。`inline` 对单表达式函数是好习惯。

---

## 数独系列

### LinK45 真假记忆碎片

**思路**：数独验证器——检查填数是否与初始矩阵一致 + 每行/列/3×3 块 1~9 不重复。四步依次验证，全通过才输出 Yes。

**关键代码**：
```cpp
bool check_row() {
    for (int i = 0; i < 9; i++) {
        bool st[10] = {false};
        for (int j = 0; j < 9; j++) {
            int t = b[i][j];
            if (st[t]) return false;     // 重复出现
            st[t] = true;
        }
    }
    return true;
}
// check_col 同理；check_block 枚举 9 个 3×3 块左上角
```

**总结**：数独验证的四步：输入合法性 → 行唯一 → 列唯一 → 块唯一。检查前需 `memset(st, false)`。

---

### LinK46 寻找林克的回忆(1)

**思路**：标准数独求解，DFS 逐格填数。用 `st_row[x][t]`、`st_col[y][t]`、`st_block[x/3][y/3][t]` O(1) 判冲突。找一解即返回 true。

**关键代码**：
```cpp
bool dfs(int x, int y) {
    if (y == 9) x++, y = 0;
    if (x == 9) { /* 输出 */ return true; }
    if (g[x][y] != 0) return dfs(x, y + 1);  // 已填，跳过
    for (int t = 1; t <= 9; t++)
        if (!st_row[x][t] && !st_col[y][t] && !st_block[x/3][y/3][t]) {
            st_row[x][t] = st_col[y][t] = st_block[x/3][y/3][t] = true;
            g[x][y] = t;
            if (dfs(x, y + 1)) return true;   // 找到解立即返回
            g[x][y] = 0;                      // 回溯
            st_row[x][t] = st_col[y][t] = st_block[x/3][y/3][t] = false;
        }
    return false;
}
```

**总结**：三数组 O(1) 判冲突比位运算版更直观。初始化时把已知数字标记好，DFS 跳过即可。找一解即停（return true 逐层退出）。

---

### LinK47 寻找林克的回忆(2)

**思路**：数独位运算版 + **MRV 启发式**——优先填候选最少的格。`row/col/block` 用 9 位 bitmask 表示可用数字，`get(x,y) = row[x] & col[y] & block[x/3][y/3]` 得候选集。

**关键代码**：
```cpp
int get(int x, int y) { return row[x] & col[y] & block[x/3][y/3]; }

bool dfs(int cnt) {
    if (!cnt) return true;
    int minv = 10, x, y;
    for (int i = 0; i < 9; i++)                 // ★ MRV: 找候选最少的空格
        for (int j = 0; j < 9; j++)
            if (str[i*9+j] == '.') {
                int t = ones[get(i, j)];          // 候选数 = mask 中 1 的个数
                if (t < minv) { minv = t; x = i; y = j; }
            }
    for (int i = get(x, y); i; i -= lowbit(i)) { // 遍历候选集
        int t = log[lowbit(i)];                   // lowbit 转位号
        row[x] -= 1<<t; col[y] -= 1<<t; block[x/3][y/3] -= 1<<t;  // 放置
        str[x*9+y] = '1'+t;
        if (dfs(cnt - 1)) return true;
        row[x] += 1<<t; col[y] += 1<<t; block[x/3][y/3] += 1<<t;  // 撤销
        str[x*9+y] = '.';
    }
    return false;
}
```

**总结**：MRV（Minimum Remaining Values）是 CSP 搜索最有效的启发式——每次选可选数字最少的格子能大幅缩小搜索树。`ones[mask]` 和 `log[mask]` 打表 O(1) 查询。

---

### LinK48 寻找林克的回忆(3)

**思路**：靶形数独——每个格子有权值（6~10 分），求最高总分。需要在数独基础上遍历所有解取最大值（不能找到一解就停）。

**关键代码**：
```cpp
int getScore(int x, int y, int t) {
    return (min(min(x, 8-x), min(y, 8-y)) + 6) * t;  // 离中心越近分越高
}

void dfs(int cnt, int score) {
    if (!cnt) { ans = max(ans, score); return; }       // 找所有解，取最大分
    // ... MRV 选格 ...
    for (int i = get(x, y); i; i -= lowbit(i)) {
        int t = log[lowbit(i)] + 1;
        draw(x, y, t);
        dfs(cnt - 1, score + getScore(x, y, t));       // 累加分数
        draw(x, y, -t);                                 // 负号 = 撤销
    }
}
```

**总结**：`draw(x, y, -t)` 用负数标记撤销的设计很巧妙，统一了放置和撤销逻辑。`ans = -1` 初始以区分无解情况。

---

## 动态规划 — 入门

### LinK62 数字三角形

**思路**：自底向上 DP——`f[i][j] += max(f[i+1][j], f[i+1][j+1])`。直接原地修改，答案在 `f[1][1]`。

**关键代码**：
```cpp
for (int i = n - 1; i; i--)                   // 从倒数第二行往上
    for (int j = 1; j <= i; j++)
        f[i][j] += max(f[i + 1][j], f[i + 1][j + 1]); // 正下 vs 右下
cout << f[1][1] << endl;                       // 答案在顶部
```

**总结**：DP 两个方向——自顶向下（答案在最后一行）vs 自底向上（答案集中在起点）。自底向上可以原地修改数组。

---

### LinK69 摘花生

**思路**：二维网格最大路径和——`f[i][j] = max(f[i-1][j], f[i][j-1]) + w[i][j]`。从左上到右下，只能右/下移动。

**关键代码**：
```cpp
for (int i = 1; i <= n; i++)
    for (int j = 1; j <= m; j++)
        f[i][j] = max(f[i - 1][j], f[i][j - 1]) + w[i][j];  // 上方 vs 左方
cout << f[n][m] << endl;
```

**总结**：求**最大值**时全局数组默认 0 恰好适用——第一行/列边界 `f[0][j]=f[i][0]=0` 天然正确。多组数据不必清空 f（会被覆写）。

---

### LinK70 最低通行费

**思路**：与摘花生形式相同但求**最小值**，必须把边界初始化为 INF，起点特殊处理。(2N-1) 时间限制暗示只能右/下。

**关键代码**：
```cpp
for (int i = 1; i <= n; i++)
    for (int j = 1; j <= n; j++) {
        if (i == 1 && j == 1) f[i][j] = w[i][j];              // 起点
        else {
            f[i][j] = INF;
            if (i > 1) f[i][j] = min(f[i][j], f[i-1][j] + w[i][j]);
            if (j > 1) f[i][j] = min(f[i][j], f[i][j-1] + w[i][j]);
        }
    }
```

**总结**：求最小值时**边界必须设 INF**——否则 `min(dp[0][j], ...)` 会错选 0。这是求 max 和求 min 在初始化上的关键区别。

---

## 动态规划 — 背包

### LinK63 林克的01背包

**思路**：`f[i][j]` = 前 i 件、容量 j 的最大价值。`f[i][j] = max(f[i-1][j], f[i-1][j-v[i]] + w[i])`。二维版 j 正序逆序均可。

**关键代码**：
```cpp
for (int i = 1; i <= n; i++)
    for (int j = 0; j <= m; j++) {
        f[i][j] = f[i - 1][j];                          // 不选第 i 件
        if (j >= v[i])
            f[i][j] = max(f[i][j], f[i - 1][j - v[i]] + w[i]); // 选第 i 件
    }
```

**总结**：01 背包一维优化必须**逆序** j——`for(j=m; j>=v[i]; j--)`。正序会导致 f[j-v[i]] 已被本轮更新，等价于物品被多次选取（变成完全背包）。

---

### LinK64 林克的完全背包

**思路**：每件可选无限次。一维必须**正序** `for (j=v[i]; j<=m; j++)`——正序让 f[j-v[i]] 被本轮更新过，等价于同一物品可以选多次。

**关键代码**：
```cpp
for (int i = 1; i <= n; i++)
    for (int j = v[i]; j <= m; j++)          // ★ 正序！与 01 背包的唯一区别
        f[j] = max(f[j], f[j - v[i]] + w[i]);
```

**总结**：01 背包逆序 vs 完全背包正序——两者递推公式相同，仅 j 遍历方向不同。这是背包问题最重要的区分点。

---

### LinK65 多重背包问题(1)

**思路**：数据小（N,V≤100），暴力枚举每种物品选 k 个：`for(k=1; k<=s && k*v<=j; k++)`，j 逆序（01 模式）。

**关键代码**：
```cpp
for (int i = 1; i <= n; i++) {
    int v, w, s; cin >> v >> w >> s;
    for (int j = m; j >= 0; j--)             // 逆序（01 模式）
        for (int k = 1; k <= s && k * v <= j; k++)  // 枚举选几个
            f[j] = max(f[j], f[j - k * v] + k * w);
}
```

**总结**：朴素多重背包 = 把每种物品拆成 s 件独立物品 + 01 背包。$O(N \times V \times s) \approx 10^6$（N,V,s≤100）。

---

### LinK66 多重背包问题(2)

**思路**：数据大（N≤1000, V≤2000, s≤2000），必须二进制拆分：s=13 → 拆成 1+2+4+6 四个打包，log 级别减少物品数。

**关键代码**：
```cpp
int cnt = 0;
for (int i = 1; i <= n; i++) {
    int a, b, s; cin >> a >> b >> s;
    int k = 1;
    while (k <= s) {
        cnt++; v[cnt] = a * k; w[cnt] = b * k;  // 打包 k 件
        s -= k; k *= 2;
    }
    if (s > 0) { cnt++; v[cnt] = a * s; w[cnt] = b * s; } // 剩余打包
}
n = cnt;  // 更新物品数，后续走 01 背包
```

**总结**：二进制拆分核心——1,2,4,...,2^k, 余数 可组合出 0~s 的任意整数。物品数从 s 降到 log s。

---

### LinK67 分组背包问题

**思路**：每组最多选 1 件。循环顺序：组 → 容量(逆序) → 组内物品。j 逆序 + k 在最内层的顺序保证了互斥。

**关键代码**：
```cpp
for (int i = 1; i <= n; i++) {               // 枚举组
    for (int j = m; j >= 1; j--) {            // 逆序容量
        for (int k = 1; k <= s[i]; k++) {     // 枚举组内物品
            if (v[i][k] <= j)
                f[j] = max(f[j], f[j - v[i][k]] + w[i][k]);
        }
    }
}
```

**总结**：循环顺序至关重要——`i → j(逆序) → k` 保证互斥。若 `i → k → j(正序)` 则同一物品会被多次选，失去分组意义。

---

### LinK68 混合背包问题

**思路**：根据 si 分类处理——si=0（完全，正序）、si=-1（01，转 s=1 走二进制拆分）、si>0（多重，二进制拆分）。

**关键代码**：
```cpp
if (!s) {                                     // 完全背包
    for (int j = v; j <= m; j++) f[j] = max(f[j], f[j - v] + w);
} else {
    if (s == -1) s = 1;                       // 01 背包 → 转多重
    for (int k = 1; k <= s; k *= 2) {          // 二进制拆分
        for (int j = m; j >= k * v; j--) f[j] = max(f[j], f[j - k*v] + k*w);
        s -= k;
    }
    if (s) for (int j = m; j >= s*v; j--) f[j] = max(f[j], f[j - s*v] + s*w);
}
```

**总结**：三种背包混合时，按 si 分类处理即可，都操作同一个 f[] 数组——各类物品互相独立、可以混合选取。

---

## 动态规划 — LIS/LCS

### LinK71 最长上升子序列

**思路**：`f[i]` = 以 a[i] 结尾的 LIS 长度。`f[i] = max(f[i], f[j]+1)` 当 `a[j] < a[i]`。$O(N^2)$，N≤1000。

**关键代码**：
```cpp
for (int i = 1; i <= n; i++) {
    f[i] = 1;                                  // 自己成序列，长度至少 1
    for (int j = 1; j < i; j++)
        if (a[j] < a[i]) f[i] = max(f[i], f[j] + 1);
}
int ans = 0;
for (int i = 1; i <= n; i++) ans = max(ans, f[i]);  // ★ 答案遍历取 max，不是 f[n]!
```

**总结**：最终答案不一定是 `f[n]`——最长上升子序列未必以最后一个元素结尾。这个坑很常见。

---

### LinK72 最长上升子序列(2)

**思路**：贪心+二分 O(N log N)。维护 `q[i]` = 长度为 i 的上升子序列的最小末尾值。q 单调增，二分找最后一个 < a[i] 的位置。

**关键代码**：
```cpp
int len = 0;
for (int i = 0; i < n; i++) {
    int l = 0, r = len;
    while (l < r) {
        int mid = l + r + 1 >> 1;
        if (q[mid] < a[i]) l = mid; else r = mid - 1;  // 最后 < a[i] 的位置
    }
    len = max(len, r + 1);
    q[r + 1] = a[i];                                    // 更新或扩展
}
```

**总结**：`q[i]` 存的是每种长度的"最小末尾"，不一定是真正的 LIS 序列。`l+r+1>>1` 是上取整二分，防死循环。

---

### LinK73 拦截导弹

**思路**：两问——① 最长不上升子序列（`h[i] <= h[j]`，注意等号）；② 最少系统数 = LIS 长度（Dilworth 定理）。

**关键代码**：
```cpp
// 第一问：最长不上升
for (int i = 0; i < n; i++) {
    f[i] = 1;
    for (int j = 0; j < i; j++)
        if (h[i] <= h[j]) f[i] = max(f[i], f[j] + 1);  // 不上升：h[i] ≤ h[j]
    res = max(res, f[i]);
}
// 第二问：贪心分配
for (int i = 0; i < n; i++) {
    int k = 0;
    while (k < cnt && q[k] < h[i]) k++;  // 找最低能拦截的
    if (k == cnt) q[cnt++] = h[i]; else q[k] = h[i];  // 分配或新开
}
```

**总结**：Dilworth 定理——最少链覆盖数 = 最长反链长度。输入是单行不定个数，用 `getline + stringstream` 解析。

---

### LinK75 最长公共子序列

**思路**：`f[i][j]` = A 前 i 个和 B 前 j 个的 LCS 长度。`a[i]==b[j]` 时 `f[i][j]=f[i-1][j-1]+1`，否则 `max(f[i-1][j], f[i][j-1])`。

**关键代码**：
```cpp
cin >> n >> m >> a + 1 >> b + 1;       // 下标从 1 开始
for (int i = 1; i <= n; i++)
    for (int j = 1; j <= m; j++) {
        if (a[i] == b[j])
            f[i][j] = f[i - 1][j - 1] + 1;           // 匹配
        else
            f[i][j] = max(f[i - 1][j], f[i][j - 1]); // 不匹配
    }
```

**总结**：`cin >> a+1` 从 a[1] 开始填，让字符串下标与 DP 对齐。当 a[i]!=b[j] 时不需要考虑 `f[i-1][j-1]`（已被 max 覆盖）。

---

## 动态规划 — 区间DP

### LinK76 石子合并

**思路**：区间 DP——`f[i][j]` = 合并 [i,j] 的最小代价。`f[i][j] = min(f[i][k] + f[k+1][j] + sum(i,j))`。必须按区间长度递增枚举。

**关键代码**：
```cpp
memset(f, 0x3f, sizeof f);
for (int len = 1; len <= n; len++)               // ★ 区间长度递增
    for (int i = 1; i + len - 1 <= n; i++) {
        int j = i + len - 1;
        if (len == 1) { f[i][j] = 0; continue; }  // 单堆不需合并
        for (int k = i; k < j; k++)                // 枚举分割点
            f[i][j] = min(f[i][j], f[i][k] + f[k+1][j] + s[j] - s[i-1]);
    }
```

**总结**：区间 DP 通用模板——先初始化 len=1（代价为 0），按 len 递增递推，枚举分割点 k。前缀和 O(1) 算区间和。$O(N^3)$，N≤300 可过。
