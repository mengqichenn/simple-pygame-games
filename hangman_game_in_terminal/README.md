# 🎮 Hangman Game — Python Terminal Edition

A classic **Hangman game** developed in Python and played directly in the terminal.

The goal is simple: guess a randomly selected English word before reaching the maximum number of penalties!

This project was created to practice Python fundamentals, user input handling, file management, command-line arguments, and game logic.

## ✨ Features

- 💻 Terminal-based gameplay, without a graphical interface
- 🔤 Random English word generation using the `english-words` package
- 📂 Support for custom word lists using the `-f` argument
- ⌨️ Guess individual letters or complete words
- 🎨 Progressive ASCII Hangman drawings
- ❤️ Maximum of 12 penalties per game
- 📝 Input history and feedback messages
- 🧹 Automatic terminal screen clearing
- 🏆 Best score tracking saved locally in `best_score.txt`

## 🛠️ Technologies

- **Python 3**
- **english-words** — Default English word collection
- **random** — Random word selection
- **argparse** — Command-line argument handling
- **os** — Terminal clearing and file management
- **datetime** — Recording the date of the best score

## 📁 Project Structure

```text
hangman_game_in_terminal/
├── hangman_terminal.py
├── hangman_stages.py
├── README.md
└── best_score.txt        # Created when a record is saved
```

The `hangman_stages.py` file contains the ASCII drawings used to display the Hangman's progress.

## 🚀 Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-folder>/hangman_game_in_terminal
```

### 2. Install the required package

```bash
python -m pip install english-words
```

No Pygame installation is required for this version.

### 3. Run the game

```bash
python hangman_terminal.py
```

A random English word will be selected automatically.

## 📂 Using a Custom Word List

You can also play with your own list of words instead of the default English word collection.

Create a text file named `my_wordlist.txt`:

```text
python
computer
programming
keyboard
developer
```

Then run:

```bash
python hangman_terminal.py -f my_wordlist.txt
```

You can also use the longer argument:

```bash
python hangman_terminal.py --file my_wordlist.txt
```

Each non-empty line in the file represents one possible word.

## 🎯 How to Play

1. Launch the game in your terminal.
2. A random word is selected and displayed as underscores (`_`).
3. Enter a letter or a complete word.
4. Press **ENTER** to submit your guess.
5. Correct letters are revealed in the hidden word.
6. Incorrect guesses increase your penalty counter.
7. Guess the word before reaching 12 penalties to win!

### Penalty System

| Action | Penalty |
|---|---|
| Correct letter | 0 |
| Incorrect letter | +1 |
| Correct word | 0 |
| Incorrect word of the correct length | +5 |
| Invalid word length | 0 |
| Repeated letter | 0 |

**Maximum penalties: 12**

## 🏆 Best Score System

The game saves the best score locally in `best_score.txt`.

The score is based on the number of recorded attempts, and the file includes the date of the record.

Example:

```text
2026-10-17 -- 8 attempts
```

When a player achieves a better score, the previous record is replaced.

## 🧠 What I Learned

Through this project, I practiced:

- Python variables, loops, and conditional statements
- Working with lists and strings
- Reading keyboard input using `input()`
- Creating and importing Python modules
- Using external Python packages
- Parsing command-line arguments with `argparse`
- Reading and writing text files
- Handling file paths and terminal commands
- Implementing game rules and tracking scores

## 🔮 Possible Future Improvements

- [ ] Add difficulty levels
- [ ] Add word categories
- [ ] Improve input validation
- [ ] Add a replay option
- [ ] Add a leaderboard
- [ ] Add automated tests

## 🎮 Graphical Version

A graphical version of this Hangman game is also available in the `hangman_pygame/` directory.

It includes a Pygame interface, interactive buttons, a timer, background music, and sound effects.

---

*Built with Python as a personal programming project.*