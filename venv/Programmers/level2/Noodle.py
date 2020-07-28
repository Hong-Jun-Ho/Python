import heapq


def solution(stock, dates, supplies, k):
    cnt = 0
    start = 0
    h = []
    while stock < k:
        for i in range(start, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(h, -supplies[i])
                start = i + 1
            else:
                break
        stock += -heapq.heappop(h)
        cnt += 1
    return cnt

print(solution(4,[4,10,15],[20,5,10],30))