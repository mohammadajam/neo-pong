import pygame as pg
from ball import Ball
from wall import Wall
from text import Text
from player import Player


def main():
    w, h = 1280, 720
    clock = pg.time.Clock()
    fps = 60
    colour = {
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255)
    }

    score = [
        0,  # player 1
        0  # player 2
    ]

    dis = pg.display.set_mode((w, h))
    pg.display.set_caption("Neo Pong")

    ball = Ball(int(w/2), int(h/2), 10, colour['red'])

    walls = [
        Wall(50, 50, 10, h-90, colour['white'], 'horz'),
        Wall(w-60, 50, 10, h-90, colour['white'], 'horz'),
        Wall(50, 50, w-100, 10, colour['white'], 'vert'),
        Wall(50, h-50, w-100, 10, colour['white'], 'vert')
    ]

    players = [
        Player(80, int(h/2-50), 10, 100, colour['blue'], pg.K_w, pg.K_s, 'horz'),
        Player(w-90, int(h / 2 - 50), 10, 100, colour['green'], pg.K_UP, pg.K_DOWN, 'horz')
    ]

    while True:
        clock.tick(fps)
        pg.display.update()
        dis.fill(colour['black'])
        for event in pg.event.get():
            if event.type == pg.QUIT:
                print(f'Player 1: {score[0]}     Player 2: {score[1]}')
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    print(f'Player 1: {score[0]}     Player 2: {score[1]}')
                    return

        ball.draw(dis)
        ball.move()

        Text(f"Score: {score[0]}", colour['blue'], dis, 50, 10)
        Text(f"Score: {score[1]}", colour['green'], dis, w-160, 10)

        for wall in walls:
            wall.draw(dis)
            if wall.collide(ball.x, ball.y, ball.radius) == "horz":
                if ball.x < w/2:
                    score[1] += 1
                elif ball.x > w/2:
                    score[0] += 1
                ball.speed_x *= -1
                ball.reset(int(w/2), int(h/2))

            if wall.collide(ball.x, ball.y, ball.radius) == "vert":
                ball.speed_y *= -1

        for player in players:
            player.draw(dis)
            player.move(70, 660)
            if player.collide(ball.x, ball.y, ball.radius) == 'horz':
                ball.speed_x *= -1


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
