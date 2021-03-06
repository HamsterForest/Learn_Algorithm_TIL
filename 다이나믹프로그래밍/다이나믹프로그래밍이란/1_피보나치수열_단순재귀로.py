"""
단순하게 재귀적으로 피보나치 수열을 해결하면 치명적인 문제가 있으니, x가 늘어날수록
수행시간이 기하급수적으로 늘어난다는 것이다. 빅오 표기로 O(2^n)이며,
x=30인경우 10억가량의 연산을 수행하여야한다.
이러한 이유중 가장 큰 부분을 차지하는 것은 동일한 연산을 반복하는 것이다.
예컨데 x=6이 들어간다면, fibo(3)연산을 3번해야한다.

이 함수에서 x=100만 2^10의 연산을 해야 하며 컴퓨터가 1초에 1억번정도의 연산을 한다고 가정 할 때
수백억년을 연산하고 있어야한다.

반복되는 연산을 줄이기위한 방법이 다이나믹 프로그랭밍이다.
"""

def fibo(x):
    if x==1 or x==2:
        return 1
    return fibo(x-1)+fibo(x-2)

print(fibo(100))