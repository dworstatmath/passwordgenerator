import random 
import string 
import requests

#function that generates a single random character
def random_character():
    choices=string.ascii_letters+string.digits+string.punctuation
    return random.choice(choices)

passwordLength=int(input("what is password length"))

#function that generates a password of random characters
def generate_strong_password():
    password=""
    for i in range(passwordLength):
        password+=random_character()
    print(password)

generate_strong_password()

def fetch_word():
    url="https://random-word-api.herokuapp.com/word?length=6"

    response=requests.get(url)
    word=response.json()[0]
    return word

def replaceLetters(word):
    word = word[0].upper() + word[1:]
    if "a" in word:
        word = word.replace("a", "@")
    if "b" in word:
        word = word.replace("b","8")
    if "c" in word:
        word = word.replace("c","<")
    if "e" in word:
        word = word.replace("e","3")
    if "g" in word:
        word = word.replace("g","9")
    if "h" in word:
        word = word.replace("h","#")
    if "l" in word:
        word = word.replace("l","1")
    if "o" in word:
        word = word.replace("o","0")
    if "s" in word:
        word = word.replace("s","$")
    if "t" in word:
        word = word.replace("t","+")
    return word


# function to generate weaker but memorable password
def generate_weaker_password():
    word1 = fetch_word()
    word2 = fetch_word()
    word1 = replaceLetters(word1)
    word2 = replaceLetters(word2)
    password = word1 + word2
    return password

print(generate_weaker_password())