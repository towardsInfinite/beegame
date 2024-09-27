import pgzrun
from random import randint

TITLE = "SHOOT THE ALIEN"
WIDTH = 800
HEIGHT = 600

message = ""

alien = Actor("alien")
alien.pos = 50, 50

def draw():
    screen.clear()  # Added parentheses to clear the screen
    screen.fill(color=(128, 0, 0))
    alien.draw()
    screen.draw.text(message, center=(400, 40), fontsize=30)

def place_alien():
    alien.x = randint(50, WIDTH - 50)
    alien.y = randint(50, HEIGHT - 50)

def on_mouse_down(pos):
    global message  # Declaring 'message' as global so we can modify the global variable
    if alien.collidepoint(pos):
        message = "Good shot!"
        place_alien()
    else:
        message = "You missed!"

place_alien()
pgzrun.go()
