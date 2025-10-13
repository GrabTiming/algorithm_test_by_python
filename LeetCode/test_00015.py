# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/10/13 20:51

https://atcoder.jp/contests/abc427/tasks/abc427_c
题意：n个点 m条边，删除最少边数使得 成为二分图

思路：n最大为10，二进制枚举每种情况，如果一条边的两个点颜色相同就需要删除。最后取删除边最少的情况

"""
from typing import List, Dict


def main():
    n,m = map(int,input().split())
    a:List[int] = []
    b:List[int] = []
    for i in range(m):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    ans = m
    for i in range((1<<n)):
        tmp = m
        for j in range(m):
            if ((i>>a[j])&1) ^ ((i>>b[j])&1):
                tmp -= 1
        ans = min(ans,tmp)

    print(ans)

if __name__ == "__main__":
    main()
