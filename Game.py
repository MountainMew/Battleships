from Repository import board,player,AI
from random import randint


class game :
    def __init__(self) -> None:
        '''
        Constructor
        '''
        self.board = board()
        self.Player = player()
        self.AI = AI()
        pass
    
#-------------------------------------------------- Placements --------------------------------------------------------
    def place_ship(self,ship,start,end,len,orientation,player) :
        '''
        Places a ship on the board
        '''
        self.board.place_ship(start,end,orientation,player)
        ship.start = start
        ship.end = end
        ship.orientation = orientation
        ship.create_body()


    def valid_placement(self,start,end,len,orientation,player) :
        '''
        Checks if a ship can be placed on the board
        '''
        return self.board.valid_placement(start,end,len,orientation,player)

    def AI_place_ships(self) :
        '''
        Places the ships of the AI
        '''
        ships = self.AI.ships
        for ship in ships :
            start = (randint(0,9),randint(0,9))
            orientation = 'v' if randint(0,1) == 0 else 'h'
            end = (start[0]+ship.len-1,start[1]) if orientation == 'h' else (start[0],start[1]+ship.len-1)
            while not self.valid_placement(start,end,ship.len,orientation,2) :
                start = (randint(0,9),randint(0,9))
                orientation = 'v' if randint(0,1) == 0 else 'h'
                end = (start[0]+ship.len-1,start[1]) if orientation == 'h' else (start[0],start[1]+ship.len-1)
            self.place_ship(ship,start,end,ship.len,orientation,2)
            ship.start = start
            ship.end = end
            ship.orientation = orientation

    
#-------------------------------------------------- Turns --------------------------------------------------------
    
    def check_valid_coord_AI(self,coord) :
        '''
        Checks if the coord is valid on the AI board
        '''
        if coord[0] < 0 or coord[0] > 9 or coord[1] < 0 or coord[1] > 9 :
            raise Exception("Invalid coord")
        if self.board.get_palyer_board()[coord[0]][coord[1]] == 2 or self.board.get_palyer_board()[coord[0]][coord[1]] == 3 :
            raise Exception("Already hit")

    def check_valid_coord_Player(self,coord) :
        ''' 
        Checks if the coord is valid on the player board
        '''
        if coord[0] < 0 or coord[0] > 9 or coord[1] < 0 or coord[1] > 9 :
            raise Exception("Invalid coord")
        if self.board.get_boardAI()[coord[0]][coord[1]] == 2 or self.board.get_boardAI()[coord[0]][coord[1]] == 3 :
            raise Exception("Already hit")

    def player_turn(self,coord) :
        '''
        Player turn, where the player hits a coord
        
        '''
        sunk = 0
        self.check_valid_coord_Player(coord)
        sunk = self.hit_ship(coord,2)
        return (self.board.hit_ai(coord),sunk)

    def hit_ship(self,coord,player) :
        '''
        Checks if a ship is hit and if it is sunk
        '''

        if player == 1 :
            ships = self.Player.ships
        else :
            ships = self.AI.ships
        for ship in ships :
            if ship.is_alive() :
                if ship.orientation == 'v' :
                    if coord[0] == ship.start[0] and coord[1] >= ship.start[1] and coord[1] <= ship.end[1] :
                        ship.hit(coord)
                        if not ship.is_alive() :
                            return (f"Sunk {ship.name}.")
                        return 0
                else :
                    if coord[1] == ship.start[1] and coord[0] >= ship.start[0] and coord[0] <= ship.end[0] :
                        ship.hit(coord)
                        if not ship.is_alive() :
                            return (f"Sunk {ship.name}")
                        return 0

    def ai_turn(self) :
        '''
        AI turn, where the AI hits a coord
        The coord is chosen randomly until a ship is hit, then the AI will try to hit the rest of the ship
        by checking the surrounding coords
        '''
        hit = False
        if len(self.AI.possible_hits) > 0 :
            while self.AI.possible_hits != [] :
                coord = tuple(self.AI.possible_hits.pop())
                try:
                    self.check_valid_coord_AI(coord)    
                except Exception :
                    print("Invalid coord")
                    continue
                self.hit_ship(coord,1)
                hit = True
                x = self.board.hit_player(coord)
                if x == True :
                    self.AI.last_hit = coord
                    for i in (-1,1) :
                        point = (coord[0]+i,coord[1])
                        point2 = (coord[0],coord[1]+i)
                        if point[0] >= 0 and point[0] <= 9 and point[1] >= 0 and point[1] <= 9 :
                            if self.board.get_palyer_board()[point[0]][point[1]] == 0 or self.board.get_palyer_board()[point[0]][point[1]] == 1 :
                                self.AI.possible_hits.append((coord[0]+i,coord[1]))
                        if point2[0] >= 0 and point2[0] <= 9 and point2[1] >= 0 and point2[1] <= 9 :
                            if self.board.get_palyer_board()[point2[0]][point2[1]] == 0 or self.board.get_palyer_board()[point2[0]][point2[1]] == 1 :
                                self.AI.possible_hits.append((coord[0],coord[1]+i))
                return (x,self.check_GameOver(2))
        if self.AI.possible_hits == [] or hit == False:
            x = randint(0,9)
            y = randint(0,9)
            self.hit_ship((x,y),1)
            z = self.board.hit_player((x,y))
            if z == True :
                self.AI.last_hit = (x,y)
                for i in [-1,1] :
                    if self.board.get_palyer_board()[x+i][y] == 0 or self.board.get_palyer_board()[x+i][y] == 1:
                        self.AI.possible_hits.append((x+i,y))
                    if self.board.get_palyer_board()[x][y+i] == 0 or self.board.get_palyer_board()[x][y+i] == 1 :
                        self.AI.possible_hits.append((x,y+i))
            return (z,self.check_GameOver(2))
        '''
        x = randint(0,9)
        y = randint(0,9)
        self.hit_ship((4,4),1)
        return (self.board.hit_player((4,4)),self.check_GameOver(2))
        '''


#--------------------------------------------------  Getters --------------------------------------------------------  
    def get_player_ships(self) :
        '''
        Returns the player ships
        '''
        return self.Player.ships
    
    
    def get_palyer_board(self):
        '''
        Returns the player board
        '''
        return self.board.get_palyer_board()

    def get_Ai_board(self):
        '''
        Returns the AI board
        '''
        return self.board.get_boardAI()

#--------------------------------------------------  Checkers --------------------------------------------------------
    def check_GameOver(self,player) :
        ''' 
        Checks if the game is over
        '''
        if player == 2 :
            ships = self.Player.ships
        else :
            ships = self.AI.ships
        for ship in ships :
            if ship.is_alive() :
                return False
        return True

