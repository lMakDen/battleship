import pygame
import time
import math
from random import randint
from  random import choice 
#from msilib import Directory
pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0, 200, 0)
blue = (0,148,255)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
block_color = (53, 155, 255)
bright_grey = (192,192,192)
grey = (128,128,128)
yellow = (255,216,0)
bright_yellow = (255,233,127)

gameDisplay = pygame.display.set_mode((display_width,display_height))#Создаем игровое окно
battleshipImg = pygame.image.load('1.png')
background = pygame.image.load('fon.png')
background2 = pygame.image.load('fon2.png')
background3 = pygame.image.load('fon3.png')
background4 = pygame.image.load('fon4.png')
background5 = pygame.image.load('fon5.png')
background6 = pygame.image.load('fon6.png')
background7 = pygame.image.load('fon7.png')
background8 = pygame.image.load('fon8.png')
background9 = pygame.image.load('fon9.png')
background10 = pygame.image.load('fon10.png')
background11 = pygame.image.load('fon11.png')
background12 = pygame.image.load('fon12.png')
Single_Ship = pygame.image.load('Singl_Ship1.png')
composition = pygame.image.load('sostav.png')
kill = pygame.image.load('kill.png')
mimo = pygame.image.load('mimo.png')
clock = pygame.time.Clock()
pause = False


                
            
def kill_ship(board,wounded):# Функция которая определяет убили мы корабль или ранили, если убили то меняет все поля корабля на "K"
    quantity_wounded = 0
    for element in board:
        if element[0] =="R":
            quantity_wounded +=1
    if quantity_wounded == int(wounded):
        for element in board:
            if element[0] =="R":
                element[0] = "K"             
    
        
