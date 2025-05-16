'''
codeforces: 282A. Bit++
https://codeforces.com/problemset/problem/282/A

'''

def fun(n,ope):
    x = 0
    for i in range(n):
        if ope[i] == 'X++' or ope[i] == '++X':
            x += 1
        elif ope[i] == 'X--' or ope[i] == '--X':
            x -= 1
    return x

n = int(input())
ope = []
for i in range(n):
    ope.append(input())

print(fun(n,ope))