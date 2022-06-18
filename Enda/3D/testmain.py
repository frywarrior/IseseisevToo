import pygame as py

py.init()

SCREEN_W, SCREEN_H = 640, 480
SCREEN = py.display.set_mode((SCREEN_W, SCREEN_H), vsync=1)
py.display.set_caption("3D test")

clock = py.time.Clock()


def vec3d(x, y):
    return [x, y]


def triangle(vec, vec2, vec3):
    s_w, s_h = SCREEN_W / 2, SCREEN_H / 2
    points = vec
    points[0], points[1] = points[0] + s_w, points[1] + s_h

    points2 = vec2
    points2[0], points2[1] = points2[0] + s_w, points2[1] + s_h

    points3 = vec3
    points3[0], points3[1] = points3[0] + s_w, points3[1] + s_h

    return py.draw.polygon(SCREEN, "white", (points, points2, points3), 1)


def mesh():
    pass


def main():
    running = True
    while running:
        clock.tick(60)
        [quit() for event in py.event.get() if event.type == py.QUIT]
        py.display.update()
        triangle([0, 0], [50, 50], [0, 50])

main()