def ship_killing(board):
    index = 0
    for element in board:
        
        if element[0] == "K":
            if index == 0:#расматриваем вариант, если убитый корабль наъодится в 1 строке нашего поля{
                if board[index+1][0] =="O" or board[index+1][0]=="M":
                    battleship(board[index+1][1][0][0],board[index+1][1][1][0],mimo)
                    board[index+1][0] = "M"
                if board[index+10][0] =="O" or board[index+10][0]=="M":
                    battleship(board[index+10][1][0][0],board[index+10][1][1][0],mimo) 
                    board[index+10][0] = "M"
                if board[index+11][0] =="O" or board[index+11][0]=="M":
                    battleship(board[index+11][1][0][0],board[index+11][1][1][0],mimo)
                    board[index+11][0] = "M"
            if index > 0 and index < 9:
                if board[index-1][0] =="O" or board[index-1][0]=="M":
                    battleship(board[index-1][1][0][0],board[index-1][1][1][0],mimo)
                    board[index-1][0] = "M" 
                if board[index+1][0] =="O" or board[index+1][0]=="M":
                    battleship(board[index+1][1][0][0],board[index+1][1][1][0],mimo)
                    board[index+1][0] = "M"
                if board[index+9][0] =="O" or board[index+9][0]=="M":
                    battleship(board[index+9][1][0][0],board[index+9][1][1][0],mimo)
                    board[index+9][0] = "M"
                if board[index+10][0] =="O" or board[index+10][0]=="M":
                    battleship(board[index+10][1][0][0],board[index+10][1][1][0],mimo) 
                    board[index+10][0] = "M"
                if board[index+11][0] =="O" or board[index+11][0]=="M":
                    battleship(board[index+11][1][0][0],board[index+11][1][1][0],mimo)
                    board[index+11][0] = "M"
            if index == 9:
                if board[index-1][0] =="O" or board[index-1][0]=="M":
                    battleship(board[index-1][1][0][0],board[index-1][1][1][0],mimo)
                    board[index-1][0] = "M"
                if board[index+9][0] =="O" or board[index+9][0]=="M":
                    battleship(board[index+9][1][0][0],board[index+9][1][1][0],mimo)
                    board[index+9][0] = "M"
                if board[index+10][0] =="O" or board[index+10][0]=="M":
                    battleship(board[index+10][1][0][0],board[index+10][1][1][0],mimo) 
                    board[index+10][0] = "M"#расматриваем вариант, если убитый корабль наъодится в 1 строке нашего поля}
            if index == 90:
                if board[index-10][0] =="O" or board[index-10][0]=="M":
                    battleship(board[index-10][1][0][0],board[index-10][1][1][0],mimo)
                    board[index-10][0] = "M"
                if board[index-9][0] =="O" or board[index-9][0]=="M":
                    battleship(board[index-9][1][0][0],board[index-9][1][1][0],mimo)
                    board[index-9][0] = "M"
                if board[index+1][0] =="O" or board[index+1][0]=="M":
                    battleship(board[index+1][1][0][0],board[index+1][1][1][0],mimo)
                    board[index+1][0] = "M"
            if index > 90 and index < 99:
                if board[index-10][0] =="O" or board[index-10][0]=="M":
                    battleship(board[index-10][1][0][0],board[index-10][1][1][0],mimo)
                    board[index-10][0] = "M"
                if board[index-9][0] =="O" or board[index-9][0]=="M":
                    battleship(board[index-9][1][0][0],board[index-9][1][1][0],mimo)
                    board[index-9][0] = "M"
                if board[index-11][0] =="O" or board[index-11][0]=="M":
                    battleship(board[index-11][1][0][0],board[index-11][1][1][0],mimo)
                    board[index-11][0] = "M"
                if board[index-1][0] =="O" or board[index-1][0]=="M":
                    battleship(board[index-1][1][0][0],board[index-1][1][1][0],mimo)
                    board[index-1][0] = "M"
                if board[index+1][0] =="O" or board[index+1][0]=="M":
                    battleship(board[index+1][1][0][0],board[index+1][1][1][0],mimo)
                    board[index+1][0] = "M"
            if index == 99:
                if board[index-11][0] =="O" or board[index-11][0]=="M":
                    battleship(board[index-11][1][0][0],board[index-11][1][1][0],mimo)
                    board[index-11][0] = "M"
                if board[index-10][0] =="O" or board[index-10][0]=="M":
                    battleship(board[index-10][1][0][0],board[index-10][1][1][0],mimo)
                    board[index-10][0] = "M"
                if board[index-1][0] =="O" or board[index-1][0]=="M":
                    battleship(board[index-1][1][0][0],board[index-1][1][1][0],mimo)
                    board[index-1][0] = "M"
                
                
                
            if index > 9 and index < 90:
                if int(str(index)[1]) == 0:
                    if board[index-9][0] =="O" or board[index-9][0]=="M":
                        battleship(board[index-9][1][0][0],board[index-9][1][1][0],mimo)
                        board[index-9][0] = "M"
                    if board[index-10][0] =="O" or board[index-10][0]=="M":
                        battleship(board[index-10][1][0][0],board[index-10][1][1][0],mimo)
                        board[index-10][0] = "M" 
                    if board[index+1][0] =="O" or board[index+1][0]=="M":
                        battleship(board[index+1][1][0][0],board[index+1][1][1][0],mimo)
                        board[index+1][0] = "M" 
                    if board[index+10][0] =="O" or board[index+10][0]=="M":
                        battleship(board[index+10][1][0][0],board[index+10][1][1][0],mimo) 
                        board[index+10][0] = "M"
                    if board[index+11][0] =="O" or board[index+11][0]=="M":
                        battleship(board[index+11][1][0][0],board[index+11][1][1][0],mimo)
                        board[index+11][0] = "M"
                
                if int(str(index)[1]) == 9:
                    if board[index-11][0] =="O" or board[index-11][0]=="M":
                        battleship(board[index-11][1][0][0],board[index-11][1][1][0],mimo)
                        board[index-11][0] = "M"
                    if board[index-10][0] =="O" or board[index-10][0]=="M":
                        battleship(board[index-10][1][0][0],board[index-10][1][1][0],mimo)
                        board[index-10][0] = "M"
                    if board[index-1][0] =="O" or board[index-1][0]=="M":
                        battleship(board[index-1][1][0][0],board[index-1][1][1][0],mimo)
                        board[index-1][0] = "M"
                    if board[index+9][0] =="O" or board[index+9][0]=="M":
                        battleship(board[index+9][1][0][0],board[index+9][1][1][0],mimo)
                        board[index+9][0] = "M"
                    if board[index+10][0] =="O" or board[index+10][0]=="M":
                        battleship(board[index+10][1][0][0],board[index+10][1][1][0],mimo) 
                        board[index+10][0] = "M"             
                
                if  int(str(index)[1]) > 0 and int(str(index)[1]) < 9: #выбираем часть нашего поля, которая не включает крайние строки
                    if board[index-10][0] =="O" or board[index-10][0]=="M":
                        battleship(board[index-10][1][0][0],board[index-10][1][1][0],mimo)
                        board[index-10][0] = "M"
                    if board[index-9][0] =="O" or board[index-9][0]=="M":
                        battleship(board[index-9][1][0][0],board[index-9][1][1][0],mimo)
                        board[index-9][0] = "M"
                    if board[index-11][0] =="O" or board[index-11][0]=="M":
                        battleship(board[index-11][1][0][0],board[index-11][1][1][0],mimo)
                        board[index-11][0] = "M"
                    if board[index+10][0] =="O" or board[index+10][0]=="M":
                        battleship(board[index+10][1][0][0],board[index+10][1][1][0],mimo) 
                        board[index+10][0] = "M"
                    if board[index+9][0] =="O" or board[index+9][0]=="M":
                        battleship(board[index+9][1][0][0],board[index+9][1][1][0],mimo)
                        board[index+9][0] = "M"
                    if board[index+11][0] =="O" or board[index+11][0]=="M":
                        battleship(board[index+11][1][0][0],board[index+11][1][1][0],mimo)
                        board[index+11][0] = "M"
                    if board[index-1][0] =="O" or board[index-1][0]=="M":
                        battleship(board[index-1][1][0][0],board[index-1][1][1][0],mimo)
                        board[index-1][0] = "M"
                    if board[index+1][0] =="O" or board[index+1][0]=="M":
                        battleship(board[index+1][1][0][0],board[index+1][1][1][0],mimo)
                        board[index+1][0] = "M"
        index += 1
