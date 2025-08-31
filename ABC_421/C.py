# coding = utf-8
#!/usr/bin/env python

"""
题意：一个字符串有AB两种字符，可以交换相邻的字符，问最少需要几次操作才能使得没有项目字符相邻

思路：那每种字符要么是偶数位要么是奇数位，遍历一下判断就好

"""

def main():
    n = int(input())
    s = input()
    cor_idx = 0
    cnt1 = 0
    for idx,c in enumerate(s):
        if c == 'B':
            cnt1 += abs(idx -cor_idx)
            cor_idx +=2
    cor_idx = 0
    cnt2 = 0
    for idx,c in enumerate(s):
        if c == 'A':
            cnt2 += abs(idx -cor_idx)
            cor_idx +=2
    print(min(cnt1,cnt2))

if __name__ == '__main__':
    main()