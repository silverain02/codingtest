#ch11_1
import sys
input = sys.stdin.readline

#입력받기
n=int(input())
lst = list(map(int,input().split()))
#내림차순 정렬
lst.sort(reverse=True)

result=0
while True:
    elem = lst[0]
    del lst[:elem]
    result+=1
    if len(lst)==0:
        break
print(result)