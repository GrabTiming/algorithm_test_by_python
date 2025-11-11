# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/11/11 23:23
"""
from typing import List


def main():
    n,m,k = map(int, input().split())

    head_list:List[int] = list(map(int, input().split(' ')))
    body_list:List[int] = list(map(int, input().split(' ')))

    head_list.sort()
    body_list.sort()
    l,r,res = 0,0,0
    while l < n and r < m:
      if head_list[l] <= body_list[r]:
         res += 1
         l += 1
      r += 1

    if res >= k:
         print("Yes")
    else:
         print("No")





if __name__ == "__main__":
    main()
