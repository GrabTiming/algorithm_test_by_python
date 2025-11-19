# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/11/19 22:42

https://atcoder.jp/contests/abc432/tasks/abc432_b

题意：给出一个数，将它的各个数位重新排列得到最小的数，不能包含前导零
"""


def main():
    num = input()
    digits = [int(i) for i in num]
    digits.sort()
    idx = 0
    while idx < len(digits):
        if digits[idx]!=0:
            digits[0],digits[idx] = digits[idx],digits[0]
            break
        idx += 1
    print(''.join(map(str,digits)))




if __name__ == "__main__":
    main()
