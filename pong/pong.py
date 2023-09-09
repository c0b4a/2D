from pyglet import app
from pyglet import clock
from pyglet import image
from pyglet import text
from pyglet.media import Player, load
from pyglet.window import key, Window
from random import SystemRandom
import sys

#splits to 40*31
CELL_SIZE = 20

#create window
window = Window(820, 620)

class PlayerClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.d_Y = 0
        #make main body
        self.body = ((x,y))

#called when the window is opened or updated
@window.event
def on_draw():
    window.clear()
    draw_player()
    draw_opponent()
    draw_background()
    if gameOver:
        screenText.draw()

@window.event
def on_key_press(symbol, modifiers):
    global player
    if not gameOver:
        #sets speeds
        if symbol == key.UP or symbol == key.W:
            player.d_Y = CELL_SIZE
        if symbol == key.DOWN or symbol == key.S:
            player.d_Y = -CELL_SIZE
        if symbol == None:
            player.d_Y = 0
    else:
        if symbol == key.SPACE:
            new_game()

#def contact_check():
#    global gameOver
#    if ballLoc:
#        if coords == [playerX, playerY]:
#            gameOver = True

def create_background():
    background = []
    #draws divider
    for y in range(window.width // CELL_SIZE):
        if y % 2 == 1:
            background.append((window.width // CELL_SIZE // 2 * CELL_SIZE, y * CELL_SIZE))
    #draws borders
    for x in range(window.width // CELL_SIZE):
        background.append((x * CELL_SIZE, 0 * CELL_SIZE))
        background.append((x * CELL_SIZE, window.height - CELL_SIZE))
    return background

def draw_background():
    for coords in background:
        draw_square(coords[0], coords[1], CELL_SIZE)

def draw_square(x, y, size, color = (255, 255, 255, 0)):
    sprite = image.create(size, size, image.SolidColorImagePattern(color))
    sprite.blit(x, y)

def draw_opponent():
    currentLength = 0
    y = opponent.y - CELL_SIZE
    #prints three body squares
    while currentLength < bodyLength:
        draw_square(opponent.x, y, CELL_SIZE)
        y += CELL_SIZE
        currentLength += 1

def draw_player():
    currentLength = 0
    y = player.y - CELL_SIZE
    #prints three body squares
    while currentLength < bodyLength:
        draw_square(player.x, y, CELL_SIZE)
        y += CELL_SIZE
        currentLength += 1

def game_over_screen():
    global screenText
    screenText = text.Label(f'Game Over\n Score: {score}\n(press space to play again)',
                          font_name = 'Times New Roman',
                          font_size = 24,
                          x = window.width//2, y = window.height//2,
                          anchor_x = 'center', anchor_y = 'center',
                          multiline = True, width = window.width,
                          align = 'center')

def move_player():
    global player
    if player.d_Y > 0:
        if player.y < 28 * CELL_SIZE:
            player.y += player.d_Y
    elif player.d_Y < 0:
        if player.y > 2 * CELL_SIZE:
            player.y += player.d_Y
    elif player.d_Y == 0:
        player.y = player.y

#def new_game():

#def play_sound(wavFile):
#    if not audioPlayer.playing:
#        audioPlayer.queue(wavFile)
#        audioPlayer.play()

def set_clock(clockSpeed = 1/15):
    clock.schedule_interval(update, clockSpeed)

def update(dt):
    if not gameOver:
        move_player()
    if gameOver:
        game_over_screen()

#audio handler
audioPlayer = Player()
background = create_background()
bodyLength = 3

#wavs
bounceWav = load('audio/bounce.wav', streaming = False)

#default game status
gameOver = False
score = 0

#establish players
player = PlayerClass(0, window.height // CELL_SIZE // 2 * CELL_SIZE)
opponent = PlayerClass(window.width - 1 * CELL_SIZE, window.height // CELL_SIZE // 2 * CELL_SIZE)

#clock
set_clock()

app.run()