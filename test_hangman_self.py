
import os

START_GAME_POINT = 10
game_lenth = 3


# Clearing the Screen
os.system('cls')

test_text = "apple"

print("apple")

# create a pattern
pattern = []
for i in range(len(test_text)-1):
    pattern.append("_")

#display pattern
print(pattern)



matched_indexes = []
l1_new = [] 
i = 0
length = len(test_text)
point = 0
Flage = False
for game_run in range(game_lenth):
    
    for x in range(length-1):
     
     while i < length-1:

        l1_input = input("Input a checter a, b c :  ")
        temp = l1_input
        for y in range(length-1):
            if l1_input == str(test_text[y]):
                
                # cheak input str if use in this game previusly

                    matched_indexes.append(i)
                    # change l1 array with "_"
                
                    pattern[i] = str(l1_input)
                    i += 1

                    print(test_text)
                    print("pattern", pattern)
                    
                    print(length)

                    Flage = True
                
            else:
            
                pattern[i] = str("_")
                i +=1

                print(test_text)
                print("pattern", pattern)
                
                print(length)

                Flage = False

        #pattern = l1_new.replace(l1_new)
        if Flage == True:
            print(f'{l1_input} is present in {test_text} at indexes {matched_indexes}')
            #point = START_GAME_POINT - 1
            #print("Your point : ", point)
            Flage == True

        elif Flage == False:
            print("Invalid Input")
            #point = START_GAME_POINT - 1
            #print("Your point : ", point)
            Flage == False

        point = START_GAME_POINT - 1
        print("Your point : ", point) 


    if Flage == True and point == length:
          
        START_GAME_POINT = START_GAME_POINT + ((length-1)*((length-2)//2))
        print("Your total point ", START_GAME_POINT)
               
    else:
        START_GAME_POINT = START_GAME_POINT - ((length-1)*((length-2)//2))
        

    game = input("Did you want to play again y/n y for yes n for no")
    if game == "y" and Flage == True:
        game_lenth = game_lenth + 1
        print("Your total point ", START_GAME_POINT)
        point = 0
        continue
    else:
        break

           

print(test_text)
print(pattern)
print(length)
print("Your total point ", START_GAME_POINT)

