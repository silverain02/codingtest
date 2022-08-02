def solution(food_times, k):
    answer = 0
    
    i=0
    while i < k+1: #k+1회 반복
        j = i%3
        
        if food_times.count(0) == len(food_times): #원소가 다 0
            answer = -1
        
        if food_times[j] == 0:
            i += 1
            k += 1
            continue
                
        food_times[j] -= 1
        
        if i == k: #네트워크 중단 후 첫 회차
                answer = j+1        
        
        i += 1
        
    return answer

print(solution([3,1,2],5))

