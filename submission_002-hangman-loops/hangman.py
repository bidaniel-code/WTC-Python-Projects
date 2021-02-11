import random


def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    word_completion = "_" * len(word)
    random_index = random.randint(0, len(word)-1)
    letter = word[random_index]
    return word_completion[:random_index] + letter + word_completion[random_index+1:]


# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    if char in original_word and char not in answer_word:
        return True
    return False


# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    ans = answer_word
    for i, letter in enumerate(original_word):
        if char == letter:
            ans = answer_word[:i] + char + answer_word[i+1:]
    return ans


def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer

def do_wrong_answer(number_guesses):
    print("Wrong! Number of guesses left: " + str(number_guesses))
    draw_figure(number_guesses)


# TODO: Step 4: update to use number of remaining guesses
# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses: int):
    if number_guesses == 4:
        print('/----')
        print('|')
        print('|')
        print('|')
        print('|')
        print('_______')
    elif number_guesses == 3:
        print('/----')
        print('|   0')
        print('|')
        print('|')
        print('|')
        print('_______')
    elif number_guesses == 2:
        print('/----')
        print('|   0')
        print('|   |')
        print('|   |')
        print('|')
        print('_______')
    elif number_guesses == 1:
        print('/----')
        print('|   0')
        print('|  /|\\')
        print('|   |')
        print('|')
        print('_______')
    elif number_guesses == 0:
        print('/----')
        print('|   0')
        print('|  /|\\')
        print('|   |')
        print('|  / \\')
        print('_______')


# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):
    number_guesses = 5
    original_word = word
    ans = answer
    print("Guess the word: " + answer)
    while number_guesses > 0:
        my_char = get_user_input()
        if my_char.lower() == 'exit' or my_char.lower() == 'quit':
            print("Bye!")
            break
        answer_word = word + my_char
        if is_missing_char(original_word, answer, my_char) == True:
            ans = do_correct_answer(original_word, ans, my_char)
        elif number_guesses == 1:
            print("Sorry, you are out of guesses. The word was: " + word)
            #draw_figure(0)
            break
        else:
            number_guesses -=1
            do_wrong_answer(number_guesses)
        if ans == word:
            break


# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)
    
    run_game_loop(selected_word, current_answer)

