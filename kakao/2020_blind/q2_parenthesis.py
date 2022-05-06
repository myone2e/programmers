p = "()))((()"

def idx_balance(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i

pairs = {')':'('}

def check_correct(s):
    stack = []
    for c in s:
        if c in pairs: # check wheter closing parenthesis (key)
            if stack and stack[-1] == pairs[c]: # not empty and top value can close out 
                stack.pop()
            else:
                return False
        else: # if open parenthesis, can add as many as we want
            stack.append(c)
    if stack: # if stack is not empty after the process
        return False
    else:
        return True

def solution(p):
    answer = ''
    if p == '':
        return answer
    idx = idx_balance(p)
    u = p[:idx + 1]
    v = p[idx+1:]
    
    # "올바른 괄호 문자열"이면, v에 대해 함수를 수행한 결과를 붙여 반환
    if check_correct(u) == True:
        answer = u + solution(v)
    # u가 올바른 괄호 문자열"이 아니라면 아래의 과정을 수행
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) # 처음과 마지막 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)
    return answer


    
            
        