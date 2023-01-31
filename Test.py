import pygame, sys
import random

# ------------------------------------
#             WORDS FILE
# ------------------------------------
f = open('words_easy.txt', 'r')
level_1 = f.read()
level_1 = level_1.split('\n')
f.close()

f = open('words_hard.txt', 'r')
level_2 = f.read()
level_2 = level_2.split('\n')
f.close()

f = open("custom_list_words.txt")
level_custom = f.read()
level_custom = level_custom.split('\n')
f.close()

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

GREEN_LIGHT = (226, 233, 192)
GREEN_LIGHT2 = (238, 243, 217)

DARK_GREEN = (122, 169, 92)
DARK_GREEN2 = (139, 193, 105)

RED_CHERRY = ( 167, 0, 30)
RED_LIGHTER = (193, 0, 35)

STRANGE_BROWN = (149, 81, 73)
BROWN_TO_ORANGE = (189, 115, 106)

BLACK_NOT_BLACK = (30, 15, 28)
BLACK_TO_RED = (80, 15, 28)

OTHER_BROWN = (175, 114, 73)

WORD_FONT = pygame.font.Font('Fonts/Pixeled.ttf', 12)
TITLE = pygame.font.Font("Fonts/Baby Doll.ttf", 60)
BENGUIAT = pygame.font.Font("Fonts/Benguiat.ttf", 30)


# ------------------------------------
#           HANGMAN STATUS
# ------------------------------------
# We create a list with all the images of Hangman's different states :
images_hangman = []
for i in range(7): # 6 steps
    picture = pygame.image.load("Hangman/hangman" + str(i) + ".png")
    images_hangman.append(picture)

# ------------------------------------
#             WORD TO GUESS
# ------------------------------------

random_word = random.choice(level_1)
word_to_guess = "_ " * len(random_word)
text = WORD_FONT.render(word_to_guess, False, BLACK)

# ------------------------------------
#               BUTTONS  
# ------------------------------------
def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def button(text, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos() 
    click = pygame.mouse.get_pressed() 
    # print(click)

    # When mouse hovers the button, active color change to inactive color
    if (x + w) > mouse[0] > x and (y + h) > mouse[1] > y:
        pygame.draw.rect(win, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(win, ic, (x, y, w, h))

    textSurf, textRect = text_objects(text, BENGUIAT)
    textRect.center = ( (x + (w/2)), (y + (h/2)))
    win.blit(textSurf, textRect)

# ------------------------------------
#             NEW WORD
# ------------------------------------
def insert_word():
    running = True
    new_word = ''

    input_rect = pygame.Rect(125, 470, 200, 50)
    explanation_1 = "Enter your new word and press"
    explanation_2 = "Enter. It will be added"
    explanation_3 = "to the personalized list"
    
    while running:
        # We need to create the background here for the Backspace
        word_background = pygame.image.load("Pictures/score_background.png")
        win.blit(word_background, (0,0))

        # Title :
        title2 = pygame.image.load("Pictures/Title2.png")
        win.blit (title2, (100, 150))

        display_explanation_1 = WORD_FONT.render(explanation_1, False, WHITE)
        win.blit(display_explanation_1, (75, 370))

        display_explanation_2 = WORD_FONT.render(explanation_2, False, WHITE)
        win.blit(display_explanation_2, (115, 400))

        display_explanation_3 = WORD_FONT.render(explanation_3, False, WHITE)
        win.blit(display_explanation_3, (110, 430))
        
        text_surface = WORD_FONT.render(new_word, False, WHITE)
        win.blit(text_surface,(138, 475))
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
                    f = open('custom_list_words.txt', 'a')
                    f.write("\n")
                    f.write(new_word.lower())
                    f.close()
                    new_word = 'Word added !'
                else:
                    new_word += event.unicode

# ------------------------------------
#         CHOICE GAME LEVEL
# ------------------------------------    
def choice_level():
    running = True
     
    # Enter name : 
    name = ''
    explanation_1 = "Enter your name and press"
    explanation_2 = "Enter, then chose a level"
    input_name = pygame.Rect(75, 130, 300, 50)

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
        win.blit(display_name, input_name)
        pygame.draw.rect(win, BLACK_TO_RED, input_name, 2)
        
        # button("SAVE YOUR NAME", 75, 175, 300, 50, RED_CHERRY, BROWN_TO_ORANGE, save_name(name))
        button("EASY GAME", 75, 300, 300, 50, RED_CHERRY, BROWN_TO_ORANGE)
        button("HARD GAME", 75, 375, 300, 50, RED_CHERRY, BROWN_TO_ORANGE)
        button("CUSTOM GAME", 75, 450, 300, 50, RED_CHERRY, BROWN_TO_ORANGE)
        button("BACK TO MENU", 75, 625, 300, 50, RED_CHERRY, BLACK_TO_RED, main)
        button("RUN AWAY", 75, 700, 300, 50, RED_CHERRY, BROWN_TO_ORANGE, quit)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_name.collidepoint(event.pos):
                    active = True
            
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                        
                    elif event.key == pygame.K_RETURN:
                        saved_name = name 
                        print(saved_name)
                        

                    else:
                        name += event.unicode
        
        pygame.display.update()

def save_name(name):
    run = True
    while run:
        saved_name = name
        print(saved_name)
        run = False

# ------------------------------------
#               GAME
# ------------------------------------ 
# def game(list_words):


# ------------------------------------
#                 MAIN
# ------------------------------------
def main():
    global running

    # Background :
    menu_background = pygame.image.load("Pictures/menu_background.png")
    win.blit(menu_background, (0,0))
    pygame.display.flip()
    
    while running:

        # Title :
        title = pygame.image.load("Pictures/Title1.png")
        win.blit(title, (65, 30))

        # Buttons :
        button("PLAY", 12.5, 500, 200, 50, RED_CHERRY, BLACK_NOT_BLACK, choice_level)
        button("NEW WORD", 237.5, 500, 200, 50, RED_CHERRY, BLACK_TO_RED, insert_word)
        button("SCORES", 12.5, 575, 200, 50, RED_CHERRY, OTHER_BROWN)
        button("RUN AWAY", 237.5, 575, 200, 50, RED_CHERRY, BROWN_TO_ORANGE, quit)

        #  Characters :
        demogorgon = pygame.image.load("Pictures/demogorgon.png")
        win.blit(demogorgon, (330, 645))
        dustin = pygame.image.load("Pictures/little_Dustin.png")
        win.blit(dustin, (90, 700))
        lucas = pygame.image.load("Pictures/little_Lucas.png")
        win.blit(lucas, (170, 700))
        mike = pygame.image.load("Pictures/little_Mike.png")
        win.blit(mike, (10, 700))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update()

main()