def Have_wounded_ships(board):
    wounded_ships = False
    for element in board:
        if element[0] == "R":
            wounded_ships = True
    return wounded_ships
def location_of_the_wounded_ship(board,index):#Пока Не используется
    if index > 10 and index < 89:
        if  int(str(index)[1]) > 0 and int(str(index)[1]) < 9:
            if board[index-10][0] == "R" or board[index+10][0] == "R":
                return choice([index-10,index+10])
            elif board[index-1][0] == "R" or board[index+1][0] == "R":
                return choice([index-1,index+1])
            else:
                return choice([index-10,index+10,index-1,index+1])
                  
 
def if_I_wounded_ship(board):
    index = 0
    shot = -100000
    for element in board:
        if element[0] == "R":
            if index > 9 and index < 90:
                if  int(str(index)[1]) > 0 and int(str(index)[1]) < 9:
                    
                    if (board[index-10][0] == "2" or board[index-10][0] == "3" or board[index-10][0] == "4") or (board[index+10][0] == "2" or board[index+10][0] == "3" or board[index+10][0] == "4") or (board[index-1][0] == "2" or board[index-1][0] == "3" or board[index-1][0] == "4") or (board[index+1][0] == "2" or board[index+1][0] == "3" or board[index+1][0] == "4"):    
                        if board[index-10][0] == "R" or board[index+10][0] == "R":
                            shot = choice([index-10,index+10])
                            return shot 
                        elif board[index-1][0] == "R" or board[index+1][0] == "R":
                            shot = choice([index-1,index+1])
                            return shot 
                        else:
                            shot = choice([index-10,index+10,index-1,index+1])
                            return shot
                    else:
                        print("ahaha")
                
                elif int(str(index)[1]) == 0:
                    #if (board[index-10][0] != "M" and board[index-10][0] != "R") or (board[index+10][0] != "M" and board[index+10][0] != "R") or (board[index+1][0] != "M" and board[index+1][0] != "R"):
                    if (board[index-10][0] == "2" or board[index-10][0] == "3" or board[index-10][0] == "4") or (board[index+10][0] == "2" or board[index+10][0] == "3" or board[index+10][0] == "4") or (board[index+1][0] == "2" or board[index+1][0] == "3" or board[index+1][0] == "4"):
                        if board[index-10][0] == "R" or board[index+10][0] == "R":
                            shot = choice([index-10,index+10])
                            return shot
                        else:
                            shot = choice([index-10,index+10,index+1])
                            return shot
                    
                elif int(str(index)[1]) == 9:
                    
                    if (board[index-10][0] == "2" or board[index-10][0] == "3" or board[index-10][0] == "4") or (board[index+10][0] == "2" or board[index+10][0] == "3" or board[index+10][0] == "4") or (board[index-1][0] == "2" or board[index-1][0] == "3" or board[index-1][0] == "4"):
                        if board[index-10][0] == "R" or board[index+10][0] == "R":
                            shot = choice([index-10,index+10])
                            return shot
                        else:
                            shot = choice([index-10,index+10,index-1])
                            return shot
                else:
                    print("bygaga")
                    
                                                                     
            elif index > 0 and index < 9:
                
                if (board[index+10][0] == "2" or board[index+10][0] == "3" or board[index+10][0] == "4") or (board[index-1][0] == "2" or board[index-1][0] == "3" or board[index-1][0] == "4") or (board[index+1][0] == "2" or board[index+1][0] == "3" or board[index+1][0] == "4"):     
                    if board[index-1][0] == "R" or board[index+1][0] == "R":
                        shot = choice([index-1,index+1])
                        return shot
                    else:
                        shot = choice([index+10,index-1,index+1])
                        return shot
            elif index > 90 and index < 99:
                if (board[index-10][0] == "2" or board[index-10][0] == "3" or board[index-10][0] == "4") or (board[index-1][0] == "2" or board[index-1][0] == "3" or board[index-1][0] == "4") or (board[index+1][0] == "2" or board[index+1][0] == "3" or board[index+1][0] == "4"):
                
                    if board[index-1][0] == "R" or board[index+1][0] == "R":
                        shot = choice([index-1,index+1])
                        return shot
                    else:    
                        shot = choice([index-10,index-1,index+1])
                        return shot
            elif index == 0:
                if (board[index+10][0] == "2" or board[index+10][0] == "3" or board[index+10][0] == "4") or (board[index+1][0] == "2" or board[index+1][0] == "3" or board[index+1][0] == "4"):
                
                    shot = choice([index+10,index+1])
                    return shot
            elif index == 9:
                if (board[index+10][0] == "2" or board[index+10][0] == "3" or board[index+10][0] == "4") or (board[index-1][0] == "2" or board[index-1][0] == "3" or board[index-1][0] == "4"):
               
                    shot = choice([index+10,index-1])
                    return shot
            elif index == 90:
                if (board[index-10][0] == "2" or board[index-10][0] == "3" or board[index-10][0] == "4") or (board[index+1][0] == "2" or board[index+1][0] == "3" or board[index+1][0] == "4"):
                
                    shot = choice([index-10,index+1])
                    return shot
            elif index == 99:
                if (board[index-10][0] == "2" or board[index-10][0] == "3" or board[index-10][0] == "4") or (board[index-1][0] == "2" or board[index-1][0] == "3" or board[index-1][0] == "4"):
                
                    shot = choice([index-10,index-1])
                    return shot
            else:
                print("GG")                                             
                    
    
        index +=1           
    if shot == -100000:
        print("ZASHOL!")
        return randint(0,99)
        
    return shot
            
        
