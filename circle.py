import pygame as p
p.init()

screen = p.display.set_mode((800,600))

done = False

p.draw.circle(screen, (0,255,0) , (200 , 200), 50)

p.draw.circle(screen, (255,0,0) , (400 , 400) , 50 , 2)

p.display.update()


while not done:
    for event in p.event.get():
        if event.type == p.QUIT:
            done = True

    
