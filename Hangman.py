#I LOVE PYTHON
import random
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def choose_word():
    '''Choose a word from the text'''

    global list_name
    list_name = []
    
    #Open sowpods file
    with open('SOWPODS.txt' , 'r') as my_file:
        name_of_text = my_file.readline()
        
        #Append the name of text to the list
        while name_of_text:
            list_name.append(name_of_text.strip())
            name_of_text = my_file.readline()
    
    return random.choice(list_name)


#Run game
def play_hangman_game():

    user_guess = input('Enter a letter :').upper()

    chance_of_guess = 6 #How many letters can the user guess

    while True:
        
        #Check for duplicate letter
        if user_guess in list_guessed:
            print(Fore.LIGHTYELLOW_EX + 'The letter already guessed ')
            print()
        
        #If letter exist in the word , append the letter  to guessed
        elif user_guess in word_to_guessed:
            for i in range(len(word_to_guessed)):
                if user_guess == word_to_guessed[i]:
                    guessed[i] = user_guess
                    list_guessed.append(user_guess)   

        elif user_guess not in user_input_list:
            chance_of_guess -= 1
            print(Fore.YELLOW + 'Hint :You have {} incorrect guesses left'.format(chance_of_guess))

        print(' '.join(guessed))
        
        if chance_of_guess == 0:
            print(Fore.RED + 'You lost' + Fore.WHITE + f' ,the correct word was {correct_word}')
            break
            

        if '-' not in guessed:
            print(Fore.LIGHTGREEN_EX + 'You won')
            break

        user_input_list.append(user_guess)
        user_guess = input('Enter a letter :').upper()
        




word_to_guessed = choose_word()
correct_word = word_to_guessed
guessed = '-' * len(word_to_guessed)
guessed = list(guessed) #When user guess a letter and if it is correct save to this variable

list_guessed = []
user_input_list = [] #Every letter that user input , save to this list
print('----------WELCOME TO HANGMAN GAME----------')

print('- ' * len(word_to_guessed))

play_hangman_game()

