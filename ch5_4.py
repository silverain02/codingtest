#ch5_4 미로탈출 4:00~
N,M = map(int,input().split())
#2차원 리스트로 구성
lst = []
for i in range(N):
    lst.append(list(map(int, input())))

#dfs 메소드 정의
def dfs(i,j):
    global cnt
    #현 노드 방문표시(0) 후 스택 삽입 > cnt+1
    if lst[i][j] ==  1:
        lst[i][j] = 0
        cnt += 1
    #우,하 방향 탐색 > 재귀함수 처리 (인접노드)
    if j<M-1 and lst[i][j+1]==1:
        dfs(i,j+1)
    elif i<N-1 and lst[i+1][j]==1:
        dfs(i+1,j)
    #하,우 둘다 불가능 > 함수탈출
    else:
        return 
cnt = 0
dfs(0,0)
print(cnt)