"""Золотухин_2016_07_20{Рисует указанную картинку по указанным координатам"""
def battleship(x,y,image): 
        gameDisplay.blit(image, (x,y))# blit - нарисовать одну картинку на другую
"""Золотухин_2016_07_20}"""
def Computer_shot(board,wounded,The_enemy_Field):
    live_decks = []
    Great_shot = False
    wounded_ship = False #переменная, которая говорит о том, что с прошлого хода остался раненный корабль и нужно его добить
    while Great_shot == False:
                      
        if not Have_wounded_ships(board):
            shot = randint(0,99)
        else:
            shot = int(if_I_wounded_ship(board))
            
        
        if board[shot][0] == "O":# 1 раз ругнулось
            
            battleship(board[shot][1][0][0],board[shot][1][1][0],mimo)
            board[shot][0] = "M"
            Great_shot = True
            time.sleep(0.5)
        if board[shot][0] == "1":
            board[shot][0] = "K"
            ship_killing(board)
            battleship(board[shot][1][0][0],board[shot][1][1][0],kill)
            time.sleep(0.5)
        if board[shot][0] == "2":
            battleship(board[shot][1][0][0],board[shot][1][1][0],kill)
            board[shot][0] = "R"
            wounded = "2"
            kill_ship(board,wounded)
            ship_killing(board)
            time.sleep(0.5)
            
        if board[shot][0] == "3":
            battleship(board[shot][1][0][0],board[shot][1][1][0],kill)
            board[shot][0] = "R"
            wounded ="3"
            kill_ship(board,wounded)
            ship_killing(board)
            time.sleep(0.5)
        if board[shot][0] == "4":
            battleship(board[shot][1][0][0],board[shot][1][1][0],kill)
            board[shot][0] = "R"
            wounded ="4"
            kill_ship(board,wounded)
            ship_killing(board)
            time.sleep(0.5)
        for element in board:#Проверка, есть ли еще живые корабли
            if element[0] == "1" or element[0] =="2" or element[0] =="3" or element[0] =="4":
                live_decks.append(element)
        if len(live_decks) == 0:
            for enemy in The_enemy_Field:
                if enemy[0] == "1" or enemy[0] =="2" or enemy[0] =="3" or enemy[0] =="4":
                    battleship(enemy[1][0][0],enemy[1][1][0],Single_Ship)                    
                                                          
            win_or_lose("lose")
        live_decks = []
                        
        pygame.display.update()
    return wounded
