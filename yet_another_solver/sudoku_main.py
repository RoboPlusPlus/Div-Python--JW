import numpy as np

very_easy_problem = np.array([[0, 8, 9, 0, 7, 0, 4, 3, 2],
                   [1, 2, 0, 0, 3, 0, 8, 0, 0],
                   [0, 5, 0, 6, 0, 0, 0, 0, 7],
                   [9, 0, 0, 0, 0, 1, 7, 5, 3],
                   [5, 0, 4, 7, 6, 9, 1, 0, 0],
                   [0, 0, 2, 0, 8, 3, 6, 0, 0],
                   [0, 0, 6, 0, 0, 2, 0, 0, 9],
                   [0, 7, 0, 8, 0, 0, 0, 4, 1],
                   [3, 0, 0, 4, 5, 0, 0, 8, 0]])

easy_problem  = np.array([[0, 2, 1, 3, 8, 0, 0, 4, 9],
                        [0, 0, 8, 0, 0, 4, 0, 2, 0],
                        [0, 6, 0, 0, 2, 0, 8, 0, 3],
                        [6, 1, 0, 0, 0, 7, 0, 0, 0],
                        [2, 9, 0, 0, 0, 0, 0, 8, 1],
                        [0, 0, 0, 2, 0, 0, 0, 5, 6],
                        [1, 0, 9, 0, 3, 0, 0, 7, 0],
                        [0, 5, 0, 1, 0, 0, 9, 0, 0],
                        [4, 7, 0, 0, 5, 2, 1, 3, 0]])

medium_problem  = np.array([[2, 0, 0, 1, 0, 8, 5, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 1, 7],
                           [0, 0, 0, 5, 3, 0, 0, 0, 4],
                           [0, 0, 2, 8, 4, 0, 0, 7, 1],
                           [0, 0, 0, 0, 5, 0, 0, 0, 0],
                           [4, 3, 0, 0, 6, 2, 8, 0, 0],
                           [8, 0, 0, 0, 1, 9, 0, 0, 0],
                           [9, 1, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 7, 4, 0, 5, 0, 0, 3]])

hard_problem  =  np.array([[4, 0, 7, 0, 6, 0, 0, 0, 0],
                           [9, 0, 0, 0, 0, 4, 8, 0, 0],
                           [0, 1, 0, 0, 9, 0, 0, 4, 0],
                           [0, 0, 0, 5, 0, 0, 1, 0, 4],
                           [2, 4, 0, 0, 0, 0, 0, 3, 9],
                           [1, 0, 9, 0, 0, 8, 0, 0, 0],
                           [0, 2, 0, 0, 7, 0, 0, 5, 0],
                           [0, 0, 6, 2, 0, 0, 0, 0, 7],
                           [0, 0, 0, 0, 5, 0, 3, 0, 2]])


blank_problem  = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0]])


a = np.array([[1,2], [3,4]])

class Cell:
    """
    Objekt for hver celle paa bordet

    """
    def __init__(self):
        self.cell_number = 0
        self.row_number = 0
        self.col_number = 0
        self.sqr_number = 0
        self.final_value = 0
        self.can_be_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]


    def __repr__(self):
        return "cell number = " + str(self.cell_number) + \
               "\nrow number = " + str(self.row_number) + \
               "\ncolumn number = " + str(self.col_number) + \
               "\nsquare number = " + str(self.sqr_number) + \
               "\ncan_be_values = " + str(self.can_be_values) + \
               "\nFINAL VALUE = " + str(self.final_value) + "\n\n"



