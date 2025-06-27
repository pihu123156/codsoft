board = [" " for _ in range(9)]
def print_board(board):
    for i in range(3):
        print(board[3*i] + "|" + board[3*i+1] + "|" + board[3*i+2])
        if i != 2:
            print("-----")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == player and board[condition[1]] == player and board[condition[2]] == player:
            return True
    return False

def is_draw(board):
    return " " not in board

def human_move(board):
    move = int(input("Enter your move (0-8): "))
    while board[move] != " ":
        move = int(input("Invalid move! Try again (0-8): "))
    board[move] = "O"

def minimax(board, is_maximizing):
    if check_winner(board, "X"):
        return 1
    if check_winner(board, "O"):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def computer_move(board):
    best_score = -float("inf")
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "X"

def play_game():
    board = [" " for _ in range(9)]
    print_board(board)

    while True:
        human_move(board)
        print_board(board)
        if check_winner(board, "O"):
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        computer_move(board)
        print_board(board)
        if check_winner(board, "X"):
            print("Computer wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

play_game()