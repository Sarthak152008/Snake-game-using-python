import pygame
import random
import sys

pygame.init()
pygame.font.init()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (50, 150, 255)

# Screen setup
WIDTH = 600
HEIGHT = 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game - by Sarthak")

# Clock and font
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont("comicsansms", 25)

SNAKE_SIZE = 15
FPS = 10


def text_screen(text, color, x, y):
    screen_text = FONT.render(text, True, color)
    WINDOW.blit(screen_text, [x, y])


def plot_snake(window, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(window, color, [x, y, snake_size, snake_size])


def get_random_food_pos():
    # Make food appear aligned to the grid of SNAKE_SIZE
    x = random.randrange(0, WIDTH - SNAKE_SIZE, SNAKE_SIZE)
    y = random.randrange(0, HEIGHT - SNAKE_SIZE, SNAKE_SIZE)
    return x, y


def game_loop():
    # Outer loop lets the game restart cleanly without recursion
    running = True
    while running:
        # Game variables initialization
        exit_game = False
        game_over = False
        snake_x = 45
        snake_y = 55
        velocity_x = 0
        velocity_y = 0
        snake_list = []
        snake_length = 1
        score = 0

        food_x, food_y = get_random_food_pos()

        while not exit_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = SNAKE_SIZE
                        velocity_y = 0
                    elif event.key == pygame.K_LEFT:
                        velocity_x = -SNAKE_SIZE
                        velocity_y = 0
                    elif event.key == pygame.K_UP:
                        velocity_y = -SNAKE_SIZE
                        velocity_x = 0
                    elif event.key == pygame.K_DOWN:
                        velocity_y = SNAKE_SIZE
                        velocity_x = 0

            if not game_over:
                snake_x += velocity_x
                snake_y += velocity_y

                # Check food collision (grid aligned)
                if snake_x == food_x and snake_y == food_y:
                    score += 10
                    food_x, food_y = get_random_food_pos()
                    snake_length += 3

                # Draw background and objects
                WINDOW.fill(BLACK)
                text_screen(f"Score: {score}", WHITE, 10, 10)
                pygame.draw.rect(WINDOW, RED, [food_x, food_y, SNAKE_SIZE, SNAKE_SIZE])

                snake_head = [snake_x, snake_y]
                snake_list.append(snake_head)

                if len(snake_list) > snake_length:
                    del snake_list[0]

                # Collision with self
                if snake_head in snake_list[:-1]:
                    game_over = True

                # Collision with wall
                if (
                    snake_x < 0
                    or snake_x >= WIDTH
                    or snake_y < 0
                    or snake_y >= HEIGHT
                ):
                    game_over = True

                plot_snake(WINDOW, GREEN, snake_list, SNAKE_SIZE)

            else:
                WINDOW.fill(BLACK)
                text_screen("Game Over 😢 Press Enter to Restart", RED, 80, 150)
                text_screen(f"Your Score: {score}", BLUE, 200, 200)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        # Break inner loop to restart outer loop and reinitialize variables
                        exit_game = True
                        running = True

            pygame.display.update()
            CLOCK.tick(FPS)

        # If user closed window through quit event, stop running entirely
        if not running and exit_game:
            break
        # If they pressed enter after game over, loop continues and reinitializes
        if exit_game and running:
            # If user simply closed the window (QUIT), break entirely
            if pygame.event.peek(pygame.QUIT):
                break
            # else continue to restart
            continue

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    game_loop()
