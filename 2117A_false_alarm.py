'''
Codeforces: 2117A. False Alarm
https://codeforces.com/problemset/problem/2117/A

'''

def fun(n,x,doors):
    f_ind = -1
    l_ind = -1
    for i in range(n):
        if doors[i] == 1:
            if f_ind ==-1:
                f_ind = i
            l_ind = i

    if l_ind - f_ind + 1 <=x:
        return 'Yes'
    else:
        return 'No'


t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    doors = list(map(int,input().split()))
    print(fun(n,x,doors))