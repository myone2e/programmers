import sys
input = sys.stdin.readline
s = input()

pairs = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4,
         'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

answer = ''
tmp = ''

for i in s:
    if i.isdigit():
        answer += i
    elif i.isalpha():
        tmp += i
        if tmp in pairs.keys():
            answer += str(pairs[tmp])
            tmp = ''
print(answer)

# best solution => need to change values to str
def solution(s):
    answer = s
    for key, value in pairs.items(): # (key1, value1), ...,
        answer = answer.replace(key, value) # if key -> replace it to value
    return int(answer)