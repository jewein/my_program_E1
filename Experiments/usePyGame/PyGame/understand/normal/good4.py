import pygame
from pygame.locals import *
import cv2
from OpenGL.GL import *
from OpenGL.GLU import *

import random

vertices = ((1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))
edges = ((0, 1), (0, 3), (0, 4), (2, 1), (2, 3), (2, 7), (6, 3), (6, 4), (6, 7), (5, 1), (5, 4), (5, 7))
surfaces = ((0, 1, 2, 3), (3, 2, 7, 6), (6, 7, 5, 4), (4, 5, 1, 0), (1, 5, 7, 2), (4, 0, 3, 6))
colors = (
(1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 1, 0), (1, 1, 1), (0, 1, 1), (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 0, 0), (1, 1, 1),
(0, 1, 1),)


def set_vertices(max_distance, min_distance=-20):
    x_value_change = random.randrange(-10, 10)
    y_value_change = random.randrange(-10, 10)
    z_value_change = random.randrange(-1 * max_distance, min_distance)
    new_vertices = []
    for vert in vertices:
        new_vert = []
        new_x = vert[0] + x_value_change
        new_y = vert[1] + y_value_change
        new_z = vert[2] + z_value_change
        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)
        new_vertices.append(new_vert)
    return new_vertices


def Cube(vertices):
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0

        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    max_distance = 100
    gluPerspective(45, (display[0] / display[1]), 0.1, max_distance)
    glTranslatef(random.randrange(-5, 5), random.randrange(-5, 5), -40)
    # object_passed = False
    x_move = 0
    y_move = 0
    cube_dict = {}

    for x in range(50):
        cube_dict[x] = set_vertices(max_distance)

    # glRotatef(25, 2, 1, 0)

    x = glGetDoublev(GL_MODELVIEW_MATRIX)
    camera_x = x[3][0]
    camera_y = x[3][1]
    camera_z = x[3][2]
    button_down = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEMOTION:
                if button_down == True:
                    print(pygame.mouse.get_pressed())
                    glRotatef(event.rel[1], 1, 0, 0)
                    glRotatef(event.rel[0], 0, 1, 0)

        for event in pygame.mouse.get_pressed():
            # print(pygame.mouse.get_pressed())
            if pygame.mouse.get_pressed()[0] == 1:
                button_down = True
            elif pygame.mouse.get_pressed()[0] == 0:
                button_down = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for each_cube in cube_dict:
            Cube(cube_dict[each_cube])

        pygame.display.flip()
        pygame.time.Clock().tick(30)


main()
pygame.quit()
quit()

