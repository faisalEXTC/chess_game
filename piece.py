import pygame



b_bishop = pygame.image.load("img\\bb.png")
b_king = pygame.image.load("img\\bk.png")
b_knight = pygame.image.load("img\\bkn.png")
b_pawn = pygame.image.load("img\\bp.png")
b_queen = pygame.image.load("img\\bq.png")
b_rook = pygame.image.load("img\\br.png")

w_bishop = pygame.image.load("img\\wb.png")
w_king = pygame.image.load("img\\wk.png")
w_knight = pygame.image.load("img\\wkn.png")
w_pawn = pygame.image.load("img\\wp.png")
w_queen = pygame.image.load("img\\wq.png")
w_rook = pygame.image.load("img\\wr.png")
green_circle = pygame.image.load("img\\green_circle.png")
green_circle = pygame.transform.scale(green_circle, (80, 80))

b = [b_bishop, b_king, b_knight, b_pawn, b_queen, b_rook]
w = [w_bishop, w_king, w_knight, w_pawn, w_queen, w_rook]

B = []
W = []

for img in b:
    B.append(pygame.transform.scale(img, (80, 80)))

for img in w:
    W.append(pygame.transform.scale(img, (80, 80)))



class Piece:
    img = -1
    def __init__(self,row,col,color):
        self.row = row
        self.col = col
        self.color = color
        self.move_list = []
        self.selected = False
        self.rook = False
        self.king = False
        self.pawn = False
        

    def isSelected(self):
        return self.selected

    def update_move(self,board):
        self.move_list =  self.move(board)
        return self.move_list

    def get_color(self):
        return self.color

    def get_pos(self):
        return (self.row,self.col)

    def draw(self,screen):
        if self.color == 'w':
            draws = W[self.img]
        else:
            draws = B[self.img]

        x = self.row * 80
        y = self.col * 80
        screen.blit(draws,(y,x))


class King(Piece):
    img = 1

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.king = True
        self.clastling = [True,True]

    def move(self,board):
        row = self.row
        col = self.col
        moves = []
        f = []
        try:
            #up
            if row > 0:
                p = board.board[row -1][col]
                if p == 0:
                    moves.append((row -1,col))
                elif p.color !=self.color:
                    moves.append((row -1,col))

            #down
            if row < 7:
                p = board.board[row + 1][col]
                if p == 0:
                    moves.append((row + 1,col))
                elif p.color != self.color:
                    moves.append((row + 1,col))
            
            #left
            if col > 0:
                p = board.board[row][col - 1]
                if p == 0:
                    moves.append((row,col - 1))
                elif p.color != self.color:
                    moves.append((row,col - 1))
            
            #right
            if col < 7:
                p = board.board[row][col + 1]
                if p == 0:
                    moves.append((row,col + 1))
                elif p.color != self.color:
                    moves.append((row,col + 1))
            
            #cross
            if row > 0 and col > 0:
                p = board.board[row - 1][col - 1]
                if p == 0:
                    moves.append((row - 1,col - 1))
                elif p.color != self.color:
                    moves.append((row - 1,col - 1))
            
            if row > 0 and col < 7:
                p = board.board[row -1][col +1] 
                if p == 0:
                    moves.append((row -1,col +1))
                elif p.color != self.color:
                    moves.append((row -1,col +1))

            if row < 7 and col > 0:

                p = board.board[row + 1][col -1]
                if p == 0:
                    moves.append((row + 1,col -1))
                elif p.color != self.color:
                    moves.append((row + 1,col -1))
            
            if row < 7 and col < 7:
                p = board.board[row + 1][col + 1]
                if p == 0:
                    moves.append((row + 1,col + 1))
                elif p.color != self.color:
                    moves.append((row + 1,col + 1))
            
            danger = board.danger_move(self.color)
            check,k = board.is_check()
            
            for i in moves:
                if i not in danger:
                    f.append(i)
            if self.clastling[0]:
                print("in")
                if board.board[row][col+1] == 0 and board.board[row][col+2] == 0 and not check and board.board[row][7] != 0 and (row,col+1) not in danger and (row,col+1) not in danger:
                    print("in1")
                    f.append((row,col+2))
            #queen side
            if self.clastling[1]:
                if board.board[row][col-1] == 0 and board.board[row][col-2] == 0 and board.board[row][col-3] == 0 and not check and board.board[row][0] != 0 and (row,col-1) not in danger and (row,col-2) not in danger:
                    f.append((row,col-2))

        except:
            pass
       

        return f
    

    



