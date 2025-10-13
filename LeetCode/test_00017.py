# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/10/13 22:54

3440. 重新安排会议得到最多空余时间 II
https://leetcode.cn/problems/reschedule-meetings-for-maximum-free-time-ii/description/

不会，抄题解的：
思路：获取前三空位区间，遍历每个活动，查看最大的三个空位是否能放下这个活动（注意要判断前后空位是否再前三大空位之前）

"""
from typing import List


class Solution:
   def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
      n = len(startTime)

      def get(i:int) -> int:
          if i == 0 :
              return startTime[0]
          if i == n:
              return eventTime-endTime[n-1]
          return startTime[i]-endTime[i-1]

      a,b,c = 0,-1,-1
      for i in range(1,n+1):
          sz = get(i)
          if sz > get(a):
              a,b,c = i,a,b
          elif b<0 or sz > get(b):
              a,b,c = a,i,b
          elif c<0 or sz > get(c):
              a,b,c = a,b,i

      ans = 0
      for i,(s,e) in enumerate(zip(startTime,endTime)):
          sz = e - s
          if i != a and  i+1!=a and sz <=get(a) or i !=b and i+1 !=b and sz <=get(b) or sz <= get(c):
             ans = max(ans,get(i)+sz+get(i+1))
          else :
             ans = max(ans,get(i)+get(i+1))
      return ans



def main():
    pass


if __name__ == "__main__":
    main()
