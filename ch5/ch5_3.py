#ch5_3<음료수 얼려 먹기> 2H

#dfs 메서드 정의
def dfs(i,j):
    #현재 노드 방문 처리
    if lst[i][j] == 0:
        lst[i][j] = 1
        stack.append([i,j])
    #1. 상하좌우 가능할 때 재귀함수 처리(인접노드)
    if i>0 and lst[i-1][j]==0:
        dfs(i-1,j)
    elif i<N-1 and lst[i+1][j]==0:
        dfs(i+1,j)
    elif j>0 and lst[i][j-1]==0:
        dfs(i,j-1)
    elif j<M-1 and lst[i][j+1]==0:
        dfs(i,j+1)
    else:
        #2. 인접노드 모두 처리한 경우 스택 삭제 
        stack.pop()
        # 다시 최상위 스택 탐색
        if len(stack)>0:
            dfs(stack[-1][0],stack[-1][1])
        #3. 전체 탐색완료
        else:
            return 0
        
N,M = map(int,input().split())
#2차원 리스트로 구성
lst = []
for i in range(N):
    lst.append(list(map(int, input())))

#1. 리스트(그래프)순회 하며 방문 안 한 노드(0)찾기
cnt = 0
for i in range(N):
    for j in range(M):
        if lst[i][j] == 0:
            #스택 처리용 lst
            stack = []
            #dfs 돌려서 방문처리
            dfs(i,j)
            cnt += 1

print(cnt)
            