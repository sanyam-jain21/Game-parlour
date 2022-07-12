from hungman import*
from scribble import*
from ticTacToe import*
if __name__ == '__main__':
    while 1:
        print("                                                      Enter to Game Parlour                                                  ")
        print('''1.SCRIBBLE\n2.HUNGMAN\n3.TICTAKTOE\n4.QUIT\n''')
        n=int(input("Enter Choice: "))
        if n==1:
            word_list = load_words()
            play_game(word_list)
        elif n==2:
            ch=input("do you want to enter the word(y/n):")
            if ch=='y':
                secret_word=input("Enter your word:")
            else:
                secret_word = choose_word(wordlist)
            hangman_with_hints(secret_word)
        elif n==3:
            start()
        elif n==4:
            break