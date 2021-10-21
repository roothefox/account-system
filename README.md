# account-system
# about 
this one is an account creation and viewer program.

 when you create an account and choose a password.
 
 the program hashes it using SHA256.
 you can share the password all you want but nobody can decode it.
 
to select an option just type the number on startup.

number 2 shows you the email, username, hashed password and the randomly generated user_id.

everything will be stored in a json file called accounts.json.

i wanted to add a login function but i kept getting errors.

here's an example of the .json file
```
{
    "name": "roothefox",
    "email": "randomtestmail@example.com",
    "password": "cc63371a27ea1499200087267269c495fac5a4b5c8eb3c7f51a2559a5538fdb1",
    "user_id": "650c8566-9c0f-47c3-b335-77d41cfc360c"
}
```

# usage

to start the program change to the repos directory and do
```
python account.py
```
or for the python3 users
```
python3 account.py
```

if you just opened the program for the first time you have to choose option 1
