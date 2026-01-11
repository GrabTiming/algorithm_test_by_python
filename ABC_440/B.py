# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2026/1/10 20:12
"""


def main():
    N = int(input())
    A = list(map(int, input().split()))
    res = [i for i in range(N)]
    res.sort(key=lambda x: A[x])
    print(res[0]+1,res[1]+1,res[2]+1)




if __name__ == "__main__":
    main()
