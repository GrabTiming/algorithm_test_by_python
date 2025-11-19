# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/11/19 23:21

https://atcoder.jp/contests/abc432/tasks/abc432_c

数学题，拿纸和笔写几道公式，让ai给点思路慢慢写出来就好了

"""

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)


def main():
    n,x,y = map(int, input().split())
    A_list = list(map(int, input().split()))

    max_A = max(A_list)
    min_A = min(A_list)

    if min_A * y < max_A * x:
        print("-1")
        return

    d = y-x
    g = gcd(x,d)
    m = d/g

    target = A_list[0] % m
    for i in range(1,n):
        if A_list[i] % m != target:
            print("-1")
            return

    w = min_A*y
    rem = (w- A_list[0]*x) % d
    w = w -rem
    res = (n*w - x * sum(A_list)) /d
    print(int(res))




if __name__ == "__main__":
    main()
