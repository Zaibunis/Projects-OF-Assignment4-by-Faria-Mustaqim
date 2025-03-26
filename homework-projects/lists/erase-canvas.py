import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 500
CELL_SIZE = 25
ERASER_SIZE = 50

# Colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Canvas Eraser")

# Create grid
rows, cols = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
grid = [[BLUE for _ in range(cols)] for _ in range(rows)]

# Main loop
running = True
eraser = pygame.Rect(0, 0, ERASER_SIZE, ERASER_SIZE)
while running:
    screen.fill(WHITE)
    
    # Draw grid
    for r in range(rows):
        for c in range(cols):
            pygame.draw.rect(screen, grid[r][c], (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    # Move eraser with mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()
    eraser.topleft = (mouse_x - ERASER_SIZE // 2, mouse_y - ERASER_SIZE // 2)
    
    # Erase cells
    if pygame.mouse.get_pressed()[0]:  # Left mouse button
        for r in range(rows):
            for c in range(cols):
                cell_rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                if eraser.colliderect(cell_rect):
                    grid[r][c] = WHITE
    
    # Draw eraser
    pygame.draw.rect(screen, WHITE, eraser, border_radius=10)
    pygame.draw.rect(screen, (200, 200, 200), eraser, 2)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.quit()
