import pygame, sys
import random

# ------------------------------------
#               WINDOW
# ------------------------------------
# We define the game window :
pygame.init()
SIZE = (450, 800)
win = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Stranger Hangman")

#------------------------------------
#          COLORS AND FONTS
# ------------------------------------

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED_CHERRY = ( 167, 0, 30)
RED_LIGHTER = (193, 0, 35)
STRANGE_BROWN = (149, 81, 73)
BROWN_TO_ORANGE = (189, 115, 106)
BLACK_NOT_BLACK = (30, 15, 28)
BLACK_TO_RED = (80, 15, 28)
OTHER_BROWN = (175, 114, 73)

WORD_FONT = pygame.font.Font('Fonts/Pixeled.ttf', 12)
GUESS_FONT = pygame.font.Font('Fonts/Pixeled.ttf', 20)
BENGUIAT = pygame.font.Font("Fonts/Benguiat.ttf", 30)


# ------------------------------------
#               BUTTONS  
# ------------------------------------
def text_objects(text, font):
    # We create the style of the text button, then we return it and its size (in a rectangle)
    text_surface = font.render(text, True, WHITE)
    return text_surface, text_surface.get_rect()

def button(text, x, y, w, h, ic, ac, action=None):
    # ic is for inactive color, ac is for active color
    mouse = pygame.mouse.get_pos() # It gives us information about the mouse's position
    click = pygame.mouse.get_pressed() # It gives information about the number of click

    # When mouse hovers the button, active color change to inactive color
    # We use the mouse's position to know if the cursor is on the button or not
    if (x + w) > mouse[0] > x and (y + h) > mouse[1] > y:
        pygame.draw.rect(win, ac, (x, y, w, h))

        # If action isn't given in the parameters, click on the button won't do anything
        if click[0] == 1 and action != None:
            action()

    else:
        # Button with the inactive color : 
        pygame.draw.rect(win, ic, (x, y, w, h))

    text_surf, text_rect = text_objects(text, BENGUIAT)
    text_rect.center = ((x + (w/2)), (y + (h/2))) # To have the text in the middle of the button
    win.blit(text_surf, text_rect)


# ------------------------------------
#             NEW WORD
# ------------------------------------
def insert_word():
    running = True
    new_word = ''

    # input_rect is the invisble retcangle where the user can write his new word
    input_rect = pygame.Rect(125, 470, 200, 50)

    # Explantations for the user
    explanation_1 = "Enter your new word and press"
    explanation_2 = "Enter. It will be added"
    explanation_3 = "to the personalized list"
    
    while running:
        # We need to create the background here for the Backspace
        # Indeed, if we don't do it, the correction will appear on the previous character
        word_background = pygame.image.load("Pictures/score_background.png")
        win.blit(word_background, (0,0))

        # Title :
        title2 = pygame.image.load("Pictures/Title2.png")
        win.blit (title2, (100, 150))

        # Explanations : (As I want a center effect, I can't make a loop to display the explanations, the x depends on the lenght of the text)
        display_explanation_1 = WORD_FONT.render(explanation_1, False, WHITE)
        win.blit(display_explanation_1, (75, 370))
        display_explanation_2 = WORD_FONT.render(explanation_2, False, WHITE)
        win.blit(display_explanation_2, (115, 400))
        display_explanation_3 = WORD_FONT.render(explanation_3, False, WHITE)
        win.blit(display_explanation_3, (110, 430))
        
        # Input : 
        text_surface = WORD_FONT.render(new_word, False, WHITE)
        win.blit(text_surface, (225 - text_surface.get_width()/2, 475)) #To write in the middle of the rectangle
        pygame.draw.rect(win, RED_CHERRY, input_rect, 2)

        button("BACK TO MENU", 75, 700, 300, 50, RED_CHERRY, STRANGE_BROWN, main)

        pygame.display.flip()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    new_word = new_word[:-1]
                elif event.key == pygame.K_RETURN:
                    f = open('custom_list_words.txt', 'a') # a is for append, it will write the content at the end of the file
                    f.write("\n")
                    f.write(new_word.lower()) # New word is written in lowercase
                    f.close()
                    new_word = 'Word added !'
                else:
                    new_word += event.unicode # To write with the keyboard


