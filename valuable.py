import pygame

m_c=False
start_time=0
x=True
orange=(232,98,49)
dark_blue=(54, 48, 98)
light_blue=(77, 76, 125)
white=(245, 245, 245)
yellow=(249, 148, 23)
y=(249, 148, 23, 255)
w=(245, 245, 245, 255)

game_list=[[5,1,1,1,5],[2,0,0,0,0],[2,0,0,0,0],[2,0,0,0,0],[5,0,0,0,5]]

sq0=pygame.Rect(195,195,100,100)
sq1=pygame.Rect(195,300,100,100)
sq2=pygame.Rect(195,405,100,100)
sq3=pygame.Rect(300,195,100,100)
sq4=pygame.Rect(300,300,100,100)
sq5=pygame.Rect(300,405,100,100)
sq6=pygame.Rect(405,195,100,100)
sq7=pygame.Rect(405,300,100,100)
sq8=pygame.Rect(405,405,100,100)

sq9=pygame.Rect(90,195,100,100)
sq10=pygame.Rect(90,300,100,100)
sq11=pygame.Rect(90,405,100,100)

sq48=pygame.Rect(90,90,100,100)
sq12=pygame.Rect(195,90,100,100)
sq13=pygame.Rect(300,90,100,100)
sq14=pygame.Rect(405,90,100,100)
sq86=pygame.Rect(510,90,100,100)

sq15=pygame.Rect(510,195,100,100)
sq16=pygame.Rect(510,300,100,100)
sq17=pygame.Rect(510,405,100,100)

sq42=pygame.Rect(90,510,100,100)
sq18=pygame.Rect(195,510,100,100)
sq19=pygame.Rect(300,510,100,100)
sq20=pygame.Rect(405,510,100,100)
sq26=pygame.Rect(510,510,100,100)

list_sq=[[sq48,sq12,sq13,sq14,sq86],[sq9,sq0,sq3,sq6,sq15],[sq10,sq1,sq4,sq7,sq16],[sq11,sq2,sq5,sq8,sq17],[sq42,sq18,sq19,sq20,sq26]]

check_lis=[[1,4],[2,4],[3,4],[4,1],[4,2],[4,3]]

mute=pygame.image.load('noun-mute.png')
unmute=pygame.image.load('mute.png')

FONT_B='Pixeboy-z8XGD.ttf'

