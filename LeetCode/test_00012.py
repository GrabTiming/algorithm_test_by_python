# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/9/20 09:43


895. 最大频率栈
https://leetcode.cn/problems/maximum-frequency-stack/description/

思路：
代码写得有些抽象，堆栈元素设为[val,cnt,time]，分别表示值，栈中相同元素个数，该元素插入时间，排序规则按 cnt(从大到小),time(从后到前)
然后用一个map记录下每种元素的次数，堆栈pop出来发现次数不对，就校准次数重新入栈

"""


import heapq

class Pair:

   def __init__(self, val, cnt,time):
      self.val = val
      self.cnt = cnt
      self.time = time

   def __str__(self):
      return str(self.val) + ":" + str(self.cnt) + ":" + str(self.time)

   def __lt__(self, other):
     if self.cnt == other.cnt:
       return self.time > other.time
     else:
       return self.cnt > other.cnt


class FreqStack:

   def __init__(self):
      self.queue = []
      self.map = {}
      self.time = 0

   def push(self, val: int) -> None:
      cnt = self.map.get(val,0)
      self.map[val] = cnt + 1
      heapq.heappush(self.queue,Pair(val,cnt+1,self.time))
      self.time += 1
      # for i in self.queue:
      #    print(i)
      # print("++++++++++++++++++++++++++++")



   def pop(self) -> int:
      tmp:Pair = Pair(0,0,0)
      while self.queue and self.queue[0].cnt != self.map.get(self.queue[0].val,0):
          tmp = heapq.heappop(self.queue)
          if self.map.get(tmp.val,0):
             heapq.heappush(self.queue, Pair(tmp.val, self.map[tmp.val],tmp.time))
      pair:Pair = heapq.heappop(self.queue)
      self.map[pair.val] -= 1

      # for i in self.queue:
      #    print(i)
      # print("======================================")
      return pair.val



def main():
    fst = FreqStack()
    fst.push(5)
    fst.push(7)
    fst.push(5)
    fst.push(7)
    fst.push(4)
    fst.push(5)
    print(fst.pop())
    print(fst.pop())
    print(fst.pop())
    print(fst.pop())



if __name__ == "__main__":
    main()
