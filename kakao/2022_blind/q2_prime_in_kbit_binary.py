def check_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int((n**0.5))+1):
            if n % i == 0:
                return False
    return True

def binary_transform(num, base):
    lib = '0123456789ABCDEF'
    q, r = divmod(num, base)
    return binary_transform(q, base) + lib[r] if q else lib[r]


# 소수 양 옆의 0 은 무시 가능 & 101 등 0이 가운데 껴있으면 소수 아님
def solution(n, k):
    if k != 10:
        trans = str(binary_transform(n,k))
    else:
        trans = str(n)
    nums = list(trans.split('0'))
    while '' in nums: # split('0') 까지만하면 중간에 0이 여러개인 경우 ''가 들어감
        nums.remove('')
    answer = 0

    for num in nums:
        if check_prime(int(num)):
            answer += 1
    return answer
#n = 110011
#k = 10
#print(solution(n,k))