"""Золотухин_2016_08_06{Функция, которая выставляет 3-х палубный корабль на растоянии 1 клетки от существующих кораблей"""
def deck_3(board, decks):
    good_position_for_ship = False
    
    while good_position_for_ship == False:
        side = ["up","left"]       
        direction = choice(side)
        index_vreated_ships = []
        index = 0
        bad_cell = 0
                                   
        for ship in board:#проверяем сначало 3 верхних горизонтальных клетки дальше переходим на нижние и так 5 раз
            if ship[0] == "1" or ship[0] =="2" or ship[0] == "3" or ship[0] == "4":
                index_vreated_ships.append(index - 11)
                index_vreated_ships.append(index - 10)
                index_vreated_ships.append(index - 9)
                index_vreated_ships.append(index -1)
                index_vreated_ships.append(index)
                index_vreated_ships.append(index + 1)
                index_vreated_ships.append(index + 9)
                index_vreated_ships.append(index + 10)
                index_vreated_ships.append(index + 11)
                good_position_for_ship = True
            index +=1
        if direction == "up":
            first_deck = randint(0,79)#поставил до 79, т.к палубы ставятся сверху вниз
            for index_element in index_vreated_ships:
                if decks == 3:
                    if index_element == first_deck or index_element == (first_deck + 20):
                        good_position_for_ship = False
                if decks == 2:
                    if index_element == first_deck or index_element == (first_deck + 10):
                        good_position_for_ship = False
                if decks == 1:
                    if index_element == first_deck:
                        good_position_for_ship = False
                    
        else:
            first_deck = int(str(randint(0,9)) + str(randint(0,7))) 
            for index_element in index_vreated_ships:
                if decks == 3:
                    if index_element == first_deck or index_element == (first_deck + 2):
                        good_position_for_ship = False
                if decks == 2:
                    if index_element == first_deck or index_element == (first_deck + 1):
                        good_position_for_ship = False
                if decks == 1:
                    if index_element == first_deck:
                        good_position_for_ship = False
                        
        if good_position_for_ship:
            if direction == "up":
                for ship in board:
                    if decks == 3:
                        if ship[1][0][0]== board[first_deck][1][0][0] and ship[1][1][0]== board[first_deck][1][1][0]:
                            ship[0]= "3"# 1 палуба
                        if ship[1][0][0]== board[first_deck][1][0][0] and ship[1][1][0]== board[first_deck][1][1][0] + 20:
                            ship[0]= "3"# 2 палуба
                        if ship[1][0][0]== board[first_deck][1][0][0] and ship[1][1][0]== board[first_deck][1][1][0] + 20 * 2:
                            ship[0]= "3"# 3 палуба
                    if decks == 2:
                        if ship[1][0][0]== board[first_deck][1][0][0] and ship[1][1][0]== board[first_deck][1][1][0]:
                            ship[0]= "2"# 1 палуба
                        if ship[1][0][0]== board[first_deck][1][0][0] and ship[1][1][0]== board[first_deck][1][1][0] + 20:
                            ship[0]= "2"# 2 палуба
                    if decks == 1:
                        if ship[1][0][0]== board[first_deck][1][0][0] and ship[1][1][0]== board[first_deck][1][1][0]:
                            ship[0]= "1"# 1 палуба            
                        
            else:
                for ship in board:
                    if decks == 3:
                        if ship[1][0][0]== board[first_deck][1][0][0] and ship[1][1][0]== board[first_deck][1][1][0]:
                            ship[0]= "3"# 1 палуба
                        if ship[1][0][0]== board[first_deck][1][0][0] + 20 and ship[1][1][0]== board[first_deck][1][1][0]:
                            ship[0]= "3"# 2 палуба
                        if ship[1][0][0]== board[first_deck][1][0][0] + 20 * 2 and ship[1][1][0]== board[first_deck][1][1][0]:
                            ship[0]= "3"# 3 палуба
                    if decks == 2:
                        if ship[1][0][0]== board[first_deck][1][0][0] and ship[1][1][0]== board[first_deck][1][1][0]:
                            ship[0]= "2"# 1 палуба
                        if ship[1][0][0]== board[first_deck][1][0][0] + 20 and ship[1][1][0]== board[first_deck][1][1][0]:
                            ship[0]= "2"# 2 палуба
                    if decks == 1:
                        if ship[1][0][0]== board[first_deck][1][0][0] and ship[1][1][0]== board[first_deck][1][1][0]:
                            ship[0]= "1"# 1 палуба
                
        
    return board
