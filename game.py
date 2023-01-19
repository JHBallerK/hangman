import random

def over_write():
    with open("kat.txt","w") as n:
        
        n.write('') 

def user_input():
    write_in=input("fill in the word: ")

    return write_in


def write_to(words):

    with open("kat.txt","a") as k:
            k.write(words)
            k.write("\n")
    


def create_file():
    for i in range(2):    
        write1=user_input()
        words=write_to(write1)
     

def the_words():
    with open("kat.txt","r") as kk:
        words=kk.readlines()

    return words

def select_word(words):
    #slect the random word
    word=words[random.randint(0,len(words)-1)]

    return word.strip()

def select_random_letter(word):
   #select a random letter
    picked_word=list(word)
    random_letter=picked_word[random.randint(0,len(word)-2)]

    word =[]
    for i in picked_word:
        if  i != random_letter:
            word.append("_")
        else:
            word.append(i) 
        
    print("guess the missing letters in the word","".join(word))
    return "".join(word)


def player_input():
    player=input("guess the missing letters: ")

    return player



def is_missing(char,selected_word,random_letter):
    if char in selected_word and char not in random_letter:
        return True
    else:
        return False

def fill_in_missing_letter(char,selected_word,random_letter):
    
    random_letter=list(random_letter)

    for x in range(len(selected_word)):
        if char == selected_word[x]:
            random_letter[x]= char
    
                                                                                      
    return "".join(random_letter)

def make_correct(selected_word,answer,player):
        answer=fill_in_missing_letter(answer,selected_word,player)
        print(answer)
        return answer


def run_game():
    over_write()
    create_file()
    guess_words =the_words()
    selected_word = select_word(guess_words)
    fill_in_word=select_random_letter(selected_word)
    turns=len(selected_word)
    print(turns)
    while turns >= 0 :
        player = player_input()
        check_input=is_missing(player,selected_word,fill_in_word)
        fill_in_word=fill_in_missing_letter(player,selected_word,fill_in_word)
        print(fill_in_word)  
        if fill_in_word==selected_word:
            print("congrats! you guessed the word correctly")
            break
        if check_input == False :
            print("incorrect guess ,guess again")
            print("guesses left",turns)
            turns-=1
    if turns == -1:
        print("Sorry, you are out of guesses. The word was: ",selected_word)


run_game()
