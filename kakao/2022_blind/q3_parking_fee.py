fees = [180, 5000, 10, 600] # 180분 5000원이 기본, 이후 10분 당 600원
# 나간 기록 없으면 '23:59' 출차 간주 # 같은 애가 하루 두 번 이상 올 수 있음 ㅅㅂ
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
           "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

import math

def calculate_fee(total_time, fees): # total_time minute으로 넣어라
    fee = fees[1] # 기본 요금 징수
    if total_time > fees[0]:
        fee += int(math.ceil((total_time - fees[0])/fees[2])) * fees[3]
    return fee
    
# 차량 번호가 작은 순서대로 요금 출력
def solution(fees, records):
    dict_1 = {}
    for r in records:
        dict_1[r.split()[1]] = []

    for r in records:
        time, car, io = r.split()
        dict_1[car].append(io)
        dict_1[car].append(time)

    # (key, value) 로 담긴 리스트를 다시 dict로 변환해야 함
    sdict = dict(sorted(dict_1.items())) # key 기준으로 정렬. keys만 하면 리스트에 키만 담김. reverse = True 하면 desc
    answer = []

    for r in sdict.values():
        total_min = 0
        if r.count('IN') == r.count('OUT'): # 그래도 자정 전에 잘 나간경우
            ptr = 0
            while ptr < len(r):
                i, o = r[ptr+1].split(':'), r[ptr+3].split(':')
                ih, im, oh, om = int(i[0]), int(i[1]), int(o[0]), int(o[1]) # int('01') = 1로 인식함
                if om < im: # 12시 50분 들어와서 1시 5분..
                    hour = oh - ih - 1
                    minute = om + 60 - im
                    total_min += hour*60 + minute
                else:
                    hour = oh - ih
                    minute = om - im
                    total_min += hour*60 + minute
                ptr += 4
        else: # 자정 전에 안나간 경우
            ptr = 0
            while ptr < len(r):
                if ptr+2 < len(r): # in & out 있는 애들
                    i, o = r[ptr+1].split(':'), r[ptr+3].split(':')
                    ih, im, oh, om = int(i[0]), int(i[1]), int(o[0]), int(o[1]) # int('01') = 1로 인식함
                    if om < im: # 12시 50분 들어와서 1시 5분..
                        hour = oh - ih - 1
                        minute = om + 60 - im
                        total_min += hour*60 + minute
                    else:
                        hour = oh - ih
                        minute = om - im
                        total_min += hour*60 + minute
                    ptr += 4
                else: # out only
                    i = r[ptr+1].split(':')
                    ih, im, oh, om = int(i[0]), int(i[1]), 23, 59 # int('01') = 1로 인식함
                    hour = oh - ih
                    minute = om - im
                    total_min += hour*60 + minute
                    ptr += 4
        
        fee = calculate_fee(total_min, fees)
        answer.append(fee)
    return answer

print(solution(fees, records))
