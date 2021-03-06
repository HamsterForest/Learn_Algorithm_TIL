"""
dfs란 깊이 우선 탐색
그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘

그래프는 노드와 간선으로 이루어짐

그래프의 두가지 표현방식-> 인접행렬, 인접리스트

인접리스트가 인접 행렬방식에 비하여 메모리를 효율적으로 사용 다만 
인접 행렬방식에 비해 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도 느림

노드 : 0, 1, 2
1. 0과1 노드는 7간선으로 연결됨.
2. 0과 2노드는 5간선으로 연결됨.
3. 1과 2사이에는 아무런 연결이 없음.
"""

#행이 3개인 2차원 리스트로 인접 리스트 표현
graph=[[] for _ in range(3)]
print(graph)
#노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))#1은 노드 7은 간선
graph[0].append((2,5))

#노드1에 연결된 노드 정보 저장
graph[1].append((0,7))

#노드2에 연결된 노드 정보 저장
graph[2].append((0,5))

print(graph)