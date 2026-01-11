# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2026/1/11 09:40

https://atcoder.jp/contests/abc440/tasks/abc440_d

题意：给出一个数组A，每次询问第Y小的 大于等于X的 不出现在A的 数是多少

思路：二分答案， 对于 答案 ans，去计算它是第几小的，与Y做比较， [ans-x+1] - (x~ans这个区间有多少个数出现在A中)


"""
import bisect
import sys

input = sys.stdin.readline

def lower_bound(num,A):
    return bisect.bisect_left(A,num)

def upper_bound(num,A):
    return bisect.bisect_right(A,num)


def main():
    INF = 2*(10**9)+10
    n,q = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    for _ in range(q):
        x,y = map(int,input().split())
        L,R = x-1,x+y+n
        x_idx = lower_bound(x, A)
        while L < R:
            mid = (L+R)//2
            count = mid - x + 1
            count -= upper_bound(mid,A) - x_idx
            if count < y:
                L = mid + 1
            else:
                R = mid
        print(R)


if __name__ == "__main__":
    main()
