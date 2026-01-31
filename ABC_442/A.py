# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2026/1/31 10:00
"""


def main():
    s = input()
    cnt = 0
    for i in s :
       if i == 'i' or i == 'j':
          cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