class Board81:
    """
    Dette er en class for objekter som skal representere et sudoku-brett.
    Lager 81 Cell-objekter ved initialisering.

    """
    def __init__(self, start_board):
        self.cells = []
        self.flat_start_board = start_board.flatten()
        self.board_repr = ""

        # Bygger objekter for alle celler paa brettet
        for i in range(0,81):
            cell_stub = Cell()
            cell_stub.cell_number = i
            cell_stub.col_number = (i % 9)
            cell_stub.row_number = (i // 9)
            cell_stub.sqr_number = cell_stub.col_number // 3
            cell_stub.sqr_number = (cell_stub.sqr_number + 3) if cell_stub.row_number >= 3 else cell_stub.sqr_number
            cell_stub.sqr_number = (cell_stub.sqr_number + 3) if cell_stub.row_number >= 6 else cell_stub.sqr_number
            self.cells.append(cell_stub)
#        print(cells)

            self.rows = start_board
            self.columns = np.transpose(start_board)
            self.squares = []

        for i in range(9):
            sq = set()
            self.squares.append(sq)

        for cell_count, cell_value in enumerate(self.flat_start_board):
            #print(str(cell_value) + " " + str(cell_count))
            self.cells[cell_count].final_value = cell_value
            if cell_value > 0:
                self.cells[cell_count].can_be_values.clear()

        for cell in self.cells:
            self.squares[cell.sqr_number].add(cell.final_value)
            #print("\nself.squares \n")
            #print(self.squares)

    def cellupdate(self):
        changes = 0
        for cell in self.cells:
            #print("in cell " + str(cell))
            #print(cell.final_value)
            if cell.final_value < 1:
                #print("found cell with final value < 0 " + str(cell))
                cant_be_values = set()
                taken_row_vals = self.rows[cell.row_number]
                taken_column_vals = self.columns[cell.col_number]
                taken_square_vals = self.squares[cell.sqr_number]

                for value in taken_row_vals:
                    cant_be_values.add(value)

                for value in taken_column_vals:
                    cant_be_values.add(value)

                for value in taken_square_vals:
                    cant_be_values.add(value)

                for value in cant_be_values:
                    if value in cell.can_be_values:
                        cell.can_be_values.remove(value)
                        changes += 1

                if len(cell.can_be_values) == 1:
                    cell.final_value = cell.can_be_values[0]
                    cell.can_be_values.clear()
                    self.rows[cell.row_number][cell.col_number] = cell.final_value
                    self.columns[cell.col_number][cell.row_number] = cell.final_value
                    self.squares[cell.sqr_number].add(cell.final_value)

        return changes

    def can_anyone_else_be(self):
        for cell in self.cells:
            for value in cell.can_be_values:
                pass



    def __repr__(self):
        for row in self.rows:
            self.board_repr = self.board_repr + str(row) + "\n"

        return self.board_repr



    def verify_rows(self):
        row_set_error_found = False
        message = []
        row_sets = []
        for i in range(9):
            row_set = set()
            row_sets.append(row_set)
            for value in self.rows[i]:
                if value in row_sets[i]:
                    if value > 1:
                        row_set_error_found = True
                        message.append("Duplicate value in row {}, with value {}".format(i, value))
                row_sets[i].add(value)
            #print(row_sets[i])
        return row_set_error_found, message

    def verify_columns(self):
        col_set_error_found = False
        message = []
        col_sets = []
        for i in range(9):
            col_set = set()
            col_sets.append(col_set)
            for value in self.rows[i]:
                if value in col_sets[i]:
                    if value > 1:
                        col_set_error_found = True
                        message.append("Duplicate value in column {}, with value {}".format(i, value))
                col_sets[i].add(value)
            #print(col_sets[i])
        return col_set_error_found, message

    def verify_squares(self):
        pass

    def verify_cells(self):
        pass

    def check_self(self):
        message = []
        error_in_rows, row_message = self.verify_rows()
        error_in_cols, col_message = self.verify_columns()

        error_found = error_in_rows or error_in_cols

        message.append(row_message)
        message.append(col_message)

        return error_found, message

    def show_square_cells(self, square_to_display):
        for cell in self.cells:
            if(cell.sqr_number == square_to_display):
                print(cell)




def run():
    loop_changes = 0
    go = True
    iterations = 0
    board = Board81(hard_problem)
    board.check_self()

    while loop_changes > 0 or go:
        go = False
        loop_changes = board.cellupdate()
        iterations += 1
        print(str(loop_changes) + " loop changes at iteration " + str(iterations) + "\n")

    print(board.cells)
    print(board)
    error_found, error_message = board.check_self()
    print("error found = " + str(error_found))
    print(error_message)
    print("\n\nRows\n")
    print(board.rows)
    #print("\n\ncolumns\n")
    #print(board.columns)
    #print("\n\nsquares\n")
    #print(board.squares)
    #board.show_square_cells(0)

run()
