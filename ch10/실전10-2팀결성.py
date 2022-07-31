#실전10-2팀결성
#입력받기
import sys
input = sys.stdin.readline
n,m=map(int,input().split())

#특정원소가 속한 집합을 찾기
def find_parent(parent,x):
    #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return parent[x]
#두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        
parent = [0]*(n+1) #부모 테이블 초기화
#부모 테이블 상에서, 부모를 자기자신으로 초기화
for i in range(1,n+1):
    parent[i]=i

for i in range(m):
    t,a,b=map(int,input().split())
    if t: #같은 팀 여부 확인 연산
        if find_parent(parent,b)==find_parent(parent,a):
            print('YES')
        else:
            print('NO')
        
    else: #팀 합치기 연산
        union_parent(parent,a,b)
    
    