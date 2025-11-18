# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/11/17 08:44

https://ac.nowcoder.com/acm/contest/22353/1001
题意：给定一个数组，每次询问 [l,r] ,问在这个区间内的数的个数
"""
from typing import List


def get_min_index(nums:List[int], target:int):
   l = 0
   r = len(nums)-1
   while l<r:
      mid = l+(r-l)//2
      if nums[mid] < target:
           l = mid+1
      else:
           r = mid
   return l

def get_max_index(nums:List[int], target:int):
   l = 0
   r = len(nums)-1
   while l<r:
      mid = l+ (r-l+1)//2
      if nums[mid] <= target:
           l = mid
      else:
           r = mid-1
   return l

def main():
    n,q = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    for i in range(q):
        l,r = map(int, input().split())
        idx_l = get_min_index(nums, l)
        idx_r = get_max_index(nums, r)
        if nums[idx_r] > r:
           idx_r -= 1
        print(idx_r-idx_l+1)

if __name__ == "__main__":
    main()
