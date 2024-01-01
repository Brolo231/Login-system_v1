# Login-system_v1
My first, and very simple, login system.

My thought process when creating this simple login system was the idea to make something that could do the fundamental tasks of a login system, even if it was overly simplified, had security issues, and other problems.

My future goals and version additions of my login system are as follows: 

* Hash passwords for security reasons 
* Ask the user to enter their password twice to see if the passwords match
* Ask the user if they would like to enter their own password or if they would like a password generated for them
* A GUI interface

NOTE: There is a security issue within this program. My first thoughts when designing this program was to create a storage system that stores a user's username and password together and then when asked to login, the system would check if those passwords match. Instead I created two separate files to store the information separately. However, if someone eneters a correct username but someone else's password, they will still be logged in. This is the first issue i need to adress when designing my next login system. 
