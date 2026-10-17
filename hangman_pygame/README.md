# 🎮 Hangman Game — Python & Pygame

A classic **Hangman game** developed in Python using the **Pygame** library.

The goal is simple: guess a randomly selected English word before reaching the maximum number of penalties!

This project was created to practice Python programming, graphical interfaces, event handling, file management, and game development with Pygame.

## ✨ Features

- 🎮 Interactive graphical interface built with Pygame
- 🔤 Random English word generation using the `english-words` package
- ⌨️ Keyboard input to guess individual letters or complete words
- 🖼️ Progressive Hangman drawing based on incorrect guesses
- ❤️ Maximum of 12 penalties per game
- ⏱️ Game timer displaying minutes, seconds, and centiseconds
- 🏆 Best score tracking, saved locally in `best_score.txt`
- 🎵 Background music and sound effects for winning and losing
- 🔄 PLAY AGAIN button to start a new game
- 🏠 Main menu with PLAY and QUIT buttons

## 🛠️ Technologies

- **Python 3**
- **Pygame** — Graphics, sounds, keyboard and mouse events
- **english-words** — Random English word generation
- **os** — File path management
- **random** — Random word selection
- **datetime** — Recording the date of the best score

## 📁 Project Structure

```text
hangman/
├── hangman_pygame.py
├── best_score.txt
├── feature/
│   ├── fond.png
│   ├── tatamusic-game-gaming-video-game-music-482380.mp3  => (NOT INCLUDED, TO DOWNLOAD IT FOLLOW THE STEPS IN Background Music)
│   ├── win.mp3
│   └── lose.mp3
└── README.md
```

The `feature/` directory contains the graphical and audio resources used by the game.

## 🚀 Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Install the required packages

```bash
python -m pip install pygame english-words
```

### 3. Run the game

```bash
python hangman_pygame.py
```

Make sure the `feature/` folder contains the required image and audio files.

## 🎯 How to Play

1. Launch the game and click **PLAY**.
2. A random English word is selected.
3. Enter a letter or a complete word using your keyboard.
4. Press **ENTER** to submit your guess.
5. Correct letters are revealed in the hidden word.
6. Incorrect guesses increase your penalty counter.
7. Guess the entire word before reaching 12 penalties to win!




🏆 Best Score System

The game records the lowest number of attempts required to win.
The best score is saved locally in best_score.txt with the following format:

2026-10-17 -- 8 attempts

When a player wins with fewer attempts than the previous record, the file is automatically updated.



🎵 Background Music

This game uses "Game Gaming Video Game Music" by Tatamusic, available on Pixabay which is subject to the Pixabay Content License.

The music is not included in this repository.
To enable background music:

    - Download the track from Pixabay. (link : https://pixabay.com/fr/music/jeux-vid%C3%A9o-game-gaming-video-game-music-482380/)
    - Don't have to rename it just to place it inside the feature/ folder.
    - Then launch the game normally.

The game also works without background music.


🔊 Sound Effects Credits

The following sound effects are used in this project:

    - Victory sound: piglevelwin2.mp3 by Tuudurt — CC0
    - Game Over sound: Game Over Arcade by Mountain_Man — CC0

    Both sound effects are licensed under Creative Commons Zero (CC0).

Special thanks to the creators for sharing their work!



🔮 Possible Future Improvements

    - Add difficulty levels (Easy, Medium, Hard)

    - Add word categories

    - Add a pause button

    - Improve animations and visual effects

    - Add a leaderboard