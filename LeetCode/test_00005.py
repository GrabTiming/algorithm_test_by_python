# coding=utf-8
#!/usr/bin/env python

"""
https://leetcode.cn/problems/count-collisions-on-a-road/
2211. 统计道路上的碰撞次数

思路：对于向右的车，遇到S或者L 一定会撞上；对于向左同理；从左向右扫一遍向右的车，从右向左扫一遍向左的车

"""


class Solution:
    def countCollisions(self, directions: str) -> int:
        if not directions:
            return 0
        res:int = 0

        R_num = 0
        for c in directions:
            if c == 'R':
                R_num = R_num + 1
            else:
                res = res + R_num
                R_num = 0
        L_num = 0
        for c in reversed(directions):
            if c == 'L':
                L_num = L_num + 1
            else :
                res = res + L_num
                L_num = 0

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.countCollisions("RLRSLL"))