#ch11_2
import sys
input = sys.stdin.readline().rstrip
#입력받기
lst = list(map(int,input()))

#리스트 순회> 0,1이면 더하고 그 외는 곱하기
result=lst[0]
for i in range(1,len(lst)):
    if lst[i-1]==0 or lst[i-1]==1:
        result += lst[i]
    else:
        result *= lst[i]
        
print(result)
        