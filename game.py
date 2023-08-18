import pyglet
from pyglet.window import key
from pyglet.window import mouse

window = pyglet.window.Window()
image = pyglet.resource.image('sprite.png')

event_logger = pyglet.window.event.WindowEventLogger()
window.push_handlers(event_logger)

@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)

@window.event
def on_key_press(symbol, modifiers):
    print('A key was pressed')

pyglet.app.run()