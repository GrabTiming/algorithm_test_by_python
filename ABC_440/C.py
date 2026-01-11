# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2026/1/10 20:27

https://atcoder.jp/contests/abc440/tasks/abc440_c

题意：一个长度为n的数组，要求执行一次操作，任取一个正整数x，对于所以位置 (i+x)%2w < w ，将它们的值取总和，问总和最小是多少

思路: 可以想到 如果n < w ,那么可以令 所有  (i+x)%2w >=w 直接返回0
当n >=w 时，设 s[i] 为 将对2w取模为i的所有位置加起来， 那么题意要求 就是找到某个 i 使得 s[i...i+w-1] 最小，
为防止数组越界，可以将s数组 变成 s+s ，然后求前缀和

"""


def solve():
   n,w = map(int,input().split())
   a = list(map(int,input().split()))
   if n < w:
      print(0)
      return
   a_sum = [0] * (w*2+1)
   for i in range(0,n):
      a_sum[i%(2*w)] += a[i]
   a_ss = [0] * (w*4+1)
   for i in range(1,w*4+1):
      a_ss[i] = a_ss[i-1] + a_sum[(i-1)%(2*w)]
   res = 10**18
   for i in range(1,w*2+1):
      res = min(res,a_ss[i+w-1]-a_ss[i-1])

   print(res)


def main():
   t = int(input())
   while t >0:
      t-=1
      solve()

if __name__ == "__main__":
    main()

"""
1
8 2
1 10 10 1 1 10 10 1
"""