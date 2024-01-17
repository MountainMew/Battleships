from Game import game
import os
from Domain import Error
### Battleship
#The game is described [here](https://en.wikipedia.org/wiki/Battleship_(game))

#The game is played on a grid of 10x10 squares. Each player has 5 ships of different sizes:
#* Carrier (5)
#* Battleship (4)
#* Cruiser (3)
#* Destroyer (2)
#* Submarine (2)


class UI :
    def __init__(self) :
        self.game = game()
        

    def start_game(self) :
        GameOver = False
        x = 0
        self.print_board_player()
        self.place_ships()
        
        self.game.AI_place_ships()
        self.print_board_AI()

        while not GameOver :
            #os.system('cls' if os.name == 'nt' else 'clear')
            self.print_board_AI()
            self.print_board_player()
            self.Player_Turn()
            GameOver = self.game.check_GameOver(1)
            if GameOver :
                print("You won!")
                break
            self.AI_Turn()
            GameOver = self.game.check_GameOver(2)
            if GameOver :
                print("AI won!")
                break

    
    def place_ships(self) :
        start = [0,0]
        end = [0,0]
        ships = self.game.get_player_ships()
        for ship in ships :
            placed = False
            while not placed :
                print(f"Place your {ship.name}")
                orientation = input("Orientation (h/v): ")
                while orientation != 'h' and orientation != 'v' :
                    print("Invalid orientation")
                    orientation = input("Orientation (h/v): ")
                while True :
                    try :
                        print(f"Start:")
                        start[0] = int(input("X: "))
                        start[1] = int(input("Y: "))
                    except ValueError :
                        print("Invalid input")
                    else :
                        break
                    
                while True :
                    try :
                        print(f"End:")
                        end[0] = int(input("X: "))
                        end[1] = int(input("Y: "))
                    except ValueError :
                        print("Invalid input")
                    else :
                        break
                if end[1] < start[1] :
                    start[1],end[1] = end[1],start[1]
                if end[0] < start[0] :
                    start[0],end[0] = end[0],start[0]
                placed = self.game.valid_placement(start,end,ship.len,orientation,1)
                if placed == False :
                    print("Invalid placement")
            self.game.place_ship(ship,start,end,ship.len,orientation,1)
            self.print_board_player()
        
        

    def Player_Turn(self) :
        
        print("Your turn")
        sunk = 0
        while True :
            try :
                x = int(input("X: "))
                y = int(input("Y: "))
            except ValueError :
                print("Invalid input")
                continue
            try :
                (hit,sunk) = self.game.player_turn((x,y))
            except Exception as e :
                print(e)
                continue
            else :
                break
            
        if hit == True :
            print("Hit")
            if sunk == True :
                print(f"You sunk {sunk}")
        else :
            print("Miss")

        if hit == True :
            self.game.hit_ship((x,y),2)
            return self.game.check_GameOver(1)
        return False
   
    def AI_Turn(self) :
        game_over = False
        print("AI turn")
        (hit,game_over) = self.game.ai_turn()
        if hit == True :
            print("The AI hit your ship")
        else :
            print("The AI missed your ships")
        return game_over
        

 
    def print_board_player(self) :
        '''
        🟩 = Hit
        🟥 = Miss
        🟦 = empty
        🟨 = Battleship
        '''
        print("Player board :\n")
        self.board = self.game.get_palyer_board()
        self.pairs = {0 : 0 , 1 : 1, 2 : 2, 3 : 3, 4 : 4, 5 : 5, 6 : 6, 7 : 7, 8 : 8, 9 :9}
        print('-----------------------------------')
        print(' |   0  1  2  3  4  5  6  7  8  9 |')
        print('-----------------------------------')
        for row in self.pairs :
            print(f"{self.pairs[row]} |",end=' ')
            for i in range(10) : 
                if self.board[i][self.pairs[row]] == 0: print(f"🟦",end = ' ')
                elif self.board[i][self.pairs[row]] == 1: print(f"🟨",end = ' ')
                elif self.board[i][self.pairs[row]] == 2: print(f"🟩", end = ' ')
                elif self.board[i][self.pairs[row]] == 3: print(f"🟥", end = ' ')
            print('|')
        print('-----------------------------------')
        

    def print_board_AI(self) :
        '''
        🟩 = Hit
        🟥 = Miss
        🟦 = empty
        🟨 = Battleship
        '''
        print("AI board :\n")
        self.board = self.game.get_Ai_board()
        self.pairs = {0 : 0 , 1 : 1, 2 : 2, 3 : 3, 4 : 4, 5 : 5, 6 : 6, 7 : 7, 8 : 8, 9 :9}
        print('-----------------------------------')
        print('|   0  1  2  3  4  5  6  7  8  9 |')
        print('-----------------------------------')
        for row in self.pairs :
            print(f"{self.pairs[row]} |",end=' ')
            for i in range(10) : 
                if self.board[i][self.pairs[row]] == 0: print(f"🟦",end = ' ')
                elif self.board[i][self.pairs[row]] == 1: print(f"🟦",end = ' ')
                elif self.board[i][self.pairs[row]] == 2: print(f"🟩", end = ' ')
                elif self.board[i][self.pairs[row]] == 3: print(f"🟥", end = ' ')
            print('|')
        print('-----------------------------------')

ui = UI()
ui.start_game()