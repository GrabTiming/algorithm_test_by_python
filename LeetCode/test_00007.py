# coding=utf-8
#!/usr/bin/env python

"""
459. 重复的子字符串
https://leetcode.cn/problems/repeated-substring-pattern/description/

思路：

"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)