# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2026/1/6 22:35

https://atcoder.jp/contests/abc439/tasks/abc439_d

题意: 找到一个三元组 (i,j,k) 需要 满足 数组对应的三个位置的数的比例为 7:5:3 , 其中j 需要是(i,j,k)中最大或最小的一位

思路: 两次遍历，从前到后，从后到前

"""


def main():
   n = int(input())
   num_list = list(map(int,input().split()))
   num_map = {}
   res = 0

   for j in range(0,n):
      if num_list[j] % 5 == 0 :
         x = num_list[j] /5 * 3
         y = num_list[j] /5 * 7
         res += num_map.get(x,0) * num_map.get(y,0)
      num_map[num_list[j]] = num_map.get(num_list[j],0) + 1
   num_map = {}
   for j in range(n-1,-1,-1):
      if num_list[j] % 5 == 0 :
         x = num_list[j] /5 * 3
         y = num_list[j] /5 * 7
         res += num_map.get(x,0) * num_map.get(y,0)
      num_map[num_list[j]] = num_map.get(num_list[j],0) + 1
   print(res)



if __name__ == "__main__":
    main()
