import copy


class Board(object):

    X = 'x'
    O = 'o'

    def __init__(self, player='x'):
        self.board = [
            [None] * 3,
            [None] * 3,
            [None] * 3,
        ]
        self.x_won = False
        self.o_won = False
        self.draw = False
        self.x_score = 0
        self.o_score = 0
        self.player = player
        self.move_history =[]

    @classmethod
    def opp_player(cls, player):
        if player == cls.X:
            return cls.O
        return cls.X


    def is_won(self, player):

        for check in [self.x_axes, self.y_axes, self.diags]:
            if any([self.same(r, player) for r in check()]):
                return True

        return False

    def my_score(self):
        if self.player == self.X:
            return self.x_score
        return self.o_score

    def x_axes(self):
        return [self.board[0], self.board[1], self.board[2]]

    def y_axes(self):
        return [self.y_axis(0), self.y_axis(1), self.y_axis(2)]

    def y_axis(self, y):
        return [self.board[0][y], self.board[1][y], self.board[2][y]]

    def diags(self):
        return (
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[0][2], self.board[1][1], self.board[2][0]]
        )

    def same(self, array, player):
        return all([i == player for i in array])


    def is_draw(self):
        any_own = self.any_won()
        places = bool(self.get_available_moves())

        if any_own:
            return False

        if (not any_own) and (not places):
            return True

        return False

    def game_end(self):

        if self.is_draw():
            return True

        if self.any_won():
            return True

        return False


    def any_won(self):
        if (not self.x_won) and (not self.o_won):
            return True
        return False


    def update(self, x, y, player):
        # print "-------before update--------"
        # print self.board

        if not self.board[x][y]:
            self.board[x][y] = player
            self.move_history.append({player: (x,y)})
            # print "----after update---"
            # print self.board
            self.update_wins()
        else:
            raise ValueError('Already updated')

    def update_wins(self):
        self.x_won = self.is_won(self.X)
        self.o_won = self.is_won(self.O)
        self.draw = self.is_draw()
        self.update_score()

    def update_score(self):
        if self.x_won:
            self.x_score = 10
            self.o_score = -10

        if self.o_won:
            self.o_score = 10
            self.x_score = -10

        if self.draw:
            self.o_score = 0
            self.x_score = 0

    def get_available_moves(self):
        res = []
        for i in range(3):
            res = res + [(i, j) for j, hole in enumerate(self.board[i]) if hole == None]
        return res

    def copy(self):
        copy_board = Board()
        copy_board = Board()
        copy_board.board = [x[:] for x in self.board[:]]
        copy_board.update_wins()
        return copy_board


    def predict(self, depth):
        go_depth = depth if depth else 0
        move_outputs = [move(self, self.player, hole[0], hole[1], go_depth) for hole in self.get_available_moves()]
        return reduce(lambda x, y : x+y, move_outputs)


def dprint(mess, i):
    i += 1
    scale = 5
    print  ' ' * 5 * i, '|', mess


def move(board, player, x, y, depth, dt=0, res=None):
    dprint('> orig : ' + str(board.board) + ' id:' + str(id(board)), dt)
    board = board.copy()
    dprint('> Copy: ' + str(board.board) + ' id:' + str(id(board)), dt)
    opp_player = Board.opp_player(player)
    dprint("Player: " + str(player) + ' Opp:' + str(opp_player), dt)
    # dprint("Before update: "+str(board.board), dt)
    board.update(x, y, opp_player)
    dprint("After update: "+str(board.board), dt)


    if not res:
        res = {
            'score': board.my_score(),
            'depth': dt,
            'move_history': []
        }

    res['move_history'].append({opp_player: (x,y)})

    dprint('>>> Depth = ' + str(depth) + ' dt=' + str(dt) + str(depth <= dt), dt)

    if dt < depth:
        dprint("Going ahead: ", dt)
        results = []
        for hole in board.get_available_moves():
            results.extend(move(board, opp_player, hole[0], hole[1], depth, dt=dt+1, res=copy.deepcopy(res)))
        data = results
    else:
        dprint("Coming back", dt)
        res['score'] = board.my_score()
        res['depth'] = dt
        res['board'] = board.board
        data = [res]

    return data










