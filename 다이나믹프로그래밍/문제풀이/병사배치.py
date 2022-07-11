"""
백준 18353
n명의 병사가 무작위로 나열되어 있다. 각 병사는 특정한 값의 전투력을 보유하고 있으며, 
병사를 배치할 때는 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치하고자 합니다.
또한 배치과정에서는 특정한 병사를 열외시키는 방법을 이용합니다.
그러면서도 남아 있는 방사의 수가 최대가 되도록 하고 싶습니다.

해설 
이 문제의 기본 아이디어는 '가장 긴 증가하는 부분 수열'(LIS)문제이다.
하나의 수열이 주어졌을 때 값들이 증가하는 형태의 가장 긴 부분 수열을 찾는 문제이다.

예를들어 array={10,20,10,30,20,50}이 있다고 하자.
이때 가장 긴 증가하는 부분수열은 {10,20,30,50}이 될 것이다. 
d[i]=array[i]를 마지막 원소로 가지는 부분수열의 최대길이로 정의
점화식은 다음과 같다.
모든 dp테이블이 값은 모두 1로 초기화한다.
모든 0<=j<i에 대하여, d[i]=max(D[i],d[j]+1) if array[j]<array[i]
"""
import sys
n=int(input())
array=[]
array.extend(list(map(int,sys.stdin.readline().split())))

#LIS문제로 만들기 위해
array.reverse()
#dp테이블 초기화
dp=[1]*n #dp에 저장되는 값은, array[i]를 마지막 원소로 가지는 부분 수열의 최대길이

#LIS알고리즘
for i in range(1,n):#n은 배열의 길이 1~n-1
    for j in range(0,i):
        if array[j]<array[i]:#앞에 있는 것이 뒤에 있는것보다 큰경우(오름차순이 아닌경우-오름차순이여야함)
            dp[i]=max(dp[i],dp[j]+1)

#열외시켜야 하는 병사의 최소수 출력
print(n-max(dp))


