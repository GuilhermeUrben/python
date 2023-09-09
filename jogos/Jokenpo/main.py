import random
import time

import pygame

# Inicializa o Pygame
pygame.init()

# Define as cores utilizadas no jogo
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define o tamanho da janela
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Define as opções de escolha
PEDRA = 1
PAPEL = 2
TESOURA = 3

# Define as imagens de cada escolha
IMAGES = {
    PEDRA: pygame.image.load('imagens/pedra.png'),
    PAPEL: pygame.image.load('imagens/papel.png'),
    TESOURA: pygame.image.load('imagens/tesoura.png')
}

# Define a fonte utilizada no jogo
FONT = pygame.font.SysFont(None, 20)

# Define as mensagens do jogo
MESSAGES = {
    'intro': 'Bem vindo ao Jokenpô!',
    'tutorial': 'Como jogar:\n- Cada jogador joga 1 vez por rodada\n- Na rodada você terá que escolher entre Pedra, Papel ou Tesoura\n- Ganha quem conseguir "eliminar o adversário"\n- Caso a escolha for igual, resultará em empate',
    'eliminacao': 'Como eliminar:\n- Pedra {} quebra a Tesoura {}\n- Tesoura {} corta o Papel {}\n- Papel {} enrola a Pedra {}',
    'escolha': 'Escolha sua jogada:',
    'empate': 'Empate!',
    'derrota': 'Você perdeu!',
    'vitoria': 'Você venceu!'
}

# # Define os emojis utilizados no jogo
# PEDRA_EMOJI = emoji.emojize(':fist:', language='alias')
# PAPEL_EMOJI = emoji.emojize(':raised_hand:', language='alias')
# TESOURA_EMOJI = emoji.emojize(':v:', language='alias')

# Define a função que mostra a mensagem na tela


# def show_message(screen, messages, color, x, y, delay=1.0):
#     for message in messages:
#         text = FONT.render(message, True, color)
#         text_rect = text.get_rect(center=(x, y))
#         screen.blit(text, text_rect)
#         pygame.display.update()
#         time.sleep(delay)


def show_message(screen, message, color, x, y):
    text = FONT.render(message, True, color)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

# Define a função que mostra a escolha na tela


def show_choice(screen, choice, x, y):
    image = IMAGES[choice]
    screen.blit(image, (x, y))

# Define a função que mostra a jogada do computador na tela


def show_computer_choice(screen, choice, x, y):
    message = 'Computador jogou:'
    show_message(screen, message, WHITE, x, y-50)
    show_choice(screen, choice, x, y)

# Define a função que mostra a jogada do jogador na tela


def show_player_choice(screen, choice, x, y):
    message = 'Você jogou:'
    show_message(screen, message, WHITE, x, y-50)
    show_choice(screen, choice, x, y)

# Define a função que mostra o resultado na tela


def show_result(screen, result, x, y):
    show_message(screen, result, WHITE, x, y)

# Define a função principal do jogo


def main():
    # Cria a janela do jogo
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Jokenpô")

    # Define o loop do jogo
    running = True
    while running:
        # Verifica os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_1:
                    play_game(PEDRA)
                elif event.key == pygame.K_2:
                    play_game(PAPEL)
                elif event.key == pygame.K_3:
                    play_game(TESOURA)

        # Limpa a tela
        screen.fill(BLACK)

        # Mostra as mensagens na tela
        show_message(screen, MESSAGES['intro'], WHITE, WINDOW_WIDTH//2, 50)
        show_message(screen, MESSAGES['tutorial'], WHITE, WINDOW_WIDTH//2, 100)
        show_message(screen, MESSAGES['escolha'], WHITE, WINDOW_WIDTH//2, 200)

        # Mostra as opções na tela
        show_choice(screen, PEDRA, 100, 300)
        show_choice(screen, PAPEL, 250, 300)
        show_choice(screen, TESOURA, 400, 300)

        # Atualiza a tela
        pygame.display.update()

    # Finaliza o Pygame
    pygame.quit()
    print("")


main()
