def minSwapsToChessboard(board):
    n = len(board)   
    row_sum = sum(board[0])
    col_sum = sum(board[i][0] for i in range(n))    
    row_diff = abs(row_sum * 2 - n)
    col_diff = abs(col_sum * 2 - n)   
    if row_diff > 1 or col_diff > 1:
        return -1    
    row_black = 0
    for i in range(n):
        if board[0][i] != i % 2:
            row_black += 1    
    col_black = 0
    for i in range(n):
        if board[i][0] != i % 2:
            col_black += 1  
    if n % 2 == 0:
        return min(row_black, n - row_black) // 2 + min(col_black, n - col_black) // 2
    else:
        return (row_black + n - row_black) // 2 // 2 + (col_black + n - col_black) // 2 // 2

N = int(input("Enter the size N: "))
board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

result = minSwapsToChessboard(board)
print("Minimum number of swaps:", result)
