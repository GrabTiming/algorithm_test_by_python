# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2026/1/12 23:48

题意： n种饼干，每种饼干美味值为A[i] ，选K个饼干，问不同选法下，前X大总和

思路：排序，然后将相邻差值放入优先队列，每次取最小。
按思路做了之后发现不太对，最终还是看了别的老哥的解法。
对于 (i,cnt_i) ，那么它有两种发展方向，一种是将一个i替换成 i+1, 那就变成了 (i,cnt_i -1) ,而下一个位置变成(i+1,cnt_{i+1}+1)
而另一种则是从上一位置转换过来， 变成 (i,cnt_i +1) 而上一个位置变成 (i-1,cnt_{i-1}-1)

"""
import heapq
import sys

input = sys.stdin.readline

def main():
   n,k,x = map(int,input().split())
   A = list(map(int,input().split()))
   A.sort(reverse=True)
   costs = [0]+[A[i]-A[i+1] for i in range(n-1)]
   s = A[0]*k
   res = []
   if n==1:
       print(s)
       return

   queue = [(0,0,k,0)]

   for _ in range(x):
       (cost,ci,cj,j) = heapq.heappop(queue)

       res.append(s-cost)
       if j+1 < n:
           heapq.heappush(queue,(cost+costs[j+1],cj-1,1,j+1))
       if ci:
           heapq.heappush(queue,(cost+costs[j],ci-1,cj+1,j))
   for val in res:
       print(val)





if __name__ == "__main__":
    main()
