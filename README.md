# account-system
# about 
this one is an account creation and viewer program.

 when you create an account and choose a password, the program hashes it using SHA256, you can share the password all you want but nobody can decode it
to select an option just type the number on startup.
number 2 shows you the email, username, hashed password and the randomly generated user_id.
everything will be stored in a json file called accounts.json.
i wanted to add a login function but i kept getting errors.
here's an example of the .json file
```
"{\"name\": \"name\", \"email\": \"examplemail@gmail.com\", \"password\": \"hashedd_password\", \"user_id\": 8808592}"
```

# usage
