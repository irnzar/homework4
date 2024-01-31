import random
import time
import os

current_directory = os.getcwd()
file_list = os.listdir(current_directory)

if "game_logs" in file_list:
    print ("Folder exist")
else:
    new_directory = "game_logs"
    os.mkdir(new_directory)
    print("Folder created")
    
file_path = str(current_directory)+"\game_logs\game_history_"+str(int(time.time()))+".txt"
print (file_path)



number = random.randint(1,100)
guess = input("Please enter a number 1..100: ")
guess = int(guess)

with open(file_path, "a") as f:
    f.write("Time: "+str(time.time())+", Guess:"+str(guess)+", random_integer: "+str(number)+"\n")

while True:
    if number == guess:
        print("Correct")
        with open(file_path, "a") as f:
            f.write("Correct\n")
        break
    elif number > guess:
        print("too low")
        guess = input("please enter a number: ")
        guess = int(guess)
        
        with open(file_path, "a") as f:
            f.write("too low\n")
            f.write("Time: "+str(time.time())+", Guess:"+str(guess)+", random_integer: "+str(number)+"\n")
        
    else: 
        print("too high")
        
        guess = input("please enter a number: ")
        guess = int(guess)
        
        with open(file_path, "a") as f:
            f.write("too high\n")
            f.write("Time: "+str(time.time())+", Guess:"+str(guess)+", random_integer: "+str(number)+"\n")

