import pygame 
import sys
from valuable import *
from functions import *

pygame.mixer.music.load('mainmusic.mp3')
move2 = pygame.mixer.Sound("move2.wav")
error = pygame.mixer.Sound("error.wav")
victory = pygame.mixer.Sound("win1.wav")

pygame.mixer.music.play(loops=50)

f_p=5
while f_p==5: 
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			pygame.quit()
			sys.exit()

		if colorbyclick(event)==w:
			pygame.mixer.Sound.play(move2)
			f_p=w
			s_p=y
			turn=True
			o_cli=1
			break
		elif colorbyclick(event)==y:
			pygame.mixer.Sound.play(move2)
			f_p=y
			s_p=w
			turn=False
			o_cli=2
			break

pygame.draw.rect(game_board,dark_blue,[0,0,700,700])
show()

if f_p==y:
	text_white=font1.render('Yellow turn',True,(240, 240, 240),dark_blue)
	game_board. blit(text_white, (268, 40))
elif f_p==w:
	text_yellow=font1.render('White turn        ',True,(240, 240, 240),dark_blue)
	game_board. blit(text_yellow, (268, 40))

while True:
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			pygame.mixer.music.stop() 
			pygame.quit()
			sys.exit()

		if event.type==pygame.MOUSEBUTTONUP:
			pos=pygame.mouse.get_pos()

			if pos[0]>350 and pos[0]<402 and pos[1]>625 and pos[1]<675:
				pygame.mixer.music.pause()
			if pos[0]>298 and pos[0]<348 and pos[1]>625 and pos[1]<675:
				pygame.mixer.music.unpause()

			for i in range(len(list_sq)):
				for j in range(len(list_sq[i])):
					if list_sq[i][j].collidepoint(pos):
						pos_player=[i,j]
						pos_c=list_sq[i][j][:2]

						if turn:
							if bool(game_list[i][j]):
								if game_list[i][j]==2 and o_cli==1:
									if [i,j] in check_lis:
										pass
										
									elif game_list[i][j+1]==1 and game_list[i][j+2]==1:
										pass

									elif game_list[i][j+1]==1 and game_list[i][j+2]==0:
										pygame.mixer.Sound.play(move2)

										o_cli=game_list[i][j]
										pos_o=pos_c
										pygame.draw.rect(game_board,light_blue,addhundred(pos_o))
										
										pos_c=list_sq[i][j+2][:2]
										game_list[i][j+2]=2
										printcircle(pos_c,game_board,w)
										
										game_list[i][j]=0

										if isvalid(game_list,2):
											o_cli=1
										else:
											turn=not turn

									elif game_list[i][j+1]==0:
										pygame.mixer.Sound.play(move2)

										o_cli=game_list[i][j]
										pos_o=pos_c
										pygame.draw.rect(game_board,light_blue,addhundred(pos_o))
										
										pos_c=list_sq[i][j+1][:2]
										game_list[i][j+1]=2
										printcircle(pos_c,game_board,w)
										
										game_list[i][j]=0
										
										if isvalid(game_list,2):
											o_cli=1
										else:
											turn=not turn



						elif not turn:
							if bool(game_list[i][j]):
								if game_list[i][j]==1 and o_cli==2:
									if [i,j] in check_lis:
										pass

									elif game_list[i+1][j]==2 and game_list[i+2][j]==2:
										pass
									
									elif game_list[i+1][j]==2 and game_list[i+2][j]==0:
										pygame.mixer.Sound.play(move2)

										o_cli=game_list[i][j]
										pos_o=pos_c
										pygame.draw.rect(game_board,light_blue,addhundred(pos_o))
										
										pos_c=list_sq[i+2][j][:2]
										game_list[i+2][j]=1
										printcircle(pos_c,game_board,y)
										
										game_list[i][j]=0

										if isvalid(game_list,1):
											o_cli=2
										else:
											turn=not turn

									elif game_list[i+1][j]==0:

										pygame.mixer.Sound.play(move2)

										o_cli=game_list[i][j]
										pos_o=pos_c
										pygame.draw.rect(game_board,light_blue,addhundred(pos_o))
										
										pos_c=list_sq[i+1][j][:2]
										game_list[i+1][j]=1
										printcircle(pos_c,game_board,y)
										
										game_list[i][j]=0
										
										if isvalid(game_list,1):
											o_cli=2
										else:
											turn=not turn

		if o_cli==1:
			text_white=font1.render('White turn        ',True,(240, 240, 240),dark_blue)
			game_board. blit(text_white, (268, 40))
		elif o_cli==2:
			text_yellow=font1.render('Yellow turn',True,(240, 240, 240),dark_blue)
			game_board. blit(text_yellow, (268, 40))

		if winner(game_list):
			pygame.mixer.music.stop()
			
			if x:
				pygame.mixer.Sound.play(victory)
				x=False
			
			pygame.draw.rect(game_board,orange,[0,225,700,250])
			pygame.draw.rect(game_board,dark_blue,[0,0,700,98])
			tyellow=font.render('        yellow is winner        ',True,(6, 5, 10),orange)
			twhite=font.render('        white is winner        ',True,(6, 5, 10),orange)
			if numwinner(game_list)==1:
				game_board.blit(tyellow,(120, 330))
			elif numwinner(game_list)==2:
				game_board.blit(twhite,(130, 330))

			o_cli="fake"
			m_c=True

			
	pygame.display.update()
	



	

	





			

			





		