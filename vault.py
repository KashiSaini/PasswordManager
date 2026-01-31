from cryptography.fernet import Fernet
import os

# Run only once to create key
def generate_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as f:
            f.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt(text):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(text.encode()).decode()

def decrypt(text):
    key = load_key()
    f = Fernet(key)
    return f.decrypt(text.encode()).decode()


#What is Fernet?
""" Fernet = encryption system
it does symmtric enryption """

#import os
""" checking if file exists
interacting with system files """
#os.path.exists("secret.key")
""" “Do we already have an encryption key?” """

#function generate key
""" Check if key already exists:- os.path.exists("secret.key")
Why?
We must create key only ONCE
If we create new key → old passwords become useless. """

""" Create new encryption key
key = Fernet.generate_key()
makes a random key """

""" Save key to file
with open("secret.key", "wb") as f:
    f.write(key)
"wb" = write binary
because key is not normal text
it is bytes
Now file appears:
secret.key """

#function load_key()
""" def load_key():
    return open("secret.key", "rb").read()
What this does
Opens secret.key
reads the key
returns it
"rb" = read binary
Think:
Take house key from drawer """

#function encrypt()
""" def encrypt(text):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(text.encode()).decode() """

""" Get key
key = load_key()
Bring secret key from file """

""" Create Fernet object
f = Fernet(key)
Think:
Create lock machine using your key """

""" Convert text → bytes
text.encode()
Because:
encryption works on bytes
not normal string
Example:
"hello" → b"hello" """

""" Encrypt
f.encrypt(...)
Converts:
"hello"
into:
gAAAAABlY.... """

""" decode()
.decode()
Encrypted result is bytes
We convert to normal string to store in JSON """

#function decrypt()
""" def decrypt(text):
    key = load_key()
    f = Fernet(key)
    return f.decrypt(text.encode()).decode() """

""" Same steps but reverse:
load key
create Fernet
convert string → bytes
decrypt
bytes → string """









