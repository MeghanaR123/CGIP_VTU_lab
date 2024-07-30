#Develop a program to demonstrate basic geometric operations on the 2D object
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
# Initialize Pygame and set up an OpenGL display
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glClearColor(1, 1, 1, 1) # Set background color to white
# Set up the view
glMatrixMode(GL_PROJECTION) 
glLoadIdentity()
gluOrtho2D(0, display[0], 0, display[1])
glMatrixMode(GL_MODELVIEW)
# Triangle properties
tri_x, tri_y = display[0] // 2, display[1] // 2
angle = 0
scale = 1
def draw_triangle(x, y, angle, scale):
    glPushMatrix()
    glTranslatef(x, y, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)
    glScalef(scale, scale, 1.0)
    
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 1.0) # Blue color
    glVertex2f(0, 50) # Top vertex
    glVertex2f(-50, -50) # Bottom left vertex
    glVertex2f(50, -50) # Bottom right vertex
    glEnd()
    
    glPopMatrix()
# Main loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
   tri_x -= 5 # Translate left
  if keys[pygame.K_RIGHT]:
   tri_x += 5 # Translate right
  if keys[pygame.K_UP]:
   tri_y += 5 # Translate up
  if keys[pygame.K_DOWN]:
   tri_y -= 5 # Translate down
  if keys[pygame.K_q]:
   angle += 5 # Rotate counter-clockwise
  if keys[pygame.K_e]:
   angle -= 5 # Rotate clockwise
  if keys[pygame.K_w]:
   scale += 0.1 # Scale up
  if keys[pygame.K_s]:
   scale -= 0.1 # Scale down
  if scale < 0.1:
   scale = 0.1
  glClear(GL_COLOR_BUFFER_BIT)
  draw_triangle(tri_x, tri_y, angle, scale)
  pygame.display.flip()
  pygame.time.wait(30)
pygame.quit()
