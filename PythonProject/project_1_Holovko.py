import random


def display_board(board):
    print("+-------" * 3 + "+")
    for row in board:
        print("|       " * 3 + "|")
        for cell in row:
            print(f"|   {cell}   ", end="")
        print("|")
        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")


def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                raise ValueError("Invalid move. Enter a number between 1 and 9.")

            for row in range(3):
                for col in range(3):
                    if board[row][col] == str(move):
                        board[row][col] = 'O'
                        return
            print("Square already taken. Try again.")
        except ValueError as e:
            print(e)


def make_list_of_free_fields(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] not in ['X', 'O']]


def victory_for(board, sign):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)) or all(board[j][i] == sign for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False


def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = random.choice(free_fields)
        board[row][col] = 'X'


def main():
    board = [[str(3 * i + j + 1) for j in range(3)] for i in range(3)]
    board[1][1] = 'X'  # Computer starts with 'X' in the center
    display_board(board)

    while True:
        enter_move(board)
        display_board(board)
        if victory_for(board, 'O'):
            print("Congratulations! You win!")
            break
        if not make_list_of_free_fields(board):
            print("It's a draw!")
            break

        print("Computer's turn...")
        draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print("Computer wins! Better luck next time.")
            break
        if not make_list_of_free_fields(board):
            print("It's a draw!")
            break


if __name__ == "__main__":
    main()
