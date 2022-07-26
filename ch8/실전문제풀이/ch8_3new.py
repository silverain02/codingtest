#ch8_3 개미전사
import sys
n = int(sys.stdin.readline())
lst = [int(x) for x in sys.stdin.readline().split()]
#dp테이블 초기화
d = [0]*n
d[n-1] = lst[n-1]
d[n-2] = lst[n-2]
#보텀업다이나믹
for i in range(n-3,-1,-1):#역순회
    stack = []
    for j in range(2,n-i):
        stack.append(d[i+j])
    d[i]=lst[i]+max(stack)
d.pop()
d.pop()#끝 두 원소 제거

print(max(d))

    
