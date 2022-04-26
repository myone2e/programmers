n = 8
k = 2 # 시작점 idx
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"] #["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]

import heapq # 힙 자료구조를 사용함
# heapq 모듈을 사용하면 heapq.pop과 heapq.push 들의 시간복잡도가 O(logN) 이기 때문

def solution(n, k, cmd):
    # left에는 현재 행 -1 ~ 0 값들이 내림차순으로 정렬된 최대 힙 자료구조
    # right에는 현재 행 ~ 마지막 행 값들이 오름차순으로 정렬된 최소 힙 자료구조
    left, right, delete = [], [], [] 
    
    for i in range(n):
        heapq.heappush(right, i) # right을 0, 1, 2, 3, 4, .... n-1 로 만듦
    for i in range(k):
        heapq.heappush(left, -heapq.heappop(right)) # right에서 0부터 뽑아서 음수 붙여서 저장 0, -1, -2, ....
        # right에서 작은 애들은 사라짐
    
    for c in cmd:
        if len(c) > 1:
            step = int(c[2:])
            direction = c[0]
            
            if direction == 'D': # 아래로 내려가는 경우 => right을 줄여야함
                for _ in range(step):
                    if right:
                        heapq.heappush(left, -heapq.heappop(right)) # right에서 작은 순서대로 뽑아서 음수 붙여서 left로 이동
            elif direction == 'U':
                for _ in range(step):
                    if left:
                        heapq.heappush(right, -heapq.heappop(left))
        
        elif c == 'C':
            # 값을 삭제하되, 가장 최근에 삭제된 값을 복구하기 쉽도록 stack 형태를 사용한다
            delete.append(heapq.heappop(right))
            
            if not right: # 삭제된 행이 마지막이였을 경우 위에서 하나 끌어옴
                heapq.heappush(right, -heapq.heappop(left))
        elif c == 'Z':
            tmp = delete.pop() # LIFO
            
            if tmp < right[0]:
                heapq.heappush(left, -tmp)
            else:
                heapq.heappush(right, tmp)
    result = []
    while left:
        result.append(-heapq.heappop(left))
    while right:
        result.append(heapq.heappop(right))
    result = set(result)
    
    answer = ''
    for i in range(n):
        if i in result:
            answer += 'O'
        else:
            answer += 'X'
    return answer
print(solution(n, k, cmd))