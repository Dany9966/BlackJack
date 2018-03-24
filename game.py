import pygame
import random

pygame.init()

display_width = 800
display_height = 600

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 155, 0)
red = (255, 0, 0)
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')

img = pygame.image.load('snakeHead.png')
appleImg = pygame.image.load('apple.png')
icon = pygame.image.load('icon.jpg')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
FPS = 10
# direction = 'right'

small_font = pygame.font.Font('NotoSansCJK-Black.ttc', 25)
med_font = pygame.font.Font('NotoSansCJK-Black.ttc', 40)
large_font = pygame.font.Font('NotoSansCJK-Black.ttc', 80)
AppleThickness = 30


def score(score):
    text = small_font.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, [0, 0])


def randApppleGen():
    randAppleX = round(random.randrange(0, display_width - AppleThickness))  # / 10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - AppleThickness))  # / 10.0) * 10.0
    return randAppleX, randAppleY


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                intro = False

        gameDisplay.fill(white)
        message_to_screen('Welcome to Slither',
                          green,
                          -100,
                          'large')
        message_to_screen('The objective of the game is to eat red apples',
                          black,
                          -30)
        message_to_screen('The more apples you eat, to longer you get',
                          black,
                          10)
        message_to_screen('If you run into yourself, or the edges, you die',
                          black,
                          50)
        message_to_screen('Press C to play or Q to quit',
                          black,
                          180,
                          'medium')
        pygame.display.update()


def snake(block_size, snakelist):
    if direction == 'right':
        head = pygame.transform.rotate(img, 270)
    if direction == 'left':
        head = pygame.transform.rotate(img, 90)
    if direction == 'up':
        head = pygame.transform.rotate(img, 0)
    if direction == 'down':
        head = pygame.transform.rotate(img, 180)
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])  # draw snake


def text_Objects(text, clr, size):
    if size == 'small':
        textSurface = small_font.render(text, True, clr)
    if size == 'medium':
        textSurface = med_font.render(text, True, clr)
    if size == 'large':
        textSurface = large_font.render(text, True, clr)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace = 0, size = 'small'):
    textSurf, textRect = text_Objects(msg, color, size)
    textRect.center = (display_width/2), (display_height/2)+y_displace
    gameDisplay.blit(textSurf, textRect)


def gameLoop():
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 20
    lead_y_change = 0
    snakelist = []
    snakeLength = 1
    block_size = 20
    randAppleX, randAppleY = randApppleGen()
    gameExit = False
    gameOver = False
    global direction
    direction = 'right'
    while not gameExit:
        while gameOver:
            gameDisplay.fill(white)
            message_to_screen('GAME OVER',
                              red,
                              -50,
                              'large')
            message_to_screen('Press C to play again or Q to quit',
                              green,
                              50,
                              'medium')

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:

                        gameLoop()

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                gameOver = True
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                    direction = 'left'

                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                    direction = 'right'

                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                    direction = 'up'
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    direction = 'down'

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)

        gameDisplay.blit(appleImg, (randAppleX, randAppleY))

        snakeHead = [lead_x, lead_y]
        snakelist.append(snakeHead)
        if len(snakelist) > snakeLength:
            del snakelist[0]

        for eachSegment in snakelist[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
        snake(block_size, snakelist)
        score(snakeLength-1)

        pygame.display.update()

        if randAppleX < lead_x < randAppleX + AppleThickness or randAppleX < lead_x + block_size < randAppleX + AppleThickness:
            if randAppleY < lead_y < randAppleY + AppleThickness:
                # print("x and y cross over")
                randAppleX, randAppleY = randApppleGen()
                snakeLength += 1
            elif randAppleY < lead_y + block_size < randAppleY + AppleThickness:
                # print("x and y crossover")
                randAppleX, randAppleY = randApppleGen()
                snakeLength += 1

        clock.tick(FPS)

    pygame.quit()
    quit()


game_intro()
gameLoop()
