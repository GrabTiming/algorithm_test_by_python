# coding = utf-8
#!/usr/bin/env python

def main():
    mp = {}
    n = int(input())
    for i in range(n):
        s = input()
        mp[i+1] = s
    num,name= (input()).split()
    num = int(num)
    if mp.get(num,"") == name:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()