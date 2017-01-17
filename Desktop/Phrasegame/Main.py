import random

dictmovie = {'Hasta la ____, Baby': 'Vista','You are ______': 'terminated'}

def moviequotes():
    score = 0
    d = random.choice(list(dictmovie.keys()))
    print(d)
    rawinput = input("Place your answer here:")
    for rawinput in dictmovie:
        print(d)
        score+=1
        print(score)
        rawinput = input("Place your answer here:")
    else:
        print("You lose, you stupid idiot")




moviequotes()

