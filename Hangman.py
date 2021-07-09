import random

animals = ["rabbit", "tiger", "elephant"]
countries = ["usa", "ukraine", "russia"]
painters = ["rembrandt", "monet", "dali"]
topics = [animals, countries, painters]

def print_hung(hung):
    if hung == 0:
        print("\n" * 8)
    elif hung == 1:
        print(" |----\n |\n |\n |\n |\n |\n |\n |\n/ \\")
    elif hung == 2:
        print(" |----\n |   |\n |\n |\n |\n |\n |\n |\n/ \\")
    elif hung == 3:
        print(" |----\n |   |\n |   O\n |\n |\n |\n |\n |\n/ \\")
    elif hung == 4:
        print(" |----\n |   |\n |   O\n |   |\n |   |\n |\n |\n |\n/ \\")
    elif hung == 5:
        print(" |----\n |   |\n |   O\n |  /|\ \n |   |\n |\n |\n |\n/ \\")
    elif hung == 6:
        print(" |----\n |   |\n |   O\n |  /|\ \n |   |\n |  / \ \n |\n |\n/ \\ GAME OVER")

def changeWord(word, symbol, index):
    word = word[:index] + symbol + word[index+1:]
    return word

def relace_user_word(st, sym, user_word):
    pos = 0
    while(st.find(sym, pos) != -1):
        index = st.find(sym, pos)
        user_word = changeWord(user_word, sym, index)
        pos = index + 1
    return user_word

def create_hung_word():
    choice = int(input("Choose a topic: 1.Animals\n2.Countries\n3.Painters"))
    random_choice = random.randint(0, 2)
    hung_word = topics[choice-1][random_choice]
    return hung_word

def create_user_word():
    user_word = ""
    for i in range(0, len(hung_word)):
        user_word += "_"
    return user_word

def logic():
    hung = 0
    win = False
    global user_word
    print_hung(hung)
    print(user_word)
    while hung < 6 or win:
        temp = user_word
        letter = input("Write your letter: ")
        if len(letter) > 1:
            print("GAME OVER")
            exit()
        user_word = relace_user_word(hung_word, letter, user_word)
        if temp == user_word:
            hung += 1
        elif user_word == hung_word:
            win = True
            print("YOU WIN!")
            exit()
        print_hung(hung)
        print(user_word)

hung_word = create_hung_word()
user_word = create_user_word()
logic()

