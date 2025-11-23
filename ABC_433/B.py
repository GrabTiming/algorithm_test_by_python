# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/11/23 11:03

https://atcoder.jp/contests/abc433/tasks/abc433_b

题意：给出一个队列，对于位置i，找到左边 比位置i大的第一个数的位置

思路：单调栈，对于位置i，如果栈顶元素 <= 该位置元素就pop，一直找到 大于该位置的元素

"""


def main():
   n = map(int,input())
   num_list = list(map(int,input().split()))

   stack = []
   top = 0
   for (idx,num) in enumerate(num_list):
       while top > 0 and num_list[stack[top-1]] <= num:
               stack.pop()
               top -= 1
       if top > 0 :
           print(stack[top-1]+1)
       else:
           print(-1)
       stack.append(idx)
       top += 1

if __name__ == "__main__":
    main()
