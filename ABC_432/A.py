# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/11/18 21:24
"""


def main():
   nums = list(map(int, input().split()))
   nums.sort(reverse=True)
   print(''.join(map(str, nums)))


if __name__ == "__main__":
    main()
