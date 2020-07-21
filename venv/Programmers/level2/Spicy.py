# def solution(scoville, K):
#     answer = 0
#     scoville.sort(reverse=True)
#     while True:
#         if scoville[-1] < K:
#             mix1 = scoville.pop()
#             mix2 = scoville.pop() * 2
#             scoville.append(mix1+mix2)
#             scoville.sort(reverse=True)
#             answer+=1
#         else:
#             break
#     if scoville[0]<K:
#         return -1
#     return answer
#
# print(solution([1, 2, 3, 9, 10, 12], 7))

#---------------------- 아래는 힙으로 위에는 시간초과 ============

def solution(scoville,K):
    import heapq
    heap =[]
    answer =0
    for i in scoville:
        heapq.heappush(heap, i)
    while heap:
        if heap[0]>=K:
            return answer
        mix1 = heapq.heappop(heap)
        if heap:
            mix2 = heapq.heappop(heap)*2
            heapq.heappush(heap,mix1+mix2)
        answer+=1
    return -1
print(solution([1, 2, 3, 9, 10, 12], 7))
