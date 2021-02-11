import random
from random import shuffle


def run_game():
    """
    TODO: implement Mastermind code here
    """
    shuffled = []
    while len(shuffled) < 4:
        num = random.randint(1,8)
        if num in shuffled:
            continue
        else:
            shuffled.append(num)    
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    num_turns = 12
    valid = False
    number = ''
    while num_turns > 0:
        while valid == False:
            number = input("Input 4 digit code: ")
            if(len(number) == 4):
                valid = True
                break
            else:
                print("Please enter exactly 4 digits.")
        valid = False
        if(num_turns == 0):
            break

        right = 0
        wrong = 0
        correct = []
        incorrect = []
        num = str(number)
        for i in range(0,4):
            if int(num[i]) == shuffled[i]:
                right += 1
                correct.append(num[i])
            elif int(num[i]) in shuffled:
                wrong += 1
                incorrect.append(num[i])
        print(f"Number of correct digits in correct place:     {right}")
        print(f"Number of correct digits not in correct place: {wrong}")
        num_turns -=1
        if right != 4:
            print(f"Turns left: {num_turns}")
        if right == 4:
            print("Congratulations! You are a codebreaker!")
            print("The code was: {}{}{}{}".format(shuffled[0],shuffled[1],shuffled[2],shuffled[3]))
            num_turns = 0



if __name__ == "__main__":
    run_game()
