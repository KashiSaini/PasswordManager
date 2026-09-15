from auth import login
from vault import generate_key, encrypt, decrypt
import json
import os

# create key if not exists
generate_key()

print("=== Password Manager ===\n")

def load_data():
    if not os.path.exists("data.json"):
        return {}

    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except:
        return {}


def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


def add_password():
    site = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    enc_pass = encrypt(password)

    data = load_data()

    data[site] = {
        "username": username,
        "password": enc_pass
    }

    save_data(data)

    print("Password saved!\n")


def view_password():
    site = input("Website to view: ")

    data = load_data()

    if site in data:
        print("Username:", data[site]["username"])
        print("Password:", decrypt(data[site]["password"]))
    else:
        print("No entry found\n")


def menu():
    while True:
        print("1. Add Password")
        print("2. View Password")
        print("3. Exit")

        ch = input("Choose: ")

        if ch == "1":
            add_password()

        elif ch == "2":
            view_password()

        elif ch == "3":
            break

        else:
            print("Invalid choice\n")


# -------- PROGRAM START --------

if login():
    menu()
else:
    print("Access denied")


#PART 1 – IMPORTS
""" from auth import login
from vault import generate_key, encrypt, decrypt
import json
import os

What each line means
Line	Meaning
from auth import login:-  Use the login() function you created earlier
from vault import generate_key:-  Function to create secret.key
encrypt, decrypt:-  Functions to secure passwords
json:-  To store data in JSON file
os:-  To check if files exist """

#PART 2 – CREATE KEY ON START
""" generate_key() """
""" When program starts:
If secret.key not exist → create it
If already exists → do nothing
So encryption always works. """

#PART 3 – LOAD DATA FUNCTION
""" def load_data():
Purpose:
Read passwords from data.json
Step by step
1. If file not exist
if not os.path.exists("data.json"):
    return {}
Means:
First time app runs
No data.json yet
return empty dictionary
{} = no passwords stored
2. Try to open file
try:
    with open("data.json", "r") as f:
        return json.load(f)
open file
read JSON
convert to Python dictionary
Example file:
{
  "gmail": {
     "username": "nishant",
     "password": "gAAAA...."
  }
}
Becomes:
{
  "gmail": { ... }
}
3. If error happens
except:
    return {}
If:
file corrupted
empty
wrong format
return empty instead of crash """

#PART 4 – SAVE DATA
""" def save_data(data): """
""" Purpose:
Write dictionary → data.json
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
json.dump = convert python → json
indent=4 = pretty format """

#PART 5 – ADD PASSWORD
""" def add_password():
1. Take input
site = input("Website: ")
username = input("Username: ")
password = input("Password: ")
User enters:
gmail
nishant
mypass
2. Encrypt password
enc_pass = encrypt(password)
VERY IMPORTANT
original: mypass
stored: gAAAAABxyz...
3. Load old data
data = load_data()
Get existing passwords
4. Add new entry
data[site] = {
    "username": username,
    "password": enc_pass
}
Dictionary becomes:
{
  "gmail": {
      "username": "nishant",
      "password": "encrypted..."
  }
}
5. Save back
save_data(data)
Write to file. """

#PART 6 – VIEW PASSWORD
""" def view_password():
1. Ask which site
site = input("Website to view: ")
2. Load data
data = load_data()
3. Check if exists
if site in data:
If found:
print("Username:", data[site]["username"])
print("Password:", decrypt(data[site]["password"]))
Decrypt before showing!
4. If not found
else:
    print("No entry found")
 """

#PART 7 – MENU SYSTEM
""" def menu():
    while True:
Infinite loop until user exit.
Show options
print("1. Add Password")
print("2. View Password")
print("3. Exit")
Take choice
ch = input("Choose: ")
Call functions
if ch == "1":
    add_password()
elif ch == "2":
    view_password()
elif ch == "3":
    break
break = exit loop """

#PART 8 – PROGRAM START
""" if login():
    menu()
else:
    print("Access denied")
FLOW:
First → login()
If correct → open menu
Else → block """