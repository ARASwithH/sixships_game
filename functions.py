import pygame 
import sys
from valuable import *

def print_game_board(in_list):
	print(in_list[0])
	print(in_list[1])
	print(in_list[2])
	print(in_list[3])
	print(in_list[4])
	print()

def colorbyclick(event):
	if event.type==pygame.MOUSEBUTTONUP:
		pos=pygame.mouse.get_pos()
		coler=game_board.get_at((pos))
		return coler
	
pygame.mixer.init()
pygame.init() 
game_board=pygame.display.set_mode((700, 700)) 
programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)
pygame.display.set_caption('Six Ships!')
game_board.fill(dark_blue)
pygame.draw.rect(game_board,yellow,[400,250,100,100])
pygame.draw.rect(game_board,white,[200,250,100,100])
font=pygame.font.Font(FONT_B,50)
font1=pygame.font.Font(FONT_B,37)
tex1=font.render('Choose your color',True,(240, 240, 240))
game_board. blit(tex1, (168, 400))
pygame.display.update()

def show():
	for i in list_sq:
		for j in i:
			pygame.draw.rect(game_board,light_blue,j)
	pygame.draw.circle(game_board,yellow,[245,140],40)
	pygame.draw.circle(game_board,yellow,[350,140],40)
	pygame.draw.circle(game_board,yellow,[455,140],40)
	pygame.draw.circle(game_board,white,[140,245],40)
	pygame.draw.circle(game_board,white,[140,350],40)
	pygame.draw.circle(game_board,white,[140,455],40)

	pygame.draw.rect(game_board,dark_blue,(510,510,100,100))
	pygame.draw.rect(game_board,dark_blue,(90,90,100,100))
	pygame.draw.rect(game_board,dark_blue,(510,90,100,100))
	pygame.draw.rect(game_board,dark_blue,(90,510,100,100))

	game_board.blit(mute,(352,625))
	game_board.blit(unmute,(298,625))

def printcircle(pos,game_board,color):
    poss=[]
    for i in pos:
        i+=50
        poss.append(i)
    poss=tuple(poss)
    pygame.draw.circle(game_board,color,poss,40)

def addhundred(pos):
	hun=100
	pos.append(hun)
	pos.append(hun)

	return tuple(pos)

def winner(in_list):
	if in_list[4][2]==1 and in_list[4][3]==1 and in_list[4][1]==1:
		return True , 
	elif in_list[3][4]==2 and in_list[2][4]==2 and in_list[1][4]==2:
		return True
	else:
		return False
	
def numwinner(in_list):
    if in_list[4][2]==1 and in_list[4][3]==1 and in_list[4][1]==1:
        return 1
    elif in_list[3][4]==2 and in_list[2][4]==2 and in_list[1][4]==2:
        return 2
    else:
        return False
    
def isvalid(board,player):
	if player==2:
		if board[4][1]==1 and board[4][2]==1 and board[1][3]==2 and board[2][3]==2 and board[3][3]==2 and board[0][3]==1:
			return True
		elif board[4][1]==1 and board[4][3]==1 and board[1][2]==2 and board[2][2]==2 and board[3][2]==2 and board[0][2]==1:
			return True
		elif board[4][2]==1 and board[4][3]==1 and board[1][1]==2 and board[2][1]==2 and board[3][1]==2 and board[0][1]==1:
			return True
		
		elif board[4][1]==1 and board[4][2]==1 and board[1][3]==2 and board[2][3]==2 and board[3][3]==1:
			return False
		elif board[4][1]==1 and board[4][3]==1 and board[1][2]==2 and board[2][2]==2 and board[3][2]==1:
			return False
		elif board[4][2]==1 and board[4][3]==1 and board[1][1]==2 and board[2][1]==2 and board[3][1]==1:
			return False
		
		elif board[4][1]==1 and board[4][2]==1 and board[2][3]==2 and board[3][3]==2 and board[0][3]==1:
			return False
		elif board[4][1]==1 and board[4][3]==1 and board[2][2]==2 and board[3][2]==2 and board[0][2]==1:
			return False
		elif board[4][2]==1 and board[4][3]==1 and board[2][1]==2 and board[3][1]==2 and board[0][1]==1:
			return False
		


		elif board[4][1]==1 and board[4][2]==1 and board[2][3]==2 and board[3][3]==2 :
			return True
		elif board[4][1]==1 and board[4][3]==1 and board[2][2]==2 and board[3][2]==2 :
			return True
		elif board[4][2]==1 and board[4][3]==1 and board[2][1]==2 and board[3][1]==2 :
			return True
		
		elif board[4][1]==1 and board[4][2]==1 and board[1][3]==2 and board[2][3]==2 :
			return True
		elif board[4][1]==1 and board[4][3]==1 and board[1][2]==2 and board[2][2]==2 :
			return True
		elif board[4][2]==1 and board[4][3]==1 and board[1][1]==2 and board[2][1]==2 :
			return True
		
		else:
			return False
		
	elif player==1:

		if board[1][4]==2 and board[2][4]==2 and board[3][1]==1 and board[3][2]==1 and board[3][3]==1 and board[3][0]==2:
			return True
		elif board[1][4]==2 and board[3][4]==2 and board[2][1]==1 and board[2][2]==1 and board[2][3]==1 and board[2][0]==2:
			return True
		elif board[2][4]==2 and board[3][4]==2 and board[1][1]==1 and board[1][2]==1 and board[1][3]==1 and board[1][0]==2:
			return True
		
		elif board[1][4]==2 and board[2][4]==2 and board[3][1]==1 and board[3][2]==1 and board[3][3]==2:
			return False
		elif board[1][4]==2 and board[3][4]==2 and board[2][1]==1 and board[2][2]==1 and board[2][3]==2:
			return False
		elif board[2][4]==2 and board[3][4]==2 and board[1][1]==1 and board[1][2]==1 and board[1][3]==2:
			return False

		elif board[1][4]==2 and board[2][4]==2 and board[3][2]==1 and board[3][3]==1 and board[3][0]==2:
			return False
		elif board[1][4]==2 and board[3][4]==2 and board[2][2]==1 and board[2][3]==1 and board[2][0]==2:
			return False
		elif board[2][4]==2 and board[3][4]==2 and board[1][2]==1 and board[1][3]==1 and board[1][0]==2:
			return False
		
		

		elif board[1][4]==2 and board[2][4]==2 and board[3][2]==1 and board[3][3]==1 :
			return True
		elif board[1][4]==2 and board[3][4]==2 and board[2][2]==1 and board[2][3]==1 :
			return True
		elif board[2][4]==2 and board[3][4]==2 and board[1][2]==1 and board[1][3]==1 :
			return True
		
		elif board[1][4]==2 and board[2][4]==2 and board[3][1]==1 and board[3][2]==1 :
			return True
		elif board[1][4]==2 and board[3][4]==2 and board[2][1]==1 and board[2][2]==1 :
			return True
		elif board[2][4]==2 and board[3][4]==2 and board[1][1]==1 and board[1][2]==1 :
			return True
		
		else:
			return False
	
    
