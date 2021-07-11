import json
import random
import hashlib 
import pathlib

print('1. create account')
print('2.load account')

e = input('choose an option')
if e == '1':
    print('you chose to create an account')
    username = input('username:')
    email = input('email:')
    password = input('choose a password')
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    userid = random.randint(0000000, 9999999)

    dictionary ={
        "name" : username,
        "email" : email,
        "password" : password_hash ,
        "user_id" : userid
    }
  
    
    json_data = json.dumps(dictionary)
  
    with open("account.json", "w") as outfile:
        json.dump(json_data, outfile)

with open('account.json', 'r') as read_file:
  data = json.load(read_file)

if e == "2":
    My_file=open('account.json')
    try:
        My_file.close()
        print(data)
    except FileNotFoundError:
        print("Files couldn't be opened!")        
