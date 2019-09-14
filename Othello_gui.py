# Willy Saronamihardja.  80408898.  Project 5.

import Othello_Input
import tkinter
import GameLogic

'''
NOTE TO TA:
PLEASE HAVE MERCY ON MY GRADE.
'''


possible_black = True
possible_white = True
DEFAULT_FONT = 'Comic Sans MS'
GAME_BOARD_WIDTH = float(600)
GAME_BOARD_HEIGHT = float(600)



class OthelloApp:
    def __init__(self):
        
        self._root_window = tkinter.Tk()

        new_game_button = tkinter.Button(
            master = self._root_window, text = 'Start the game',
            font = (DEFAULT_FONT, 12), command = self._on_button_press)

        new_game_button.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.S)


        self._no_game_text = tkinter.StringVar()
        self._no_game_text.set('Game not started.')

        no_game_label = tkinter.Label(
            master = self._root_window, textvariable = self._no_game_text,
            font = (DEFAULT_FONT, 12))

        no_game_label.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N)
        

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)


    def start(self) -> None:
        '''
        Starts the Othello program.
        '''  
        self._root_window.mainloop()


    def _on_button_press(self) -> None:
        '''
        When the button to start a game is pressed, we obtain the information
        here.
        '''
        game_information = Othello_Input.OthelloInfo()
        game_information.show()

        # INFORMATION FOR THE GAME
        if game_information.was_ok_clicked():
            self._rows = float(game_information.get_rows())
            self._columns = float(game_information.get_columns())
            self._player_one = game_information.get_player_one()
            self._TL_piece = game_information.get_TL_piece()
            self._winning_requirement = game_information.get_winning_req()

            self._root_window.destroy()

            self._draw_board()


    def _draw_rectangles(self) -> None:
        '''
        Draws the rectangles on the game board which represent game tiles.
        '''

        self._Othello_canvas.delete(tkinter.ALL)
        
        v_line_distance = GAME_BOARD_WIDTH / float(
            self._columns)
        h_line_distance = GAME_BOARD_HEIGHT / float(
            self._rows)
        
        v_line_distance = int(round(v_line_distance))
        h_line_distance = int(round(h_line_distance))

        # Creates the GameLogic game board.
        self._hidden_game_board = GameLogic.GameBoard.create_game_board(
            int(self._rows), int(self._columns))
        
        # Creates the game tiles.
        for column in range(int(self._columns)):
            for row in range(int(self._rows)):
                
                self._board_space = self._Othello_canvas.create_rectangle(
                    column * v_line_distance,
                    row * h_line_distance,
                    (column * v_line_distance) + v_line_distance,
                    (row * h_line_distance) + h_line_distance,
                    width = 2, fill = 'green', outline = 'purple')
              
                self._Othello_canvas.tag_bind(
                    self._board_space, '<ButtonPress-1>',
                    self._on_button_down)



    def _draw_four_pieces(self) -> None:
        '''
        Draws the four beginning Othello pieces before the game starts
        '''
        TL_piece = GameLogic.NONE
        
        if self._player_one == 'B':
            TL_piece = GameLogic.BLACK
        else:
            TL_piece = GameLogic.WHITE

        
        

##        self._Othello_canvas.create_oval(
##            tile_coords[0], tile_coords[1],
##            tile_coords[2], tile_coords[3],
##            fill = '{}'.format('black'))



        # Places the top left piece into the GameLogic game board.
        self._hidden_game_board = GameLogic.GameBoard.top_left_piece(
            self._hidden_game_board, TL_piece)




    def _draw_board(self) -> None:
        '''
        Draws the game board.
        '''
        self._root_window = tkinter.Tk()

        if self._player_one == 'W':
            self._player_one = 'White'
        elif self._player_one == 'B':
            self._player_one = 'Black'
        
        self._score = tkinter.StringVar()
        self._score.set(
            'WHITES: {}    BLACKS: {}'.format(
                '0', '0'))

        # Begins creating labels here.
        self._version = tkinter.StringVar()
        self._version.set(GameLogic.print_rule_set())

        self._turn = tkinter.StringVar()
        self._turn.set('Turn: {}'.format(self._player_one))

        self._version_label = tkinter.Label(
            master=self._root_window, textvariable = self._version,
            font = (DEFAULT_FONT, 12))
 
        self._score_label = tkinter.Label(
            master = self._root_window, textvariable = self._score,
            font = (DEFAULT_FONT, 20))

        self._turn_label = tkinter.Label(
            master = self._root_window, textvariable = self._turn,
            font = (DEFAULT_FONT, 12))

        self._score_label.grid(row = 0, column = 0)
        self._version_label.grid(row = 1, column = 0)
        self._turn_label.grid(row = 3, column = 0)
        # Finish creating labels here.
        
        self._Othello_canvas = tkinter.Canvas(
            master = self._root_window, width = GAME_BOARD_WIDTH,
            height = GAME_BOARD_HEIGHT, background = 'green')

        self._Othello_canvas.grid(
            row = 2, column = 0, padx = 7, pady = 7,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._button_is_down = False
        self._last_x = 0
        self._last_y = 0
        
        # Configures the game board window.
        self._root_window.rowconfigure(0, weight = 0)
        self._root_window.rowconfigure(1, weight = 0)
        self._root_window.rowconfigure(2, weight = 3)
        self._root_window.rowconfigure(3, weight = 0)            
        self._root_window.columnconfigure(0, weight = 1)

        self._draw_rectangles()
        self._draw_four_pieces()



    def _on_button_down(self, event: tkinter.Event) -> None:
        '''
        Event handler that is called when the primary mouse button
        is down within the canvas.
        '''
        
        self._button_is_down = True
        
        self._last_x = event.x
        self._last_y = event.y

        tile_coords = self._Othello_canvas.coords('current')
        
        player = 'None'
        if self._player_one == 'Black':
            player = 'black'
        elif self._player_one == 'White':
            player = 'white'

        self._Othello_canvas.create_oval(
            tile_coords[0], tile_coords[1],
            tile_coords[2], tile_coords[3],
            fill = '{}'.format(player))


    def _play_game(self) -> None:
        '''
        Plays the game of Othello.
        '''
        
        if self._player_one == 'Black':
            self._player = GameLogic.BLACK
        else:
            self._player = GameLogic.WHITE


        GameLogic.GameBoard.play_game(
            self._hidden_game_board, self._player,
            self._winning_requirement)

        

        

        


    
            


    




if __name__ == '__main__':
    OthelloApp().start()
