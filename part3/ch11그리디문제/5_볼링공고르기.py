#ch11_5 볼링공 고르기
import sys
input = sys.stdin.readline
#입력받기
n,m=map(int,input().split())
lst = list(map(int,input().split()))

result=0
for i in range(len(lst)): #리스트 순회
    #해당 원소 오른쪽 부분에서 해당원소 개수를 뺀 것 
    result += (len(lst)-(i+1)) - lst[i+1:len(lst)].count(lst[i])
print(result)