'''
codeforces: 514A. Chewback and Number
https://codeforces.com/problemset/problem/514/A

'''

def fun(num):
    res = 0
    for d in num:
        if res == 0 and d == '9':
            res +=9
        elif int(d) > 9-int(d):
            res = res*10 + (9-int(d))
        else:
            res = res*10 + int(d)
    return res

num = input()
print(fun(num))