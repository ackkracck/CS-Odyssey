import turtle
import pygame
import random
import sys

# ---------------------
# TURTLE SETUP (Race)
# ---------------------
wn = turtle.Screen()
wn.title("Turtle Skill Race")
wn.bgcolor("lightblue")
wn.setup(width=800, height=600)

# Draw finish line
finish_line = 250
line = turtle.Turtle()
line.hideturtle()
line.penup()
line.goto(finish_line, 200)
line.pendown()
line.right(90)
line.forward(400)

# Create turtles
player = turtle.Turtle(shape="turtle")
player.color("green")
player.penup()
player.goto(-300, 50)

opponent = turtle.Turtle(shape="turtle")
opponent.color("red")
opponent.penup()
opponent.goto(-300, -50)

# Scoreboard turtle
scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(0, 250)

# Announcer turtle
announcer = turtle.Turtle()
announcer.hideturtle()
announcer.penup()
announcer.goto(0, 200)

# Celebration turtle
celebrator = turtle.Turtle()
celebrator.hideturtle()
celebrator.speed(0)

player_score = 0
opponent_score = 0
round_number = 0

def update_scoreboard():
    scoreboard.clear()
    scoreboard.write(
        f"Round: {round_number} | Player: {player_score} | Opponent: {opponent_score}",
        align="center",
        font=("Arial", 16, "bold")
    )

def announce_winner(message):
    announcer.clear()
    announcer.write(message, align="center", font=("Arial", 14, "normal"))

# ---------------------
# SOUND SETUP
# ---------------------
pygame.init()
pygame.mixer.init()

try:
    cheer_sound = pygame.mixer.Sound("cheer.wav")
    buzzer_sound = pygame.mixer.Sound("buzzer.wav")
    click_sound = pygame.mixer.Sound("click.wav")
except:
    cheer_sound = buzzer_sound = click_sound = None

def play_sound(sound):
    if sound:
        sound.play()

def celebrate(message, winner=True):
    announcer.clear()
    announcer.write(message, align="center", font=("Arial", 20, "bold"))
    
    colors = ["red", "yellow", "blue", "green", "purple", "orange"]
    for _ in range(30):
        celebrator.penup()
        celebrator.goto(random.randint(-300, 300), random.randint(-200, 200))
        celebrator.dot(random.randint(10, 30), random.choice(colors))
    
    if winner:
        play_sound(cheer_sound)
    else:
        play_sound(buzzer_sound)

# ---------------------
# PYGAME MINI-GAMES
# ---------------------
FONT = pygame.font.Font(None, 48)

