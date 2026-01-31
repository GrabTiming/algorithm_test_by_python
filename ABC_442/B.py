# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2026/1/31 10:06
"""


def main():

    n = int(input())
    is_playing = 0
    vol = 0
    for i in range(n):
        op = int(input())
        if op == 1:
            vol += 1
        elif op == 2:
            vol = max(0,vol-1)
        else:
            is_playing = 1 - is_playing

        print("Yes" if is_playing == 1 and vol >= 3 else "No")



if __name__ == "__main__":
    main()
