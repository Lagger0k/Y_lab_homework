import itertools
import pygame
import sys
from typing import Any


def ai_turn(board: dict, attempts: int) -> bool:
    """Делает ход компьютера."""
    for attempt in range(attempts):
        for cell in board.keys():
            if board[cell] == 0:
                board[cell] = 'o'
                if check_lose(board, 'o'):
                    board[cell] = 0
                    continue
                return False
    return True


def check_lose(board: dict, char: str) -> str | bool:
    """Проверяет есть ли проигравший."""
    result = []
    for x_offset in range(6):
        for y_offset in range(6):
            result.append(_check_lose_5_x_5(board, char, x_offset, y_offset))
    if char in result:
        return char + ' ' + 'loss'
    return False


def _check_lose_5_x_5(board: dict, char: str, x_offset: int, y_offset: int) -> str | bool:
    """Проверяет есть ли 5 знаков в ряд."""
    for row in range(5):
        if [board[(x_offset + column, y_offset + row)] for column in range(5)].count(char) == 5:
            return char
    for column in range(5):
        if [board[(x_offset + column, y_offset + row)] for row in range(5)].count(char) == 5:
            return char
    if [board[(x_offset + i, y_offset + i)] for i in range(5)].count(char) == 5:
        return char
    if [board[(x_offset + abs(-4 + i), y_offset + i)] for i in range(5)].count(char) == 5:
        return char
    return False


if __name__ == '__main__':
    pygame.init()

    size_block = 50
    margin = 5
    width = height = size_block * 10 + margin * 11

    size_window = (width, height)
    screen = pygame.display.set_mode(size_window)
    pygame.display.set_caption("Обратные крестики-нолики")

    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    white = (255, 255, 255)

    points = itertools.product([x for x in range(10)], [x for x in range(10)])
    points_dict: dict[tuple[int, int], Any] = dict.fromkeys(points, 0)

    turn = 0
    game_over = False

    while True:
        if turn % 2 != 0 and not game_over:
            free_cells = 100 - turn
            game_over = ai_turn(points_dict, free_cells)
            turn += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over and turn % 2 == 0:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                x = mouse_x // (size_block + margin)
                y = mouse_y // (size_block + margin)
                if points_dict[(x, y)] == 0:
                    points_dict[(x, y)] = "x"
                    turn += 1

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_over = False
                points = itertools.product([x for x in range(10)], [x for x in range(10)])
                points_dict = dict.fromkeys(points, 0)
                turn = 0
                screen.fill(black)

        if not game_over:
            for point, sign in points_dict.items():
                if sign == 'o':
                    color = green
                elif sign == 'x':
                    color = red
                else:
                    color = white

                x = point[0] * size_block + (point[0] + 1) * margin
                y = point[1] * size_block + (point[1] + 1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))

                if color == red:
                    pygame.draw.line(screen, white, (x + 3, y + 3), (x + size_block - 3, y + size_block - 3), 3)
                    pygame.draw.line(screen, white, (x + size_block - 3, y + 3), (x + 3, y + size_block - 3), 3)
                elif color == green:
                    pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3,
                                       3)
            if turn % 2 == 0:
                symbol = 'o'
            else:
                symbol = 'x'
            game_over = check_lose(points_dict, symbol)

            if turn == 100:
                game_over = 'Ничья'

            if game_over:
                screen.fill(black)
                font = pygame.font.SysFont('stxingkai', 80)
                text = font.render(f'Game over {game_over}', True, white)
                text_rect = text.get_rect()
                text_x = screen.get_width() / 2 - text_rect.width / 2
                text_y = screen.get_height() / 2 - text_rect.height / 2
                screen.blit(text, [text_x, text_y])
            pygame.display.update()
