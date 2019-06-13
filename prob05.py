# 문제5.
# 함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.


def mysum(*num):
    sum_all = 0
    for number in num:
        sum_all += number
    return sum_all


print(mysum())
print(mysum(1))
print(mysum(1, 2))
print(mysum(1, 2, 3))
print(mysum(1, 2, 3, 4))