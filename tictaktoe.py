import copy
import curses
import time


x = 'x'
o = 'o'
n = None

LOG = False


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
        # import pdb; pdb.set_trace()  # XXX BREAKPOINT
        any_own = self.any_won()
        places = bool(self.get_available_moves())

        if (not any_own) and (not places):
            return True

        return False

    def game_end(self):

        # if self.any_won() and self.x_score ==0 and self.o_score==0:
            # print 'd=', self.is_draw(), 'w=',self.any_won(),' pX=',self.x_score,self.x_won," pO=",self.o_score,self.o_won, 'board=',self.board
            # print "is won: x ",self.is_won('x'), '  o: ',self.is_won('o')

        if self.is_draw() or self.any_won() or (not self.get_available_moves()):
            return True

        return False


    def any_won(self):
        if self.x_won or self.o_won:
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

    def status(self):
        print "x_won: ",self.x_won," o_won:",self.o_won," x_score:", self.x_score, "o_score:",self.o_score, " is_draw:",self.is_draw()," end:",self.game_end()


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

        if ((not self.o_won) and (not self.x_won)) or self.draw:
            self.o_score = 0
            self.x_score = 0

    def get_available_moves(self):
        res = []
        for i in range(3):
            res = res + [(i, j) for j, hole in enumerate(self.board[i]) if hole == None]
        return res

    def copy(self, copy_moves=True):
        copy_board = Board()
        copy_board.board = [x[:] for x in self.board[:]]

        if copy_moves:
            copy_board.move_history = copy.deepcopy(self.move_history)

        copy_board.update_wins()
        return copy_board


    def predict(self):
        last_move_player = self.opp_player(self.player)
        print ">>>>>>>>>>>>>>>> last_move player :" ,last_move_player
        # init=True copies history_moves, but we dont need historical moves
        move_outputs = [move(self, last_move_player, hole[0], hole[1], init=False) for hole in self.get_available_moves()]
        print '\n>>>>>>>', self.board
        return reduce(lambda x, y : x+y, move_outputs)

    def print_board(self):
        print "~~~~~~ TTT BOARD ~~~~~~"
        for i in range(3):
            for j in range(3):
                data = game.board[i][j]
                print data,

                if data:
                    print '   ',
                else:
                    print  '',
            print ''
        print "~~~~~~~~~~~~~~~~~~~~~~~"


#-------------------------------------------------------------------------------


def dprint(mess, i):
    if not LOG:
        return

    i += 1
    scale = 5
    print  ' ' * 5 * i, '|', mess


def move(board, player, x, y, dt=0, init=True):
    dprint('> orig : ' + str(board.board) + ' id:' + str(id(board)), dt)
    board = board.copy(copy_moves=init)
    dprint('> Copy: ' + str(board.board) + ' id:' + str(id(board)), dt)
    opp_player = Board.opp_player(player)
    dprint("Player: " + str(player) + ' Opp:' + str(opp_player), dt)
    dprint("Before update: "+str(board.board), dt)
    board.update(x, y, opp_player)
    dprint("After update: "+str(board.board), dt)

    if not board.game_end():
        dprint("Going ahead: ", dt)
        results = []
        for hole in board.get_available_moves():
            results.extend(move(board, opp_player, hole[0], hole[1], dt=dt+1))
        data = results
    else:
        dprint("Coming back", dt)
        res = {}
        res['score'] = board.my_score()
        # res['depth'] = dt
        res['board'] = board.board
        res['move_history'] = board.move_history
        res['move_len'] = len(board.move_history)

        data = [res]

    return data






def even_loop():
    game = Board()
    game.board=[
            [x,o,x],
            [n,n,o],
            [n,n,n]]
    game.update_wins()


    while not game.game_end():
        game.print_board()
        o_move = raw_input("O enter your move: \n")
        ox, oy = o_move.split('--')
        ox, oy = int(ox), int(oy)
        game.update(ox, oy, Board.O)

        if game.game_end():
            continue

        game.print_board()
        data = game.predict()

        # print '--' * 20
        # for d in data:print d
        # print '--' * 20

        wins = filter(lambda x:x['score']==10, data)
        draws = filter(lambda x:x['score']==0, data)
        looses = filter(lambda x:x['score']==-10, data)

        if wins:
            moves = wins
        elif draws:
            moves=draws
        else:
            moves = looses

        short_moves = sorted(moves, key=lambda x: x['move_len'])

        # print "Going with ",short_moves[0]
        next_move = short_moves[0]['move_history'][0][Board.X]

        # print "Moving X to ", next_move
        game.update(next_move[0], next_move[1], Board.X)


    print "________________Game stats___________________\n"
    print game.print_board()
    print "[Robo's score:", game.x_score, "]"
    print "[Your score: ", game.o_score, ']'

    if game.x_score == 10:
        print "ROBO WON !!!"
    elif game.o_score == 10:
        print "YOU YOU YOU WON"
    else:
        print "TIE TIE"

    print "_____________________________________________\n"



def gen_grid(screen, vg):
    for g in vg:
        sprint("".join(g))


def sprint(screen, content):
    content = content + '\n'
    screen.addstr(content)


def UI():

	vg = [
		[' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
		[' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
		[' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
		['--', '--', '--', '|', '--', '--', '--', '|', '--', '--', '--'],
		[' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
		[' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
		[' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
		['--', '--', '--', '|', '--', '--', '--', '|', '--', '--', '--'],
		[' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
		[' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
		[' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ']
	]

	try:
		screen = curses.initscr()
		curses.noecho()
		curses.curs_set(0)
		screen.keypad(1)
		gen_grid(screen, vg)

		while True:
			event = screen.getch()
			if event == ord("q"): break


	except Exception as e:
		print str(e)
		curses.endwin()




if __name__ == "__main__":
	UI()




