# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2026/1/10 10:09

https://atcoder.jp/contests/abc436/tasks/abc436_d

题意： 一个n,m的图，从左上角到右下角需要走多少步， '.'是正常道路，'#'障碍，还有其他小写字母，相同字母可以传送

思路: bfs, 除了常规的上下左右，还有在第一次遇到字母c的时候，把所有是c字母的位置放到队列中，

"""
from collections import deque


def main():
    n,m = map(int,input().split())
    s = []
    for i in range(n):
       t = input()
       s.append(t)
    f = []
    inf = n*m +10

    same_word = []
    is_add = [0]*26
    d = [(0,-1),(0,1),(-1,0),(1,0)]
    for i in range(26):
        same_word.append([])
    for i in range(n):
        for j in range(m):
            if s[i][j] != '.' and s[i][j] !='#':
                same_word[int(ord(s[i][j])-ord('a'))].append((i,j))

    for i in range(n):
        f.append([inf]*m)

    f[0][0] = 0
    q = deque()
    q.append((0,0))

    while q:
        x,y = q.popleft()
        # print(x,y,f[x][y],s[x][y])
        for (dx,dy) in d:
            nx = x + dx
            ny = y + dy
            if nx<0  or nx>=n or ny<0 or ny>=m:
                continue
            if s[nx][ny] =='#' or f[nx][ny]!=inf:
                continue
            f[nx][ny] = f[x][y] + 1
            q.append((nx,ny))

        if s[x][y] =='.':
            continue
        c = int(ord(s[x][y])-ord('a'))
        if is_add[c]:
            continue
        is_add[c] = 1
        for (nx,ny) in same_word[c]:
            if f[nx][ny] != inf:
                continue
            f[nx][ny] = f[x][y] + 1
            q.append((nx,ny))

    if f[n-1][m-1] >= inf:
       print(-1)
    else:
       print(f[n-1][m-1])


if __name__ == "__main__":
    main()
