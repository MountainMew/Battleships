class ship :
    '''
    Class that represents a ship
    '''
    def __init__(self,start,end,len,name) -> None:
        '''
        Constructor for the ship class
        '''
        self.__name = name
        self.__start = start
        self.__end = end
        self.__len = len
        self.__sunk = False
        self.__orientation = 'v' if start[0] == end[0] else 'h'
        self.body = []
   
    @property 
    def name(self) :
        return self.__name
    @name.setter
    def name(self,name) :
        self.__name = name
    
    @property 
    def start(self) :
        return self.__start
    @start.setter
    def start(self,start) :
        self.__start = start

    @property
    def end(self) :
        return self.__end
    @end.setter
    def end(self,end) :
        self.__end = end

    @property
    def len(self) :
        return self.__len
    @len.setter
    def len(self,len) :
        self.__len = len

    @property
    def sunk(self) :
        return self.__sunk
    @sunk.setter
    def sunk(self,sunk) :
        self.__sunk = sunk

    @property
    def orientation(self) :
        return self.__orientation
    @orientation.setter
    def orientation(self,orientation) :
        self.__orientation = orientation

    def create_body(self) :
        '''
        Creates the body of the ship
        '''
        if self.__orientation == 'v' :
            for i in range(self.__start[1],self.__end[1]+1) :
                self.body.append((self.__start[0],i))
        else :
            for i in range(self.__start[0],self.__end[0]+1) :
                self.body.append((i,self.__start[1]))

    def is_alive(self) :
        '''
        Checks if the ship is alive or not
        '''
        return not self.__sunk

    def hit(self,position) :
        ''' 
        Checks if the ship was hit or not and returns True if it was hit and False if it wasn't and also removes the position from the body of the ship
        '''
        if position in self.body :
            self.body.remove(position)
            if len(self.body) == 0 :
                self.__sunk = True
                return True
            return False
        else :
            return False

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o,ship) :
            return self.__name == __o.name
        return False

    def __str__(self) -> str:
        return f"Name: {self.__name} | Start: {self.__start} | End: {self.__end} | Length: {self.__len} | Orientation: {self.__orientation} | Sunk: {self.__sunk} | Body: {self.body}"


class Error(Exception):
    """Base class for other exceptions"""
    pass

