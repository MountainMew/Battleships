import random as rand
from Domain import ship

class board :
    def __init__(self):
        '''
        Constructor
        '''
        self.Board_Player = [[0] * 10 for _ in range(10)]
        self.Board_AI = [[0] * 10 for _ in range(10)]
        


    def get_boardP(self) :
        '''
        Returns the board of the player
        '''
        return self.Board_Player

    def get_boardAI(self) :
        '''
        Returns the board of the AI
        '''
        return self.Board_AI

    def place_ship(self,start,end,orientation,player) :
        '''
        Places a ship on the board of the player or the AI depending on the player parameter
        '''
        if player == 1 :
            if orientation == 'v' : 
                for i in range(start[1],end[1]+1) : 
                    self.Board_Player[start[0]][i] = 1  
            else :  
                for i in range(start[0],end[0]+1) : 
                    self.Board_Player[i][start[1]] = 1  
        else :
            if orientation == 'v' : 
                for i in range(start[1],end[1]+1) : 
                    self.Board_AI[start[0]][i] = 1  
            else :  
                for i in range(start[0],end[0]+1) : 
                    self.Board_AI[i][start[1]] = 1

    def valid_placement(self,start,end,len,orientation,player) :
        '''
        Checks if a ship can be placed on the board of the player or the AI depending on the player parameter
        '''
        if start[0] < 0 or start[0] > 9 or start[1] < 0 or start[1] > 9 or end[0] < 0 or end[0] > 9 or end[1] < 0 or end[1] > 9 :
            return False
        if player == 1 :
            if orientation == 'v' :
                if start[0] != end[0] :
                    return False 
                if end[1] - start[1] != len-1 :
                    return False
                for i in range(start[1],end[1]+1) : 
                    if self.Board_Player[start[0]][i] == 1 :
                        return False
            else :  
                if start[1] != end[1] :
                    return False
                if end[0] - start[0] != len-1 :
                    return False
                for i in range(start[0],end[0]+1) : 
                    if self.Board_Player[i][start[1]] == 1 :
                        return False
        else :
            if orientation == 'v' : 
                if start[0] != end[0] :
                    return False
                if end[1] - start[1] != len-1 :
                    return False
                for i in range(start[1],end[1]+1) : 
                    if self.Board_AI[start[0]][i] == 1 :
                        return False
            else :  
                if start[1] != end[1] :
                    return False
                if end[0] - start[0] != len-1 :
                    return False
                for i in range(start[0],end[0]+1) : 
                    if self.Board_AI[i][start[1]] == 1 :
                        return False
        return True

    def hit_player(self,poz : tuple) :
        '''
        Checks if the player hit a ship or not
        '''
        if self.Board_Player[poz[0]][poz[1]] == 1 :
            self.Board_Player[poz[0]][poz[1]] = 2
            return True
        else :
            self.Board_Player[poz[0]][poz[1]] = 3
            return False

    def hit_ai(self,poz : tuple) :
        '''
        Checks if the AI hit a ship or not
        '''
        if self.Board_AI[poz[0]][poz[1]] == 1 :
            self.Board_AI[poz[0]][poz[1]] = 2
            return True
        else :
            self.Board_AI[poz[0]][poz[1]] = 3
            return False

    def get_palyer_board(self):
        return self.Board_Player

class player :
    '''
    Class that represents the player's ships
    '''
    def __init__(self) :
        self.ships = [ship((0,0),(0,0),5,'carrier (5)'),
            ship((0,0),(0,0),4,'battleship (4)'),
            ship((0,0),(0,0),3,'cruiser (3)'),
            ship((0,0),(0,0),2,'destroyer (2)'),
            ship((0,0),(0,0),2,'submarine (2)')]
        


    


class AI :
    '''
    Class that represents the AI's ships and the last hit as well as the possible hits
    '''
    def __init__(self) :
        self.ships = [ship((0,0),(0,0),5,'carrier (5)'),
            ship((0,0),(0,0),4,'battleship (4)'),
            ship((0,0),(0,0),3,'cruiser (3)'),
            ship((0,0),(0,0),2,'destroyer (2)'),
            ship((0,0),(0,0),2,'submarine (2)')]
        self.last_hit = (-1,-1)
        self.last_hit_orientation = 'v'
        self.possible_hits = []
        

    