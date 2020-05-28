def printer(priorities, location):
    answer = 0

    print_list = [(pro, i) for i, pro in enumerate(priorities)]
    print_list_max = max(print_list)[0]

    while True:
        if print_list[0][0] == print_list_max:
            temp = print_list.pop(0)

            answer += 1

            if temp[1] == location:
                break
            print_list_max = max(print_list)[0]
        else:
            temp = print_list.pop(0)
            print_list.append(temp)

    return answer


print(printer([8, 7, 9, 0, 9, 9], 3))
