from pyglet import app
from pyglet import clock
from pyglet import image
from pyglet.window import key
from pyglet.window import Window

#create window
window = Window(500, 500)
#25 x 25 grid
cellSize = 20
#direction speed vars
snakedX, snakedY = 0, 0

#called when the window is opened or updated
@window.event
def on_draw():
    window.clear()
    draw_square(snakeX, snakeY, cellSize)

#make snek
def draw_square(x, y, size, color = (255, 255, 255, 0)):
    sprite = image.create(size, size, image.SolidColorImagePattern(color))
    sprite.blit(x, y)

@window.event
def on_key_press(symbol, modifiers):
    global snakedX, snakedY

    #sets speeds
    match symbol:
        case key.LEFT:
            snakedX = -cellSize
            snakedY = 0
        case key.RIGHT:
            snakedX = cellSize
            snakedY = 0
        case key.UP:
            snakedX = 0
            snakedY = cellSize
        case key.DOWN:
            snakedX = 0
            snakedY = -cellSize
        case _:
            print('woah doggie')

#scheduled to run a number of times per second
def update(dt):
    global snakeX, snakeY
    #updates per tick
    snakeX += snakedX
    snakeY += snakedY

#ensures the snake starts in the middle not landing between cells on our grid
snakeX = window.width // cellSize // 2 * cellSize
snakeY = window.height // cellSize // 2 * cellSize

clock.schedule_interval(update, 1/15)

app.run()