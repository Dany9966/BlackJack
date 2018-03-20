import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 200, 150)
red = (255, 0, 0)
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('pyJack')

gameExit = False
while not gameExit:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(green)
    pygame.draw.rect(gameDisplay, white, [350, 400, 100, 150])
    gameDisplay.fill(red, rect=[360, 410, 10, 10])
    pygame.display.update()

pygame.quit()
quit()
