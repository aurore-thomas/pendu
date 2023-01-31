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

# ------------------------------------
#               WINDOW
# ------------------------------------
# We define the game window :
pygame.init()
SIZE = (800, 600)
win = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Hangman Game")

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

WORD_FONT = pygame.font.Font('Fonts/Baby Doll.ttf', 40)
TITLE = pygame.font.Font("Fonts/Baby Doll.ttf", 60)

win.fill(WHITE)
pygame.display.flip()

# ------------------------------------
#           HANGMAN STATUS
# ------------------------------------
# We create a list with all the images of Hangman's different states :
# image_hangman = []
# for i in range(7): # 6 steps
#     picture = pygame.image.load("hangman" + str(i) + ".png")
#     image_hangman.append(picture)

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

    textSurf, textRect = text_objects(text, WORD_FONT)
    textRect.center = ( (x + (w/2)), (y + (h/2)))
    win.blit(textSurf, textRect)

# ------------------------------------
#             NEW WORD
# ------------------------------------
running = True


def insert_word():
    new_word = ''
    input_rect = pygame.Rect(200, 200, 140, 32)
    active = False 

    while running:
        win.fill(WHITE)
        if active:
            color = DARK_GREEN
        else:
            color = RED_CHERRY
        # pygame.display.flip()
        text_surface = WORD_FONT.render(new_word, False, BLACK)
        win.blit(text_surface,input_rect)
        pygame.draw.rect(win, color, input_rect, 2)

        input_rect.w = max(100, text_surface.get_width() + 10)
        pygame.display.update()
    

        for event in pygame.event.get():
            button("Back to menu", 120, 200, 250, 50, RED_CHERRY, BLACK_TO_RED)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
            
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        new_word = new_word[:-1]
                    elif event.key == pygame.K_RETURN:
                        print(new_word)
                        new_word = insert_word().lower()
                        level_1.append(new_word)
                        print(level_1)
                    else:
                        new_word += event.unicode



                

# ------------------------------------
#            GAME LOOP  
# ------------------------------------

status = 0

while running:
    text = TITLE.render("HANGMAN GAME", True, BLACK)
    text = pygame.transform.rotate(text, 90)
    win.blit(text, [100, 60])

    # button(text, x, y, w, h, ic, ac, action=None):
    button("Easy Game", 300, 50, 350, 70, GREEN_LIGHT, GREEN_LIGHT2)
    button("Hard Game", 300, 157.5, 350, 70, DARK_GREEN, DARK_GREEN2)
    button("New word", 300, 265, 350, 70, BLACK_NOT_BLACK, BLACK_TO_RED, insert_word)
    button("Scores", 300, 372.5, 350, 70, RED_CHERRY, RED_LIGHTER)
    button("Quit", 300, 480, 350, 70, STRANGE_BROWN, BROWN_TO_ORANGE, quit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if event.type == pygame.KEYDOWN:
        #     if event.unicode.isalpha():
        #         letter_proposed = (event.unicode).upper()
        #         # print(letter_proposed)
            
        # if letter_proposed 
    
    pygame.display.update()

