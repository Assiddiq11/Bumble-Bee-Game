import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500

score = 0
game_over = False


bee = Actor("bee")
bee.pos = 200,200


flower = Actor("flower")
flower.pos = 200,300


def draw():
    screen.blit("background",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score"+str(score)color="black",topleft = (10,10))
    if game_over:
        screen.fill("Blue")
        screen.draw.text("score"+str(score))