# coding = utf-8
#!/usr/bin/env python

"""
题意：
在一个无限大的棋盘，两个人同时从不同的位置移动，问过程中相遇的次数

思路：移动的次数n很大，移动的信息按方向+朝这个方向的次数，直到下次变换方向，可以将这个移动分解为 A和B 分别从某个方向出发，移动相同步数，看是否有交点

"""

def main():
    x1,y1,x2,y2 = map(int,input().split())
    N,M,L = map(int,input().split())
    S = []
    for i in range(M):
        d,cnt = input().split()
        S.append([d,int(cnt)])

    T = []
    for i in range(L):
        d,cnt = input().split()
        T.append([d,int(cnt)])

    move_list = []
    i,j = 0,0
    while i < M and j < L:
        if S[i][1] == T[j][1]:
            move_list.append([S[i][0],T[j][0],S[i][1]])
            i += 1
            j += 1
        elif S[i][1] < T[j][1]:
            move_list.append([S[i][0],T[j][0],S[i][1]])
            T[j][1] -= S[i][1]
            i += 1
        else:
            move_list.append([S[i][0],T[j][0],T[j][1]])
            S[i][1] -= T[j][1]
            j += 1

    dir = {
        "U":(-1,0),
        "D":(1,0),
        "L":(0,-1),
        "R":(0,1)
    }

    res = 0
    for (d1,d2,cnt) in move_list:
        d1 = dir[d1]
        d2 = dir[d2]
        if d1[0] == d2[0]:
            if x1 == x2:
                if d1[1] == d2[1] :
                    res += cnt if y1==y2 else 0
                else:
                    if (d1[1]!= d2[1]) and (y2-y1) % (d1[1]-d2[1]) == 0:
                        tmp = (y2-y1)/(d1[1]-d2[1])
                        if 1<=tmp <= cnt:
                            res+=1
        else :
            if d1[1] == d2[1]:
                if y1==y2 and (x2 - x1) % (d1[0] - d2[0]) == 0:
                    tmp = (x2 - x1) / (d1[0] - d2[0])
                    if 1 <= tmp <= cnt:
                        res += 1
            else:
                if ((x2 - x1) % (d1[0] - d2[0]) == 0) and ((y2 - y1) % (d1[1] - d2[1]) == 0):
                    tmp1 = (x2 - x1) / (d1[0] - d2[0])
                    tmp2 = (y2 - y1) / (d1[1] - d2[1])
                    if tmp1==tmp2 and 1 <= tmp1 <= cnt and 1 <= tmp2 <= cnt:
                        res += 1
        x1 = x1 + cnt*d1[0]
        y1 = y1 + cnt*d1[1]
        x2 = x2 + cnt*d2[0]
        y2 = y2 + cnt*d2[1]

    print(res)


if __name__ == '__main__':
    main()