# Typing challenge
def typing_challenge():
    screen = pygame.display.set_mode((500, 200))
    pygame.display.set_caption("Typing Challenge")
    word = random.choice(["python", "turtle", "race", "coding", "pygame"])
    typed = ""
    clock = pygame.time.Clock()
    
    while True:
        screen.fill((255, 255, 255))
        text = FONT.render(f"Type: {word}", True, (0, 0, 0))
        screen.blit(text, (50, 50))
        typed_text = FONT.render(typed, True, (0, 128, 0))
        screen.blit(typed_text, (50, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return typed == word
                elif event.key == pygame.K_BACKSPACE:
                    typed = typed[:-1]
                else:
                    typed += event.unicode

        pygame.display.flip()
        clock.tick(30)

# Click challenge
def click_challenge():
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Click Challenge")
    clock = pygame.time.Clock()

    target = pygame.Rect(random.randint(50, 450), random.randint(50, 450), 50, 50)

    while True:
        screen.fill((200, 200, 255))
        pygame.draw.rect(screen, (255, 0, 0), target)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                play_sound(click_sound)
                return target.collidepoint(event.pos)

        pygame.display.flip()
        clock.tick(30)

# Math challenge
def math_challenge():
    screen = pygame.display.set_mode((500, 200))
    pygame.display.set_caption("Math Challenge")
    clock = pygame.time.Clock()

    a, b = random.randint(1, 10), random.randint(1, 10)
    answer = str(a + b)
    typed = ""

    while True:
        screen.fill((255, 255, 255))
        text = FONT.render(f"{a} + {b} = ?", True, (0, 0, 0))
        screen.blit(text, (50, 50))
        typed_text = FONT.render(typed, True, (0, 128, 0))
        screen.blit(typed_text, (50, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return typed == answer
                elif event.key == pygame.K_BACKSPACE:
                    typed = typed[:-1]
                else:
                    typed += event.unicode

        pygame.display.flip()
        clock.tick(30)

# Reaction challenge
def reaction_challenge():
    screen = pygame.display.set_mode((500, 300))
    pygame.display.set_caption("Reaction Challenge")
    clock = pygame.time.Clock()

    waiting = True
    start_time = None

    while True:
        if waiting:
            screen.fill((100, 100, 100))
            text = FONT.render("Wait for green...", True, (255, 255, 255))
            screen.blit(text, (100, 120))
            pygame.display.flip()
            pygame.time.wait(random.randint(1000, 3000))
            waiting = False
            start_time = pygame.time.get_ticks()
        else:
            screen.fill((0, 255, 0))
            text = FONT.render("PRESS SPACE!", True, (0, 0, 0))
            screen.blit(text, (120, 120))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        reaction_time = pygame.time.get_ticks() - start_time
                        return reaction_time < 1000  # must react within 1 sec

            pygame.display.flip()
            clock.tick(30)

# Dodge challenge (arcade-style)
def dodge_challenge():
    screen = pygame.display.set_mode((500, 400))
    pygame.display.set_caption("Dodge Challenge")
    clock = pygame.time.Clock()

    player = pygame.Rect(225, 350, 50, 20)
    obstacles = [pygame.Rect(random.randint(0, 450), -50, 50, 20)]
    speed = 5
    survived = 0

    while True:
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 255, 0), player)

        for obs in obstacles:
            pygame.draw.rect(screen, (255, 0, 0), obs)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.move_ip(-7, 0)
        if keys[pygame.K_RIGHT] and player.right < 500:
            player.move_ip(7, 0)

        # Move obstacles
        for obs in obstacles:
            obs.move_ip(0, speed)
            if obs.colliderect(player):
                play_sound(buzzer_sound)
                return False
        
        # Add new obstacles
        if random.randint(1, 20) == 1:
            obstacles.append(pygame.Rect(random.randint(0, 450), -50, 50, 20))

        survived += 1
        if survived > 150:  # survive for a short time
            play_sound(cheer_sound)
            return True

        pygame.display.flip()
        clock.tick(30)

# Catch challenge (catch falling objects)
def catch_challenge():
    screen = pygame.display.set_mode((500, 400))
    pygame.display.set_caption("Catch Challenge")
    clock = pygame.time.Clock()

    basket = pygame.Rect(225, 350, 50, 20)
    fruit = pygame.Rect(random.randint(0, 450), -50, 30, 30)
    speed = 5

    while True:
        screen.fill((255, 255, 200))
        pygame.draw.rect(screen, (0, 0, 255), basket)
        pygame.draw.ellipse(screen, (255, 100, 0), fruit)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket.left > 0:
            basket.move_ip(-7, 0)
        if keys[pygame.K_RIGHT] and basket.right < 500:
            basket.move_ip(7, 0)

        fruit.move_ip(0, speed)

        if fruit.colliderect(basket):
            play_sound(cheer_sound)
            return True
        if fruit.top > 400:
            play_sound(buzzer_sound)
            return False

        pygame.display.flip()
        clock.tick(30)

# ---------------------
# GAME LOOP
# ---------------------
challenges = [typing_challenge, click_challenge, math_challenge, reaction_challenge, dodge_challenge, catch_challenge]

while True:
    round_number += 1
    challenge = random.choice(challenges)
    result = challenge()

    if result:
        player.forward(50)
        player_score += 1
        announce_winner(f"Round {round_number}: Player wins!")
        play_sound(cheer_sound)
    else:
        opponent.forward(50)
        opponent_score += 1
        announce_winner(f"Round {round_number}: Opponent wins!")
        play_sound(buzzer_sound)

    update_scoreboard()

    if player.xcor() >= finish_line:
        celebrate("🎉 Player Wins the Race! 🎉", winner=True)
        wn.mainloop()
        break
    elif opponent.xcor() >= finish_line:
        celebrate("💀 Opponent Wins the Race! 💀", winner=False)
        wn.mainloop()
        break
