from functools import lru_cache
import random
import string

@lru_cache(maxsize=1)
def load_wordlist(filename="enable1.txt"):
    return open(filename).read().splitlines()

def get_random_letters(n):
    return random.sample(string.ascii_lowercase, n)

def is_word_valid(word, letters):
    return all(letter in word for letter in letters)
    # original rule: return all(letter in letters for letter in word)

def get_valid_words(letters, wordlist):
    return [word for word in wordlist if is_word_valid(word, letters)]

def ai_choose_word(words, difficulty):
    if difficulty == "easy":
        return min(words, key=len)
    elif difficulty == "medium":
        return random.choice(words)
    else:
        return max(words, key=len)

def play_round(difficulty, n_letters):
    wordlist = load_wordlist()

    valid_words = []
    while len(valid_words) < 5:
        letters = get_random_letters(n_letters)
        valid_words = get_valid_words(letters, wordlist)

    print("The letters: " + ", ".join(letters) + "\n")

    while True:
        user_word = input("Please enter your word: ---> ")
        if not is_word_valid(user_word, letters):
            print("You didn't use all the letters!")
            continue
        if user_word not in valid_words:
            print("The word doesn't seem to be in the dictionary!")
            continue
        break

    ai_word = ai_choose_word(valid_words, difficulty)

    print("\nThe computer chose a word:", ai_word, "\n")

    if len(ai_word) == len(user_word):
        print("Tie! Let's try again!")
        return None
    elif len(ai_word) > len(user_word):
        print("Computer won this round!")
        return 0
    else:
        print("You won this round!")
        return 1

def play_game():
    difficulties = {"easy": 4, "medium": 5, "hard": 6}

    rounds = 5
    points = [0, 0]

    print("\n" + " new game ".center(70, "=") + "\n")

    while True:
        difficulty = input("What difficulty do you choose? (easy, medium, hard) ---> ")
        if difficulty in difficulties:
            break
        print("Please enter the difficulty again")

    for i in range(rounds):
        print("\n" + " round {} - computer: {}, you: {} ".format(i+1, *points).center(70, "-") + "\n")
        winner = play_round(difficulty, difficulties[difficulty])
        if winner is not None:
            points[winner] += 1

    print("\nThe end! Let's see the results:\n")

    if points[0] == points[1]:
        print("Wow, a tie!")
    elif points[0] > points[1]:
        print("Too bad, you lost!")
    else:
        print("Congratulations, you won!")

def main():
    done = False
    while not done:
        play_game()
        again = input("Play again? ('q' to stop) ---> ")
        if again == "q":
            done = False

if __name__ == "__main__":
    main()