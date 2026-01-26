# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2026/1/26 23:04

https://atcoder.jp/contests/abc441/tasks/abc441_d

题意：给一个n个点m条边的 有向图，问所有从1出发，走L条边，路过的所有边权总和在[S,T]中的终点位置
思路：bfs
"""
from collections import deque

def main():
    n, m, L, S, T = map(int, input().split())
    g = [[] for _ in range(n)]
    for i in range(m):
        u,v,w = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append((v,w))

    ans = set()
    q = deque([(0,0,0)])
    while q:
        cur, step, total = q.popleft()
        if step == L:
            if S <= total <= T:
                ans.add(cur)
            continue
        for nxt, w in g[cur]:
            q.append((nxt, step+1, total+w))
    if len(ans) == 0:
        print('')
    else:
        ans = list(ans)
        ans.sort()
        for i in ans:
            print(i + 1, end=' ')






if __name__ == "__main__":
    main()
