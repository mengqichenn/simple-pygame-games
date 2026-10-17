import random
import argparse
from hangman_stages import stages
import os
from datetime import date


# define an argument to import an external file
def parse_args():
    parser = argparse.ArgumentParser(description="Hangman Game")

    parser.add_argument(
        "-f", "--file",
        type = str,
        help = "Specify the path to file which contains a list of words"
    )

    return parser.parse_args()

args = parse_args()

# add a condition if user specify a word list file or not
if args.file:
    with open(args.file, "r") as f:
        list_words = [line.strip() for line in f if line.strip()]
    word = random.choice(list_words).lower()
else:
    from english_words import get_english_words_set
    english_word_set = get_english_words_set(['web2'], lower=True)
    word = random.choice(list(english_word_set)) 


# clean the screen
def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")


# define variables
penalty = 0
max_penalty = 12
input_history = []
display = ["_"] * len(word)


# preparation for output
actual_date = date.today().strftime("%Y-%m-%d")

best_score_file = "best_score.txt"

if os.path.exists(best_score_file):
        
    with open(best_score_file, "r") as file:  
    # with open()  <--- "w" write / "a" append / "r" read
            
        content = file.read().strip()       # read if there is content in the best_score_file
        # if so, extract first the second part with seperator "--" and then extract the first value then transform into integer
        if content:
                best_score = int(content.split("--")[1].split()[0])

        else: 
                best_score = None
else: 
    best_score = None

title = ""
message = ""

# while loop
while penalty < max_penalty: 

    
    clear_screen()

    title = "Welcome to hangman game!"
    print(title)

    #display the current hangman stage
    index_stages = min(penalty, len(stages)-1)
    print(stages[index_stages])
        

    if penalty <=1:
        print(f"{' ' .join(display)} / {penalty} penalty" )
    else: print(f"{' ' .join(display)} / {penalty} penalties" )


    if message:
        print(message)

    message = ""

    # input only if there is no more "_"
    if "_" not in display:
        print(f"You found the word : {word}!")
        print(f"Letters entered : {input_history}.")

        if best_score is None:
            best_score = len(input_history)
            with open("best_score.txt", "w") as doc:
                doc.write(f"{actual_date} -- {len(input_history)} attempts")

        elif len(input_history) < best_score:
            print(f"Best ever! You guessed {word} in {len(input_history)} attempts.")
            with open("best_score.txt", "w") as doc:
                doc.write(f"{actual_date} -- {len(input_history)} attempts")
        else:
            print(f"You guessed '{word}'in {len(input_history)} attempts, but the record from {content.split("--")[0]} is {best_score} attemp")
        break


    letter = input("Enter a letter or a word : ").lower()

    # check some conditions
    if len(letter) != 1 and len(letter) != len(word):
        message = "Please reenter!"
        continue

    # for single letter
    if len(letter) == 1:
        if letter in input_history:
            message = "Already entered!"
            continue
        input_history.append(letter)

                
        # check if the letter is in word
        if letter in word:
            message = "Good one!"

            for l in range(len(word)):
                if letter == word[l]:
                    display[l] = letter
        else: 
            penalty += 1
            message = "Wrong letter!"


    # for a whole word : if right, stop the loop, else +5
    elif len(letter) == len(word):
        if letter == word:
            print(f"You found the word : {word}!")

            if best_score is None:
                best_score = len(input_history)
                with open("best_score.txt", "w") as doc:
                    doc.write(f"{actual_date} -- {len(input_history)} attempts")

            elif len(input_history) < best_score:
                print(f"Best ever! You guessed {word} in {len(input_history)} attempts.")
                with open("best_score.txt", "w") as doc:
                    doc.write(f"{actual_date} -- {len(input_history)} attempts")
            else:
                print(f"You guessed '{word}'in {len(input_history)} attempts, but the record from {content.split("--")[0]} is {best_score} attemp")


            break


        else: 
            penalty += 5
            message = "Wrong word!"



if penalty >= max_penalty:
    print(f"You lose! The word is : {word}!")
