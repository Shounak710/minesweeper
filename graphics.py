import pygame
import sys

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 10
CELL_SIZE = WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Font for text
pygame.init()
font = pygame.font.Font(None, 36)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

def draw_board(board, revealed, flagged):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            
            if revealed[y][x]:
                pygame.draw.rect(screen, GRAY, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)

            pygame.draw.rect(screen, BLACK, rect, 2)

            if revealed[y][x]:
                if board[y][x] == -1:
                    pygame.draw.circle(screen, RED, rect.center, CELL_SIZE // 4)
                elif board[y][x] > 0:
                    text = font.render(str(board[y][x]), True, BLACK)
                    screen.blit(text, text.get_rect(center=rect.center))

            elif flagged[y][x]:
                pygame.draw.rect(screen, GREEN, rect.inflate(-10, -10))


def main(game_logic):
    running = True

    while running:
        screen.fill(WHITE)

        board = game_logic.get_board()
        revealed = game_logic.get_revealed()
        flagged = game_logic.get_flagged()

        draw_board(board, revealed, flagged)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                x, y = mx // CELL_SIZE, my // CELL_SIZE

                if event.button == 1:
                    game_logic.reveal_cell(x, y)
                elif event.button == 3:
                    game_logic.toggle_flag(x, y)

    pygame.quit()
    sys.exit()


# Example usage
if __name__ == "__main__":
    import game as game
    game.play()
