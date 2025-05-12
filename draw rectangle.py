import pygame as p
p.init()

screen = p.display.set_mode((800,600))

done = False

while not done:
    for event in p.event.get():
        if event.type == p.QUIT:
            done = True

    p.draw.rect(screen, (0,255,0) , p.Rect(100,100,200,200))

    p.display.flip()

