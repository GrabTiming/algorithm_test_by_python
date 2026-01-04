# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2026/1/4 23:07

https://atcoder.jp/contests/abc439/tasks/abc439_c

题意：输入n， 找到所有不超过n的好数字
好数字定义： 一个数z ，只有一对数(x,y)使得 x^2 + y^2 = z 成立

思路：筛出 所有平方数，按从小到大排序，双重for循环组合

"""
from typing import OrderedDict


def solve(n:int) -> None:
    xx = 1
    square_list = []
    while xx * xx <= n:
        square_list.append(xx * xx)
        xx += 1

    result_dict = dict()
    for i in range(0,len(square_list)):
        for j in range(i+1,len(square_list)):
            if square_list[i] + square_list[j] <= n:
                result_dict[square_list[i] + square_list[j]] = result_dict.get(square_list[i] + square_list[j],0) + 1
            else:
                break
    res = []
    for k,v in result_dict.items():
        if v == 1:
            res.append(k)
    print(len(res))
    res.sort()
    for i in res:
        print(i,end=" ")







def main():
    n = int(input())
    solve(n)

if __name__ == "__main__":
    main()
