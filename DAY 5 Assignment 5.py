#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Project 1
#Do the project - Develop a cryptography app in python.
import onetimepad 
# python module to create GUI 
from tkinter import *
root = Tk() 
root.title("CRYPTOGRAPHY") 
root.geometry("800x600") 

def encryptMessage(): 
    pt = e1.get() 
    ct = onetimepad.encrypt(pt, 'random') 
    e2.insert(0, ct) 
def decryptMessage(): 
    ct1 = e3.get() 
    pt1 = onetimepad.decrypt(ct1, 'random') 
    e4.insert(0, pt1) 
label1 = Label(root, text ='plain text')
label1.grid(row = 10, column = 1) 
label2 = Label(root, text ='encrypted text') 
label2.grid(row = 11, column = 1) 
l3 = Label(root, text ="cipher text") 
l3.grid(row = 10, column = 10) 
l4 = Label(root, text ="decrypted text") 
l4.grid(row = 11, column = 10) 
e1 = Entry(root) 
e1.grid(row = 10, column = 2) 
e2 = Entry(root) 
e2.grid(row = 11, column = 2) 
e3 = Entry(root) 
e3.grid(row = 10, column = 11) 
e4 = Entry(root) 
e4.grid(row = 11, column = 11) 
# creating encryption button to produce the output 
ent = Button(root, text = "encrypt", bg ="red", fg ="white", command = encryptMessage) 
ent.grid(row = 13, column = 2) 
# creating decryption button to produce the output 
b2 = Button(root, text = "decrypt", bg ="green", fg ="white", command = decryptMessage) 
b2.grid(row = 13, column = 11) 
root.mainloop() 


# In[9]:


#Project 2
#Do the project - Guess the movie name in python.
import random
name = input("What is your name? ")
print("Good Luck ! ", name)

movies = ['war', 'kick', 'kgf', 'englishman', 
        'faimly', 'black', 'dhoom', 'man', 
        'rockstar', 'water', '3-idiate', 'goal'] 
movie = random.choice(movies)


print("Guess the characters")

guesses = ''
turns = 5


while turns > 0:

    failed = 0

    for char in movie: 


        if char in guesses: 
            print(char)

        else: 
            print("_")


            failed += 1


    if failed == 0:
        print("You Win") 
        print("your movie name is: ", movie) 
        break
    guess = input("guess a character:")
    guesses += guess 
    if guess not in movie:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Loose")


# In[14]:


# Project 4
# Do the project - Sending mail using Python
# from your Gmail account 
import smtplib 

#smtp Session
s=smtplib.SMTP("smtp.gmail.com",587)
#security
s.starttls
s.login("ranjeet809@gmail.com","muruvngzxpuxnnfe") #your mail id
msg = input("Enter your message here ")
s.sendmail("info@gmail.com","ranjeet809@gmail.com")
s.quit()


# In[ ]:




