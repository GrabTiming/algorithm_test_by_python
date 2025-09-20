# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/9/20 10:37

1695. 删除子数组的最大得分
https://leetcode.cn/problems/maximum-erasure-value/description/

思路：双指针，维护一个set记录子数组的元素，遍历到arr[r], l一直往右走直到set中没有arr[r]

"""
from typing import List, Set


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        num_st:Set[int] = set()
        l,r,res,tmp_sum = 0,0,0,0
        while r < len(nums):
            while nums[r] in num_st:
                num_st.remove(nums[l])
                tmp_sum -= nums[l]
                l += 1
            num_st.add(nums[r])
            tmp_sum += nums[r]
            res = max(res,tmp_sum)
            r += 1
        return res


def main():
    s = Solution()
    print(s.maximumUniqueSubarray([4,2,4,5,6]))
    print(s.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))


if __name__ == "__main__":
    main()