class Queen(Piece):
    img = 4

    def move(self,board):
        row = self.row
        col = self.col
        moves = []

        try:
            #UP
            for x in range(row-1,-1,-1):
                p = board.board[x][col]
                if p == 0:
                    moves.append((x,col))
                elif p.color != self.color:
                    moves.append((x,col))
                    break
                else:
                    break
                
            
            #DOWN
            for x in range(row+1,8,1):      
                p = board.board[x][col]
                if p == 0:
                    moves.append((x,col))
                elif p.color != self.color:
                    moves.append((x,col))
                    break
                else:
                    break
               
            
            #LEFT
            for y in range(col-1,-1,-1):
                p = board.board[row][y]
                if p == 0:
                    moves.append((row,y))
                elif p.color != self.color:
                    moves.append((row,y))
                    break
                else:
                    break

            #RIGHT
            for y in range(col+1,8,1):
                p = board.board[row][y]
                if p == 0:
                    moves.append((row,y))
                elif p.color != self.color:
                    moves.append((row,y))
                    break
                else:
                    break
            
            #top_rigth
            if row > 0:
                j = col
                for i in range(row-1,-1,-1):
                    j += 1
                    if j < 8:
                        p = board.board[i][j]
                        if p == 0:
                            moves.append((i,j))
                        elif p.color != self.color:
                            moves.append((i,j))
                            break
                        else:
                            break
                        
                    else:
                        break
            #top_left
            if row > 0:
                j = col
                for i in range(row-1,-1,-1):
                    j -= 1
                    if j > -1:
                        p = board.board[i][j]
                        if p == 0:
                            moves.append((i,j))
                        elif p.color != self.color:
                            moves.append((i,j))
                            break
                        else:
                            break
                        
                    else:
                        break
            #bottom_right
            if row < 8:
                j = col
                for i in range(row+1,8,1):
                    j += 1
                    if j < 8:
                        p = board.board[i][j]
                        if p == 0:
                            moves.append((i,j))
                        elif p.color != self.color:
                            moves.append((i,j))
                            break
                        else:
                            break
                    else:
                        break
            #bottom_left
            if row < 8:
                j = col
                for i in range(row+1,8,1):
                    j -= 1
                    if j > -1:
                        p = board.board[i][j]
                        if p == 0:
                            moves.append((i,j))
                        elif p.color != self.color:
                            moves.append((i,j))
                            break
                        else:
                            break
                    else:
                        break
        except:
            pass
        
        
        return moves
class Bishop(Piece):
    img = 0

    def move(self,board):
        row = self.row
        col = self.col
        moves = []
        try:
            #top_right
            if row > 0:
                j = col
                for i in range(row-1,-1,-1):
                    j += 1
                    if j < 8:
                        p = board.board[i][j]
                        if p == 0:
                            moves.append((i,j))
                        elif p.color != self.color:
                            moves.append((i,j))
                            break
                        else:
                            break
                        
                    else:
                        break
            #top_left
            if row > 0:
                j = col
                for i in range(row-1,-1,-1):
                    j -= 1
                    if j > -1:
                        p = board.board[i][j]
                        if p == 0:
                            moves.append((i,j))
                        elif p.color != self.color:
                            moves.append((i,j))
                            break
                        else:
                            break
                        
                    else:
                        break
            #bottom_right
            if row < 8:
                j = col
                for i in range(row+1,8,1):
                    j += 1
                    if j < 8:
                        p = board.board[i][j]
                        if p == 0:
                            moves.append((i,j))
                        elif p.color != self.color:
                            moves.append((i,j))
                            break
                        else:
                            break
                    else:
                        break
            #bottom_left
            if row < 8:
                j = col
                for i in range(row+1,8,1):
                    j -= 1
                    if j > -1:
                        p = board.board[i][j]
                        if p == 0:
                            moves.append((i,j))
                        elif p.color != self.color:
                            moves.append((i,j))
                            break
                        else:
                            break
                    else:
                        break
        except:
            pass
        
        
        return moves

