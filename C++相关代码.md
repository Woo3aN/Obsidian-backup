---
aliases:
  - C++ code
tags:
  - 编程
  - 计算机
---
# 辗转相除法
```cpp
#include <iostream>  
#include <cmath>  
using namespace std;

// 辗转相除法求最大公约数  
int gcd(int a, int b) {    while (b != 0) {        int remainder = a % b;        a = b;        b = remainder;    }    return a;  
}

// 利用 gcd 求最小公倍数  
int lcm(int a, int b) {    return a / gcd(a, b) * b;  // 先除后乘避免溢出  
}

int main() {    int a, b;    cout << "请输入两个整数: ";    cin >> a >> b;       // 取绝对值处理负数    int abs_a = abs(a);    int abs_b = abs(b);       int result_gcd = gcd(abs_a, abs_b);    int result_lcm = lcm(abs_a, abs_b);       cout << a << " 和 " << b << " 的最大公约数是: " << result_gcd << endl;    cout << a << " 和 " << b << " 的最小公倍数是: " << result_lcm << endl;       return 0;  
}
```