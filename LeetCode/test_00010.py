# coding = utf -8
#!/usr/bin/env python

"""

290. 单词规律

https://leetcode.cn/problems/word-pattern/description/

思路：双向映射唯一值，要求一对一。那么找一下word对应的字母，和字母对应的word 看看是不是符合预期就行了

"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        word_list = s.split(" ")
        if len(word_list) != len(pattern):
            return False

        word_map = {}
        char_map = {}
        for i in range(len(pattern)):
            if word_map.get(word_list[i]) is None and char_map.get(pattern[i]) is None:
                word_map[word_list[i]] = pattern[i]
                char_map[pattern[i]] = word_list[i]
            elif word_map.get(word_list[i]) is not None and word_map[word_list[i]] != pattern[i]:
                return False
            elif char_map.get(pattern[i]) is not None and char_map[pattern[i]] != word_list[i]:
                return False

        return True


