from pyglet import app
from pyglet import clock
from pyglet import image
from pyglet import text
from pyglet.media import Player, load
from pyglet.window import key, Window
from random import SystemRandom
import sys

#create window
window = Window(500, 500)

#25 x 25 grid
cellSize = 20

#ensures the snake starts in the middle not landing between cells on our grid
foodX, foodY = 0, 0
gameOver = False
snakeX = window.width // cellSize // 2 * cellSize
snakeY = window.height // cellSize // 2 * cellSize
snake_dX, snake_dY = 0, 0
snakeTail = []
tailLength = 0
audioPlayer = Player()
wavFile = load('Audio/eat_food.wav', streaming = False)

#called when the window is opened or updated
@window.event
def on_draw():
    window.clear()
    draw_square(snakeX, snakeY, cellSize)
    draw_square(foodX, foodY, cellSize, (130, 25, 25, 0))
    for coords in snakeTail:
        draw_square(coords[0], coords[1], cellSize, (133, 133, 133, 0))
    if gameOver:
        screenText.draw()

@window.event
def on_key_press(symbol, modifiers):
    global snake_dX, snake_dY
    if not gameOver:
        #sets speeds
        if symbol == key.RIGHT or symbol == key.D:
            if snake_dX != -cellSize:
                snake_dX = cellSize
                snake_dY = 0
        elif symbol == key.LEFT or symbol == key.A:
            if snake_dX != cellSize:
                snake_dX = -cellSize
                snake_dY = 0
        elif symbol == key.UP or symbol == key.W:
            if snake_dY != cellSize:
                snake_dX = 0
                snake_dY = cellSize
        elif symbol == key.DOWN or symbol == key.S:
            if snake_dY != cellSize:
                snake_dX = 0
                snake_dY = -cellSize
    else:
        if symbol == key.SPACE:
            new_game()

def body_check():
    global gameOver
    for coords in snakeTail:
        if coords == [snakeX, snakeY]:
            gameOver = True

#make snek
def draw_square(x, y, size, color = (255, 255, 255, 0)):
    sprite = image.create(size, size, image.SolidColorImagePattern(color))
    sprite.blit(x, y)

def game_over_screen():
    global screenText
    screenText = text.Label(f'Game Over\n Score: {tailLength}\n(press space to play again)',
                          font_name = 'Times New Roman',
                          font_size = 24,
                          x = window.width//2, y = window.height//2,
                          anchor_x = 'center', anchor_y = 'center',
                          multiline = True, width = window.width,
                          align = 'center')

#for snek
def wall_check():
    global gameOver
    #set bounds
    if snakeX >= cellSize * 25 or snakeY >= cellSize * 25:
        gameOver = True
    if snakeX < cellSize * 0 or snakeY < cellSize * 0:
        gameOver = True

def create_food():
    global foodX, foodY
    #set food spawn
    foodX = t_rng(0, 24) * cellSize
    foodY = t_rng(0, 24) * cellSize

def eat_food():
    global snakeTail
    play_sound()
    snakeTail.append(lastPos)
    create_food()

def move_snake():
    global snakeTail, snakeX, snakeY, tailLength
    #head movement
    snakeX += snake_dX
    snakeY += snake_dY
    tailLength = len(snakeTail)
    #tail movement
    snakeTail.append(lastPos)
    if tailLength >= 1:
        x = tailLength - 1
        while x >= 0:
            snakeTail[x] = snakeTail[x - 1]
            x -= 1
    snakeTail.pop()

def new_game():
    global gameOver, snakeTail, snakeX, snakeY, snake_dX, snake_dY
    gameOver = False
    snakeTail = []
    snakeX = window.width // cellSize // 2 * cellSize
    snakeY = window.height // cellSize // 2 * cellSize
    snake_dX, snake_dY = 0, 0

def play_sound():
    if not audioPlayer.playing:
        audioPlayer.queue(wavFile)
        audioPlayer.play()

def t_rng(lower, upper):
    rng = SystemRandom()
    randomNumber = rng.randint(lower, upper)
    return randomNumber

def update(dt):
    global lastPos, snake_dX, snake_dY
    lastPos = [snakeX, snakeY]
    if snakeX == foodX and snakeY == foodY:
        eat_food()
    if not gameOver:
        move_snake()
    
    #boundaries for snek
    wall_check()
    body_check()
    if gameOver:
        game_over_screen()

#initial
create_food()

#clock
clock.schedule_interval(update, 1/15)

app.run()