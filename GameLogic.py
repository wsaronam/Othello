# Willy Saronamihardja.  80408898.  Project 5.


import collections
import Othello_gui


NONE = 0
WHITE = 1
BLACK = 2



def print_rule_set() -> None:
    '''
    Prints out which rule set the Othello game will be running on.
    '''
    return 'Full'




class InvalidMoveError(Exception):
    pass



    
class GameInfo:
        
    def obtain_board_rows() -> int:
        '''
        Obtains the amount of board rows that will be used in this game of
        Othello.
        '''
        rows = int(input())
        return rows

           

    def obtain_board_columns() -> int:
        '''
        Obtains the amount of board columns that will be used in this game of
        Othello.
        '''
        columns = int(input())
        return columns



    def obtain_first_turn() -> str:
        '''
        Obtains which player is playing first.
        '''
        player_one = input().upper()
        if player_one == 'B':
            return BLACK
        else:
            return WHITE


    def winning_requirement() -> str:
        '''
        Obtains the requirement for winning this Othello game.
        '''
        answer = input()
        return answer







class GameBoard:

    
    def create_game_board(rows: int, columns: int) -> [[int]]:
        '''
        Creates a list of lists of int that will be used to make the user
        interface of the Othello game board.
        '''
        board = []
        for col in range(columns):
            board.append([])
            for row in range(rows):
                board[-1].append(0)
        return board


    def top_left_piece(game_board: [[int]], TL_piece: str) -> [[int]]:
        '''
        Determines which piece will be at the top left of the game board.
        '''
        
        half_of_game_board = int((len(game_board) / 2) - 1)
        
        
        for lst in game_board:
            len_of_lst = len(lst)
            
        len_of_lst = int((len_of_lst / 2) - 1)
        
        if TL_piece == BLACK:
            game_board[half_of_game_board][len_of_lst] = 2
            game_board[half_of_game_board + 1][len_of_lst] = 1
            game_board[half_of_game_board][len_of_lst + 1] = 1
            game_board[half_of_game_board + 1][len_of_lst + 1] = 2
            
        elif TL_piece == WHITE:
            game_board[half_of_game_board][len_of_lst] = 1
            game_board[half_of_game_board + 1][len_of_lst] = 2
            game_board[half_of_game_board][len_of_lst + 1] = 2
            game_board[half_of_game_board + 1][len_of_lst + 1] = 1

        return game_board



    def display_first_board(game_board: [[int]], rows: int, columns: int) -> None:
        '''
        Creates the first Othello game board for the user to see.
        '''
        for i in range(rows):
            row_board = ''
            for j in range(columns):
                if game_board[j][i] == 0:
                    row_board += ".  "
                elif game_board[j][i] == 1:
                    row_board += "W  "
                elif game_board[j][i] == 2:
                    row_board += "B  "
            print(row_board)
            print ()

    

    def switch_players(player: str) -> str:
        '''
        Given the player whose turn it is now, returns the opposite player.
        '''
        if player == WHITE:
            return BLACK
        else:
            return WHITE


    def board(game_board: [[int]]) -> None:
        '''
        Displays the board for all turns after the first.
        '''
        for i in range(ROWS):
            row_board = ''
            for j in range(COLUMNS):
                if game_board[j][i] == 0:
                    row_board += ".  "
                elif game_board[j][i] == 1:
                    row_board += "W  "
                elif game_board[j][i] == 2:
                    row_board += "B  "
            print(row_board)
            print ()



    def play_game(game_board: [[int]], player: str, win_req: str) -> '?':
        '''
        Plays the game of othello.
        '''

        if Othello_gui.possible_black == False:
            if Othello_gui.possible_white == False:
                print ('No moves remaining.')
                blacks = 0
                whites = 0
                for lst in game_board:
                    for num in lst:
                        if num == BLACK:
                            blacks += 1
                        elif num == WHITE:
                            whites += 1

                if win_req == '<':
                    if blacks < whites:
                        print ('WINNER: BLACK')
                    elif whites < blacks:
                        print ('WINNER: WHITE')
                    elif blacks == whites:
                        print ('WINNER: NONE')
                elif win_req == '>':
                    if blacks > whites:
                        print ('WINNER: BLACK')
                    elif whites > blacks:
                        print ('WINNER: WHITE')
                    elif blacks == whites:
                        print ('WINNER: NONE')
                            
                raise SystemExit
        else:
            pass
        
        
        if player == BLACK:
            print ('TURN: B')
        else:
            print ('TURN: W')

        answer = input()
        row = int(answer[0])
        column = int(answer[-1])

        

        try:
            potential_spots = check_all(game_board, player, (row, column))
        except:
            print ('INVALID')
            GameBoard.play_game(game_board, player, win_req)

                             
        if potential_spots == None:
            print ('INVALID')
            GameBoard.play_game(game_board, player, win_req)

            
        elif potential_spots == []:
            print ('Not a possible move.')
            if player == BLACK:
                Othello_gui.possible_black = False
                GameBoard.play_game(game_board, GameBoard.switch_players(player), win_req)
            else:
                Othello_gui.possible_white = False
                GameBoard.play_game(game_board, GameBoard.switch_players(player), win_req)

        
            

        
        for lst in potential_spots:
            for num in lst:
                row = num[0]
                column = num[1]
                if player == BLACK:
                    game_board[column - 1][row - 1] = BLACK
                elif player == WHITE:
                    game_board[column - 1][row - 1] = WHITE
        
        blacks = 0
        whites = 0
        for lst in game_board:
            for num in lst:
                if num == BLACK:
                    blacks += 1
                elif num == WHITE:
                    whites += 1

        counter = 0

        for lst in game_board:
            for num in lst:
                if num == 0:
                    counter += 1
                    
        if counter == 0:
            if win_req == '<':
                if blacks < whites:
                    print ('WINNER: BLACK')
                elif whites < blacks:
                    print ('WINNER: WHITE')
                elif blacks == whites:
                    print ('WINNER: NONE')
            elif win_req == '>':
                if blacks > whites:
                    print ('WINNER: BLACK')
                elif whites > blacks:
                    print ('WINNER: WHITE')
                elif blacks == whites:
                    print ('WINNER: NONE')
                    
            raise SystemExit
        
        else:
            pass

        Othello_gui.possible_black = True
        Othello_gui.possible_white = True
            
                    
        print ('B: ' + str(blacks) + '  ' + 'W: ' + str(whites))

        new_player = GameBoard.switch_players(player)

        GameBoard.board(game_board)        

        GameBoard.play_game(game_board, new_player, win_req)




