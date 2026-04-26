import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

pink = (255, 192, 203)
purple = (160, 32, 240)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
ERASER_COLOR = pink

radius = 7
mode = 'pen'
color = purple
draw = False
start = None

def clear_screen():
    screen.fill(pink)

clear_screen()

button_rects = {
    "Red": pygame.Rect(10, 10, 50, 30),
    "Green": pygame.Rect(10, 50, 50, 30),
    "Blue": pygame.Rect(10, 90, 50, 30),
    "Eraser": pygame.Rect(10, 130, 50, 30),
    "Circle": pygame.Rect(10, 170, 50, 30),
    "Rect": pygame.Rect(10, 210, 50, 30),
    "Square": pygame.Rect(10, 250, 70, 30),
    "Clear": pygame.Rect(10, 290, 50, 30),
    "Right Triangle": pygame.Rect(10, 330, 110, 30),
    "Equilateral Triangle": pygame.Rect(10, 370, 140, 30),
    "Rhombus": pygame.Rect(10, 410, 90, 30)
}

def draw_buttons():
    for i, j in button_rects.items():
        pygame.draw.rect(screen, purple, j, 2)
        font = pygame.font.Font(None, 20)
        label = font.render(i, True, purple)
        screen.blit(label, (j.x + 10, j.y + 5))

flag = True
while flag:
    draw_buttons()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, j in button_rects.items():
                    if j.collidepoint(event.pos):
                        if i == "Red":
                            color = red
                            mode = 'pen'
                        elif i == "Green":
                            color = green
                            mode = 'pen'
                        elif i == "Blue":
                            color = blue
                            mode = 'pen'
                        elif i == "Eraser":
                            mode = 'eraser'
                        elif i == "Circle":
                            mode = 'circle'
                        elif i == "Rect":
                            mode = 'rectangle'
                        elif i == "Square":
                            mode = 'square'
                        elif i == "Right Triangle":
                            mode = "Right Triangle"
                        elif i == "Equilateral Triangle":
                            mode = "Equilateral Triangle"
                        elif i == "Rhombus":
                            mode = "Rhombus"
                        elif i == "Clear":
                            clear_screen()
                start = event.pos
                draw = True

        if event.type == pygame.MOUSEBUTTONUP:
            if mode in ['rectangle', 'circle', 'square', "Right Triangle", "Equilateral Triangle", "Rhombus"] and start:
                end_pos = event.pos
                if mode == 'rectangle':
                    pygame.draw.rect(screen, color, (*start, end_pos[0] - start[0], end_pos[1] - start[1]), 2)
                elif mode == 'circle':
                    radius = max(abs(end_pos[0] - start[0]), abs(end_pos[1] - start[1])) // 2
                    center = ((start[0] + end_pos[0]) // 2, (start[1] + end_pos[1]) // 2)
                    pygame.draw.circle(screen, color, center, radius, 2)
                elif mode == 'square':
                    side = min(abs(end_pos[0] - start[0]), abs(end_pos[1] - start[1]))
                    pygame.draw.rect(screen, color, (start[0], start[1], side, side), 2)
                elif mode == "Right Triangle":
                    RT = [
                        (start[0], start[1]),
                        (end_pos[0], end_pos[1]),
                        (start[0], end_pos[1])
                    ]
                    pygame.draw.polygon(screen, color, RT, 2)
                elif mode == "Equilateral Triangle":
                    base_mid = ((start[0] + end_pos[0]) // 2, end_pos[1])
                    height = abs(end_pos[1] - start[1])
                    ET = [
                        (start[0], end_pos[1]),
                        (end_pos[0], end_pos[1]),
                        (base_mid[0], start[1] - height)
                    ]
                    pygame.draw.polygon(screen, color, ET, 2)
                elif mode == "Rhombus":
                    mid_x = (start[0] + end_pos[0]) // 2
                    mid_y = (start[1] + end_pos[1]) // 2
                    R = [
                        (mid_x, start[1]),
                        (end_pos[0], mid_y),
                        (mid_x, end_pos[1]),
                        (start[0], mid_y)
                    ]
                    pygame.draw.polygon(screen, color, R, 2)
            draw = False

        if event.type == pygame.MOUSEMOTION and draw:
            x, y = event.pos
            if mode == 'pen':
                pygame.draw.circle(screen, color, (x, y), radius)
            elif mode == 'eraser':
                pygame.draw.circle(screen, ERASER_COLOR, (x, y), radius)