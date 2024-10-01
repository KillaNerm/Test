import character 
import pygame
import sys
import log_db

pygame.init() #Ініціалізація пайгейм - це просто потрібно


#налаштування екрану
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('it is need') #Це заголовок для вікна - не думаю що він є обовязковим) 





# Кординати для таблиці
coordinate_x, coordinate_y = 0, 0
sql_connect = log_db.sqlite3.connect(log_db.LOG_DB)


# Основний цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                coordinate_x -= 1
                key_pressed = event.key
                action_description = "Moved left"
                insert_query = """INSERT INTO logs (key_pressed, coordinate_x, coordinate_y, action_description)
                              VALUES (?, ?, ?, ?);"""
                sql_connect.execute(insert_query, (key_pressed, coordinate_x, coordinate_y, action_description))
                sql_connect.commit()  
                print(1)      
        
        
            elif event.key == pygame.K_RIGHT:
                coordinate_x += 1
                key_pressed = event.key
                action_description = "Moved right"
        
        
            elif event.key == pygame.K_UP:
                coordinate_y += 1
                key_pressed = event.key
                action_description = "Moved up"
        
        
            elif event.key == pygame.K_DOWN:
                coordinate_y -= 1
                key_pressed = event.key
                action_description = "Moved down"
                
                
                    
            
            
        
    
    




# bob = character.Character("Bob")

# bob.get_stats()
