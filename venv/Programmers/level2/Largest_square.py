# def solution(board):
#     answer = 1234
#     max = 1
#
#     def search(row, col):
#         count = 0
#         ran = min(len(board) - row, len(board[0]) - col)
#         for n in range(ran):
#             if board[row + n][col + n] == 1:
#                 count += 1
#             else:
#                 return count
#         return count
#
#     def bfs(row, col, count):
#         for i in range(row, row + count):
#             for j in range(col, col + count):
#                 if board[i][j] != 1:
#                     return False
#         return True
#     count2 =0
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j] == 1:
#                 count2 +=1
#                 sjfqdl = search(i, j)
#                 if bfs(i, j, sjfqdl):
#                     if sjfqdl > max:
#                         max = sjfqdl
#
#     if count2 ==0: max = 0
#     answer = max * max
#     return answer
def solution(board):
    answer = 0
    row = len(board)
    col = len(board[0])
    for i in range(1,row):
        for j in range(1,col):
            if board[i][j] != 0:
                board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1
    max_list = []
    for i in range(row):
        max_list.append(max(board[i]))
    return max(max_list) ** 2

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
