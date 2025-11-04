# NOTE: THIS IS A STANDALONE COPY OF THE REAL GUARDS SUBSYSTEM. THE ONE USED FOR RUSK-BOTV1.10 IS A BIT DIFFERENT VERSION THAN THIS. KEEP IN MIND WHILE USING.

import os
from encrypter import encrypter


characters = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M","q", "w", "e", "r", "t", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "_", "+", "[", "]", "\\", "|", ":", ";", "'", "\"", "<", ",", ">", ".", "/", "?"]
hash_failed = []
hasher = []
illegal_chars = []


while True:

    illegal_chars.clear()
    hash_failed.clear()
    hasher.clear()

    sign = input("> Would you like to login or signup? Press 1 for signup, and 2 for login : ").lower()
    
    if sign == "1":

        user1 = input("> Enter Username : ").strip()
        pass1 = input("> Enter Password : ").strip()

        for ch in user1:
                
                if ch not in characters:
                    illegal_chars.append(ch)


        for ch in pass1:
                if ch not in characters:
                     illegal_chars.append(ch)

        userlen = len(user1)
        passlen = len(pass1)

        if len(illegal_chars) != 0:
             
             print(f"Your username or password contains illegal characters! Choose another.")
        
        elif userlen <3 or userlen > 20:
            print("> Your selected username must be b/w 3 and 20 characters! Your existing username does not meet that criteria! Choose another.")

        elif passlen <3 or passlen > 20:
             print("> Your selected password must be b/w 3 and 20 characters! Your existing password does not meet that criteria! Choose another.")


        elif userlen >= 3 and userlen <= 20 and passlen >= 3 and passlen <= 20:

            with open("user.txt","r") as userfile:

                userlines = [line.strip() for line in userfile]

                if user1 in userlines:
                    print("> Your username already exists! Choose another.")

                elif user1 not in userlines:

                    with open("user.txt","a") as userfile:
                         
                        userfile.write(f"{user1}\n")

                    with open("pass.txt","a") as passfile:
                             
                        for ch in pass1:
                                
                            try:
                                
                                hashed_char = encrypter.get(ch)
                                    
                                if hashed_char:
                                        
                                    hasher.append(hashed_char)
                                        
                                else:
                                    hash_failed.append(ch)

                            except Exception:
                                hash_failed.append(ch)

                        
                        if len(hash_failed) != 0:

                            print("Your password could not be parsed!")
                        
                        elif len(hash_failed) == 0:

                            passfile.write(f"{''.join(hasher)}\n")




    elif sign == "2":
        
        user2 = input("> Enter your username : ").strip()
        pass2 = input("> Enter your password : ").strip()

        hashed_pass = []

        for ch in pass2:

            try:

                hashed_char = encrypter.get(ch)

                if hashed_char:

                    hashed_pass.append(hashed_char)

            except Exception:
                
                print("Wrong username or password!")
                continue
            
        hashed_pass2 = ''.join(hashed_pass)

        with open("user.txt","r") as userfile, open("pass.txt","r") as passfile:

            userlist = [line.strip() for line in userfile]
            passlist = [line.strip() for line in passfile]

            if user2 in userlist:
                userindex = userlist.index(user2)
                passchecker = passlist[userindex]

                if  hashed_pass2 == passchecker:
                    print (f"Welcome, {user2}")
                    print ("Press Enter to continue")
                    enter = input("> ")

                    os.system('cls' if os.name=="nt" else 'clear')
                    break

                else:
                    print("Wrong username or password!")

                
            else:
                    print("Wrong username or password!")

    else:

        print("> You have not signed up or logged in to your account to start a conversation yet!")