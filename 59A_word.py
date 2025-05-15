'''
codeforce : 59A. Word
https://codeforces.com/problemset/problem/59/A

'''

def fun(word):
    upper = 0
    lower = 0

    for char in word:
        if char.isupper():
            upper += 1
        else:
            lower += 1

    if upper > lower:
        return word.upper()
    else:
        return word.lower()
    

word = input()
print(fun(word))