# ------------------------------------
#         CHOICE GAME LEVEL
# ------------------------------------    
def choice_level():
    running = True
     
    # name is the variable where the user enters his name. Saved name is the one which be used 
    # as parameters to call the game functions
    name = ''
    saved_name = ''
    explanation_1 = "Enter your name and press"
    explanation_2 = "Enter, then chose a level"
    input_name = pygame.Rect(75, 130, 300, 50)

    # We use this variables as parameter for the game functions
    easy = "easy"
    hard = "hard"
    custom = "custom"

    actual_score = 0 # This value will change with the function question(), when the player enter his name

    while running:
        # Background :
        # We need to create the background in the loop because of the key Backspace.
        game_background = pygame.image.load("Pictures/game_background.png")
        win.blit(game_background, (0,0))

        display_explanation_1 = WORD_FONT.render(explanation_1, False, WHITE)
        win.blit(display_explanation_1, (87, 50))
        display_explanation_2 = WORD_FONT.render(explanation_2, False, WHITE)
        win.blit(display_explanation_2, (98, 80))
         
        display_name = WORD_FONT.render(name, True, WHITE)
        win.blit(display_name, (220 - display_name.get_width() /2, 135))
        pygame.draw.rect(win, BLACK_TO_RED, input_name, 2)
        
        # I can't use the action parameter in the function "button", beacause of the parameters of the called function.
        # So we have to indicate the mouse position and if there is a click on a button. Then, depending on 
        # the position, we are redirected to the game, which has as parameter the difficulty chosen, the user's name and the actual score of the player
        mouse = pygame.mouse.get_pos() 
        click = pygame.mouse.get_pressed()
        button("EASY GAME", 75, 300, 300, 50, RED_CHERRY, BROWN_TO_ORANGE)
        if (75 + 300) > mouse[0] > 75 and (300 + 50) > mouse[1] > 300 and click[0] == 1:
            game(easy, saved_name, actual_score)
        button("HARD GAME", 75, 375, 300, 50, RED_CHERRY, BROWN_TO_ORANGE)
        if (75 + 300) > mouse[0] > 75 and (375 + 50) > mouse[1] > 375 and click[0] == 1:
            game(hard, saved_name, actual_score)
        button("CUSTOM GAME", 75, 450, 300, 50, RED_CHERRY, BROWN_TO_ORANGE)
        if (75 + 300) > mouse[0] > 75 and (450 + 50) > mouse[1] > 450 and click[0] == 1:
            game(custom, saved_name, actual_score)
        button("BACK TO MENU", 75, 625, 300, 50, RED_CHERRY, BLACK_TO_RED, main)
        button("RUN AWAY", 75, 700, 300, 50, RED_CHERRY, BROWN_TO_ORANGE, quit)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                # To delete a wrong letter, the variable name is replaced by the same letters except the last
                # Indeed, this method enters all the character until the last one (which is excluded)
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                    
                elif event.key == pygame.K_RETURN:
                    saved_name = name
                    actual_score = question(name)
                    if actual_score != 0:
                            name = "Nice to see you again"
                    else:
                        name = "Welcome new player"

                else:
                    name += event.unicode
        
        pygame.display.update()

# ------------------------------------
#          DO WE KNOW YOU ?
# ------------------------------------ 
def question(name):
    # We open the file "scores.txt" in order the save the contents in a list (list in the list)
    f = open("scores.txt", "r")
    list= f.read()
    f.close()
    list= list.split("\n")
    for line in range(0, len(list)):
        list[line] = list[line].split(" ")
    # print(list)

    for i in range(0, len(list)):
            if list[i][0] == name:
                actual_score = list[i][1]
                print(actual_score)
                return actual_score

    actual_score = 0
    return actual_score

