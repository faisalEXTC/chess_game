import pygame
import os
from piece import King
from piece import Queen
from piece import Bishop
from piece import Knight
from piece import Pawn
from piece import Rook

background = pygame.image.load('img\\board.png')
size_of_bg = background.get_rect().size
square_width = int(size_of_bg[0]/8)
square_height = int(size_of_bg[1]/8)
screen = pygame.display.set_mode(size_of_bg)
cell_selected = pygame.image.load('img\\green_box.png')
cell_selected = pygame.transform.scale(cell_selected, (80, 80))
yell = pygame.image.load('img\\yellow_box.png')
yell = pygame.transform.scale(yell, (80, 80))
red = pygame.image.load('img\\red_box.png')
red = pygame.transform.scale(red, (80, 80))
green_circle = pygame.image.load("img\\green_circle.png")
green_circle = pygame.transform.scale(green_circle, (80, 80))
pygame.display.set_caption('Chess')
screen.blit(background,(0,0))

def pixel_to_chess(pixel_cord):
    x = pixel_cord[0]/square_width
    y = pixel_cord[1]/square_height
    return (int (x), int (y))

def chess_to_pixel(chess_coord):
    return (chess_coord[0]*square_width,chess_coord[1]*square_height)


class Board:
    def __init__(self):
        self.row = -1
        self.col = -1
        self.isselected = False
        self.turn = "w"
        self.check = False
        
        self.board = [[0 for x in range(8)] for _ in range(8)]

        self.board[0][0] = Rook(0, 0, "b")
        self.board[0][1] = Knight(0, 1, "b")
        self.board[0][2] = Bishop(0, 2, "b")
        self.board[0][3] = Queen(0, 3, "b")
        self.board[0][4] = King(0, 4, "b")
        self.board[0][5] = Bishop(0, 5, "b")
        self.board[0][6] = Knight(0, 6, "b")
        self.board[0][7] = Rook(0, 7, "b")

        self.board[1][0] = Pawn(1, 0, "b")
        self.board[1][1] = Pawn(1, 1, "b")
        self.board[1][2] = Pawn(1, 2, "b")
        self.board[1][3] = Pawn(1, 3, "b")
        self.board[1][4] = Pawn(1, 4, "b")
        self.board[1][5] = Pawn(1, 5, "b")
        self.board[1][6] = Pawn(1, 6, "b")
        self.board[1][7] = Pawn(1, 7, "b")

        self.board[7][0] = Rook(7, 0, "w")
        self.board[7][1] = Knight(7, 1, "w")
        self.board[7][2] = Bishop(7, 2, "w")
        self.board[7][3] = Queen(7, 3, "w")
        self.board[7][4] = King(7, 4, "w")
        self.board[7][5] = Bishop(7, 5, "w")
        self.board[7][6] = Knight(7, 6, "w")
        self.board[7][7] = Rook(7, 7, "w")

        self.board[6][0] = Pawn(6, 0, "w")
        self.board[6][1] = Pawn(6, 1, "w")
        self.board[6][2] = Pawn(6, 2, "w")
        self.board[6][3] = Pawn(6, 3, "w")
        self.board[6][4] = Pawn(6, 4, "w")
        self.board[6][5] = Pawn(6, 5, "w")
        self.board[6][6] = Pawn(6, 6, "w")
        self.board[6][7] = Pawn(6, 7, "w")


    def make_move(self,chess_coord,piece):
        row = chess_coord[0]
        col = chess_coord[1]
        # print("move cord  row",row," col ",col)
        if piece.king:
            piece.clastling = [False,False]
            if abs(col - piece.col) == 2:
                if piece.color == 'w':
                    l = 7
                else:
                    l = 0

                if col > piece.col:
                    p = self.board[l][7]
                    self.board[l][5] = p
                    self.board[l][7] = 0
                    p.row = l
                    p.col = 5
                else:
                    p = self.board[l][0]
                    self.board[l][3] = p
                    self.board[l][0] = 0
                    p.row = l
                    p.col = 3
        if piece.rook:
            if piece.row == 0 and piece.col == 0:
                self.board[0][4].clastling[1] = False
            if piece.row == 0 and piece.col == 7:
                self.board[0][4].clastling[0] = False
            if piece.row == 7 and piece.col == 0:
                self.board[7][4].clastling[1] = False
            if piece.row == 7 and piece.col == 7:
                self.board[7][4].clastling[0] = False
        self.board[row][col] = piece
        self.board[piece.row][piece.col] = 0
        piece.row = row
        piece.col = col
        if piece.pawn:
            if piece.color == "w":
                if piece.row == 0:
                    self.board[row][col] = Queen(row, col, "w")         
            else:
                if piece.row == 7:
                    self.board[row][col] = Queen(row, col, "b")

    def draw(self,move=[]):
        screen.blit(background,(0,0))
        chess_coord = (self.col,self.row)
        chess_coord = chess_to_pixel(chess_coord)
        if self.isselected:
            p = self.board[self.row][self.col]
            if p == 0 or p.color == self.turn:
                screen.blit(cell_selected,chess_coord)
            
        if move:
            for i in move:       
                if self.board[i[0]][i[1]] == 0:
                    screen.blit(green_circle,chess_to_pixel((i[1],i[0])))
                else:
                    screen.blit(yell,chess_to_pixel((i[1],i[0])))
        
        ischeck,king = self.is_check()
        if ischeck:
            screen.blit(red,chess_to_pixel((king[1],king[0])))

        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 0:
                    continue
                else:
                    pice = self.board[i][j]
                    pice.draw(screen)
        
    
    def danger_move(self,color):
        danger = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != 0:
                    if self.board[i][j].color != color and not self.board[i][j].king:
                        for move in self.board[i][j].update_move(self):
                            danger.append(move)
        
        return danger

    def is_check(self):
        king = (-1,-1)
        danger = self.danger_move(self.turn)
        for i in range(8):
            for j in range(8):
                if self.board[i][j] !=0:
                    if self.board[i][j].king and self.board[i][j].color == self.turn:
                        king = (i,j)
        
        if king in danger:
            self.check = True
            return True,king
        
        self.check = False
        return False,king

    def opp_color(self):
        if self.turn == 'w':
            return 'b'
        return 'w'
    
