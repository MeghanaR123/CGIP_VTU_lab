import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
vertices = (
    (-1, -1, -1),
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, 1, 1)
)
edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
)
surfaces = (
    (0, 1, 2, 3),
    (3, 2, 6, 7),
    (7, 6, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 6, 2),
    (4, 0, 3, 7)
)
colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1)
)
def Cube():
    glBegin(GL_QUADS)
    for i, surface in enumerate(surfaces):
        glColor3fv(colors[i])
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()
    glBegin(GL_LINES)
    glColor3f(0, 0, 0)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    clock = pygame.time.Clock()
    translate = [0, 0, 0]
    rotate = [0, 0, 0]
    scale = 1
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            translate[0] -= 0.05
        if keys[pygame.K_RIGHT]:
            translate[0] += 0.05
        if keys[pygame.K_UP]:
            translate[1] += 0.05
        if keys[pygame.K_DOWN]:
            translate[1] -= 0.05
        if keys[pygame.K_x]:
            rotate[0] += 3
        if keys[pygame.K_z]:
            rotate[2] += 3
        if keys[pygame.K_y]:
            rotate[1] += 3
        if keys[pygame.K_w]:
            scale += 0.05
        if keys[pygame.K_s]:
            scale -= 0.05
        if scale < 0.05:
            scale = 0.
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glTranslatef(*translate)
        glScalef(scale, scale, scale)
        glRotatef(rotate[0], 1, 0, 0)
        glRotatef(rotate[1], 0, 1, 0)
        glRotatef(rotate[2], 0, 0, 1)
        Cube()
        glPopMatrix()
        pygame.display.flip()
        clock.tick(60)
if __name__ == "__main__":
    main()
