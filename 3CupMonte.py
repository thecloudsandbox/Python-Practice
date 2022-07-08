from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():
    
    guess = ''
    
    #While is to ensure input is only a 0, 1, or 2
    while guess not in ['0','1','2']:
        #Input always returns a string, so we want to return an int
        guess = input('Pick a number of 0, 1, or 2:')
    
    #Returns input string as integer
    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess] == '0':
        print('Correct!')
    else:
        print('Incorrect guess!')
        print(mylist)


#Initial List
mylist = [' ','0',' ']

#Shuffle List
mixlist = shuffle_list(mylist)

#User Guess
guess = player_guess()

#Check Guess
check_guess(mixlist,guess)