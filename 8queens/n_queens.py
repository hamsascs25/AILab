
import random

N = 8

# Calculate the number of attacking queen pairs
def calculate_heuristic(board):
    attacks = 0

    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j]:
                attacks += 1
            elif abs(board[i] - board[j]) == abs(i - j):
                attacks += 1

    return attacks


# Print chessboard
def print_board(board):
    for row in range(N):
        for col in range(N):
            if board[col] == row:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()


# Hill Climbing Algorithm
def hill_climbing():
    board = [random.randint(0, 7) for _ in range(N)]

    while True:
        current_h = calculate_heuristic(board)

        if current_h == 0:
            print("\nSolution Found!")
            print_board(board)
            print("Heuristic Value:", current_h)
            return

        best_board = board[:]
        best_h = current_h

        for col in range(N):
            for row in range(N):
                if board[col] != row:
                    new_board = board[:]
                    new_board[col] = row

                    h = calculate_heuristic(new_board)

                    if h < best_h:
                        best_h = h
                        best_board = new_board

        if best_h >= current_h:
            print("\nLocal Minimum Reached. Restarting...")
            board = [random.randint(0, 7) for _ in range(N)]
        else:
            board = best_board


# Main Program
hill_climbing()
