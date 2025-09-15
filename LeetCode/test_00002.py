# coding = utf-8
#!/usr/bin/env python
from typing import List, Dict

"""
字母异位词： https://leetcode.cn/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-100-liked
"""

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        word_map: Dict[str,List[str]] = dict()

        for s in strs:
            tmp = ''.join(sorted(s))
            if word_map.get(tmp) is None:
                word_map[tmp] = []
            word_map[tmp].append(s)

        return list(word_map.values())

if __name__ == "__main__":
    solution = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    res = solution.groupAnagrams(strs)
    print(res)
