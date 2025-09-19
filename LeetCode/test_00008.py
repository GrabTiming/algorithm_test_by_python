# coding=utf-8
#!/usr/bin/env python
import bisect
import heapq
from typing import List

"""
https://leetcode.cn/problems/design-task-manager/

任务管理器系统 
要维护一个按照一定顺序排序的队列，且要支持队列种元素的修改
用一个堆维护，再加一个map映射元素id和元素，修改时将原本的元素设为无效，将修改后的新元素重新插入

"""

MX = -1

class Task:

    def __init__(self,user_id,task_id,priority):
        self.user_id = user_id
        self.task_id = task_id
        self.priority = priority


    def __lt__(self, other):
        if self.priority == other.priority:
            return self.task_id < other.task_id
        return self.priority < other.priority

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.queue = []
        self.task_map = {}
        for task in tasks:
            user_id = task[0]
            task_id = task[1]
            priority = task[2]
            task_obj = Task(user_id, -task_id, -priority)
            self.task_map[task_id] = (priority,user_id)
            heapq.heappush(self.queue, task_obj)


    def add(self, userId: int, taskId: int, priority: int) -> None:
        task_obj = Task(userId, -taskId, -priority)
        self.task_map[taskId] = (priority,userId)
        heapq.heappush(self.queue, task_obj)

    def edit(self, taskId: int, newPriority: int) -> None:

        self.add(self.task_map[taskId][1], taskId, newPriority)

    def rmv(self, taskId: int) -> None:

        self.task_map[taskId] = (-1,-1)

    def execTop(self) -> int:
        while self.queue:
            task = heapq.heappop(self.queue)
            if self.task_map[-task.task_id] == (-task.priority,task.user_id):
                self.rmv(-task.task_id)
                return task.user_id
        return -1

if __name__ == '__main__':
    # tasks =[[1,20,10],[2,28,34],[10,12,40],[4,8,6]]
    tasks = [[8,17,33],[4,14,42]]
    task_manager = TaskManager(tasks)
    task_manager.edit(14,21)

    print(task_manager.execTop())