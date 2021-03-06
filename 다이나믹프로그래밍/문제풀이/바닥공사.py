"""
가로의 길이가 n, 세로의 길이가 2인 직사각형 형태의 얇은 바닥이 있다.
이 얇은 바닥을 1*2의 덮개, 2*1의 덮개, 2*2의 덮개를 이용해 채우고자 한다.

이 바닥을 채우는 모든 경우의 수를 구하는 프로그램을 구하시오.

--------------------------------------------------------------------------------------
최적의 해를 구하는게 아니라 모든 경우의 수를 구하는 것이다.
1. 작은 바닥의 종류를 순더대로 a,b,c라고 칭하자
2. a는 반드시 2개씩 설치해야 한다.
3. a 2개와 b 2개는 c와 동일하다.
4. n을 2로 나누고 나머지가 있으면 그 나머지를 b로 채운다.
5. n//2안에 a와 b가 두개씩 자유롭게 올 수 있다.

점화식은 어떻게 만들까
1. 왼쪽부터 차례로 채워나간다.
2. 왼쪽부터 i-1까지 채워져 있으면 선택은 b만 가능하다.
3. 왼쪽부터 i-2까지 채워져 있으면 a와 c만 가능하다.(b를 고려하지 않는 이유는 2번에서 이미 고려했기 때문이다.)
a_i=a_(i-1)+a_(i-2)*2[*2는 i-2에서는 a와 c 이렇게 두 가지가 가능하므로]
"""
n=int(input())

a=[0]*n
a[0]=1
a[1]=3

for i in range(2,n):
    a[i]=a[i-1]+a[i-2]*2
print(a)