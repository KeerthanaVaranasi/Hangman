import random
word_list = ['wares','soup','mount','extend','brown','expert','tired','humidity','backpack','crust','dent','market','knock','smite','windy','coin','throw','silence','bluff','downfall','climb','lying','weaver','snob', 'kickoff','match','quaker','foreman','excite','thinking','mend', 'allergen','pruning', 'coat','emerald','coherent',
'manic','multiple', 'square','funded','funnel','sailing','dream', 'mutation','strict','mystic','film','guide','strain','bishop','settle','plateau', 'emigrate','marching','optimal','medley','endanger','wick', 'condone','schema','rage','figure','plague','there','reusable','refinery','suffer','captive','flipping','prolong','main',
'dinner', 'rabbit','chill','seed', 'born', 'shampoo','italian', 'giggle','palm','globe','wise','running','sunlight','spending',
'crunch','tangle', 'forego','tailor', 'divinity','probe',  'bearded','premium','featured',  'serve','borrower','examine','legal', 'snow','whisper','bundle','bracket','deny','blurred','pentagon','reformed','polarity','jumping','gain','laundry',
'hobble','culture','whittle', 'docket','mayhem', 'build','peel','board','keen','glorious','singular','cavalry','present','cold','hook','salted','just', 'dumpling','glimmer','drowning',  'admiral','sketch','subject','upright','sunshine','slide','calamity', 'gurney','adult' 'game','stocking','folly', 'action',
'bubbling', 'scented','sprinter','bingo','egyptian','comedy','rung','outdated','radical','escalate','mutter','desert','memento','kayak','talon', 'portion','affirm','dashing','fare','battle','pupil','swing', 'thicket','reserve','murder','costly','corduroy','bump','oncology','swatch','rundown','steal','teller','cable','oily', 'official','trim','fluent',
'shield','butler','stitch','stub','sabotage','parlor','prompt','heady','horn','rework','painful','composer','glance','eagle','solvent','hybrid','buffet','lively']


#selecting random word from list
def get_word():
    word = random.choice(word_list)
    print("Length of the word is",len(word))
    return word.upper()



#play function
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play HANGMAN!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("please guess a letter or word:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter",guess)
            elif guess not in word:
                print(guess,"is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job",guess,"is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i,letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word",guess)
            elif guess != word:
                print(guess," is not the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("congrats,you guessed the word! you win!")
    else:
        print("Sorry,you ran out of tries.the word was "+ word +".Maybe next time!")


				
#display_hangman function for printing hangman based on the tries
def display_hangman(tries):
    stages  = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -

        """,
        """
            --------
            |      |
            |      O
            |     \\|
            |      |
            |     
            -
        """,
        """
            --------
            |      |
            |      O
            |      |
            |      |
            |     
            -
        """,
        """
            --------
            |      |
            |      O
            |    
            |      
            |     
            -
        """,
        """
            --------
            |      |
            |      
            |    
            |      
            |     
            -
        """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
