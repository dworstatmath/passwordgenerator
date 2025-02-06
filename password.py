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

print(fetch_word())