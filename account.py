import json
import random
import hashlib 
import uuid
from hmac import compare_digest

print('1. create account')
print('2.load account')

e = input('choose an option')
if e == '1':
    print('you chose to create an account')
    username = input('username:')
    email = input('email:')
    password = input('choose a password')
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    dictionary ={
        'name' : username,
        'email' : email,
        'password' : password_hash ,
        "user_id": str(uuid.uuid4())
    }
  
    with open('account.json', 'w') as r:
        json.dump(dictionary, r, indent = 4)

with open('account.json', 'r') as read_file:
  data = json.load(read_file)

if e == "2":
    print(data)

with open('account.json', 'r') as read_file:
    data = json.load(read_file)

if e == '3':
    user = input('username:')

    if data["name"] == user:
        password = input("password:")
        new_hash = hashlib.sha256(password.encode()).hexdigest()
        if compare_digest(new_hash, data["password"]):
          print('login success')
        else:
          print('pass incorrect')
    else:
        print('incorrect username')
