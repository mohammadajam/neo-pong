import pygame as pg


class Ball:
    def __init__(self, x: int, y: int, radius: int, colour: tuple):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour

        self.speed_x = 5
        self.speed_y = 3

    def draw(self, display: pg.Surface):
        pg.draw.circle(display, self.colour, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def reset(self, reset_x: int, reset_y: int):
        self.x = reset_x
        self.y = reset_y
