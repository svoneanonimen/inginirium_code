import pygame as t

t.init()
FPS = 100000
BLACK = (0,) * 3
GRAY = (100,) * 3
WHITE = (255,) * 3
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
LG = (0, 200, 200)
CROSS = '#046582'
CIRCLE = '#e4bad4'
W, H = 600, 600

win = t.display.set_mode((600, 600))
clock = t.time.Clock()


def draw_circle(sc, x, y, size):
    x = (x + .5) * size
    y = (y + .5) * size
    t.draw.circle(sc, CIRCLE, (x, y), (size - 3) // 2, 2)


def draw_cross(sc, x, y, size):
    x = x * size + 3
    y = y * size + 3
    t.draw.line(sc, CROSS, (x, y), (x + size - 3, y + size - 3), 3)
    t.draw.line(sc, CROSS, (x + size - 3, y), (x, y + size - 3), 3)


def is_eend(board):
    check_i_line = lambda x, i: True if x[i][0] == x[i][1] == x[i][2] != 0 else False
    check_i_col = lambda x, i: x[0][i] == x[1][i] == x[2][i] != 0
    check_main_diag = lambda x: x[0][0] == x[1][1] == x[2][2] != 0
    check_secondary_diag = lambda x: x[0][2] == x[1][1] == x[2][0] != 0
    for i in range(3):
        if check_i_col(board, i):
            return 'col', i
        if check_i_line(board, i):
            return 'line', i
    if check_main_diag(board):
        return 'diag', 1
    if check_secondary_diag(board):
        return 'diag', 2
    return None


class Board:
    def __init__(self, w, h, size):
        self.W, self.H = w, h
        self.size = size
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.move = 1

    def click(self, mouse_pos):
        x = mouse_pos[0] // self.size
        y = mouse_pos[1] // self.size
        self.board[y][x] = self.move
        self.move = -self.move

    def render(self, screen):
        t.draw.line(screen, GRAY, (0, 200), (self.W, 200))
        t.draw.line(screen, GRAY, (0, 400), (self.W, 400))
        t.draw.line(screen, GRAY, (200, 0), (200, self.H))
        t.draw.line(screen, GRAY, (400, 0), (400, self.H))
        for y in range(3):
            for x in range(3):
                if self.board[y][x] == 1:
                    draw_cross(screen, x, y, self.size)
                elif self.board[y][x] == -1:
                    draw_circle(screen, x, y, self.size)

    def chek_end(self):
        is_end_info = is_eend(self.board)
        shift = self.W // 10
        if is_end_info is not None:
            type_end = is_end_info[0]
            number = is_end_info[1]
            if type_end == 'col':
                x0, y0 = (number + 0, 5) * self.size, shift
                x1, y1 = x0, self.H - shift
            elif type_end == 'line':
                x0, y0 = shift, (number + .5) * self.size
                x1, y1 = self.W - shift, y0
            elif type_end == 'diag':
                if number == 1:
                    x0, y0 = shift, shift
                    x1, y1 = self.W - shift, self.H - shift
                elif number == 2:
                    x0, y0 = shift, self.H - shift
                    x1, y1 = self.W - shift, shift
            t.draw.line(win, RED, (x0, y0), (x1, y1), 10)
            t.display.update()
            t.time.delay(3000)
            return True
        else:
            return False


t.display.set_caption('итайцы рис перепаяли')

board = Board(W, H, 200)
# while 1 always true
while True:
    for event in t.event.get():
        if event.type == t.QUIT:
            t.quit()
            exit()
        if event.type == t.MOUSEBUTTONDOWN:
            board.click(event.pos)

    win.fill(WHITE)
    board.render(win)
    t.display.update()

    keys = t.key.get_pressed()
    if keys[t.K_ESCAPE] or board.chek_end():
        t.quit()
        exit()
    clock.tick(FPS)
