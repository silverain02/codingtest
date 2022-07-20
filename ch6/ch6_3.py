#ch6_3 성적이 낮은 순서로 학생 출력하기 5:23~43
N = int(input())
x = {}
for i in range(N):
    name, score = map(str,input().split())
    x[name] = int(score)
#value기준 내림차순 정렬
sorted_x = sorted(x.items(), key = lambda x:x[1])

for elem in sorted_x:
    print(elem[0], end = ' ')