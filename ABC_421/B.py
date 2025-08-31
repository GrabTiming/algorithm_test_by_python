# coding = utf-8
#!/usr/bin/env python

"""按照题意模拟即可"""

def main():
    x, y = map(int, input().split())
    for i in range(2,10):
        tmp = x + y
        tmp = int("".join(reversed(str(tmp))))
        # 去掉前导零
        x = y
        y = tmp
    print(y)

if __name__ == '__main__':
    main()