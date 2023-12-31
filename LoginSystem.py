# Simple Login system

# Login
def Login():
    while True:
        # text file to store usernames
        with open('Usernames.txt') as users:
            Usernames_txt = [line.strip() for line in users.readlines()]
        # text file to store passwords
        with open('Passwords.txt') as passes:
            # line.strip() removes whitespace to make checking for existing values easier
            Passwords_txt = [line.strip() for line  in passes.readlines()]
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if username in Usernames_txt and password in Passwords_txt:
                print("You are logged in successfully")
                break
            else:
                print("Your details are incorrect")
                User()

# Sign up
def SignUp():
    while True:
        with open('Usernames.txt') as users:
            Usernames_txt = [line.strip() for line in users.readlines()]
        with open('Passwords.txt') as passes:
            Passwords_txt = [line.strip() for line  in passes.readlines()]
            username = input("Enter a username: ")
            if username not in Usernames_txt:
                password = input("Enter a password of 8 or more characters: ")
                if len(password) >= 8:
                    if password not in Passwords_txt:
                        # text file appending

                        # we only want to append our usernames and passwords once the username and password have
                        # both met specific requirements
                        with open('Usernames.txt', 'a') as usernames:
                            usernames.write(username + '\n')
                        with open('Passwords.txt', 'a') as passwords:
                            passwords.write(password + '\n')
                        break
                else:
                    print("Your password must be more than 8 characters.")
            elif username in Usernames_txt:
                print("Username already exists. Please enter a different username")


def User():
    while True:
        question = input("Do you want to login (Type L) or sign up (Type S)?")
        if question.upper() == "L":
            Login()
            break
        elif question.upper() == "S":
            SignUp()
            # If a user signs up we want the program to ask them to login immediately after signing up
            User()
            break

def main():
    User()

main()
