# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/11/18 22:03

https://ac.nowcoder.com/acm/contest/22353/1003

思路：二分答案，假设答案为x，按照题意模拟计算每一天的快乐值不小于这个x，看看能不能满足条件即可

"""
from typing import List


def check(p:List[int],d:int,x:int):

    now = 0
    idx = 0
    n = len(p)
    res = []
    for count in range(1,d+1):
        while idx < n and now < x:
            now += p[idx]
            res.append(count)
            idx += 1
        if now < x:
            return False,[]
        now = now/2
    # 吃不完的放到最后一天吃完
    while idx < n:
        res.append(d)
        idx += 1
    return True,res



def main():
    n,d = map(int, input().split())
    p = []
    for i in range(n):
        p.append(int(input()))
    l = 0
    r = 5* (10 ** 10)+10
    ans = None
    while l < r :
        mid = l + (r-l+1)//2
        flag,res = check(p,d,mid)
        if flag:
            l = mid
            ans = res
        else:
            r = mid - 1

    print(l)
    for x in ans:
        print(x)




if __name__ == "__main__":
    main()
