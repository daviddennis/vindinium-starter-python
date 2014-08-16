from random import choice
import time
from game import Game, HeroTile, MineTile

class Bot:
    pass


m = {
    '': 'Stay',
    'n': 'North',
    'e': 'East',
    's': 'South',
    'w': 'West',
    }

stay = 'Stay'
n = 'North'
e = 'East'
s = 'South'
w = 'West'

class StrategyBot(Bot):

    def __init__(self):
        self.board_printed = False

    def _to_pos(self, pos_dict):
        return (pos_dict['x'], pos_dict['y'])

    def print_board(self, board):
        for tiles in board.tiles:
            for x in tiles:
                if isinstance(x, HeroTile):
                    print 'H',
                elif isinstance(x, MineTile):
                    print 'M',
                else:
                    print x,
            print '\n',
        

    def move(self, state):
        game = Game(state)
        if not self.board_printed:
            self.print_board(game.board)
            self.board_printed = True

        board = game.board
        hero = game.hero
        hero_pos = self._to_pos(hero.pos)

        #print hero_pos

        new_pos = board.to(hero_pos, w)

        if new_pos == hero_pos:
            return s

        if board.passable(new_pos):
            return w

        return s


class RandomBot(Bot):

    def move(self, state):
        game = Game(state)
        dirs = ['Stay', 'North', 'South', 'East', 'West']
        return 'South'#choice(dirs)


class FighterBot(Bot):
    def move(self, state):
        dirs = ['Stay', 'North', 'South', 'East', 'West']
        return choice(dirs)



class SlowBot(Bot):
    def move(self, state):
        dirs = ['Stay', 'North', 'South', 'East', 'West']
        time.sleep(2)
        return choice(dirs)
