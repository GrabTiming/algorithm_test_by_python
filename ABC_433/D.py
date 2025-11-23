# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/11/23 11:40

https://atcoder.jp/contests/abc433/tasks/abc433_d

题意： 问一个数组中有多少对数(i,j)，使得A[i]和A[j] 拼接起来是M的倍数

思路：
A数组最大的数 是1e9，有十位，那么处理出每个数 A[i]乘上10的 0到10次方 模M的余数。
对于A[i],假设它的长度为d，模M后为X，那么该数的贡献为 数组中的数乘上 10的d次方 后模M 为(M-X) 的数量
"""
from typing import List, Dict


def handle_mod(num:int,M:int,B:List[Dict[int,int]]):
    """
    处理每个数 乘从10的1次方到10次方 模M的余数 ，统计各个数位，各余数的值
    :param num:
    :param M:
    :param B:
    :return:
    """
    x = num % M
    y = 10 % M
    for i in range(1, 11):
        z = x * y % M
        B[i][z] = B[i].get(z, 0) + 1
        # print("B[{}][{}]:{}".format(i,z,B[i][z]))
        y = y * 10 % M



def main():
    n,M = map(int,input().split())
    nums = list(map(int,input().split()))
    B = []
    for i in range(0,11):
        B.append({})

    res = 0
    for num in nums:
       handle_mod(num,M,B)

    for num in nums:
        d = len(str(num))
        m = num % M
        # print(d,m, B[d].get((M - m)%M,0))
        res = res + B[d].get((M-m)%M, 0)

    print(res)







if __name__ == "__main__":
    main()
