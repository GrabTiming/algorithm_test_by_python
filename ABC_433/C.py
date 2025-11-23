# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
@Author : Liang2003
@Time   : 2025/11/23 11:21

题目：统计字符串中满足条件的子串数量
条件：子串长度为偶数，前一半字符相同，后一半字符相同，且后一半字符 = 前一半字符 + 1
"""


def main():
    # 读取输入
    s = input().strip()
    if not s:  # 处理空字符串
        print(0)
        return

    # 在字符串末尾添加哨兵字符，便于处理边界
    s = s + " "

    # 将连续相同字符分组，存储为 (字符, 连续出现次数)
    char_groups = []
    current_char = s[0]
    current_count = 1

    # 从第二个字符开始遍历（跳过索引0）
    for char in s[1:]:
        if char == current_char:
            current_count += 1
        else:
            char_groups.append((int(current_char), current_count))
            current_char = char
            current_count = 1

    # 统计满足条件的子串数量
    result = 0

    # 遍历相邻的字符组
    for i in range(len(char_groups) - 1):
        current_digit, current_count = char_groups[i]
        next_digit, next_count = char_groups[i + 1]

        # 检查是否满足条件：后一个字符 = 前一个字符 + 1
        if next_digit == current_digit + 1:
            # 取两个连续段的最小长度作为可形成的子串数量
            result += min(current_count, next_count)

    print(result)


if __name__ == "__main__":
    main()