import pygame
from board import Board
from board import pixel_to_chess
from board import chess_to_pixel


gameEnded = False
board = Board()
while not gameEnded:
    danger = []
    move = []
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT: 
            gameEnded = True
            break

        if event.type ==  pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            # print("poss",pos)
            chess_coord = pixel_to_chess(pos)
            if board.col == chess_coord[1] and board.row == chess_coord[0] and board.isselected == True:
                board.row = -1
                board.col = -1
                board.isselected = False

            else:
                board.row = chess_coord[1]
                board.col = chess_coord[0]
                print(f"row {board.row}, col {board.col}")
                board.isselected = True        
        
        if board.isselected:
            piece = board.board[board.row][board.col]
            if piece == 0:
                move = []
            else:
                
                if board.turn == piece.color:
                    piece.selected = True
                    move = piece.update_move(board)
                    if piece.selected:
                        if event.type ==  pygame.MOUSEBUTTONDOWN:
                            pos1 = pygame.mouse.get_pos()
                            chess_coord1 = pixel_to_chess(pos1)
                            row = chess_coord1[1]
                            col = chess_coord1[0]
                            if (row,col) in move:
                                board.make_move((row,col),piece)
                                                    
                                if board.turn == "w":
                                    board.turn = "b"
                                else:
                                    board.turn = "w"                                        
                        else:
                            piece.selected = False
                else:
                    move = [] 
        
        board.draw(move)
        
    
    
        pygame.display.update()


pygame.quit() 
