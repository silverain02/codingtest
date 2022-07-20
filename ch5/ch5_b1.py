#ch5_b1 17086 아기상어2
N,M = map(int,input().split())
#2차원 리스트로 구성
cnt = 0
stack = []
lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))

#dfs정의
def dfs(x,y,d):
    global cnt
    global stack
    if (x<=-1 or x>=N or y<=-1 or y>=M):
        stack = []
        return
    if lst[x][y] == 0: #0 나오면 반복
        stack.append(d)
        if d == 0: #초기 > 전체 탐색
            stack.pop()
            #상좌하우 탐색 
            dfs(x-1,y,'u') 
            dfs(x,y-1,'l') 
            dfs(x+1,y,'d') 
            dfs(x,y+1,'r')
            #대각선 탐색
            dfs(x-1,y+1,'ur')
            dfs(x-1,y-1,'ul')
            dfs(x+1,y+1,'dr')
            dfs(x+1,y-1,'dl')
            return 
        #한방향으로 계속 탐색
        elif d == 'u':
            dfs(x-1,y,'u')
        elif d == 'l':
            dfs(x,y-1,'l')
        elif d == 'd':
            dfs(x+1,y,'d')
        elif d == 'r':
            dfs(x,y+1,'r')
        elif d == 'ur':
            dfs(x-1,y+1,'ur')
        elif d == 'ul':
            dfs(x-1,y-1,'ul')
        elif d == 'dr':
            dfs(x+1,y+1,'dr')
        elif d == 'dl':
            dfs(x+1,y-1,'dl')
    if lst[x][y] == 1:
        if d == 0:
            stack_indi.append(0)
            return
        else:
            stack_indi.append(len(stack)+1)
            stack = []
        return
    return
        
#리스트 순회
stack_result = []
for i in range(N):
    for j in range(M):
        stack_indi = []
        dfs(i,j,0)
        stack_result.append(min(stack_indi))
print(max(stack_result))

#예제2 ...