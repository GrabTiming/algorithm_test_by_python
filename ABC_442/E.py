# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2026/1/31 13:37

题意：二维坐标系，从原点 向点A 延伸出一条射线，问 射线从点A顺时针转到点B 会扫描到多少个点

思路： 极角排序

"""

import math
from bisect import bisect_left, bisect_right
import sys
from collections import Counter
from functools import cmp_to_key
from itertools import accumulate

input = sys.stdin.readline
# 定义常量
N = 10 ** 6 + 5


def get_half(x,y):
    if  y < 0 or (y == 0 and x > 0):
        return 0
    return 1

def cmp(cor1,cor2):
    h1 = get_half(cor1[0],cor1[1])
    h2 = get_half(cor2[0],cor2[1])
    if h1 != h2:
        return h1 - h2

    x1,y1 = cor1
    x2,y2 = cor2
    res = x1*y2 - x2*y1
    if res > 0: # 从cor1 到 cor2 需要逆时针
        return 1
    elif res < 0: # 从cor1 到 cor2 需要顺时针
        return -1
    return 0

def main():
    n,q = map(int,input().split())
    dire = []
    for i in range(n):
        x,y = map(int,input().split())
        g = math.gcd(abs(x),abs(y))
        x //= g
        y //= g
        dire.append((x,y))

    dir_count = Counter(dire)
    unique_dir = list(dir_count.keys())

    unique_dir.sort(key=cmp_to_key(cmp))
    M = len(unique_dir)
    dir_idx = {d: i for i,d in enumerate(unique_dir)}
    counts = list(dir_count[unique_dir[i]] for i in range(M))
    counts = counts + counts
    pre_sum = list(accumulate(counts))
    pre_sum = [0] + pre_sum
    for i in range(q):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        ca = dir_idx[dire[a]]
        cb = dir_idx[dire[b]]
        if cmp(dire[a],dire[b]) == 1:
            ca,cb = ca,cb+M
        print(pre_sum[cb+1] - pre_sum[ca])







if __name__ == "__main__":
    main()