# ------------------------------------
#               GAME
# ------------------------------------ 
def game(difficulty, name, score):
    running = True
    letter_attempt = ''
    player = name
    actual_score = score
    actual_difficulty = difficulty
    
    # We create a list with the other files, depending on the chosen level :
    if difficulty == 'easy':
        f = open('words_easy.txt', 'r')
        list = f.read()
        list= list.split('\n')
        # print(list)
        # print("easy")
    elif difficulty == 'hard':
        f = open('words_hard.txt', 'r')
        list = f.read()
        list = list.split('\n')
        # print(list)
        # print("difficult")
    elif difficulty == 'custom':
        f = open("custom_list_words.txt", "r")
        list = f.read()
        list = list.split('\n')
        # print(list)
        # print("custom")

    f.close()

    # We chose a random word in the list, and we create its equivalent in "_"
    random_word = random.choice(list)
    word_to_guess = "_" * len(random_word) #Thank to the chosen font, I don't need to add space between the underscores
    # print(random_word)

    # We create a list with all the images of Hangman's different states :
    images_hangman = []
    for i in range(7): # 6 steps
        picture = pygame.image.load("Hangman/hangman" + str(i) + ".png")
        images_hangman.append(picture)
    
    done = False
    status = 0

    while running:
        mouse = pygame.mouse.get_pos() 
        click = pygame.mouse.get_pressed()
        
        # Background :
        game_background = pygame.image.load("Pictures/game2_background.png")
        win.blit(game_background, (0,0))
        
        # Display score:
        display_score_text = WORD_FONT.render("Score : ", True, WHITE)
        win.blit(display_score_text, (50, 745))
        display_score = WORD_FONT.render(str(actual_score), True, WHITE)
        win.blit(display_score, (140, 745))

        # Display Player's name:
        display_name_text = WORD_FONT.render("Player : ", True, WHITE)
        win.blit(display_name_text, (50, 720))
        display_name = WORD_FONT.render(player, True, WHITE)
        win.blit(display_name, (140, 720))

        # HangEleven :
        win.blit(images_hangman[status], (20, 50))

        # Display word :
        word_display = GUESS_FONT.render(word_to_guess, True, WHITE)
        win.blit(word_display, (170, 300))
        
        # Characters :
        dustin = pygame.image.load("Pictures/little_Dustin.png")
        win.blit(dustin, (90, 600))
        lucas = pygame.image.load("Pictures/little_Lucas.png")
        win.blit(lucas, (170, 600))
        mike = pygame.image.load("Pictures/little_Mike.png")
        win.blit(mike, (10, 600))

        button("RUN AWAY", 250, 740, 180, 40, RED_CHERRY, BROWN_TO_ORANGE, quit)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                letter_attempt = str(event.unicode).lower()
                print(letter_attempt)
                
                if letter_attempt in random_word:
                    for i in range(0, len(random_word)):
                        if random_word[i] == letter_attempt:
                            word_to_guess = word_to_guess[:i] + random_word[i] + word_to_guess[i+1:]
                            print(word_to_guess)
                else:
                    status +=1

            if word_to_guess == random_word or status == 6:
                done = True

        # if victory :   
        if done == True and status < 6:
            status = 0
            victory_text = "You saved everyone !"
            victory = WORD_FONT.render(victory_text, True, WHITE)
            win.blit(victory, (120, 350))
            eleven = pygame.image.load("Pictures/little_Eleven.png")
            win.blit(eleven, (250, 600))

            # As previously, we cannot use the button action because of the parameters.
            # Also, I can't incremente the score before because of the loop. It will endlessly
            # incremente. So I choose to display the new score only on the next game.
            button("PLAY AGAIN", 37.5, 410, 375, 40, RED_CHERRY, BROWN_TO_ORANGE)
            if (37.5 + 375) > mouse[0] > 37.5 and (410 + 40) > mouse[1] > 410 and click[0] == 1:
                if difficulty == "hard":
                    actual_score = int(actual_score) + 3
                else:
                    actual_score = int(actual_score) + 1
                game(actual_difficulty, player, actual_score)

            button("SAVE SCORE AND MENU", 37.5, 480, 375, 40, RED_CHERRY, BROWN_TO_ORANGE)
            if (37.5 + 375) > mouse[0] > 37.5 and (480 + 40) > mouse[1] > 480 and click[0] == 1:
                if difficulty == "hard":
                    actual_score = int(actual_score) + 3
                else:
                    actual_score = int(actual_score) + 1
                save_score(player, actual_score)
                main()

        # if defeat :
        if status == 6 and done == True:
            defeat_text = "Everyone died !"
            defeat = WORD_FONT.render(defeat_text, True, WHITE)
            win.blit(defeat, (160, 350))

            # Characters :
            portion = pygame.image.load("Pictures/background_portion.png")
            win.blit(portion, (0, 590))
            dustin = pygame.image.load("Pictures/dead_dustin.png")
            win.blit(dustin, (90, 600))
            lucas = pygame.image.load("Pictures/dead_lucas.png")
            win.blit(lucas, (170, 600))
            mike = pygame.image.load("Pictures/dead_mike.png")
            win.blit(mike, (10, 600))
            demogorgon = pygame.image.load("Pictures/demogorgon.png")
            win.blit(demogorgon, (250, 560))

            button("PLAY AGAIN", 100, 410, 250, 40, RED_CHERRY, BROWN_TO_ORANGE)
            if (100 + 250) > mouse[0] > 100 and (410 + 40) > mouse[1] > 410 and click[0] == 1:
                actual_score = int(actual_score) - 1
                game(actual_difficulty, player, actual_score)

            button("SAVE SCORE", 100, 480, 250, 40, RED_CHERRY, BROWN_TO_ORANGE)
            if (100 + 250) > mouse[0] > 100 and (480 + 40) > mouse[1] > 480 and click[0] == 1:
                actual_score = int(actual_score) - 1
                save_score(player, actual_score)
                scores()

        pygame.display.update()


