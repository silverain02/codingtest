#6_무지의 먹방 라이브 3회차 시도 28.1/100
def solution(food_times, k):
    answer = 0
    
    if sum(food_times)<=k:
        return -1
    
    import copy
    cnt=0
    
    #첫cnt업데이트
    stack=copy.deepcopy(food_times)
    stack = [i for i in stack if i != 0]
    cnt += len(stack)
    
    #k가 위치한 블록 파악
    while k > cnt:
        
        #리스트 업데이트
        for i in range(len(food_times)):
            if food_times[i] != 0:
                food_times[i] -= 1
        
        #cnt업데이트
        stack=copy.deepcopy(food_times)
        stack = [i for i in stack if i != 0]
        cnt += len(stack)
        
        
    #블록 내 k의 위치 파악
    if k == cnt:
        answer =1
    else:
        answer = food_times.index(stack[k-cnt])+1        
             
    return answer

print(solution([3,1,2],6))