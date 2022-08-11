#19_연산자 끼워넣기/2회차
import copy
import sys
input = sys.stdin.readline

#입력받기
n = int(input())
nums=list(map(int,input().split()))
oper=list(map(int,input().split()))

#초기화
oper_cmb = []
temp = []

#dfs(재귀) 함수 정의
def dfs(i,c_oper,temp):
    global oper_cmb
    #가능한 연산자가 하나만 남은 경우
    if sum(c_oper) == 1:
        oper_cmb.append(temp+[c_oper.index(1)])
        return
    #현 노드(연산자) 사용 처리
    c_oper[i] -= 1
    temp.append(i)
    #현재 사용가능한 노드(연산자) 재귀적 방문
    for j in range(len(c_oper)):
        if c_oper[j] != 0:
            c_oper = copy.deepcopy(c_oper)
            temp = copy.deepcopy(temp)
            dfs(j,c_oper,temp)
#연산자 조합 구성
for i in range(n-1):
    if oper[i] != 0:
        c_oper = copy.deepcopy(oper)
        dfs(i,c_oper,temp)
