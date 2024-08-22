def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([spot == player for spot in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2-i] == player for i in range(3)]):
        return True

    return False

def check_draw(board):
    return all([spot != " " for row in board for spot in row])

def play_game():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

    while not game_over:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        # Get player input
        move = input("Enter your move (1-9): ")

        if move not in [str(i) for i in range(1, 10)]:
            print("Invalid move. Please enter a number between 1 and 9.")
            continue

        move = int(move) - 1
        row, col = divmod(move, 3)

        if board[row][col] != " ":
            print("That spot is already taken. Choose another.")
            continue

        board[row][col] = current_player

        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"

    # Ask if players want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_game()
    else:
        print("Thanks for playing!")

# Start the game
play_game()
