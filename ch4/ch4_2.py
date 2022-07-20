#ch4_2
loc = input()
#입력받은 위치 행렬로 전환
x = ['a','b','c','d','e','f','g','h']
x1 = x.index(loc[:1]) +1
y1 = int(loc[1:])
cnt = 0
#선택 가능한 이동 경로
move = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
for m in move:
    x2 = x1 + m[0]
    y2 = y1 + m[1]
    if x2<1 or x2>8 or y2<1 or y2>8:
        continue
    else:
        cnt += 1
print(cnt)