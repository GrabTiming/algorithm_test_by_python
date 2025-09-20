# coding=utf-8
#!/usr/bin/env python

"""

https://leetcode.cn/problems/bitwise-ors-of-subarrays/description/
898. 子数组按位或操作

不会做，看题解


思路：暴力二重循环，将每个子数组的或和存进set里, 对于arr[r] = x , 往前遍历，记录或和，如果无法增大，说明继续往左也无法增大了，直接退出循环
数据范围是1e4 , 由于二进制操作的性质，第二重循环只有log 的复杂度，因此不会超时

"""
from typing import List


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        st = set()

        for (idx,num) in enumerate(arr) :
            st.add(num)
            for j in range(idx-1,-1,-1):

                if arr[j]|num == arr[j]:
                    break
                arr[j]|=num
                st.add(arr[j])
        return len(st)


if __name__ == "__main__":
    s = Solution()
    print(s.subarrayBitwiseORs([1,1,2]))

