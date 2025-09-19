# coding=utf-8
#!/usr/bin/env python

"""

2696. 删除子串后的字符串最小长度
https://leetcode.cn/problems/minimum-string-length-after-removing-substrings/description/

思路：用栈的思想，一边遍历一边与栈顶元素匹配，满足条件pop出来

"""
from typing import List


class Solution:
    def minLength(self, s: str) -> int:
        if not s :
            return 0
        st:List[str] = []
        res = len(s)
        for i in range(len(s)):
            if s[i] == 'D':
                if len(st) > 0 and st[len(st)-1] =='C':
                    st.pop()
                    res-=2
                else:
                    st.append(s[i])
            elif s[i] == 'B':
                if len(st) > 0 and st[len(st)-1] =='A':
                    st.pop()
                    res-=2
                else:
                    st.append(s[i])
            else:
                st.append(s[i])
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.minLength("ACBBD"))



