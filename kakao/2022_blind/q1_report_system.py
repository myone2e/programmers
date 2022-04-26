id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2 # 정지 제한선

# 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
def solution(id_list, report, k):
    report_dict = {} # 신고한 사람을 담자 / 유저 : 신고자들
    for id in id_list:
        report_dict[id] = set()

    for r in report:
        report_dict[r.split()[-1]].add(r.split()[0])

    mail_dict = {} # 신고한 사람을 담자 / 유저 : 신고자들
    for id in id_list:
        mail_dict[id] = 0

    for val in report_dict.values(): # 메일을 발송한 쇳수
        if len(val) >= k: # 정지가 된다면
            for v in val:
                mail_dict[v] += 1
    answer = [n for n in mail_dict.values()]
    return answer