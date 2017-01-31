import random

dictmovie = {'Hasta la ____, Baby': False ,'You are ______': False,'I\'m gonna make him an ____ he can\'t refuse.':False,'Toto, I\'ve a feeling we\'re not in ____ anymore.':False,'Help, I\'ve _____ and I can\'t get up':False,'Here\'s ___ at you, kid.': False,'May the ____ be with you.':False,'Fasten your ____. It\'s going to be a bumpy night':False,'What we\'ve got here is failure to ____.':False,'RAAAARRRHH, Get to the ____':False, 'Louis, I think this is the beginning of a beautiful ____.': False,'You can\'t handle the ___!': False,'___? We ain\'t got no ____! We don\'t need no ____! I don\'t have to show you any stinking ____!': False, 'I’ll be ___': False,'Houston, we have a ____.': False,
'____, for lack of a better word, is good.': False, '____, my dear Watson.': False,'Here\'s ____!': False}
movieanswers = ['vista','terminated','offer','Kansas','fallen','looking','Force','seatbelts','communicate','chopper','friendship','truth','badges','back','problem','greed','elementary','Johnny']


def moviequotes():
    movie_quotes = []
    score = 0
    #chooses random key from a dictionary
    d = random.choice(list(dictmovie.keys()))
    #adds it to list for no repeated use within game
    movie_quotes.append(d)
    print(d)
    rawinput = input("Place your answer here:")
    if rawinput not in movieanswers:
        print("You lose, you stupid idiot")
    else:
        #loops function so game can repeat questions
        for rawinput in movieanswers:
            d = random.choice(list(dictmovie.keys()))
            if d in movie_quotes:
                d = random.choice(list(dictmovie.keys()))
                for d in movie_quotes:
                    d = random.choice(list(dictmovie.keys()))
                    if d not in movie_quotes:
                        movie_quotes.append(d)
                        # places score in game
                        print(d)
                        score += 1
                        print('Your Score:%s' % score)
                        rawinput = input("Place your answer here:")
                        if rawinput not in movieanswers:
                            print("You lose, you stupid idiot")
                            break
                else:
                    if d not in movie_quotes:
                        d = random.choice(list(dictmovie.keys()))
                        print(d)
                        score += 1
                        print('Your Score:%s' % score)
                        rawinput = input("Place your answer here:")
                        if rawinput not in movieanswers:
                            print("You lose, you stupid idiot")
                            break

#similiar code with few tweaks made
dicttrivia = {'You may enter, but you may not come in, I have space, but no room, I have keys, but open no lock. What am I?': False,'It\'s not a baby though you hold in the arms close to your bosom. It\'s not an Indian man though it has long beard. It\'s not a monkey though its tail is bent. It\'s not a bird though it has beautiful voice. What am I?': False,'When it is alive we sing, when it is dead we clap our hands. What is it?':False,'Cut my skin out. I\'m not going to cry, but you will! What am I?':False,' A spirited jig it dances bright, Banishing all but darkest night. Fire can\'t kill it but water can. Share it, it won\'t get less unless wind will ruin it.': False}
triviaanswers = ['computer','harp','birthday candles','onion']
def Riddle():
    triviaquotes = []
    riddle = []
    score = 0
    d = random.choice(list(dicttrivia.keys()))
    triviaquotes.append(d)
    print(d)
    rawinput = input("Place your answer here:")
    if rawinput not in triviaanswers:
        print("You lose, you stupid idiot")
    else:
        for rawinput in triviaanswers:
            d = random.choice(list(dicttrivia.keys()))
            if d in triviaquotes:
                d = random.choice(list(dicttrivia.keys()))
                for d in triviaquotes:
                    d = random.choice(list(dicttrivia.keys()))
                    if d not in triviaanswers:
                        triviaquotes.append(d)
                        print(d)
                        score += 1
                        print('Your Score:%s' % score)
                        rawinput = input("Place your answer here:")
                        if rawinput not in triviaanswers:
                            print("You lose, you stupid idiot")
                            break
                            break

            else:
                    if d not in triviaquotes:
                        d = random.choice(list(dicttrivia.keys()))
                        print(d)
                        score += 1
                        print('Your Score:%s' % score)
                        rawinput = input("Place your answer here:")
                        if rawinput not in triviaanswers:
                            print("You lose, you stupid idiot")
                            break




dictphrases = {'A Chip on Your ____': False,'A Dime a ___': False,'A Fool and His ____ Are Soon Parted': False,'A Piece of ___': False,'Back To the ___ Board': False
}
phrasesanswers = ['shoulder','dozen','cake','money','drawing']

def commonphrases():
    phrases = []
    score = 0
    d = random.choice(list(dictphrases.keys()))
    phrases.append(d)
    print(d)
    rawinput = input("Place your answer here:")
    if rawinput not in phrasesanswers:
        print("You lose, you stupid idiot")
    else:
        for rawinput in phrasesanswers:
            d = random.choice(list(dictphrases.keys()))
            if d in phrases:
                d = random.choice(list(dictphrases.keys()))
                for d in phrases:
                    d = random.choice(list(dictphrases.keys()))
                    if d not in phrases:
                        phrases.append(d)
                        print(d)
                        score += 1
                        print('Your Score:%s' % score)
                        rawinput = input("Place your answer here:")
                        if rawinput not in phrasesanswers:
                            print("You lose, you stupid idiot")
                            break
                            break
                else:
                    if d not in phrases:
                        d = random.choice(list(dictphrases.keys()))
                        print(d)
                        score += 1
                        print('Your Score:%s' % score)
                        rawinput = input("Place your answer here:")
                        if rawinput not in phrasesanswers:
                            print("You lose, you stupid idiot")
                            break
                            break


def enrico():
    print('Mr.Enrico: Nice to see the projects all finished up, but before we can move on you must solve these questions.')
    player_input = input('What’s the name for excessive bodily hair growth in women?\n'
                    'Place your answer here:')
    if player_input == 'hirsutism':
        player_input = input('How many bones are there in a giraffe\'s neck? \n Place your answer here:')
        if player_input == '7':
            player_input = input('What makes Homer so stupid in The Simpsons? \n Place your answer:')
            if player_input == 'crayon in his nose':
                player_input = input('What was Mickey Mouse’s name before it was changed to Mickey? \n Place your answer here:')
                if player_input == 'Mortimer':
                    print('Congratulations, you defeated my git push attempt, you scripter!')
                else:
                    print('So close yet so far')
            else:
                print('You\'re just like Homer')
        else:
            print('Another one bites the dust')
    else:
        print('Down at the front gate')









def input_code():
    player_input = input('Input a code:')
    if player_input == '510':
        print(enrico())
    elif player_input == '2020':
        print('Lets graduate!')
    elif player_input == '10':
        print('Perfect 10 Tye Dillinger')
    elif player_input == '434':
        print('Punk')
    elif player_input == '69':
        print('Weirdo')
    elif player_input == '3.14':
        print('pi! see you later')
    else:
        print('Invalid Code')
    pass
#creates the menu for the game
ans=True
while ans:
    print ("""The Game of Jericho
    1.Movie Quotes
    2.Riddle
    3.Common Phrases
    4.Input Code
    5.Exit/Quit
    """)
    ans= input("What would you like to do? ")
    if ans == '1':
        print(moviequotes())
    elif ans == '2':
        print(Riddle())
    elif ans == '3':
        print(commonphrases())
    elif ans == '4':
        print(input_code())
    elif ans == '5':
        print('See you next time')
        break
