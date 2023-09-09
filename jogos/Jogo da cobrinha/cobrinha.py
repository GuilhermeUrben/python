import random

import pygame

# Definir constantes para o jogo
WIDTH = 1080
HEIGHT = 720
FPS = 10

# Definir cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Iniciar Pygame e criar janela
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Definir classe para a cobrinha


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT / 2
        self.speedx = 0
        self.speedy = 0
        self.body = [(self.rect.x, self.rect.y)]

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.body.insert(0, (self.rect.x, self.rect.y))
        self.body.pop()

    def grow(self):
        self.body.append((self.rect.x, self.rect.y))

    def reset(self):
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT / 2
        self.speedx = 0
        self.speedy = 0
        self.body = [(self.rect.x, self.rect.y)]

# Definir classe para a comida


class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - 10, 10)
        self.rect.y = random.randrange(0, HEIGHT - 10, 10)


# Criar grupo de sprites e adicionar a cobrinha e a comida
all_sprites = pygame.sprite.Group()
snake = Snake()
food = Food()
all_sprites.add(snake)
all_sprites.add(food)

# Loop principal do jogo
running = True
while running:
    # Manter loop na taxa de FPS definida
    clock.tick(FPS)

    # Processar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.speedx = -10
                snake.speedy = 0
            elif event.key == pygame.K_RIGHT:
                snake.speedx = 10
                snake.speedy = 0
            elif event.key == pygame.K_UP:
                snake.speedx = 0
                snake.speedy = -10
            elif event.key == pygame.K_DOWN:
                snake.speedx = 0
                snake.speedy = 10

    # Verificar colisão da cobrinha com a comida
    if pygame.sprite.collide_rect(snake, food):
        food.kill()
        food = Food()
        all_sprites.add(food)
        snake.grow()

    # Verificar colisão da cobrinha com a comida
    if pygame.sprite.collide_rect(snake, food):
        food.kill()
        food = Food()
        all_sprites.add(food)
        snake.grow()

    # Verificar colisão da cobrinha com a parede
    if snake.rect.x < 0 or snake.rect.x > WIDTH or snake.rect.y < 0 or snake.rect.y > HEIGHT:
        running = False

        # Exibir mensagem de "Game Over"
        font = pygame.font.Font(None, 50)
        text = font.render("Game Over", True, WHITE)
        text_rect = text.get_rect()
        text_rect.centerx = screen.get_rect().centerx
        text_rect.centery = screen.get_rect().centery
        screen.blit(text, text_rect)
        pygame.display.update()

    # Atualizar sprites e desenhar na tela
    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Atualizar tela
    pygame.display.flip()
