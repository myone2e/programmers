words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

from bisect import bisect_left, bisect_right

# fro?? => froaa ~ frozz 에 속하는 애들 카운팅
def count_range(word, left_val, right_val):
    right_idx = bisect_right(word, right_val)
    left_idx = bisect_left(word, left_val)
    return right_idx - left_idx

# 모든 단어들을 길이마다 나누어서 저장하기 위한 리스트
array = [[] for _ in range(10001)]
# 모든 단어들을 길이마다 나누어서 뒤집어 저장하기 위한 리스트 # ?가 앞에 나오는 경우를 위해서
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    # 길이에 따라 분류
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])
    
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for q in queries:
        if q[0] != '?': # 물음표로 시작 안하면
            res = count_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z')) # a로 바꾼거랑 z로 바꾼거 안에 다 들어감
        else: # 물음표로 시작한다면
            res = count_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z')) # 쿼리도 뒤집어야함
    
        answer.append(res)
    return answer
