def solution(heights):
    answer = []
    for p_index in range(len(heights)-1, -1, -1):
        Check = False
        for c_index in range(p_index-1, -1, -1):
            if heights[p_index] < heights[c_index]:
                Check = True
                answer = [c_index + 1] + answer
                break
        if not Check:
            answer = [0] + answer
    return answer

print(solution([6, 9, 5, 7, 4]))
