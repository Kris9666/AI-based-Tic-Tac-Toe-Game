import random
import copy
import numpy as np

class Board:
    def __init__(self):
        
        self.board = [['0','0','0'], ['0','0','0'], ['0','0','0']]
        self.board_marked = 0
        self.length = len(self.board)
        self.width = max(len(line) for line in self.board)

        if (self.length != 3 or self.width != 3):
            raise Exception("Invalid Tic Tac Toe Board")
        else:
            print("Valid Tic Tac Toe Board")
            self.print_board()


    def print_board(self):
        print()
        print("\n------\n". join(["|".join(i) for i in self.board]))
        print()
        return


    def player(self):
        if self.isEmpty():
            player =  'X'
        
        if self.board_marked % 2 == 1:
            player = 'O'

        elif self.board_marked % 2 == 0:
            player = 'X'
        
        return player


    def isEmpty(self):
        return self.board_marked == 0


    def isFull(self):
        return self.board_marked == 9

    
    def mark_sqrs(self, row, col):
        player = self.player()
        self.board[row][col] = player
        self.board_marked += 1

    
    def empty_sqr(self, row, col):
        return self.board[row][col] == '0'
    


    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(self.length):
            for col in range(self.width):
                if self.empty_sqr(row, col):
                    empty_sqrs.append((row,col))

        return empty_sqrs


    
    def final_val(self):
        #Vertical Wins
        for col in range(self.width):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '0':
                return self.board[0][col]
            
        #Horizontal Wins
        for row in range(self.length):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != '0':
                return self.board[row][0]

        #Diagonal Wins
        # (0,0), (1,1), (2,2)
        # (0,2), (1,1), (2,0)
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '0':
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '0':
            return self.board[0][2]

        return 0

    def manual_move(self):
        row = int(input("Enter your row input : "))
        col = int(input("Enter your col input : "))
        if self.empty_sqr(row, col):
            self.mark_sqrs(row, col)
            return
        else:
            print("That position is already filled")
        return


class AI:
    def __init__(self):
        pass

    def rnd(self, board):
        empty_sqrs = board.get_empty_sqrs()
        idx = random.randrange(0, len(empty_sqrs))
        return empty_sqrs[idx]

    def minimax(self, board, maximing):
        case = board.final_val()

        if case == 'X':
            return 1, None
        if case == 'O':
            return -1, None
        elif board.isFull():
            return 0, None

        if maximing:
            v = -100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for(row,col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqrs(row, col)
                eval = self.minimax(temp_board, False)[0]
                if eval > v:
                    v = eval
                    best_move = (row,col)

                
            return v, best_move

        elif not maximing:
            v = 100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for(row,col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqrs(row, col)
                eval = self.minimax(temp_board, True)[0]
                if eval < v:
                    v = eval
                    best_move = (row,col)

                
            return v, best_move

    def ai_move(self, main_board):
        if main_board.isEmpty():
            move = self.rnd(main_board)
        else:
            val, move = self.minimax(main_board, True)

        row, col = move
        main_board.mark_sqrs(row, col)
        return




class Game:

    def __init__(self):
        self.board = Board()
        self.ai = AI()



def main():
    game = Game()
    board = game.board
    ai = game.ai
    # print(game.player())
    print(board.get_empty_sqrs())
    while(8):
        if board.player() == 'X':
            ai.ai_move(board)
        elif board.player() == 'O':
            board.manual_move()
            

        board.print_board()
        print(board.get_empty_sqrs())
        print(board.final_val())

main()
