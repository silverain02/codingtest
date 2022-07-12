#ch3_3
N,M = map(int,input().split())#행,열 개수
card = []
#각 행 리스트로 저장
for i in range(N):
    L = list(map(int,input().split()))
    card.append(L)
#각 행의 리스트 최소값 저장
minL = []
for L in card:
    minL.append(min(L))
#최소값 중의 최대값 출력
print(max(minL))

