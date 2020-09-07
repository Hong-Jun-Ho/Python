import time
def solution(n,S,x):
    start_time = time.time()
    count =0
    location = 0
    while location<=n and S[location] != x:
        location +=1
        count+=1
    if location>n :
        count+=1

    end_time = time.time()
    print("time:", end_time - start_time)
    return location

print(solution(3,[1,4,5,6,1,1,4,5,6,1,1,4,5,6,1,1,4,5,6,1,1,4,5,6,1,1,4,5,6,1,1,4,5,6,1,1,4,5,6,1,2],2))