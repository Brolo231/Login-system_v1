import random
import numpy as np

def Login():
    while True:
        with open('Usernames.txt') as users:
            Usernames_txt = [line.strip() for line in users.readlines()]
        with open('Passwords.txt') as passes:
            Passwords_txt = [line.strip() for line  in passes.readlines()]
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if username in Usernames_txt and password in Passwords_txt:
                print("You are logged in successfully")
                break
            else:
                print("Your details are incorrect")
                User()

def SignUp():
    while True:
        with open('Usernames.txt') as users:
            Usernames_txt = users.readlines()
        with open('Passwords.txt') as passes:
            Passwords_txt = passes.readlines()
            username = input("Enter a username: ")
            if username not in Usernames_txt:
                password = input("Your password must be 8 or more characters: ")
                if len(password) >= 8:
                    if password not in Passwords_txt:
                        with open('Usernames.txt', 'a') as usernames:
                            usernames.write(username + '\n')
                        with open('Passwords.txt', 'a') as passwords:
                            passwords.write(password + '\n')
                        break


def User():
    while True:
        question = input("Do you want to login (Type L) or sign up (Type S)?")
        if question.upper() == "L":
            Login()
            break
        elif question.upper() == "S":
            SignUp()
            User()
            break

def main():
    User()

main()
