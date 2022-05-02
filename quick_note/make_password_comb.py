from itertools import combinations
import sys
input = sys.stdin.readline

l, c = map(int, input().split())
cand = list(map(str, input().split()))
cand.sort()

min_conso = 2
min_vowel = 1

vowel = ['a','e','i','o','u']

for password in combinations(cand, l):
    cnt_vowel = 0
    cnt_conso = 0
    for i in password:
        if i in vowel:
            cnt_vowel += 1
        else:
            cnt_conso += 1
    if cnt_vowel >= 1 and cnt_conso >= 2:
        print(''.join(password))
    