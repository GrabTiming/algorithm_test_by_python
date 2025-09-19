# coding=utf-8
#!/usr/bin/env python
from typing import List

"""

128. 连续最长子序列
https://leetcode.cn/problems/longest-consecutive-sequence/description/

思路：用一个set或者map装着元素，每个元素，如果它是第一个开头，就不断+1往后搜，然后统计答案取max

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in nums:
                current = num
                tmp_len = 1
                while current + 1 in nums:
                    current += 1
                    tmp_len += 1
                res = max(res, tmp_len)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive([100,4,200,1,3,2]))




