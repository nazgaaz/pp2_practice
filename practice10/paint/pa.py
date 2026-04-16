import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# Colors
PINK = (255, 192, 203)
PURPLE = (160, 32, 240)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
BLACK = (0, 0, 0)

ERASER_COLOR = PINK

radius = 7
mode = 'pen'
color = PURPLE
drawing = False
start_pos = None

font = pygame.font.Font(None, 20)

# Fill background
def clear_screen():
    screen.fill(PINK)

clear_screen()

# Buttons
button_rects = {
    "Red": pygame.Rect(10, 10, 70, 30),
    "Green": pygame.Rect(10, 50, 70, 30),
    "Blue": pygame.Rect(10, 90, 70, 30),
    "Eraser": pygame.Rect(10, 130, 70, 30),
    "Circle": pygame.Rect(10, 170, 70, 30),
    "Rect": pygame.Rect(10, 210, 70, 30),
    "Clear": pygame.Rect(10, 250, 70, 30),
}

def draw_buttons():
    for name, rect in button_rects.items():
        pygame.draw.rect(screen, PURPLE, rect, 2)
        label = font.render(name, True, PURPLE)
        screen.blit(label, (rect.x + 8, rect.y + 8))

def get_button_clicked(pos):
    for name, rect in button_rects.items():
        if rect.collidepoint(pos):
            return name
    return None

flag = True
while flag:
    draw_buttons()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicked_button = get_button_clicked(event.pos)

                if clicked_button == "Red":
                    color = RED
                    mode = 'pen'
                elif clicked_button == "Green":
                    color = GREEN
                    mode = 'pen'
                elif clicked_button == "Blue":
                    color = BLUE
                    mode = 'pen'
                elif clicked_button == "Eraser":
                    mode = 'eraser'
                elif clicked_button == "Circle":
                    mode = 'circle'
                elif clicked_button == "Rect":
                    mode = 'rectangle'
                elif clicked_button == "Clear":
                    clear_screen()
                else:
                    # Start drawing only if user clicked outside the buttons
                    start_pos = event.pos
                    drawing = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if drawing and start_pos is not None:
                    end_pos = event.pos

                    if mode == 'rectangle':
                        x = min(start_pos[0], end_pos[0])
                        y = min(start_pos[1], end_pos[1])
                        w = abs(end_pos[0] - start_pos[0])
                        h = abs(end_pos[1] - start_pos[1])
                        pygame.draw.rect(screen, color, (x, y, w, h), 2)

                    elif mode == 'circle':
                        center = ((start_pos[0] + end_pos[0]) // 2,
                                  (start_pos[1] + end_pos[1]) // 2)
                        radius = max(abs(end_pos[0] - start_pos[0]),
                                     abs(end_pos[1] - start_pos[1])) // 2
                        pygame.draw.circle(screen, color, center, radius, 2)

                drawing = False
                start_pos = None

        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                x, y = event.pos
                if mode == 'pen':
                    pygame.draw.circle(screen, color, (x, y), radius)
                elif mode == 'eraser':
                    pygame.draw.circle(screen, ERASER_COLOR, (x, y), radius)

pygame.quit()