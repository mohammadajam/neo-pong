import pygame as pg


class Wall:
    def __init__(self, x: int, y: int, width: int, height: int, colour: tuple, should_return: str):
        self.rect = pg.Rect(x, y, width, height)
        self.colour = colour
        self.should_return = should_return

    def draw(self, display: pg.Surface):
        pg.draw.rect(display, self.colour, self.rect, 0, 20)

    def collide(self, ball_x, ball_y, ball_radius):
        if self.rect.x+self.rect.width > ball_x-ball_radius and self.rect.x < ball_x+ball_radius:
            if self.rect.y+self.rect.height > ball_y-ball_radius and self.rect.y < ball_y+ball_radius:
                return self.should_return
