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
int gcd(int a, int b) {
    while (b != 0) {
        int remainder = a % b;
        a = b;
        b = remainder;
    }
    return a;
}
// 利用 gcd 求最小公倍数
int lcm(int a, int b) {
    return a / gcd(a, b) * b;  // 先除后乘避免溢出
}
int main() {
    int a, b;
    cout << "请输入两个整数: ";
    cin >> a >> b;
    
    // 取绝对值处理负数
    int abs_a = abs(a);
    int abs_b = abs(b);
    
    int result_gcd = gcd(abs_a, abs_b);
    int result_lcm = lcm(abs_a, abs_b);
    
    cout << a << " 和 " << b << " 的最大公约数是: " << result_gcd << endl;
    cout << a << " 和 " << b << " 的最小公倍数是: " << result_lcm << endl;
    
    return 0;
}
```

# 链表尾插法
```cpp
#include<iostream>
using namespace std;
// 定义链表节点结构体
struct node
{
    int val;        // 节点存储的数据
    node* next;     // 指向下一个节点的指针
};
// 创建链表的函数
node* createList()
{
    node* head = NULL;  // 链表头指针，初始为空
    node* tail = NULL;  // 链表尾指针，用于快速在末尾添加新节点
    int x;              // 用于存储每次读入的整数
    // 循环读入整数，当读入的数为-1时停止循环
    // cin >> x 会返回cin对象，可以用于判断是否成功读入
    // x != -1 判断读入的数是否为结束标记
    while (cin >> x && x != -1) {
        // 创建新节点，使用 new 动态分配内存
        // node{x, NULL} 是C++11的初始化方式，等价于 node *newNode = new node; newNode->val = x; newNode->next = NULL;
        node* newNode = new node{x, NULL};
        
        // 如果链表为空（头指针为NULL）
        if (head == NULL) {
            head = newNode;   // 新节点作为头节点
            tail = head;      // 尾指针也指向这个节点（因为只有一个节点）
        } 
        // 如果链表不为空
        else {
            tail->next = newNode;  // 当前尾节点的next指向新节点
            tail = newNode;        // 更新尾指针为新节点
        }
    }
    // 返回链表头指针
    // 如果没有输入任何正整数，head 保持为 NULL
    return head;
}
int main()
{
    node* head = NULL;  // 声明头指针，初始化为空
    head = createList(); // 调用函数创建链表，并将返回的头指针赋值给head
    // 判断链表是否为空
    if (head == NULL)
    {
        // 如果没有输入任何正整数（链表为空），输出 -1
        cout << "-1 ";
    }
    else
    {
        // 链表不为空，遍历链表并输出所有节点的值
        node* p = head;  // 用指针p遍历链表，初始指向头节点
        while (p != NULL)  // 当p不为空时循环
        {
            cout << p->val << " ";  // 输出当前节点的值，后面加一个空格
            p = p->next;            // p指向下一个节点
        }
    }
    return 0;  // 程序正常结束
}
```

# 链表头插法
```cpp
#include<iostream>
using namespace std;
struct node
{
    int val;
    node* next;
};
node* createList()
{
    node* head = NULL;  // 头指针初始为空
    int x;              // 用于存储每次读入的整数
    
    // 循环读入整数，直到遇到-1
    while (cin >> x && x != -1) {
        // 使用头插法创建新节点
        // 每次新节点都插入到链表的最前面
        node* newNode = new node{x, NULL};  // 创建新节点
        newNode->next = head;               // 新节点的next指向当前头节点
        head = newNode;                     // 更新头指针指向新节点
    }
    
    return head;  // 返回链表头指针
}


```


