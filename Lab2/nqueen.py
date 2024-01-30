import time

def display(board):
    for row in board:
        print(row)

def isSafe(board, x, y, n):
    # column test : check if the column is already filled or not

    for row in range(x):
        if board[row][y] == 'Q':
            return False
        
    # Top left diagonal test : check if the top left diagonal cells are already filled or not
        r = x - 1
        c = y - 1

        while (r>=0 and c>=0):
            if board[r][c] == 'Q':
                return False
            
            r = r - 1
            c = c - 1

    # Top right Diagonal test :
        
        r = x - 1
        c = y + 1
        while(r>=0 and c<n):
            if board[r][c] == 'Q':
                return False
            
            r = r - 1
            c = c + 1
        
    return True

def nQueensSolver(board, x , n):
    if (x>=n):
        return True
    
    for col in range(n):
        if(isSafe(board, x , col, n)):
            board[x][col] = 'Q'
            if (nQueensSolver(board, x + 1, n)):
                return True
            board[x][col] = ' '
    return False


if __name__ == "__main__":
    n = int(input("Enter no. of queens: "))

    board = [[' ']*n for i in range(n)]

    time1 = time.time()
    solutionFound = nQueensSolver(board, 0 , n)
    time2 = time.time()

    timeTaken = time2 - time1

    if(solutionFound):
        display(board)
        print("Time taken is: ", timeTaken)
    else:
        print("No solution")
   