#ch6_b1 2470
N = int(input())
lst = list(map(int,input().split()))
#리스트 순회하며 모든 합의 경우 저장
lst2 = []
lst_sum = []
for i in range(N):
    for j in range(i+1,N): #해당 원소 이후
        lst2.append((lst[i],lst[j]))
        lst_sum.append(abs(lst[i]+lst[j]))
m = min(lst_sum)
m_index = lst_sum.index(m)

print(f'{lst2[m_index][0]} {lst2[m_index][1]}')