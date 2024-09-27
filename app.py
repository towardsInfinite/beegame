import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500

score = 0
game_over = False

bee = Actor("bee")  # Corrected the assignment
bee.pos = 100, 100

flower = Actor("flower")
flower.pos = 200, 200

def draw():
    screen.blit("background", (0, 0))
    flower.draw()
    bee.draw()
    screen.draw.text("score: " + str(score), color="black", topleft=(10, 20))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Times up! " + str(score), midtop=(WIDTH / 2, 10), fontsize=40, color='red')  # Corrected WIDTH usage

def place_flower():
    flower.x = randint(70, WIDTH - 70)  # Used WIDTH instead of width
    flower.y = randint(70, HEIGHT - 70)  # Used HEIGHT instead of width

def time_up():
    global game_over
    game_over = True

def update():
    global score  # Ensure the global score is updated
    
    if keyboard.left:
        bee.x -= 2
    if keyboard.right:
        bee.x += 2
    if keyboard.up:
        bee.y -= 2
    if keyboard.down:  # Corrected to keyboard.down
        bee.y += 2
    
    if bee.colliderect(flower):  # Fixed the method name to colliderect
        score += 10
        place_flower()

clock.schedule(time_up, 10.0)

pgzrun.go()
