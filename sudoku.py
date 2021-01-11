import pygame as py
import sys
import SudokuSolver as ss

board = [
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]
]

FPS = 60
WHITE = (250, 250, 255)
BLUE1 = (184, 237, 252)
BLUE2 = (220, 245, 252)
CLICKED = (247, 181, 173)
BLACK = (10, 10, 10)
RED = (250, 0, 0)
WRONG_LIMIT = 10

size = (700, 500)
square_width = 50
square_size = (square_width, square_width)
background_size = (450, 450)

background_color = (184, 237, 252)
background_other_color = (220, 245, 252)
selected_color = (200, 50, 100)

# Start of code
py.init()
class Game:
    def __init__(self):
        self._board = [
            [0,0,0,2,6,0,7,0,1],
            [6,8,0,0,7,0,0,9,0],
            [1,9,0,0,0,4,5,0,0],
            [8,2,0,1,0,0,0,4,0],
            [0,0,4,6,0,2,9,0,0],
            [0,5,0,0,0,3,0,2,8],
            [0,0,9,3,0,0,0,7,4],
            [0,4,0,0,5,0,0,3,6],
            [7,0,3,0,1,8,0,0,0]
        ]
        
        # initialize the 9x9 grid
        self.squares = []
        for i in range(9):
            self.squares.append([])
            for j in range(9):
                # self.squares[i].append(py.Rect((j * square_width, i * square_width), square_size))
                self.squares[i].append(Grid(board[i][j], j, i))
        
        self._selectedx = -1
        self._selectedy = -1
        self._wrong = 0
        self.error_text = py.Surface((200, 100))

        # initialize solve button
        self.solve_button = py.Surface((100, 50))
        self.solve_button.fill(BLUE2)
        screen.blit(self.solve_button, (background_size[0] + 50, 400))
        

    def show_grid(self):
        for i in range(9):
            for j in range(9):
                screen.blit(self.squares[i][j].surface, (square_width * j, square_width * i))

    def show_border_and_number(self):
        for i in range(9):
            for j in range(9):
                if i == self._selectedy and j == self._selectedx:
                    self.squares[i][j].update_grid(True)
                else:
                    self.squares[i][j].update_grid(False)
    
                self.squares[i][j].write_number()

    def select_grid(self, x, y):
        # highlight the grid selected (x and y coordinates of 9x9 grid)
        self._selectedx = x
        self._selectedy = y
        return
    
    def deselect(self):
        self._selectedx = -1
        self._selectedy = -1
        return

    def memo_number(self, number):
        # Memo input number to grid if number isn't assigned yet (is 0)
        if self.squares[self._selectedy][self._selectedx].number == 0:
            self.squares[self._selectedy][self._selectedx].set_memo_number(number)

    def selected_has_memo(self):
        return self.squares[self._selectedy][self._selectedx].get_memo_number() != 0

    def check_selected_square(self):
        # Return True if 
        # 1. selected square has a memo'd number
        # 2. selected square's number is valid
        # Return False otherwise
        row = self._selectedy
        col = self._selectedx
        return ss.can_solve(self._board, row, col, self.squares[row][col].get_memo_number())

    def update_board(self):
        # updates the selected grid to adopt the memo'd number
        row = self._selectedy
        col = self._selectedx
        square = self.squares[row][col]
        self._board[row][col] = square.get_memo_number()
        square.update_number()

    def enter_wrong_number(self):
        # things happen if you enter wrong number 
        if self._wrong < WRONG_LIMIT:
            self._wrong += 1
        return
    
    def show_answers_wrong(self):
        self.error_text.fill(BLUE1)
        if py.font:
            if self._wrong < WRONG_LIMIT:
                font = py.font.SysFont("arial", 14)
                text = font.render("{} of {} incorrect attempt(s).".format(self._wrong, WRONG_LIMIT), 1, BLACK)
                textpos = text.get_rect(center=(100, 50))
            else:
                font = py.font.SysFont("arial", 14)
                text = font.render("You have {} or more wrong.".format(WRONG_LIMIT), 1, BLACK)
                textpos = text.get_rect(center=(100, 50))
            self.error_text.blit(text, textpos)
        screen.blit(self.error_text, (square_width*9 + 20, 20))

    def show_solve_button(self):
        # show solve button
        self.solve_button.fill(BLUE2)
        if py.font:
            font = py.font.SysFont("arial", 24)
            text = font.render("Solve", 1, BLACK)
            textpos = text.get_rect(center=(50, 25))
            self.solve_button.blit(text, textpos)
        screen.blit(self.solve_button, (background_size[0] + 50, 400))
        return
    
    def solve_button_clicked(self):
        
        return

