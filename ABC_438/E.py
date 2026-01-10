# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2026/1/8 23:39

https://atcoder.jp/contests/abc438/tasks/abc438_e

题意：每个人i都有一个桶i，每一时刻 第i个人会往他当前拿的桶加 i个单位的水，然后传给第A[i]个人。
询问Q次，在T[i]时刻编号为B[i]的桶有多少单位的水

思路：想了很久处理环内环外的做法，最终还是做不了，看了一个老哥的 倍增法解法，学习一下
f[i][x] 表示 i往下走 1<<x 步的位置
g[i][x] 表示 i往下走 1<<x 步积累的贡献
"""

def LII():
    return list(map(int,input().split()))

def main():
    n,q = map(int,input().split())
    A = list(map(int,input().split()))
    A = [i-1 for i in A]
    LG = 30
    f = [[0]* n for _ in range(LG)]
    g = [[0]* n for _ in range(LG)]

    for i in range(n):
        f[0][i] = A[i]
        g[0][i] = i+1

    for i in range(1,LG):
        for j in range(n):
            f[i][j] = f[i-1][f[i-1][j]]
            g[i][j] = g[i-1][j] + g[i-1][f[i-1][j]]

    for i in range(q):
        t,b = map(int,input().split())
        res = 0
        b-=1
        for j in range(0,LG):
            if (t>>j)&1:
                res += g[j][b]
                b = f[j][b]
        print(res)

if __name__ == "__main__":
    main()
