#실전10-4커리큘럼(답안예시참고)
import copy
from collections import deque
#노드의 개수 입력받기
v=int(input())
#모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0]*(v+1)
#각 노드에 연결된 간선 정보를 담기위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v+1)]
#각 강의시간 0 초기화
time=[0]*(v+1)

#방향 그래프의 모든 간선 정보를 입력받기
for a in range(1,v+1):
    lst = list(map(int,input().split()))
    time[a]=lst[0]
    b_lst = lst[1:-1]
    for b in b_lst:
        indegree[a]+=1
        graph[b].append(a)#정점 A에서 B로 이동가능


#위상정렬 함수
def topology_sort():
    result=copy.deepcopy(time)#알고리즘 수행 결과를 담을 리스트
    q=deque() #큐 기능을 위한 deque라이브러리 사용
    
    #처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
    
    #큐가 빌 때까지 반복
    while q:
        #큐에서 원소 꺼내기
        now=q.popleft()
        #해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]:
            result[i]=max(result[i],result[now]+time[i])
            indegree[i]-=1
            #새로 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] ==0:
                q.append(i)
    
    #위상정렬을 수행한 결과 출력
    for i in range(1,v+1):
        print(result[i])
        
topology_sort()