class Grid:
    def __init__(self, num, x, y):
        if num != 0:
            self._is_given = True
        else:
            self._is_given = False

        self.number = num
        self.surface = py.Surface(square_size)
        if (x // 3 == 1 and (y // 3 == 0 or y // 3 == 2)) or (y // 3 == 1 and (x // 3 == 0 or x // 3 == 2)):
            self._color = BLUE2
        else:
            self._color = BLUE1
        self.surface.fill(self._color)
        self._memo = 0
    
    def update_grid(self, selected):
        # Fill grid with designated color
        if selected:
            self.surface.fill(CLICKED)
            py.draw.rect(self.surface, BLACK, ((0, 0), square_size), 1)
        else:
            self.surface.fill(self._color)
            py.draw.rect(self.surface, BLACK, ((0, 0), square_size), 1)
    
    def update_number(self):
        # memo'ed number shows up as number
        self.number = self._memo
        self._memo = 0
    
    def write_number(self):
        # Writes number to square
        if not py.font:
            print("font not loaded")
            return
        
        if self.number != 0:
            # render number on square
            font = py.font.SysFont("arial", 24, True if self._is_given else False)
            text = font.render(str(self.number), 1, BLACK)
            textpos = text.get_rect(center=(square_width // 2, square_width // 2))
            self.surface.blit(text, textpos)
            return
        
        if self._memo != 0:
            # render memo'ed number
            font = py.font.SysFont("arial", 17, False, True)
            text = font.render(str(self._memo), 1, BLACK)
            textpos = text.get_rect(center=(square_width // 2, square_width // 4))
            self.surface.blit(text, textpos)
            return

    def set_memo_number(self, num):
        # Memo number to square
        self._memo = num
        return
    
    def get_memo_number(self):
        return self._memo


screen = py.display.set_mode(size)

g = Game()

mousex, mousey = (0, 0)
mouse_clicked = False
selected_square = None
all_correct = True
game_over = False

def clicked_square(valx, valy):
    # Given the x and y coordinates of clicked position,
    # returns the coordinates of the box (0 ~ 8, 0 ~ 8)
    if valx > background_size[0] or valy > background_size[0]:
        return None
    return [valx // square_width, valy // square_width]

while 1:
    for event in py.event.get():
        if event.type == py.QUIT: 
            # Exit = quit game
            py.quit()
            sys.exit()
            
        elif event.type == py.KEYUP and event.key == py.K_ESCAPE:
            # ESC or mouse click off the grid = deselect grid
            selected_square = None

        elif event.type == py.MOUSEBUTTONUP:
            # mouse click 
            mousex, mousey = event.pos

            # Check if mouse clicks one of the squares
            selected_square = clicked_square(mousex, mousey)
            
        elif event.type == py.KEYUP and event.key == py.K_UP:
            if selected_square is not None:
                # move square up
                selected_square[1] = (selected_square[1] + 8) % 9
        
        elif event.type == py.KEYUP and event.key == py.K_DOWN:
            if selected_square is not None:
                # move square down
                selected_square[1] = (selected_square[1] + 1) % 9
        
        elif event.type == py.KEYUP and event.key == py.K_LEFT:
            if selected_square is not None:
                # move square left
                selected_square[0] = (selected_square[0] + 8) % 9
        
        elif event.type == py.KEYUP and event.key == py.K_RIGHT:
            if selected_square is not None:
                # move square right
                selected_square[0] = (selected_square[0] + 1) % 9
                

        elif event.type == py.KEYUP and event.key >= 49 and event.key <= 57:
            # key pressed is between 0 and 9
            input_number = event.key - 48
            g.memo_number(input_number) # don't memo if number is already filled

        elif event.type == py.KEYUP and (event.key == py.K_RETURN or event.key == py.K_KP_ENTER):
            # Check if: 1. selected square has memo number 
            # 2. selected square's memo number is valid
            if g.selected_has_memo():
                # check if memo number is valid
                correct = g.check_selected_square()
                if correct:
                    g.update_board()
                else:
                    all_correct = False
                    g.enter_wrong_number()
            


    # Background (white)
    screen.fill(WHITE)

    # Check if mouse clicks one of the squares
    # Indicate square to highlight (if mouse clicks on one of the squares in grid)
    if selected_square is not None:
        g.select_grid(selected_square[0], selected_square[1])
    else:
        g.deselect()
    
    # 9x9 grid with borders
    g.show_grid()
    g.show_border_and_number()

    # display text showing # of wrong attempts
    if not all_correct:
        g.show_answers_wrong()
    
    # show solve button
    g.show_solve_button()

    # set fps
    py.time.Clock().tick(FPS)
    py.display.update()

py.quit()