"""Золотухин_2016_08_06{"""                    
           

'''Золотухин_2016_08_03{Функция, которая выставляет 4-х палубный корабль'''
def deck_4(board):#Корабль строится сверху вниз и слева направо, сначало ставится 1 палуба, потом проверка на возможность установки 4 палубы, если можно то ставится 4 палуба и между ними еще 2 ставим.
    good_position_for_ship = False
    while not good_position_for_ship:         
        first_deck = randint(0,99)
        side = ["up","left"]       
        direction = choice(side)
        if direction == 'up':
            for ship in board:
                
                if ship[1][1][0]== board[first_deck][1][1][0] + 20 * 3 and ship[1][0][0]== board[first_deck][1][0][0] and ship[0] == 'O': #Проверка, можно ли по єтим координатам ставить корабль
                    good_position_for_ship = True  
                    board[first_deck][0] = '4'#1 палуба
                    ship[0] = '4'#4 палуба
            if good_position_for_ship:
                for ship in board:                     
                    if ship[1][1][0]== board[first_deck][1][1][0] + 20 and ship[1][0][0]== board[first_deck][1][0][0]:
                        ship[0] = '4' # 3 палуба 
                    if ship[1][1][0]== board[first_deck][1][1][0] + (20 * 2) and ship[1][0][0]== board[first_deck][1][0][0]:
                        ship[0] = '4'   # 2 палуба 
        else:
            for ship in board:
                if ship[1][1][0]== board[first_deck][1][1][0] and ship[1][0][0]== board[first_deck][1][0][0] + 20 * 3 and ship[0] == 'O': 
                    good_position_for_ship = True  
                    board[first_deck][0] = '4'#1 палуба
                    ship[0] = '4'#4 палуба
                if good_position_for_ship:
                    for ship in board:                     
                        if ship[1][1][0]== board[first_deck][1][1][0] and ship[1][0][0]== board[first_deck][1][0][0] + 20 :
                            ship[0] = '4' # 3 палуба 
                        if ship[1][1][0]== board[first_deck][1][1][0]  and ship[1][0][0]== board[first_deck][1][0][0] + (20 * 2):
                            ship[0] = '4'   # 2 палуба
                    
                   
    return board    
'''Золотухин_2016_08_03 }'''
    
"""Золотухин_2016_07_20{Функция рисует игровое поле с координатами каждого єлемента поля, и если надо ставит однопалубный корабль"""
def print_board(x,y):
    board = []
    x1=x
    x2=x1+20
    y1=y    
    y2=y1+20 
    for element in range(100):                  
        board.append(["O",[[x1,x2],[y1,y2]]])
        x1+=20
        x2+=20
        if x2-x>200:
            x1=x
            x2=x1+20
            y1+=20    
            y2=y1+20 
            
    
    board = deck_4(board)
    board = deck_3(board,3)
    board = deck_3(board,3)
    board = deck_3(board,2)
    board = deck_3(board,2)
    board = deck_3(board,2)
    board = deck_3(board,1)
    board = deck_3(board,1)
    board = deck_3(board,1)
    board = deck_3(board,1)
        
    return board
"""Золотухин_2016_07_20}"""

