# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/11/18 21:48

https://ac.nowcoder.com/acm/contest/22353/1002

思路：写一个前缀和，每次询问 T ，二分查找找到大于T的第一个位置，输出对应位置的音符

"""
from typing import List


def search(nums:List[int],target:int,l:int,r:int):

   while l < r :
      mid = l + (r-l)//2
      if nums[mid] <= target:
         l = mid + 1
      else:
         r = mid
   return l

def main():
   n,q = map(int,input().split())
   b = list(map(int,input().split()))
   prefix = [0] * (n+1)
   for i in range(1,n+1):
      prefix[i] = prefix[i-1]+ b[i-1]

   q_list = list((map(int,input().split())))
   for q in q_list:
      print(search(prefix,q,1,n))



if __name__ == "__main__":
    main()
