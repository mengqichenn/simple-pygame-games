import pygame
from english_words import get_english_words_set
import random
import os
from datetime import date


# ======================== path ===================================
DIR = os.path.dirname(os.path.abspath(__file__))
FEATURE = os.path.join(DIR, "feature")

BEST_SCORE_FILE = os.path.join(DIR, "best_score.txt")
BACKGROUND = os.path.join(FEATURE, "fond.png")
MUSIC = os.path.join(FEATURE, "tatamusic-game-gaming-video-game-music-482380.mp3")

WIN = os.path.join(FEATURE, "win.mp3")
LOSE = os.path.join(FEATURE, "lose.mp3")

# ======================== pygame setup ===================================

pygame.init()

WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# FIX : il faut charger l'image avant de la redimensionner
if os.path.exists(BACKGROUND):
    background = pygame.image.load(BACKGROUND).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
else:
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill((35, 40, 55))

pygame.display.set_caption("Hangman")


if os.path.exists(MUSIC):
    pygame.mixer.music.load(MUSIC)
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
else:
    print("Background music not found. Playing without music.")

win_sound = pygame.mixer.Sound(WIN)
lose_sound = pygame.mixer.Sound(LOSE)
clock = pygame.time.Clock()

# ======================== words set ===================================

english_word_set = get_english_words_set(['web2'], lower=True)

word_list = [
        word for word in english_word_set
        if 4 <= len(word) <= 14 and word.isalpha()
    ]

def pick_word():
    return random.choice(word_list).lower()


# ======================== output file ===================================

def load_best_score():
    
    if not os.path.exists(BEST_SCORE_FILE):
        return None

    # with open()  <--- "w" write / "a" append / "r" read
    with open(BEST_SCORE_FILE, "r") as file:
        content = file.read().strip()   # read if there is content in the BEST_SCORE_FILE
    # if so, extract first the second part with seperator "--" and then extract the first value then transform into integer
    try:
        return int(content.split("--")[1].split()[0])
    except (IndexError, ValueError):
        return None


def save_best_score(score):

    actual_date = date.today().strftime("%Y-%m-%d")

    with open(BEST_SCORE_FILE, "w") as file:
        file.write(f"{actual_date} -- {score} attempts")


def format_time(milliseconds):
    total_seconds = milliseconds // 1000
    minutes = total_seconds // 60
    secs = total_seconds % 60
    centisecs = (milliseconds % 1000) // 10   # les 2 premiers chiffres des millisecondes
    return f"{minutes:02d}:{secs:02d}.{centisecs:02d}"


# ======================== colors =========================================

WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
GRAY = (180, 180, 180)
DARK_GRAY = (60, 60, 60)
BLUE = (70, 130, 180)
GREEN = (70, 170, 90)
RED = (200, 70, 70)
YELLOW = (230, 190, 60)
BROWN = (125, 63, 0)
SABLE = (174, 100, 26)


# ======================== graphics =========================================

title_font = pygame.font.Font(None, 80)
big_font = pygame.font.Font(None, 60)
medium_font = pygame.font.Font(None, 40)
small_font = pygame.font.Font(None, 28)


# def draw_text

def draw_text(text, font, color, x, y):

    surface = font.render(text, True, color)

    rect = surface.get_rect(center=(x, y))

    screen.blit(surface, rect)


def draw_text_fitted(text, font, color, x, y, max_width):
    """Comme draw_text, mais réduit le texte s'il dépasse max_width."""
    surface = font.render(text, True, color)
    if surface.get_width() > max_width and surface.get_width() > 0:
        ratio = max_width / surface.get_width()
        new_size = (max(1, int(surface.get_width() * ratio)),
                    max(1, int(surface.get_height() * ratio)))
        surface = pygame.transform.smoothscale(surface, new_size)
    rect = surface.get_rect(center=(x, y))
    screen.blit(surface, rect)


# to draw a button

def draw_button(rect, text, color):

    pygame.draw.rect(screen, color, rect, border_radius=10)

    draw_text(text, medium_font, WHITE, rect.centerx, rect.centery)


# to add a menu