# ------------------------------------
#               SCORES
# ------------------------------------ 
def scores():
    running = True

    f = open("scores.txt", "r")
    list= f.read()
    f.close()
    list= list.split("\n")
    # print(list)

    for line in range(0, len(list)):
        list[line] = list[line].split(" ")
    # print(list)

    # Background :
    scores_background = pygame.image.load("Pictures/game2_background.png")
    win.blit(scores_background, (0,0))
    # Title :
    title = pygame.image.load("Pictures/title3.png")
    win.blit(title, (75, 30))

    # Names and scores (the most recent)
    for i in range(0, 8):
        win.blit(WORD_FONT.render(list[-i-1][0], True, WHITE), (100, 300 + (i*30)))
        win.blit(WORD_FONT.render(list[-i-1][1], True, WHITE), (350, 300 + (i*30)))

    while running:
        button("BACK TO MENU", 75, 650, 300, 50, RED_CHERRY, OTHER_BROWN, main)
        button("RUN AWAY", 75, 725, 300, 50, RED_CHERRY, BROWN_TO_ORANGE, quit)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

# ------------------------------------
#            SAVE SCORES
# ------------------------------------ 
def save_score(name, score):
    # We open the file "scores.txt" in order the save the contents in a list (list in the list)
    f = open("scores.txt", "r")
    list= f.read()
    f.close()
    list= list.split("\n")
    for line in range(0, len(list)):
        list[line] = list[line].split(" ")
    # print(list)

    for i in range(len(list)):
        if list[i][0] == name:
            list.pop(i)
            break
        # If the player has already played, we delete his name in the list in order to put him at the end. Then his score
        # will be displayed on the top of the scoreboard (in this way, all the current player can see their score)

    list.append([name, str(score)])
    # print(list)

    with open('scores.txt', 'w') as file: # Other way to open a file. With this method, we don't need to close it at the end.
        for i in range(len(list) - 1): # We can use the loop only until the penultimate because of the line break
            file.write(list[i][0])
            file.write(" ")
            file.write(list[i][1])
            file.write("\n")
        
        # Here we enter the last player, without line break at the end
        file.write(list[-1][0]) 
        file.write(" ")
        file.write(list[-1][1])


# ------------------------------------
#                 MAIN
# ------------------------------------
def main():
    running = True

    # Background :
    menu_background = pygame.image.load("Pictures/menu_background.png")
    win.blit(menu_background, (0,0))

    # Title :
    title = pygame.image.load("Pictures/Title1.png")
    win.blit(title, (65, 30))

    #  Characters :
    demogorgon = pygame.image.load("Pictures/demogorgon.png")
    win.blit(demogorgon, (330, 645))
    dustin = pygame.image.load("Pictures/little_Dustin.png")
    win.blit(dustin, (90, 700))
    lucas = pygame.image.load("Pictures/little_Lucas.png")
    win.blit(lucas, (170, 700))
    mike = pygame.image.load("Pictures/little_Mike.png")
    win.blit(mike, (10, 700))
    
    while running:
        button("PLAY", 12.5, 500, 200, 50, RED_CHERRY, BLACK_NOT_BLACK, choice_level)
        button("NEW WORD", 237.5, 500, 200, 50, RED_CHERRY, BLACK_TO_RED, insert_word)
        button("SCORES", 12.5, 575, 200, 50, RED_CHERRY, OTHER_BROWN, scores)
        button("RUN AWAY", 237.5, 575, 200, 50, RED_CHERRY, BROWN_TO_ORANGE, quit)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

main()
