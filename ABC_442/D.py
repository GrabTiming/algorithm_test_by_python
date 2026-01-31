# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2026/1/31 10:37

题意：两种操作，一个是对于位置x，交换x 和x+1 位置的数；第二个是区间求和
思路： 树状数组 或者 线段树。 交换操作 可以看作对 x位置 增加(a[x+1]-a[x]) 对x+1位置增加(a[x]-a[x-1])

"""

class Tree:

    def __init__(self,n):
        self.n = n
        self.tr = [0] * (n+1)


    def add(self,x,inc):
        while x <= self.n:
            self.tr[x] += inc
            x = x + (x&-x)

    def sum(self,x):
        res = 0
        while x > 0 :
            res += self.tr[x]
            x = x - (x&-x)
        return res

    def query(self,l,r):
        return self.sum(r) - self.sum(l-1)


def main():
    n,q = map(int,input().split())
    tree = Tree(2*n)
    a = list(map(int,input().split()))
    a = [0] + a
    for i in range(1,n+1):
        tree.add(i,a[i])
    for i in range(q):
        query = list(map(int,input().split()))
        if len(query) == 2:
            x = query[1]
            tree.add(x,a[x+1]-a[x])
            tree.add(x+1,a[x]-a[x+1])
            a[x],a[x+1] = a[x+1],a[x]
        else:
            l,r = query[1],query[2]
            print(tree.query(l,r))


if __name__ == "__main__":
    main()
