import pygame as pg
import numpy as np

SCREEN_W, SCREEN_H = 800, 600
FOV_V = np.pi / 4  # 45 kraadi FOV - field of view, vaate nurk
FOV_H = FOV_V * SCREEN_W / SCREEN_H


def main():
    pg.init()

    screen = pg.display.set_mode((SCREEN_W, SCREEN_H), vsync=1)
    pg.display.set_caption("3D test")
    running = True
    clock = pg.time.Clock()
    surf = pg.surface.Surface((SCREEN_W, SCREEN_H))

    # points = np.asarray([[1, 1, 1, 1, 1], [4, 2, 0, 1, 1], [1, .5, 3, 1, 1]])
    # triangles = np.asarray([[0, 1, 2]])

    points, triangles = read_obj('objects/teapot.obj')

    camera = np.asarray([13, .5, 2, 3.3, 0])

    while running:
        clock.tick(60)
        [quit() for event in pg.event.get() if event.type == pg.QUIT]

        surf.fill((125, 125, 255))

        project_points(points, camera)

        for index in range(len(triangles)):
            triangle = [points[triangles[index][0]][3:], points[triangles[index][1]][3:],
                        points[triangles[index][2]][3:]]
            color = [255, 255, 0]
            pg.draw.polygon(surf, color, triangle)

        screen.blit(surf, (0, 0))
        pg.display.update()


def project_points(points, camera):
    for point in points:
        # calculate xy angle of vector from camera point to projection point
        h_angle_camera_point = np.arctan((point[2] - camera[2]) / (point[0] - camera[0] + 1e-16))

        # check if point isn't pointing wrong direction
        if abs(camera[0] + np.cos(h_angle_camera_point) - point[0]) > abs(camera[0] - point[0]):
            h_angle_camera_point = (h_angle_camera_point - np.pi) % (2 * np.pi)

        # Calculate difference between camera angle and pointing angle
        h_angle = (h_angle_camera_point - camera[3]) % (2 * np.pi)

        # Bring to -pi to pi range
        if h_angle > np.pi: h_angle = h_angle - 2 * np.pi

        # Calculate the point horizontal screen coordinate
        point[3] = SCREEN_W * h_angle / FOV_H + SCREEN_W / 2

        # Calculate xy distance from camera point to projection point
        distance = np.sqrt((point[0] - camera[0]) ** 2 + (point[1] - camera[1]) ** 2 + (point[2] - camera[2]) ** 2)

        # Calculate angle to xy plane
        v_angle_camera_point = np.arcsin((camera[1] - point[1]) / distance)

        # Calculate difference between camera verticam angle and pointing vertical angle
        v_angle = (v_angle_camera_point - camera[4]) % (2 * np.pi)

        # Bring to -pi to pi range
        if v_angle > np.pi: v_angle = v_angle - 2 * np.pi

        # Calculate the point vertical screen coordinate
        point[4] = SCREEN_H * v_angle / FOV_V + SCREEN_H / 2


def read_obj(filename):
    vertices = []
    triangles = []
    f = open(filename)
    for line in f:
        if line[:2] == "v ":
            index1 = line.find("") + 1
            index2 = line.find("", index1 + 1)
            index3 = line.find("", index2 + 1)
            vertex = [float(line[index1:index2]), float(line[index2:index3]), float(line[index3:-1]), 1, 1]
            vertices.append(vertex)
        elif line[0] == "f":
            index1 = line.find("") + 1
            index2 = line.find("", index1 + 1)
            index3 = line.find("", index2 + 1)
            triangles.append([int(line[index1:index2]) - 1, int(line[index2:index3]) - 1, int(line[index3:-1]) - 1])
    f.close()
    return np.asarray(vertices), np.asarray(triangles)


if __name__ == "__main__":
    main()
