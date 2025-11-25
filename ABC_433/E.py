# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/11/23 22:55

https://atcoder.jp/contests/abc433/tasks/abc433_e

题意：n和m，X数组和Y数组，X[i]表示第i行最大的数，Y[j]同理，都是1到n*m的数。问是否存在一个二维矩阵，元素是1到n*m之间且不同。有则输出

思路：
1. 首先要确定 X数组中各元素不同，假设存在X[1] 和X[2] 都为Z，那二维数组的这两行之一肯定都要有 Z为max，不符题意；y数组同理
2. 从n*m遍历到1，每个数字出现的情况有以下几种：
a. 出现在X和Y，
b. 出现在X
c. 出现在Y
d  没有出现

情况a已经定死了，不讨论
情况b和情况c一样，以情况b举例。如果只出现在X，那么找到一个最小的列 i 使得 Y[i] > 当前数字，放进去就好。
情况d：维护所有行和列都没有确定最大值的位置， 当前num放进一个 min(X[r],Y[c]) 最小的位置
"""
from typing import List


def add(r:int,c:int,res:List[List[int]],ready_position:List[tuple[int,int]]):
    """

    :param r:
    :param c:
    :param res:
    :param ready_position:
    :return:
    """
    if res[r][c] != 0 :
        return
    ready_position.append((r,c))



def solve():
    n,m = map(int,input().split())
    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))

    # 验证条件1
    SX = set(X)
    SY = set(Y)
    # 存在重复元素
    if len(SX) < n or len(SY) < m :
        print("No")
        return
    map_X = {}
    map_Y = {}
    for (idx,x) in enumerate(X):
        map_X[x] = idx
    for (idx, y) in enumerate(Y):
        map_Y[y] = idx

    # 根据下面遍历的顺序，
    ready_X = []
    ready_Y = []
    ready_position = []
    res = []
    for i in range(0,n):
        res.append([0]*m)

    # 根据下面遍历的顺序， 上面ready_X,ready_Y,ready_position 满足从开始到末尾，min(X,Y)是递减的
    for num in range(n*m,0,-1):
        r = map_X.get(num,-1)
        c = map_Y.get(num,-1)
        if r !=-1 and c !=-1:
            res[r][c] = num
            for i in ready_Y:
                add(r,i,res,ready_position)
            for i in ready_X:
                add(i,c,res,ready_position)
            ready_X.append(r)
            ready_Y.append(c)
        elif r !=-1:
            if len(ready_Y) == 0:
                print("No")
                return
            col = ready_Y[-1]
            res[r][col] = num
            for c in ready_Y:
                add(r,c,res,ready_position)
            ready_X.append(r)
        elif c !=-1:
            if not ready_X :
                print("No")
                return
            row = ready_X[-1]
            res[row][c] = num
            for r in ready_X:
                add(r,c,res,ready_position)
            ready_Y.append(c)
        else:
            if len(ready_position) == 0 :
                print("No")
                return
            r,c = ready_position.pop()
            res[r][c] = num


    print("Yes")
    for i in range(0,n):
        for j in range(0,m):
            print(res[i][j],end=" ")
        print()




def main():
    t = int(input())
    while t>0 :
        t -= 1
        solve()



if __name__ == "__main__":
    main()
