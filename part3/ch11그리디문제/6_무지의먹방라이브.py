def solution(food_times, k):
    answer = 0
    
    for i in range(k+1): #k+1회 반복
        j = i%3
        while food_times[j] == 0:
            j+=1
            if j > 2:
                j %= 3
        food_times[j] -= 1
        
        if i == k: #네트워크 중단 후 첫 회차
            answer = j+1
        
    return answer

print(solution([3,1,2],5))

#1,2 통과 / 3~ 시간초과