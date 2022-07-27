import pygame
from random import randrange

res = 800
size = 50

x = randrange(0, res, size)
y = randrange(0, res, size)
apple = randrange(0, res, size), randrange(0, res, size)
dirs = {'S': True, 'A': True, 'W': True, 'D': True}
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 8
score = 0

pygame.init()
screen = pygame.display.set_mode([res, res])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 56, bold=True)
img = pygame.image.load('sticker.webp').convert()
img = pygame.transform.scale(img, (800, 800))
img2 = pygame.image.load('sticker2.webp').convert()
img2 = pygame.transform.scale(img2, (800, 800))
music = pygame.mixer.music.load('papich-ya-uedu-v-solyanogo.mp3')
pygame.mixer.music.play()
sound1 = pygame.mixer.Sound('papich-ez_s6YYgopJ.mp3')
sound1.set_volume(5)
sound2 = pygame.mixer.Sound('papich-ob-igre-v-dotu.mp3')
while True:
    pygame.mixer.music.set_volume(0.8)
    screen.blit(img2, (0, 0))
    # рисовка змейки и яблок
    [(pygame.draw.rect(screen, pygame.Color('green'), (i, j, size - 2, size - 2))) for i, j in snake]
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, size, size))
    # счетчик
    render_score = font_score.render(f'SCORE:{score}', True, pygame.Color('orange'))
    screen.blit(render_score, (5, 5))
    pygame.display.flip()
    clock.tick(fps)
    # движение змейки
    x += dx * size
    y += dy * size
    snake.append((x, y))
    snake = snake[-length:]
    # сьедание яблока
    if snake[-1] == apple:
        apple = randrange(0, res, size), randrange(0, res, size)
        length += 1
        score += 1
        fps += 1
        sound1.play()
    # game over
    if x < 0 or x > res - size or y < 0 or y > res - size or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', True, pygame.Color('orange'))
            pygame.mixer.music.pause()
            sound2.play(1)
            screen.blit(img, (0, 0))
            screen.blit(render_end, (res // 2 - 200, res // 3))


            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # управление
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'S': False, 'A': True, 'W': True, 'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'S': True, 'A': True, 'W': False, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'S': True, 'A': True, 'W': True, 'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'S': True, 'A': False, 'W': True, 'D': True}
