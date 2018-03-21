import pygame
import random

pygame.init()

display_width = 800
display_height = 600

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 200, 150)
red = (255, 0, 0)
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')


clock = pygame.time.Clock()
FPS = 20

font = pygame.font.SysFont(None, 25)


def snake(block_size, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, white, [XnY[0], XnY[1], block_size, block_size])  # draw snake

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])
    pygame.display.update()


def gameLoop():
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0
    snakelist = []
    snakeLength = 1
    block_size = 10
    randAppleX = round(random.randrange(0, display_width - block_size)/10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - block_size)/10.0) * 10.0
    gameExit = False
    gameOver = False
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(green)
            message_to_screen('GAME OVER: press C to play again or Q to quit', red)
            pygame.display.update()

            for event in pygame.event.get():
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

                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0

                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

            # keyup event handling
            # if event.type == pygame.KEYUP:
              #  if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               #     lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(green)
        # make sure to draw apples BEFORE snake
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size]) # draw apple

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakelist.append(snakeHead)
        if len(snakelist) > snakeLength:
            del snakelist[0]

        for eachSegment in snakelist[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
        snake(block_size, snakelist)

        # gameDisplay.fill(red, rect=[360, 410, 10, 10])
        pygame.display.update()
        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
            randAppleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
            snakeLength += 1
        clock.tick(FPS)

    pygame.quit()
    quit()

gameLoop()