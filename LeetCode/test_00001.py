# coding=utf-8
#!/usr/bin/env python

"""
leetcode：两数之和 https://leetcode.cn/problems/two-sum/description/?envType=study-plan-v2&envId=top-100-liked
"""

from typing import List, Tuple


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_map = dict()
        for (idx, num) in enumerate(nums):

            if num_map.get(target-num) is not None:
                return [num_map[target-num],idx]
            num_map[num] = idx
        return []

if __name__ == "__main__":
    solution = Solution()

    print(solution.twoSum([1,2,3,4,5],3))
