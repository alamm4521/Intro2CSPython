import hangman as hangman
import hangman_helper as hang_helper
import os

# Clearing the Screen
os.system('cls')

words = "apple"
wrong_guess_list = []
#T for sample data

letter = "T"
pattern = ['_', '_', '_', '_', '_']

#print(hang_helper.get_input())

#hangman.update_word_pattern(word, pattern, letter)
#load word_list 


#print(hang_helper.set_seed(len(hang_helper.load_words())), "hang_helper.set_seed(111)")

#for i in range(len(word)):
#print(pattern)
#print(hangman.run_single_game(list_words=" ", score=0))
#print(hangman.match_letter(word, pattern, letter))
#hang_helper.load_words(file='ex4_tests\words.txt')
#print(len("acetylphenylhydrazine"))
#print(hang_helper.get_input())
"""n = 0
point = (n*((n+1)//2))
print(point)
data = "000000"
if (len(data) == 1):
    print("len 1", data)
else:
    print("len data", len(data), data) """  

#hangman.cheak_valid_input(word, letter, pattern, wrong_guess_lst = letter, points = 0, msg = "")

"""
def main():
    print("Hello World!")


if __name__ == "__main__":
    main()"""

#print(hangman.filter_words_list(words, pattern, wrong_guess_list))

print(hangman.words_matches(words))


print("work with cheak_valid_input bug and continue ")
