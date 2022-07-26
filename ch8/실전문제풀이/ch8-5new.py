#ch8-5효율적화폐구성
#입력받기
n,m = map(int,input().split())
coin = []
for i in range(n):
    coin.append(int(input()))
#최소계산횟수기록용 dp테이블
d = [0]*100
#보텀업 다이나믹
for i in range(max(coin)+1):
    #입력받은 coin은 자기자신을 사용해 최소계산횟수 1
    if i in coin:
        d[i]=1
    #입력받은coin으로 계산 불가능한 값
    elif i != 0:
        d[i]=-1
for i in range(max(coin)+1,m+1):
    stack=[]
    for j in coin:
        if d[i-j] != -1:
            stack.append(d[i-j]+1) #계산불가능값만 아니면 coin만큼 뺀 값의 계산횟수 추가
    d[i]=min(stack)#각 coin뺀 값의 계산횟수의 최솟값
print(d[m])
    