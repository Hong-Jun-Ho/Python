def solution(bridge_length, weight, truck_weights):
    answer = 0
    temp = []
    bridge_weight = 0
    i = 0
    while i < len(truck_weights):
        answer += 1
        if bridge_weight + truck_weights[i] > weight:
            temp.append(0)
        else:
            temp.append(truck_weights[i])
            bridge_weight += truck_weights[i]
            i += 1

        if len(temp) >= bridge_length:
            bridge_weight -= temp[0]
            temp.pop(0)

    return answer + bridge_length


print(solution(2, 10, [7, 4, 5, 6]))
