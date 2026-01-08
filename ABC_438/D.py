# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2026/1/8 01:11

https://atcoder.jp/contests/abc438/tasks/abc438_d

题意：三个数组A、B、C，求A[1..X]+B[X+1..Y]+C[Y+1..n] 的最大值，其中 1<X<Y<n

思路：对于A[1..X]+B[X+1..Y] 可以维护一个数组dp ，dp[i][0]表示指针还在A数组，还没跳到B数组的最大值，dp[i][1]表示指针已经跳到B数组的最大值

那么题目的式子就可以表示成： dp[i][1] + suf_C[i+1] 其中 2<=i and i <= n+1

"""


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    suf_C = [0]*(n+2)
    for i in range(n,0,-1):
        suf_C[i] = suf_C[i+1] + C[i-1]

    dp = []
    for i in range(n+1):
        dp.append([0,0])
    # 边界情况，第一个元素一定要取A
    dp[1][0] = A[0]
    dp[1][1] = 0
    for i in range(2,n+1):
        dp[i][0] = dp[i-1][0] + A[i-1]
        dp[i][1] = max(dp[i-1][0],dp[i-1][1]) +B[i-1]


    res = 0
    for i in range(2,n):
        res = max(res, dp[i][1] + suf_C[i+1])
    print(res)



if __name__ == "__main__":
    main()
