import random

def digitsCheck(number:int,guess:int):
    # player guess : 952 / guess : 521
    iterable_player_guess = list(str(number))
    iterable_guess = list(str(number))
    print(iterable_player_guess,iterable_guess)

    digit_counter = 0
    num_correct_digits = 0

    for digit in iterable_player_guess:
        if digit in iterable_guess:
            if iterable_player_guess.index(digit) == iterable_guess.index(digit):
                num_correct_digits+=1
                print(f'{num_correct_digits} right index')
            #print(iterable_guess.index(digit))
            digit_counter+=1
        
    if digit_counter == 0:
        print('No digit is correct.')
    else:
        print(f'number of correct digits: {digit_counter}')
        
digitsCheck(148,251)
exit()


def main():
    NUM_DIGITS = 3
    guess_min_range = '9'*(NUM_DIGITS-1)
    guess_max_range = '9'*NUM_DIGITS

    guess = random.randint(int(guess_min_range),int(guess_max_range))

    print(f'Welcome to bagels game: ')
    print(f'the number is guessed is: {guess}')
    print(f'I am thinking of a {NUM_DIGITS} digit number. Try to guess what it is!')

    for guess_num in range(1,11):
        pass_ = False
        while pass_ == False :
            player_guess = input(f'Guess #{guess_num}:')
            while len(player_guess) != NUM_DIGITS:
                print(f'Num of digits should be : {NUM_DIGITS}')
                break
            else:
                pass_ = True
        
        # check if digit in player_guess found in 
        digitsCheck(int(player_guess),guess)


if __name__ == '__main__':
    main()

