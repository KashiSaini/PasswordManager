import getpass

MASTER_PASSWORD = "admin123"

def login():
    print("=== Password Manager Login ===")

    pwd = getpass.getpass("Enter master password: ")

    if pwd == MASTER_PASSWORD:
        print("Login successful!\n")
        return True
    else:
        print("Wrong password!\n")
        return False

#What is getpass?
""" A Python module that:
takes password input
but HIDES what user types
Example:
Normal input:
input("Password: ")
User sees:
Password: mysecret
With getpass:
Password:
Nothing visible — like real login screens. """

#Master Password Variable
""" MASTER_PASSWORD = "admin123"
This is:
the correct password
stored inside program
used to compare with user input
Right now simple version
Later we will use hashing (more secure). """

#Function Definition
""" def login():
This creates a function named:
👉 login()
Purpose:
To check if user entered correct master password """

#Print Heading
""" print("=== Password Manager Login ===")
Just UI decoration
So terminal looks clean. """

#Take Password Input
""" pwd = getpass.getpass("Enter master password: ")
Step by step
Shows message:
→ Enter master password:
User types
Characters stay hidden
Value stored in variable pwd
Example:
User types → admin123
But screen shows → blank """

#Compare Password
""" if pwd == MASTER_PASSWORD:
This is the MAIN LOGIC
Means:
If user typed password
is exactly equal to
stored master password """

#If Correct
""" print("Login successful!\n")
return True
Show success message
return True to main program """

#If Wrong
""" else:
    print("Wrong password!\n")
    return False
show error
return false"""