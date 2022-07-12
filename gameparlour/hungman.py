import string
import random

WORDLIST_FILENAME = "words1.txt"


def load_words():
    
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist = load_words()

def choose_word(wordlist):
   return random.choice(wordlist)


def is_word_guessed(secret_word, letters_guessed):
    for i in secret_word :
      if i in letters_guessed:
        continue
      else:
        return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    s=''
    for i in secret_word :
      if i in letters_guessed:
        s+=i
      else:
        s+="_ "
    return s

def get_available_letters(letters_guessed):
    s=string.ascii_lowercase
    letter_left=''
    for i in s:
        if i not in letters_guessed :
            letter_left+=i
    return letter_left

def hangman(secret_word):
    guess=6
    warning=3
    print(f'''Welcome to the game Hangman!
    I am thinking of a word that is {len(secret_word)} letters long.
    --------------------'''
        )
    letters_guessed=[]
    while not is_word_guessed(secret_word,letters_guessed) and warning>0 and guess>0:
      print(f"You have {guess} guesses left.")
      print(f"Available letters: {get_available_letters(letters_guessed)} ")
      n=(input("Please guess a letter:"))
      if n.isalpha():
        n.lower()
      else:
        warning-=1
        print(f"Oops! That is not a valid letter. You have {warning} warnings left: {get_guessed_word(secret_word,letters_guessed)} ")
        continue
      if n in letters_guessed:
        warning-=1
        print(f"Oops! You've already guessed that letter. You have {warning} warnings left: {get_guessed_word(secret_word,letters_guessed)} ")
      else:
        letters_guessed.append(n)
      if n in secret_word:
        print(f"Good guess: {get_guessed_word(secret_word,letters_guessed)} ")
      else:
        print(f"Oops! That letter is not in my word.")
        print(f"Please guess a letter: {get_guessed_word(secret_word,letters_guessed)} ")
        if n in 'aeio':
          guess-=2
        else:
          guess-=1
      print("-------------")
    if is_word_guessed(secret_word,letters_guessed):
      print("Congratulations, you won!")
      u=-1
      unique=[]
      for i in secret_word:
        if i not in unique:
          u+=1
          unique.append(i)
      score=guess*u
      print("Your total score for this game is:",score)
    elif guess==0:
      print("Sorry, you ran out of guesses. The word was",secret_word)
    elif warning==0:
      print("Sorry, you ran out of warnings. The word was",secret_word)

def match_with_gaps(my_word, other_word):
    s=''
    for w in my_word:
      if w !=' ':
        s+=w
    unique=[]
    for i in my_word:
      if i not in unique:
        unique.append(i)
    n=len(other_word)
    if len(s)==n:
      for y in range(n):
        if s[y]=='_':
          if other_word[y] in unique:
            return False
           
        elif s[y]!="_":
          if s[y]!=other_word[y]:
            return False
      return True
    return False
def show_possible_matches(my_word):
    for i in wordlist:
      if match_with_gaps(my_word,i):
        print(i,",",end=" ")
    print()

def hangman_with_hints(secret_word):
    guess=6
    warning=3
    print(f'''Welcome to the game Hangman!
    I am thinking of a word that is {len(secret_word)} letters long.
    --------------------'''
        )
    letters_guessed=[]
    while not is_word_guessed(secret_word,letters_guessed) and warning>0 and guess>0:
      print(f"You have {guess} guesses left.")
      print(f"Available letters: {get_available_letters(letters_guessed)} ")
      n=(input("Please guess a letter:"))
      if n.isalpha():
        n.lower()
      elif n=="*":
        s=get_guessed_word(secret_word,letters_guessed)
        show_possible_matches(s)
        guess-=1
        continue
      else:
        warning-=1
        print(f"Oops! That is not a valid letter. You have {warning} warnings left: {get_guessed_word(secret_word,letters_guessed)} ")
        continue
      if n in letters_guessed:
        warning-=1
        print(f"Oops! You've already guessed that letter. You have {warning} warnings left: {get_guessed_word(secret_word,letters_guessed)} ")
      else:
        letters_guessed.append(n)
      if n in secret_word:
        print(f"Good guess: {get_guessed_word(secret_word,letters_guessed)} ")
      else:
        print(f"Oops! That letter is not in my word.")
        print(f"Please guess a letter: {get_guessed_word(secret_word,letters_guessed)} ")
        if n in 'aeio':
          guess-=2
        else:
          guess-=1
      print("-------------")
    if is_word_guessed(secret_word,letters_guessed):
      print("Congratulations, you won!")
      u=-1
      unique=[]
      for i in secret_word:
        if i not in unique:
          u+=1
          unique.append(i)
      score=guess*u
      print("Your total score for this game is:",score)
    elif guess==0:
      print("Sorry, you ran out of guesses. The word was",secret_word)
    elif warning==0:
      print("Sorry, you ran out of warnings. The word was",secret_word)


if __name__ == "__main__":
    ch=input("do you want to enter the word(y/n):")
    if ch=='y':
      secret_word=input("Enter your word:")
    else:
      secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

