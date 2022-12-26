import pygame as pg


class Player:
    def __init__(self, x: int, y: int, width: int, height: int, colour: tuple, up_key, down_key, should_return: str):
        self.rect = pg.Rect(x, y, width, height)
        self.colour = colour

        self.up_key = up_key
        self.down_key = down_key

        self.should_return = should_return

        self.speed = 10

    def draw(self, display: pg.Surface):
        pg.draw.rect(display, self.colour, self.rect, 0, 5)

    def move(self, upper_limit, lower_limit):
        keys = pg.key.get_pressed()
        if self.rect.y >= upper_limit:
            if keys[self.up_key]:
                self.rect.y -= self.speed
        if self.rect.y+self.rect.height <= lower_limit:
            if keys[self.down_key]:
                self.rect.y += self.speed

    def collide(self, ball_x, ball_y, ball_radius):
        if self.rect.x + self.rect.width > ball_x - ball_radius and self.rect.x < ball_x + ball_radius:
            if self.rect.y + self.rect.height > ball_y - ball_radius and self.rect.y < ball_y + ball_radius:
                return self.should_return