"""Золотухин_2016_07_20{Функция выставления вертикальной и горизонтальной надписи игрового поля"""
def digital_coordinates(x,y):#Функция вывода вертикальной номерации клеток поля
        largeText = pygame.font.SysFont("comicsansms", 15)
        alphabetic_coordinates = ["a","b","c","d","e","f","g","h","i","j"]
                
        for element in alphabetic_coordinates:
            x+=20
            TextSurf, TextRect = text_objects(str(element), largeText, black)
            TextRect.center = ((x),(y))
            gameDisplay.blit(TextSurf, TextRect)        
                        
        digital_coordinates = []
        for element in range(10):
            digital_coordinates.append(element+1)
        x-=200
        
        
        for row in digital_coordinates:
            y+=20
                        
            TextSurf, TextRect = text_objects(str(row), largeText, black)
            TextRect.center = ((x),(y))
            gameDisplay.blit(TextSurf, TextRect)        
"""Золотухин_2016_07_20}"""            

"""Золотухин_2016_07_20{Функция, которая рисует игровое поле с надписями и если нужно кораблями """
def battlefield(x,y,build_a_ships):#рисуем игровое поле
    
    digital_coordinates(x-10,y-10)
    bield = print_board(x,y)
    for row in bield: # вся строка
        #if row[0] == "O":
        battleship(row[1][0][0],row[1][1][0],battleshipImg)
        if row[0] == "4" or row[0] == "3" or row[0] == "2" or row[0] == "1":
            if build_a_ships :
                battleship(row[1][0][0],row[1][1][0],Single_Ship)
        
    
    #pygame.display.update()        
    return bield 
    #clock.tick(60)#Скорость реакции клика мышки
"""Золотухин_2016_07_20}""" 
   
"""Золотухин_2016_07_20{Функция написания текста на игровом окне"""
def text_objects(text, font, color):# функция написания текста
    textSurface = font.render(text, True, color)# cоздание новой поверхности
    return textSurface, textSurface.get_rect()
"""Золотухин_2016_07_20}""" 

