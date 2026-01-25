# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
@Author : Liang2003
@Time   : 2026/1/25 21:31

题意：给一个字符串s，包含字母A,B,C,找到符合条件的子字符串个数： A字母个数大于B

思路：

转化为前缀和，A+1，B-1 ，那么对于位置i，前缀和为sum[i] , 前面j<i  且 sum[j] < sum[i] 都可以算作贡献
那么就是逆序对的问题了，用个树状数组处理

"""

def tr_add(tr,N,x):
    while x < N:
        tr[x] += 1
        x += (x&-x)

def tr_get(tr,N,x):
    res = 0
    if x == 0:
        return 0
    while x > 0:
        res += tr[x]
        x -= (x&-x)
    return res


def main():
    n = int(input())
    s = input()
    N = 4 * n + 4
    tr = [0] * (N+1)
    ans = 0
    D = [0] * (n+1)
    D[0] = n+1
    for i,c in enumerate(s):
        D[i+1] = D[i]
        if c == 'A':
            D[i+1] +=  1
        elif c == 'B':
            D[i+1] -= 1

    for d in D:
        ans = ans + tr_get(tr, N, d-1)
        tr_add(tr, N, d)
    print(ans)


if __name__ == "__main__":
    main()
