def solution(board, moves):
    #include <string>
    result = [0]
    count =0
    for i in range(len(moves)):
        for e in range(len(board[0])):
            if board[e][moves[i]-1] != 0:
                print("뽑은 인형 : %d"%board[e][moves[i]-1])
                print("마지막에 쌓여있는 인형 %d" % result[-1])
                if board[e][moves[i]-1] == result[-1]:
                    count = count + 2
                    del result[-1]
                    board[e][moves[i] - 1] = 0
                    break
                    print("count: %d "%count)
                result.append(board[e][moves[i] - 1])
                board[e][moves[i]-1] = 0
                break
    del result[0]

    for e in range(len(board[0])):
        for i in range(len(board[0])):
            print(board[e][i],end='')
        print()

    print(result)


    return count

 
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))

