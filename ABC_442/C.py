# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2026/1/31 10:26

题意： 每个人 从没有利益冲突的人中抽三个人出来，问这样的组合数是多少
"""



def main():
   n,m = map(int,input().split())
   conflict = [0] * (n+1)
   for i in range(m):
      a,b = map(int,input().split())
      conflict[a] += 1
      conflict[b] += 1

   for i in range(1,n+1):
      no_conflict = n-1 - conflict[i]
      print(no_conflict * (no_conflict-1) * (no_conflict-2) // 6,end=" ")




if __name__ == "__main__":
    main()
