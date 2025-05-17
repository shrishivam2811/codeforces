'''
codeforces: 151A. Soft Drinking
https://codeforces.com/problemset/problem/151/A

'''

def fun(n, k, l, c, d, p, nl, np):
    return min(k*l//nl,c*d//1,p//np)//n


n, k, l, c, d, p, nl, np = map(int,input().split())

print(fun(n, k, l, c, d, p, nl, np))