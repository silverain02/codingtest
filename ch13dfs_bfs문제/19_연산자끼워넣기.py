#19_연산자 끼워넣기
import copy
#입력받기
import sys
input = sys.stdin.readline
n = int(input())
nums=list(map(int,input().split()))
oper=list(map(int,input().split()))

result = [] #계산결과 저장용 리스트
temp = []
#dfs정의(재귀)
def dfs(index,oper):
    global temp
    global n
    #연산자 조합이 끝나면, 결과 리스트에 조합 추가 후 탈출
    if len(temp) == n-1:
        oper_combi.append(temp)
        temp = []
        return
    #현재 노드(연산자) 사용처리
    oper[index] -= 1
    temp.append(index)
    #현재 연산자외 다른 연산자 재귀적 방문
    for i in range(len(oper)):
        copied_oper = copy.deepcopy(oper)
        if oper[i] != 0: #사용 가능하면
            dfs(i,copied_oper)
            
oper_combi = []
copied_oper = copy.deepcopy(oper)
# 연산자 구성
dfs(0,copied_oper)
print(len(oper_combi))
    
