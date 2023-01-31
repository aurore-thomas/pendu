import pygame
import math

# Setup display
pygame.init() #Initialisation de Pygame
WIDTH, HEIGHT = 800, 500  # Constante en majuscule
win = pygame.display.set_mode((WIDTH, HEIGHT)) # On définit la taille de la fenêtre
pygame.display.set_caption("Hangman Game") # Titre de la fenêtre

# button variable
RADIUS = 20
GAP = 15
letters = []
startx =  round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65 #Chaque lettre a déjà un numéro attribué, para la B es 66

for i in range(26):
    x = startx + GAP * 2 + ((RADIUS *2 + GAP) * (i % 13))
    y =  starty + ((i // 13) * (GAP + RADIUS *2))
    letters.append([x, y, chr(A + i), True])

# Fonts:
LETTER_FONT = pygame.font.SysFont('comicsans', 25)
WORD_FONT = pygame.font.SysFont('comicsans', 20)

# Load images
images = []
for i in range(7): #de 0 à 6, 7 non inclus
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# Game variables
hangman_status = 0
word = "DEVELOPER"
guessed = [""]

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Setup game loop
FPS = 60 #Frame Per Second
clock = pygame.time.Clock()
run = True

def draw():
    win.fill(WHITE) # Background color (white because maximum RVB)

    #Draw words:
    display_words = ""
    for letter in word:
        if letter in guessed:
            display_words += letter + " "
        else:
            display_words += "_ "
    text = WORD_FONT.render(display_words, 1, BLACK)
    win.blit(text, (400, 200))
        

    #draw buttons
    for letter in letters:
        x, y, ltr, visible = letter 
        if visible :
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
        # (x,y) = center of circle, 3 = thick

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update() #Need to update to see background color

while run: # = while run == True
    clock.tick(FPS) #It will compute how may milliseconds have passed since the previous call

    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False # => Close the window
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos() # Mouse position
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    distance = math.sqrt((x - m_x)**2 + (y -m_y)**2)
                    if distance < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status +=1

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    
    if won:
        print("Won !")

pygame.quit() #Close the window
