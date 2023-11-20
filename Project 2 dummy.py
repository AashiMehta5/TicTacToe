import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    # Ask the user if they want to play against a friend or the computer
    opponent = input("Do you want to play against a friend or the computer? (friend/computer): ")

    while True:
        print_board(board)

        if opponent == 'friend':
            # Player makes a move
            row = int(input(f"Player {current_player}, enter the row (0, 1, 2): "))
            col = int(input(f"Player {current_player}, enter the column (0, 1, 2): "))
        elif opponent == 'computer':
            if current_player == 'X':
                # Human player makes a move
                row = int(input(f"Player {current_player}, enter the row (0, 1, 2): "))
                col = int(input(f"Player {current_player}, enter the column (0, 1, 2): "))
            else:
                # Computer makes a move
                row, col = random.choice([(i, j) for i in range(3) for j in range(3) if board[i][j] == ' '])
        else:
            print("Invalid choice. Please enter 'friend' or 'computer'.")
            break

        # Check if the chosen cell is empty
        if board[row][col] != ' ':
            print("Cell already taken. Try again.")
            continue

        # Update the board
        board[row][col] = current_player

        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_tic_tac_toe()