class Knight(Piece):
    img = 2

    def move(self,board):
        row = self.row
        col = self.col
        moves = []

        try:
            #top_right
            if row > 1 and col < 7:
                p = board.board[row - 2][col + 1]
                if p == 0:
                    if row - 2 >= 0 and row - 2 < 8 and col + 1 >= 0 and col + 1 < 8:
                        moves.append((row - 2,col + 1))
                elif p.color != self.color:
                    if row - 2 >= 0 and row - 2 < 8 and col + 1 >= 0 and col + 1 < 8:
                        moves.append((row - 2,col + 1))

            if row > 0 and col < 6:
                p = board.board[row - 1][col + 2]
                if p == 0:
                    if row - 1 >= 0 and row - 1 < 8 and col + 2 >= 0 and col + 2 < 8:
                        moves.append((row - 1,col + 2))
                elif p.color != self.color:
                    if row - 1 >= 0 and row - 1 < 8 and col + 2 >= 0 and col + 2 < 8:
                        moves.append((row - 1,col + 2))
            #top_left
            if row > 1 and col > 0:
                
                p = board.board[row - 2][col - 1]
                if p == 0:
                    if row - 2 >= 0 and row - 2 < 8 and col - 1 >= 0 and col - 1 < 8:
                        moves.append((row - 2,col - 1))
                elif p.color != self.color:
                    if row - 2 >= 0 and row - 2 < 8 and col - 1 >= 0 and col - 1 < 8:
                        moves.append((row - 2,col - 1))
            
            if row > 0 and col > 1:
                p = board.board[row - 1][col - 2]
                if p == 0:
                    if row - 1 >= 0 and row - 1 < 8 and col - 2 >= 0 and col - 2 < 8:
                        moves.append((row - 1,col - 2))
                elif p.color != self.color:
                    if row - 1 >= 0 and row - 1 < 8 and col - 2 >= 0 and col - 2 < 8:
                        moves.append((row - 1,col - 2))

            #bottom_right
            if row < 6 and col < 7:
                
                p = board.board[row + 2][col + 1]
                if p == 0:
                    if row + 2 >= 0 and row + 2 < 8 and col + 1 >= 0 and col + 1 < 8:
                        moves.append((row + 2,col + 1))
                elif p.color != self.color:
                    if row + 2 >= 0 and row + 2 < 8 and col + 1 >= 0 and col + 1 < 8:
                        moves.append((row + 2,col + 1))
            
            if row < 7 and col < 6:
                
                p = board.board[row + 1][col + 2]
                if p == 0:
                    if row + 1 >= 0 and row + 1 < 8 and col + 2 >= 0 and col + 2 < 8:
                        moves.append((row + 1,col + 2))
                elif p.color != self.color:
                    if row + 1 >= 0 and row + 1 < 8 and col + 2 >= 0 and col + 2 < 8:
                        moves.append((row + 1,col + 2))
            
            #bottom_left
            if row < 6 and col > 0:
                p = board.board[row + 2][col - 1]
                if p == 0:
                    if row + 2 >= 0 and row + 2 < 8 and col - 1 >= 0 and col - 1 < 8:
                        moves.append((row + 2,col - 1))
                elif p.color != self.color:
                    if row + 2 >= 0 and row + 2 < 8 and col - 1 >= 0 and col - 1 < 8:
                        moves.append((row + 2,col - 1))
            
            if row < 7 and col > 1:
                
                p = board.board[row + 1 ][col - 2]
                if p == 0:
                    if row + 1  >= 0 and row + 1  < 8 and col - 2 >= 0 and col - 2 < 8:
                        moves.append((row + 1 ,col - 2))
                elif p.color != self.color:
                    if row + 1  >= 0 and row + 1  < 8 and col - 2 >= 0 and col - 2 < 8:
                        moves.append((row + 1 ,col - 2))
        except:
            pass
        
        
        return moves

class Rook(Piece):
    img = 5
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.rook = True
        
    def move(self,board):
        row = self.row
        col = self.col
        moves = []
        try:
            #UP
            for x in range(row-1,-1,-1):
                p = board.board[x][col]
                if p == 0:
                    moves.append((x,col))
                elif p.color != self.color:
                    moves.append((x,col))
                    break
                else:
                    break
            
            #DOWN
            for x in range(row+1,8,1):
                p = board.board[x][col]
                if p == 0:
                    moves.append((x,col))
                elif p.color != self.color:
                    moves.append((x,col))
                    break
                else:
                    break
            
            #LEFT
            for y in range(col-1,-1,-1):
                p = board.board[row][y]
                if p == 0:
                    moves.append((row,y))
                elif p.color != self.color:
                    moves.append((row,y))
                    break
                else:
                    break

            #RIGHT
            for y in range(col+1,8,1):
                p = board.board[row][y]
                if p == 0:
                    moves.append((row,y))
                elif p.color != self.color:
                    moves.append((row,y))
                    break
                else:
                    break

        except:
            pass        

        
        return moves

class Pawn(Piece):
    img = 3
    
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.pawn = True
        self.isfirst = True
        
    
    def move(self,board):
        row = self.row
        col = self.col
        moves = []
      
        
        try:
            
            if self.color == "w":
                if row == 6:
                    self.isfirst = True
                else:
                    self.isfirst = False

                if self.isfirst == True:
                    
                  
                    p = board.board[row -2][col]
                    if  p == 0:
                        moves.append((row -2, col))
                
                #up
                
                p = board.board[row -1][col]
                if p == 0:
                    moves.append((row -1,col))

                #cross
                 
                p = board.board[row -1][col -1]
                if p != 0:
                    if  p.color != self.color:
                        moves.append((row -1,col -1))
                 
                p = board.board[row -1][col +1] 
                if p != 0:
                    if p.color != self.color:
                        moves.append((row -1,j))
            else:
                if row == 1:
                    self.isfirst = True
                else:
                    self.isfirst = False

                if self.isfirst == True:
                    p = board.board[row +2][col]
                    if p == 0:
                        moves.append((row +2, col))
                
                p = board.board[row + 1][col]
                if p == 0:
                    moves.append((row + 1,col))

                #cross
                
                p = board.board[row + 1][col -1]
                if  p != 0:
                    if  p.color != self.color:
                        moves.append((row + 1,col -1))
                
                p = board.board[row + 1][col + 1]
                if p != 0:
                    if p.color != self.color:
                        moves.append((row + 1,col + 1))

        except:
            pass

        return moves 
