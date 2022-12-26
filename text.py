import pygame as pg


class Text:
    def __init__(self, text: str, colour: tuple, display: pg.Surface, x: int, y: int):
        self.font = pg.font.SysFont('timesnewroman', 32)
        self.text = self.font.render(f'{text}', True, colour)
        display.blit(self.text, (x, y))
