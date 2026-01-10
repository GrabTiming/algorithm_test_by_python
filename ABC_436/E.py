# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2026/1/10 10:58

https://atcoder.jp/contests/abc436/tasks/abc436_e

题意：一个数组P， 是一个1~n的序列， 可以交换任意两个位置的数，假设将P变回[1,2...n]的最小操作为K，
问在保证最小操作的同时，第一次操作不同的情况有多少种

思路：这题不会，看了榜单上某位大佬的代码后才想通。 对于位置P[i]和i 是一定要交换的，视为有联系。那么对于这些有联系的点组成的集合，集合内部的操作是可以任意交换的
因此 统计集合的大小size，那么每个集合的贡献为 size*(size-1)/2

"""

def LII():
    return list(map(int, input().split()))

def fd(i,fa,size):
    if i == fa[i]:
        return i
    size[fa[i]] += size[i]
    size[i] = 0
    fa[i] = fd(fa[i],fa,size)
    return fa[i]

def main():
    n = int(input())
    fa = [0]*(n+1)
    size = [0] * (n+1)
    for i in range(1,n+1):
        fa[i] = i
        size[i] = 1
    p = LII()
    p = [0] + p
    for i in range(1,n+1):
        f1 = fd(i,fa,size)
        f2 = fd(p[i],fa,size)
        fa[f2] = f1

    res = 0

    for i in range(1,n+1):
        if i==fd(i,fa,size):
            res += size[i]*(size[i]-1)//2
    print(res)


if __name__ == "__main__":
    main()
