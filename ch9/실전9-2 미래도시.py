#9-2 실전 미래도시
import sys
input = sys.stdin.readline

INF = int(1e9)
n,m = map(int,input().split())
graph = [[INF]*(n+1) for _ in range(n+1)] #무한으로 초기화한 2차원 리스트

#자기자신에서 자기자신으로 가는 비용 0 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0
#각 간선 정보입력받아 1로 초기화
for _ in range(m):
    #a에서 b로(b에서 a) 가는 비용은 1로 간주
    a,b = map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

#점화식에 따라 플로이드 워셜 알고리즘 수행
for t in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][t]+graph[t][b])


#목적지 x,k입력받기
x,k = map(int,input().split())
#k를 거쳐 x로 가는 최단거리 출력
if graph[1][k]+graph[k][x]>=INF:
    print(-1)
else:
    print(graph[1][k]+graph[k][x])