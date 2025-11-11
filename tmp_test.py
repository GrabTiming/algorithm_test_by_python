# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/11/11 23:13
"""
from typing import List


def main():
    x = int(input())
    n = int(input())
    raw_str = input()
    num_list =  list(map(int, raw_str.split(' ')))
    vis:List[int] = [0] * (n)
    q = int(input())

    res = x
    for i in range(q):
        idx = int(input())
        idx -= 1
        if vis[idx] == 0:
            vis[idx] = 1
            res += num_list[idx]
        else:
            res -= num_list[idx]
            vis[idx] = 0
        print(res)

if __name__ == "__main__":
    main()
