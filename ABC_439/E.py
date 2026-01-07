# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2026/1/6 22:49

https://atcoder.jp/contests/abc439/tasks/abc439_e

题意： 有n个人， 每个人i 站在(x_i,0) ,想放风筝到 (y_i,1)。  任意两个人的这两个坐标连成的线不能有交点，问最多有多少人放风筝

思路：首先按第一关键字排序，
设位置1<=i最多放风筝的人为 f[i], 那么f[i] = max(f[j]) + 1 ,位置j需要满足 Y[j] < Y[i]
本质就是个最长上升子序列问题

"""
from bisect import bisect_left
from collections import deque


def main():
    n = int(input())
    pairs = []
    for i in range(n):
        x,y = map(int,input().split())
        pairs.append((x,y))

        # 按 x 升序排序，如果 x 相同则按 y 降序（重要）
    pairs.sort(key=lambda item: (item[0], -item[1]))

    # 然后对 y 坐标求 LIS
    y_coords = [pair[1] for pair in pairs]

    # 使用二分查找求 LIS
    lis = []
    for y in y_coords:
        pos = bisect_left(lis, y)
        if pos == len(lis):
            lis.append(y)
        else:
            lis[pos] = y

    print(len(lis))



if __name__ == "__main__":
    main()