"""Золотухин_2016_07_20{Функция создания кнопки и ее действия в случае нажатия на нее"""
def button(msg, x, y, w, h, ic, ac, action = None): #функция кнопки
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    
    #print(mouse)
    if x + w > mouse[0] > x and y + h > mouse[1] > y: # Меняется яркость кнопки когда наводим мышкой
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()     
         
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText, black)
    textRect.center = (( x + (w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)
"""Золотухин_2016_07_20}""" 

"""Золотухин_2016_07_20{Функция закрытия игрового окна"""       
def quitgame():
    pygame.quit()
    quit()
"""Золотухин_2016_07_20}"""     

"""Золотухин_2016_07_20{Функция выхода с паузы""" 
def unpause():
    global pause
    pause = False
"""Золотухин_2016_07_20}"""     

"""Золотухин_2016_07_20{Функция паузы""" 
def paused():
    gameDisplay.fill(white)
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText, black)
    TextRect.center = ((display_width / 2),(display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue!", 150, 450, 100, 50, green, bright_green, unpause)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)
        
        pygame.display.update()
        clock.tick(15)
"""Золотухин_2016_07_20}"""        
"""Золотухин_2016_07_30{Функция попадания в корабль"""         
def win_or_lose(win_or_lose):
        
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("You "+win_or_lose, largeText,black)
    TextRect.center = ((display_width / 2),(display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)
        pygame.display.update()
        clock.tick(15)
"""Золотухин_2016_07_30}""" 
def quantity_life_ships(board,ship):
    quantity = 0
    for element in board:
        if element[0] == str(ship):
            quantity +=1
         
    return str(quantity)            
    


"""Золотухин_2016_07_20{Функция перед игрового окна""" 
def game_intro():# game_intro и game_loop - 2 основные функции, game_intro - функция меню, в ней расположены кнопки и т.д,game_loop - функция основной игры, запускается принажатии кнопки "Go" в основном меню
    intro = True
    fon = choice([background,background2,background3,background4,background5,background6,background7,background8,background9,background10,background11,background12])
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        gameDisplay.blit(fon, (0,0))
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("Battleship", largeText, blue)
        TextRect.center = ((display_width / 2),(display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)
        
        pygame.display.update()
        clock.tick(15)
"""Золотухин_2016_07_20}""" 
def composition(board):
    largeText = pygame.font.SysFont("comicsansms", 15)
    TextSurf, TextRect = text_objects("Линкор   -", largeText, red)
    TextRect.center = ((80),(250))
    gameDisplay.blit(TextSurf, TextRect)
    
    largeText = pygame.font.SysFont("comicsansms", 15)
    TextSurf, TextRect = text_objects("Крейсер", largeText, red)
    TextRect.center = ((80),(280))
    gameDisplay.blit(TextSurf, TextRect)
    
    largeText = pygame.font.SysFont("comicsansms", 15)
    TextSurf, TextRect = text_objects("Эсминец", largeText, red)
    TextRect.center = ((80),(310))
    gameDisplay.blit(TextSurf, TextRect)
    
    largeText = pygame.font.SysFont("comicsansms", 15)
    TextSurf, TextRect = text_objects("Катер", largeText, red)
    TextRect.center = ((80),(340))
    gameDisplay.blit(TextSurf, TextRect)
    
    largeText = pygame.font.SysFont("comicsansms", 15)
    TextSurf, TextRect = text_objects(quantity_life_ships(board,1), largeText, red)
    TextRect.center = ((130),(250))
    gameDisplay.blit(TextSurf, TextRect)
    
    
    
    
"""Золотухин_2016_07_20{Функция игрового окна"""
def game_loop():
    global pause
    
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    

    thingCount = 1

    dodged = 0
    

    gameExit = False
    fon = choice([background,background2,background3,background4,background5,background6,background7,background8,background9,background10,background11,background12]) 
    gameDisplay.fill(white)# Делаем белый фон игрового окна
    gameDisplay.blit(fon, (0,0))
    The_enemy_Field = battlefield(510,20,False) #Поле врага
            
    My_field = battlefield(70,20,True)  #Наше поле
       
    
    
    attempt = 0
    wounded = ""
    
    while not gameExit:# Распознаем мышку
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #if event.type == pygame.KEYDOWN:# Движение картинки
             #   if event.key == pygame.K_p:
              #      pause = True
               #     paused()
                                
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            button("Restart", 350, 450, 100, 50, yellow, bright_yellow, game_loop)
            #composition(My_field)
            
            live_decks = []
            
            if click[0] == 1 and The_enemy_Field[0][1][0][0] < mouse[0] and mouse[0] < The_enemy_Field[99][1][0][1] and The_enemy_Field[0][1][1][0] < mouse[1] and mouse[1] < The_enemy_Field[99][1][1][1]:
                
                for look_on_x in The_enemy_Field:
                    if look_on_x[1][0][0]< mouse[0] and mouse[0] < look_on_x[1][0][1]:
                        for look_on_y in look_on_x[1]:
                            
                            if look_on_y[0]< mouse[1] and mouse[1] < look_on_y[1]:
                                if look_on_x[0] == "1":
                                    battleship(look_on_x[1][0][0],look_on_y[0],kill)
                                    look_on_x[0] = "K"# убил или ранил
                                    ship_killing(The_enemy_Field)
                                    for element in The_enemy_Field:#Проверка, есть ли еще живые корабли
                                        if element[0] == "1" or element[0] =="2" or element[0] =="3" or element[0] =="4":
                                            live_decks.append(element)
                                    if len(live_decks) == 0:
                                        win_or_lose("win")
                                    live_decks = []
                                    
                                if look_on_x[0] == "4" or look_on_x[0] == "3" or look_on_x[0] == "2":
                                    print(look_on_y)
                                    battleship(look_on_x[1][0][0],look_on_y[0],kill)
                                    wounded = look_on_x[0]
                                    look_on_x[0] = "R"# убил или ранил
                                    kill_ship(The_enemy_Field,wounded)
                                    ship_killing(The_enemy_Field)
                                    
                                    
                                    for element in The_enemy_Field:#Проверка, есть ли еще живые корабли
                                        if element[0] == "1" or element[0] =="2" or element[0] =="3" or element[0] =="4":
                                            live_decks.append(element)
                                    if len(live_decks) == 0:
                                        win_or_lose("win")
                                    live_decks = []
                                elif look_on_x[0] =="O":
                                    look_on_x[0] = "M"
                                    battleship(look_on_x[1][0][0],look_on_y[0],mimo)
                                    wounded = Computer_shot(My_field,wounded,The_enemy_Field)
                                    #time.sleep(0.5)
                                elif look_on_x[0] =="M" or look_on_x[0] =="K": 
                                    print("Уже сюда стреляли")
                                   
                                                                     
                
        pygame.display.update()        
        
        clock.tick(60)
        
"""Золотухин_2016_07_20{"""

"""""""""""""""""""Действия игры"""""""""""""""""""""

pygame.display.set_caption("Battleship")# Название игрового окна
game_intro()

game_loop()        

pygame.quit() # Функция закрытия окна
quit()            
        