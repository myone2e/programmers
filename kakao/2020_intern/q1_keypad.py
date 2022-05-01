numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'

def position(num, left, right, hand): # left, right: 현재 각 손이 있는 키(숫자), hand는 자기 손
    
    keypad = {1:(0,0), 2:(0,1), 3:(0,2),
            4:(1,0), 5:(1,1), 6:(1,2),
            7:(2,0), 8:(2,1), 9:(2,2),
            '*':(3,0), 0:(3,1), '#':(3,2)}
    
    # 직선거리 = 맨하탄 거리
    dist_L = abs(keypad[num][0] - keypad[left][0]) + abs(keypad[num][1] - keypad[left][1])
    dist_R = abs(keypad[num][0] - keypad[right][0]) + abs(keypad[num][1] - keypad[right][1])
    
    if dist_L < dist_R:
        return 'L'
    elif dist_L > dist_R:
        return 'R'
    else:
        if dist_L == dist_R:
            if hand == 'right':
                return 'R'
            else:
                return 'L'

def solution(nums, hand):
    answer = ''
    left = '*'
    right = '#'
    for n in nums:
        if n in [1,4,7]:
            answer += 'L'
            left = n
        elif n in [3,6,9]:
            answer += 'R'
            right = n
        else:
            mid = position(n, left, right, hand)
            answer += mid
            if mid == 'L':
                left = n
            else:
                right = n
    return answer
