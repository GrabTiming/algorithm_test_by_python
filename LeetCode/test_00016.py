# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/10/13 22:35
"""
from typing import List


class Solution:

    def handle(self,s: str):
        return "".join(sorted(s))

    def removeAnagrams(self, words: List[str]) -> List[str]:

        if len(words) <=1:
            return words
        res:List[str] = [words[0]]
        for r in range(1,len(words)):
            if self.handle(words[r-1]) != self.handle(words[r]):
                res.append(words[r])
        return res


def main():
    solution = Solution()
    res = solution.removeAnagrams(["abba","baba","bbaa","cd","cd"])
    print(res)


if __name__ == "__main__":
    main()
