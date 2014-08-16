from random import choice
import time
from game import Game, HeroTile, MineTile
from pathing import PathBuilder, Path

class Bot:
    pass

stay = 'Stay'
n = 'North'
e = 'East'
s = 'South'
w = 'West'

class StrategyBot(Bot):

    def __init__(self):
        self.board_printed = False
        self.path_builder = PathBuilder()
        self.current_path = None

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
        self.game = game = Game(state)
        self.path_builder.game = game

        if not self.board_printed:
            self.print_board(game.board)
            self.board_printed = True

        self.board = board = game.board
        self.hero = hero = game.hero
        self.hero_pos = hero_pos = self._to_pos(hero.pos)

        #print hero_pos

        return self.seek_mine()

        # new_pos = board.to(hero_pos, w)

        # if new_pos == hero_pos:
        #     return s

        # if board.passable(new_pos):
        #     return w

        # return s

    def seek_mine(self):
        nearest_mine_pos = self.board.get_nearest_mine_pos(self.hero_pos,
                                                           self.game)
        if not self.current_path:
            mine_path = self.path_builder.construct_path(self.hero_pos,
                                                         nearest_mine_pos)
            print 'Traveling to Mine: ' + str(mine_path)
            self.current_path = Path(mine_path,
                                     self.hero_pos,
                                     nearest_mine_pos)
        next_move = self.current_path.get_next_dir()
        next_move = next_move if next_move else stay
        print 'Move: ' + next_move
        return next_move


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