def menu():

    running = True

    while running:

        screen.blit(background, (0, 0))

        draw_text("HANGMAN GAME", title_font, BLACK, WIDTH // 2, 150)

        play_rect = pygame.Rect(WIDTH // 2 - 125, 280, 250, 70)

        quit_rect = pygame.Rect(WIDTH // 2 - 125, 390, 250, 70)

        draw_button(play_rect, "PLAY", BLUE)

        draw_button(quit_rect, "QUIT", RED)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:

                if play_rect.collidepoint(event.pos):
                    return "game"

                if quit_rect.collidepoint(event.pos):
                    return "quit"


        pygame.display.flip()
        clock.tick(60)


# ======================== pics =========================================

def draw_hangman(penalty):

     # Base
    pygame.draw.line(screen, BLACK, (100, 560), (350, 560), 10)

    # Vertical pole
    if penalty >= 1:
        pygame.draw.line(screen, BROWN, (180, 560), (180, 130), 8)

    # Horizontal pole
    if penalty >= 2:
        pygame.draw.line(screen, BROWN, (180, 130), (330, 130), 8)

    # Small support
    if penalty >= 3:
        pygame.draw.line(screen, BROWN, (180, 180), (230, 130), 8)

    # Rope (raccourcie)
    if penalty >= 4:
        pygame.draw.line(screen, SABLE, (330, 130), (330, 165), 6)

    # Head (plus petite, remontée juste sous la corde)
    if penalty >= 5:
        pygame.draw.circle(screen, BLACK, (330, 195), 28, 5)

    # Body (raccourci)
    if penalty >= 6:
        pygame.draw.ellipse(screen, SABLE, (310, 215, 40, 18), 5)
        pygame.draw.line(screen, BLACK, (330, 223), (330, 320), 10)

    # Left arm
    if penalty >= 7:
        pygame.draw.line(screen, BLACK, (330, 250), (290, 285), 6)

    # Right arm
    if penalty >= 8:
        pygame.draw.line(screen, BLACK, (330, 250), (370, 285), 6)

    # Left leg
    if penalty >= 9:
        pygame.draw.line(screen, BLACK, (330, 320), (295, 370), 6)

    # Right leg
    if penalty >= 10:
        pygame.draw.line(screen, BLACK, (330, 320), (365, 370), 6)

    # Eyes when dead
    if penalty >= 12:
        pygame.draw.line(screen, RED, (318, 185), (328, 195), 4)
        pygame.draw.line(screen, RED, (328, 185), (318, 195), 4)
        pygame.draw.line(screen, RED, (332, 185), (342, 195), 4)
        pygame.draw.line(screen, RED, (342, 185), (332, 195), 4)
        pygame.draw.rect(screen, BLACK, (200, 250, 200 , 100), border_radius=8)
        draw_text("DEAD", title_font, RED, 300, 300)


# ======================== game rules =========================================

def game():

    word = pick_word()  

    penalty = 0
    max_penalty = 12

    replay_rect = pygame.Rect(400, 540, 200, 70)

    input_history = []
    display = ["_"] * len(word)
    best_score = load_best_score()
    current_input = ""
    message = "Enter a letter or a word: "
    state = "playing"

    start_time = pygame.time.get_ticks()   # temps en millisecondes depuis pygame.init()
    elapsed_time = 0

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if state != "playing":
                    if replay_rect.collidepoint(event.pos):
                        return "replay"

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    return "menu"

                if state != "playing":
                    if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        return "menu"
                    continue

                if event.key == pygame.K_BACKSPACE:
                    current_input = current_input[:-1]

                elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):

                    guess = current_input.lower()
                    current_input = ""

                    if not guess:
                        message = "Type something first"

                    elif guess in input_history:
                        message = f"'{guess}' already tried"

                    else:
                        input_history.append(guess)

                        if len(guess) == 1:                 # une lettre
                            if guess in word:
                                for i in range(len(word)):
                                    if word[i] == guess:
                                        display[i] = guess
                                message = "Good one!"
                            else:
                                penalty += 1
                                message = "Wrong letter!"

                        else:                                # un mot entier
                            if guess == word:
                                display = list(word)
                                message = "You found the word!"
                            elif len(guess) == len(word):
                                penalty += 5
                                message = f"'{guess}' is not the right word!"
                            else:
                                message = "Invalid word length! Try again."


                elif event.unicode.isalpha() and len(current_input) < 20:
                    current_input += event.unicode.lower()

        if state == "playing":
            
            elapsed_time = pygame.time.get_ticks() - start_time

            if "_" not in display:
                state = "won"
                win_sound.play()
                attempts = len(input_history)
                message = f"You won in {attempts} attempts!  [Enter]"

                if best_score is None or attempts < best_score:
                    save_best_score(attempts)
                    best_score = attempts

            elif penalty >= max_penalty:
                state = "lost"
                lose_sound.play()
                message = f"Game over - the word was '{word}'  [Enter]"

        # ============ affichage ==================

        screen.blit(background, (0, 0))

        draw_text("H A N G M A N", title_font, BLACK, WIDTH // 2, 50)

        draw_hangman(penalty)

        timer_text = format_time(elapsed_time)
        draw_text(timer_text, medium_font, WHITE, 600, 130)

        # ======= display game status with "_"===========
        displayed_word = " ".join(display)

        draw_text_fitted(displayed_word, big_font, BLACK, 600, 200, 380)

        # ======= display actual penalty number===========

        if penalty <= 1:
            penalty_text = f"{penalty} penalty"

        else:
            penalty_text = f"{penalty} penalties"

        color = RED if penalty >= max_penalty - 3 else BLACK
        draw_text(penalty_text, medium_font, color, 600, 270)

        # =========== display maximum penalty number ===========

        draw_text(f"Maximum: {max_penalty}", small_font, BLACK, 600, 305)

        # ============== letter history ==============

        history_text = "Letters: "

        if input_history:

            history_text += " ".join(input_history)

        else:
            history_text += " "

        draw_text_fitted(history_text, small_font, GRAY, 600, 470, 380) 
            
        # ============ input ==================

        input_rect = pygame.Rect(450, 370, 300, 55)

        pygame.draw.rect(screen, WHITE, input_rect, border_radius=8)

        draw_text(current_input, medium_font, BLACK, input_rect.centerx, input_rect.centery)

        msg_color = GREEN if state == "won" else RED if state == "lost" else BLACK
        draw_text_fitted(message, small_font, msg_color, 600, 350, 380)

        # ============ BEST SCORE ==================

        if best_score is None:

            best_text = "Best score: --"

        else:

            best_text = f"Best score: {best_score} attempts"

        draw_text(best_text, small_font, DARK_GRAY, 840, 70)

        if state != "playing":
            draw_button(replay_rect, "PLAY AGAIN", BLUE)

        pygame.display.flip()
        clock.tick(60)

    return "menu"


while True:
    choice = menu()

    if choice != "game":
        break

    while True:
        result = game()

        if result == "replay":
            continue

        if result == "quit":
            choice = "quit"
        break

    if choice == "quit":
        break

pygame.quit()
