# Create a file named hangman.py and 
# import the file helper_hangman.py in 
# which a number of functions are implemented 
# (see below for a list of functions).

import hangman_helper as hangman
import difflib
import os

INPUT_LETTER_COUNTER = 0


POINTS_INITIAL = 10
HINT_LENGTH = 3
wrong_guesses_list = []
wrong_guess_list = []

#from hangman import * 

#1. Implement the function: update_word_pattern(word, pattern, letter)

#Which takes as parameters the word, the current pattern, 
# and a letter and returns an updated pattern containing 
# the same letter.

def words_matches(word, word_list):

    #word_list = hangman.load_words()
    
    number = 3
    cutoff = 0.5

    matches = difflib.get_close_matches(word, word_list, number, cutoff)

    return matches

def return_words(word):
    
    #matches = words_matches(word)

    #matches = word

    show_suggestions = hangman.show_suggestions(word)
    
    return show_suggestions

def filter_words_list(words, pattern, wrong_guess_list):

    #wrong_guess_list = letter = str(wrong_guess_list)
    
    #word contain gusses the list of words that match the pattern and the previous guesses

    letter_txt = match_letter(words, pattern, wrong_guess_list)
    
    wrong_guess_list = list(wrong_guess_list)

    if isinstance(str(letter_txt)) == True and str(letter_txt).islower() and len(letter_txt) == 1:
        
        #pattern = str(pattern) + str(letter_txt)

        return words, pattern, wrong_guess_list

    elif letter_txt == str(words):

        #pattern = str(pattern) + str(letter_txt)

        return words, pattern, wrong_guess_list

    else:
        #if not wrong_guess_list:

        wrong_guess_list.append(letter_txt)

        return words, pattern, wrong_guess_list    

    
def wrong_guesses_list(letter):

    letter = str(letter)
    #wrong_guesses_list = []
    if letter == None:
        
        return 

    else:
        wrong_guesses_list_data = wrong_guesses_list + " " + str(letter)
        return wrong_guesses_list_data    
   

def game_points(n):
    
    if n == 2:
        n = int(n)
        points = (n*((n+1)//2))
    elif n == 4:
        n = int(n)
        points = (n*((n+1)//4))
    
    return points


# if input letter and word lertter equal return letter and index 
def cheak_valid_input(word, letter, pattern):
  
    letter = str(letter)

    if isinstance(letter, str) == True and letter.islower() and len(letter) == 1:

        msg = "Valid Input >>>>"
        hangman.display_state(pattern, wrong_guess_lst_lst,
                              points=10, msg="Valid Input >>>>")
        
        return word, letter, pattern

    elif letter == str(word):

        #msg = "Valid Input >>>>"
        hangman.display_state(pattern, wrong_guess_lst_lst=None,
                              points=10, msg="Valid Input >>>>")
        
        return word, letter, pattern

    else:
        # nothing match        
        msg = "Invalid input >>>>" 
        hangman.display_state(
            pattern, wrong_guess_lst_lst=str(letter), points=10, msg="Invalid input >>>>")

        return word, letter, pattern
        
        
def calc_HINT(n):

    if n == 0:

        n = 0

    elif n == 1:

        n = (n//HINT_LENGTH)

    elif n == 2:

        n = (2*n//HINT_LENGTH)
    else:
        (HINT_LENGTH - 1)*n//HINT_LENGTH

    return n
      

def game_HINT(word):
   
    
    return_words(word)

       
    return matches
    

def game_guess(letter):
  

    letter = str(letter)
    #letter = letter.split("!")

    return letter


def match_letter(word, pattern, letter):
        
    
    letter = str(letter[1])

    ##test this use in point section

    for i in range(len(str(word))):
        Flag = False          
        for x in range(len(str(word))): 

            if str(letter) == str(word[x]) and pattern[x] == '_':  # problem use str
                #insert matched string to pattern
                pattern[x] = str(letter)
                Flag = True
                #POINT = POINT + game_points(n=2)
                #cheak_valid_input(word, letter, pattern)
                return letter, pattern, word
            elif str(letter) == str(word[x]) and pattern[x] != '_':
                
                #wrong_guess_letter = wrong_guesses_list(None)
                #POINT = POINT - 1
                #cheak_valid_input(word, letter, pattern)

                continue
            else:
                #POINT = POINT - 1
                #cheak_valid_input(word, letter, pattern)
                #return letter, pattern, word
                continue
                                    
        continue
       
    #cheak_valid_input(word, letter, pattern)
    if pattern == word:
        return letter, pattern, word

    return letter, pattern, word                        
    
def input_letter():

    #print("######### INPUT LETTER #############")
    choice = list(hangman.get_input())
  
    return choice

def pattern_init(word):

    pattern = []
    for i in range(len(list(word))):
        pattern.append("_")

    return pattern
    
def update_word_pattern(word, pattern, letter):

    
    #pattern = match_letter(word, pattern, letter)
    letter = match_letter(word, pattern, letter)
    
    #wrong_guess_list = letter[1]
    #pattern = letter   
    #words = return_words(word)
    #filter_words_list(words, pattern, wrong_guess_list)
       
    return letter, pattern, word


def run_singel_game_points():

    return


def run_single_game(list_words, score):

    #get random words
    random_words = hangman.get_random_word(list_words)
         
    print("################# Test Data ########################################")
    print(random_words, "random_words")
    print("################# EndTest Data ########################################")

    #genarate pattarn [ _ , _ , _ , _ , _ , _ , _ , _ ]
    pattern = pattern_init(random_words)

    #run this game word lenth times
    #for i in range(len(random_words)):
    for i in range(10):

        #display game info

        #hangman.display_state(pattern, wrong_guess_lst = None , msg = "Wellcome to Hangman Game", points = POINTS_INITIAL)
        
        
        msg = "Wellcome To Hangman Game"
        hangman.display_state(pattern, wrong_guess_lst=None,
                                  msg="Wellcome to Hangman Game", points=10)


        # get input from input_letter() function
        
        letter = input_letter()
        #n = len(letter)    
        #POINTS_INITIAL = POINTS_INITIAL - 1

        #take letter input from letter
        letter_input = letter[1]
        
        # cheak_valid_input

        #cheak_valid_input(random_words, letter_input, pattern)

        if letter[0] == 1:
            
            # get data from update_word_pattern(word, pattern, letter)
            #pattern = update_word_pattern(random_words, pattern, letter)
            #letter input
            update_data = update_word_pattern(random_words, pattern, letter)
            print(update_data)
            
            #filter_words_list(suggestions_data[0], suggestions_data[1], suggestions_data[2])
            #run_single_game(list_words, score )

        elif letter[0] == 2:
            
            game_guess(letter[1])

        elif letter[0] == 3:

            game_HINT(random_words)
            suggestions_data = return_words(random_words, list_words)
              
        # get data from update_word_pattern(word, pattern, letter)
        #pattern = update_word_pattern(random_words, pattern, letter)
        #letter input output letter

    #words_matches = words_matches(random_words)
    #words = words_matches
    #filter_words_list(words, pattern, wrong_guess_list)
    
    return letter

def main():

    # Clearing the Screen
    os.system('cls')
    
    #get load words to list words
    list_words = hangman.load_words()
    run_single_game(list_words, score = 10)
    hangman.play_again(msg= "game finished !!!")

#last call main
if __name__ == "__main__":
    main()