def check_right(game_board: [[int]], player: str, coordinate: tuple) -> list:
    '''
    Checks direction of board with while loop.
    '''
    row = coordinate[0] - 1
    column = coordinate[1] - 1
    
    list_of_spots = []
    try:
        if player == WHITE:
            
            if game_board[column][row] == NONE:
                column += 1
                
                while game_board[column][row] == BLACK:
                    list_of_spots.append((row + 1, column))
                    column += 1
                    list_of_spots.append((row + 1, column))

                    if game_board[column][row] == WHITE:
                        return list_of_spots

                    else:
                        pass

        if player == BLACK:
            
            if game_board[column][row] == NONE:
                column += 1
                
                while game_board[column][row] == WHITE:
                    list_of_spots.append((row + 1, column))
                    column += 1
                    list_of_spots.append((row + 1, column))

                    if game_board[column][row] == BLACK:
                        return list_of_spots

                    else:
                        pass
    except:
        pass
     
                    
    
def check_left(game_board: [[int]], player: str, coordinate: tuple) -> list:
    '''
    Checks direction of board with while loop.
    '''
    row = coordinate[0] - 1
    column = coordinate[1] - 1
    
    list_of_spots = []
    try:
        if player == WHITE:
            
            if game_board[column][row] == NONE:
                column -= 1
                
                while game_board[column][row] == BLACK:
                    list_of_spots.append((row + 1, column + 2))
                    column -= 1
                    list_of_spots.append((row + 1, column + 2))

                    if game_board[column][row] == WHITE:
                        return list_of_spots

                    else:
                        pass

        if player == BLACK:
            
            if game_board[column][row] == NONE:
                column -= 1
                
                while game_board[column][row] == WHITE:
                    list_of_spots.append((row + 1, column + 2))
                    column -= 1
                    list_of_spots.append((row + 1, column + 2))

                    if game_board[column][row] == BLACK:
                        return list_of_spots

                    else:
                        pass
    except:
        pass
    

def check_up(game_board: [[int]], player: str, coordinate: tuple) -> list:
    '''
    Checks direction of board with while loop.
    '''
    row = coordinate[0] - 1
    column = coordinate[1] - 1
    
    list_of_spots = []
    try:
        if player == WHITE:
            
            if game_board[column][row] == NONE:
                row += 1
                
                while game_board[column][row] == BLACK:
                    list_of_spots.append((row, column + 1))
                    row += 1
                    list_of_spots.append((row, column + 1))

                    if game_board[column][row] == WHITE:
                        return list_of_spots

                    else:
                        pass

        if player == BLACK:
            
            if game_board[column][row] == NONE:
                row += 1
                
                while game_board[column][row] == WHITE:
                    list_of_spots.append((row, column + 1))
                    row += 1
                    list_of_spots.append((row, column + 1))

                    if game_board[column][row] == BLACK:
                        return list_of_spots

                    else:
                        pass
    except:
        pass


def check_down(game_board: [[int]], player: str, coordinate: tuple) -> list:
    '''
    Checks direction of board with while loop.
    '''
    row = coordinate[0] - 1
    column = coordinate[1] - 1
    
    list_of_spots = []
    try:
        if player == WHITE:
            
            if game_board[column][row] == NONE:
                row -= 1
                
                while game_board[column][row] == BLACK:
                    list_of_spots.append((row + 2, column + 1))
                    row -= 1
                    list_of_spots.append((row + 2, column + 1))

                    if game_board[column][row] == WHITE:
                        return list_of_spots

                    else:
                        pass

        if player == BLACK:
            
            if game_board[column][row] == NONE:
                row -= 1
                
                while game_board[column][row] == WHITE:
                    list_of_spots.append((row + 2, column + 1))
                    row -= 1
                    list_of_spots.append((row + 2, column + 1))

                    if game_board[column][row] == BLACK:
                        return list_of_spots

                    else:
                        pass
    except:
        pass

                


def check_all(game_board: [[int]], player: str, coordinate: tuple) -> list:
    '''
    '''
    x = coordinate[0]
    y = coordinate[1]

    list_of_all = []

    
    list_of_all.append(check_right(game_board, player, (x, y)))

    list_of_all.append(check_left(game_board, player, (x, y)))

    list_of_all.append(check_up(game_board, player, (x, y)))

    list_of_all.append(check_down(game_board, player, (x, y)))

    new_list = [num for num in list_of_all if num is not None]
    

    return new_list


def count_blacks_and_whites(game_board: [[int]]) -> tuple:
    '''
    Counts the number of black and white tiles in the game.
    '''
    blacks = 0
    whites = 0
    for lst in game_board:
        for num in lst:
            if num == BLACK:
                blacks += 1
            elif num == WHITE:
                whites += 1
    return (blacks, whites)








