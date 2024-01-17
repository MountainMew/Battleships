import unittest
import Game
import Repository
import Domain


class Test(unittest.TestCase):
    def setUp(self):
        self.game = Game.game()
        self.board = Repository.board()
        self.player = Repository.player()
        self.AI = Repository.AI()
        self.ship = Domain.ship(2)
