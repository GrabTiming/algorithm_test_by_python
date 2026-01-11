# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2026/1/10 20:10
"""


def main():
    x,y = map(int,input().split())
    res = x
    for i in range(y):
       res = res * 2
    print(res)



if __name__ == "__main__":
    main()
