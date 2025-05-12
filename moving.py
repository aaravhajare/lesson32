import pygame as p
p.init()
screen = p.display.set_mode((800,600))
p.display.set_caption("Moving square")

colors = {
  "red" : p.color("red"),
  "green" : p.color("green"),
  "yellow" : p.color("yellow"),
  "blue" : p.color("blue"),
  "white" : p.color("white")
}
d_color = colors["white"]

x,y = 30 , 30

sprite_w , sprite_h = 60 , 60

clock = p.time.Clock()

done = False

while not done:
    for event in p.event.get():
        if event.type == p.QUIT:
            done = True

    keys = p.key.get_pressed()

    if keys[p.K_LEFT]:x -= 5
    if keys[p.K_RIGHT]:x += 5
    if keys[p.K_UP]:y -= 5
    if keys[p.K_DOWN]:y += 5

    x = min(max(x,0) , 800 - sprite_w)
    y = min(max(y,0) , 600 - sprite_h)

    if x == 0 : d_color = colors["red"]
    elif x == 800 - sprite_w : d_color = colors["green"]