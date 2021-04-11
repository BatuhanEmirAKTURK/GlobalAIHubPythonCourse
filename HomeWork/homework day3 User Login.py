import time

print("""
-----------------------

       KOZMOIDEA

         Login 

-----------------------
-----------------------

For login : "x"

Quit : "q"

-----------------------
""")

logsin = input("Please, enter the action you want to do:")
time.sleep(0.3)

if logsin == "q" or logsin == "Q":
    print("\nLogging out ...")

userp = {"name":"Batuhan",
        "password":"Akturk412"
         } # Username and password will be taken from the dictionary

try1 = 3

while logsin == "x" or logsin == "X":

    user1 = input("\nPlease enter username:")
    password1 = input ("\nPlease enter the password:")

    if  user1 != userp["name"] and password1 != userp["password"]:
        try1 -=1
        time.sleep(0.3)
        print("\nUsername and password are incorrect! Please try again!","Your remaining right:{}".format(try1))

    elif  user1 == userp["name"] and password1 != userp["password"]:
        try1 -=1
        time.sleep(0.3)
        print("\nUsername is correct but password is wrong! Please try again!","Your remaining right:{}".format(try1))

    elif  user1 != userp["name"] and password1 == userp["password"]:
        try1 -=1
        time.sleep(0.3)
        print("\nPassword is correct but username is wrong! Please try again!","Your remaining right:{}".format(try1))

    else:
        print("\nLogging in...")
        time.sleep(1)
        break

    if try1 == 0:
        print("\nYour right is over, exiting...")
        time.sleep(0.3)
        break
    
