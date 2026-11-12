PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

def is_win(game): 
    for row in game:
        if ( row[0] == row[1] == row[2] and row[0] != EMPTY ): return True

    for col in range(3):
        if ( game[0][col] == game[1][col] == game[2][col] and game[0][col] != EMPTY ): return True

    if ( game[0][0] == game[1][1] == game[2][2] and game[0][0] != EMPTY ): return True 

    if ( game[0][2] == game[1][1] == game[2][0] and game[0][2] != EMPTY ): return True 

    return False

def print_board(game):
    print("\nCurrent board:")
    for row in game:
        print(" | ".join(row))
    print("-" * 9)

def main():
    game = [[EMPTY for _ in range(3)] for _ in range(3)]
    turn = False 
    
    print(f"{PLAYER_X} = Player 1")
    print(f"{PLAYER_O} = Player 2")
    
    for n in range(9):
        turn = not turn 
        
        player = "Player 1" if turn == False else "Player 2"
        mark = PLAYER_X if turn == False else PLAYER_O
        
        while True:
            print(f"\n{player} ({mark}), which cell to mark? i:[1..3], j:[1..3]: ", end="")
            try:
                i, j = map(int, input().split())
                i -= 1 
                j -= 1
                
                if not (0 <= i <= 2 and 0 <= j <= 2):
                    print("Invalid input. Please enter numbers between 1 and 3.")
                    continue
                
                if game[i][j] != EMPTY:
                    print("This cell is already taken! Please choose another.")
                    continue
                
                break
                
            except ValueError:
                print("Invalid format. Please enter two numbers separated by a space (e.g., '1 2').")

        game[i][j] = mark
        print_board(game)
        
        if is_win(game):
            print(f"\nWin! {player} ({mark}) wins the game.")
            return 
            
    print("\nTie!")

if __name__ == "__main__":
    main()
