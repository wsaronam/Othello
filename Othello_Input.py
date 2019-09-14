# Willy Saronamihardja 80408898.  Project 5.

import tkinter


DEFAULT_FONT = 'Comic Sans MS'



class OthelloInfo:
    def __init__(self):
        '''
        Initializes the Othello program.
        '''
        self._dialog_window = tkinter.Toplevel()
        
        main_label = tkinter.Label(
            master = self._dialog_window, text = 'Plese enter game information.',
            font = (DEFAULT_FONT, 12))

        main_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 8, pady = 8,
            sticky = tkinter.W)
        
        row_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Rows (even number between 4 and 16):',
            font = (DEFAULT_FONT, 12))

        row_label.grid(
            row = 1, column = 0, padx = 8, pady = 8,
            sticky = tkinter.W)

        self._row_entry = tkinter.Entry(
            master = self._dialog_window, width = 20,
            font = (DEFAULT_FONT, 12))

        self._row_entry.grid(
            row = 1, column = 1, padx = 8, pady = 1,
            sticky = tkinter.W + tkinter.E)

        column_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Columns (even number between 4 and 16):',
            font = (DEFAULT_FONT, 12))

        column_label.grid(
            row = 2, column = 0, padx = 8, pady = 8,
            sticky = tkinter.W)

        self._column_entry = tkinter.Entry(
            master = self._dialog_window, width = 20,
            font = (DEFAULT_FONT, 12))

        self._column_entry.grid(
            row = 2, column = 1, padx = 8, pady = 1,
            sticky = tkinter.W + tkinter.E)

        player_one_label = tkinter.Label(
            master = self._dialog_window, text = 'Starting Player (Type in B/W):',
            font = (DEFAULT_FONT, 12))

        player_one_label.grid(
            row = 3, column = 0, padx = 8, pady = 8,
            sticky = tkinter.W)

        self._player_one_entry = tkinter.Entry(
            master = self._dialog_window, width = 20,
            font = (DEFAULT_FONT, 12))

        self._player_one_entry.grid(
            row = 3, column = 1, padx = 8, pady = 1,
            sticky = tkinter.W + tkinter.E)

        top_left_piece_label = tkinter.Label(
            master = self._dialog_window, text = 'Top Left Piece (Type in B/W):',
            font = (DEFAULT_FONT, 12))

        top_left_piece_label.grid(
            row = 4, column = 0, padx = 8, pady = 8,
            sticky = tkinter.W)

        self._TL_entry = tkinter.Entry(
            master = self._dialog_window, width = 20,
            font = (DEFAULT_FONT, 12))

        self._TL_entry.grid(
            row = 4, column = 1, padx = 8, pady = 1,
            sticky = tkinter.W + tkinter.E)

        winning_req_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Winning Requirement (Type in >/<  > for more tiles and < for less tiles):',
            font = (DEFAULT_FONT, 12))

        winning_req_label.grid(
            row = 5, column = 0, padx = 8, pady = 8,
            sticky = tkinter.W)

        self._winning_req_entry = tkinter.Entry(
            master = self._dialog_window, width = 20,
            font = (DEFAULT_FONT, 12))

        self._winning_req_entry.grid(
            row = 5, column = 1, padx = 8, pady = 1,
            sticky = tkinter.W + tkinter.E)

        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 6, column = 0, columnspan = 2, padx = 8, pady = 8,
            sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = (DEFAULT_FONT, 12),
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = (DEFAULT_FONT, 12),
            command = self._on_cancel_button)

        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)


        self._ok_clicked = False
        self._rows = ''
        self._columns = ''
        self._player_one = ''
        self._TL_piece = ''
        self._winning_req = ''     


    def show(self) -> None:
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()


    def was_ok_clicked(self) -> bool:
        return self._ok_clicked


    def get_rows(self) -> str:
        return self._rows

    def get_columns(self) -> str:
        return self._columns

    def get_player_one(self) -> str:
        return self._player_one

    def get_TL_piece(self) -> str:
        return self._TL_piece

    def get_winning_req(self) -> str:
        return self._winning_req


    def _on_ok_button(self) -> None:
        self._ok_clicked = True
        self._rows = self._row_entry.get()
        self._columns = self._column_entry.get()
        self._player_one = self._player_one_entry.get().upper()
        self._TL_piece = self._TL_entry.get().upper()
        self._winning_req = self._winning_req_entry.get()

        self._dialog_window.destroy()


    def _on_cancel_button(self) -> None:
        self._dialog_window.destroy()





