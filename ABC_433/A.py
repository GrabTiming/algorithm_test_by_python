# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/11/23 10:48

https://atcoder.jp/contests/abc433/tasks/abc433_a

题意： 是否存在一个W 使得 (X+W) = Z * (Y+W)

X - Z*Y = (Z-1) * W

"""


def main():
    X,Y,Z = map(int,input().split())

    res1 = X - Z*Y
    res2 = Z - 1
    # print(res1)
    # print(res2)

    if X == Y*Z:
        print("Yes")
        return


    if res1 < 0 :
        print("No")
        return
    else:
        if res1 % res2 == 0:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
