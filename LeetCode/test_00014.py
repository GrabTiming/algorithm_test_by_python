# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/9/20 11:04

3325. 字符至少出现 K 次的子字符串 I
https://leetcode.cn/problems/count-substrings-with-k-frequency-characters-i/description/

思路：双指针，往右遍历，每次添加s[r]的次数，找到一个最大的l，满足[l,r]内至少有一个字母出现次数大于等于k次

"""
from typing import Dict


class Solution:

   def check(self,cnt_map:Dict[str,int], s:str,k:int):

       for key,val in cnt_map.items():
           tmp = -1 if key == s else 0
           if cnt_map.get(key,0) +tmp >= k:
               return True

       return False


   def numberOfSubstrings(self, s: str, k: int) -> int:

      l,r,n = 0,0,len(s)
      cnt_map = {}
      res = 0
      while r < n:
          cnt = cnt_map.get(s[r],0)
          cnt_map[s[r]] = cnt + 1
          while l <= r and self.check(cnt_map,s[l],k) :
            cnt_map[s[l]] -= 1
            l += 1
          if self.check(cnt_map,"",k):
              res += l+1
          r += 1
      return res



def main():
    solution = Solution()
    print(solution.numberOfSubstrings("abacb",2))
    print(solution.numberOfSubstrings("abcde",1))



if __name__ == "__main__":
    main()
