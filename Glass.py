import os
import Variables
from encrypter import encrypter
#Note - This is a standalone version

ter = "teron"
allowpy= "n"
allowpyexe = "n"
vc = "n"
user_input = ""

def TerminaTer():
    global ter, user_input

    Variables.hashed_pass2.clear()
    Variables.hashed_pass3.clear()
    Variables.vocabp.clear()
    Variables.memp.clear()
    Variables.vocablines.clear()
    Variables.memlines.clear()
    Variables.clogp.clear()
    Variables.illegal_chars.clear()

    if user_input == "<cmd:ter>" and ter == "teron":
        
        print("Bye, pal!")
        return True

    elif user_input == "<cmd:ter>" and ter == "teroff":

        return True
    
    elif user_input == "<cmd:teron>":

        ter = "teron"
        print("Ter : ON")

    elif user_input == "<cmd:teroff>":

        ter = "teroff"
        print("Ter : OFF")

    else:

        print("FATAL ERROR!")

def helper():

    Variables.hashed_pass2.clear()
    Variables.hashed_pass3.clear()
    Variables.vocabp.clear()
    Variables.memp.clear()
    Variables.vocablines.clear()
    Variables.memlines.clear()
    Variables.clogp.clear()
    Variables.illegal_chars.clear()

    global user_input

    if user_input == "<cmd:help>":

        print("<cmd:help> - Defines all functions")
        print("<cmd:help-> - Defines the selected function")
        print("<cmd:ter> - Terminated the chatbot")
        print("<cmd:teron> - Prints a 'goodbye' message when the program is terminated")
        print("<cmd:teroff> - Prints nothing when program is terminated")
        print("<cmd:verbose> - Goes itp verbose mode")
        print("<cmd:ulog> - Prints the update log")
        print("<cmd:ver> - Shows the version you are using")
        print("<cmd:tutor> - Enters tutorial mode")
        print("<cmd:clearc> - Clears the chat-logs")
        print("<cmd:clearm> - Clears the memory")
        print("<cmd:clog> - Prints the whole conversation")
        print("<cmd:cmem> - Prints the entire memory")
        print("<cmd:perm> - Edit your account permissions")
        print("<cmd:py> - Allows python code to be executed")

    elif user_input == "<cmd:help-ter>":

        print("<cmd:ter> - Terminated the chatbot")

    elif user_input == "<cmd:help-teron>":
        
        print("<cmd:teron> - Prints a 'goodbye' message when the program is terminated")

    elif user_input == "<cmd:help-teroff>":

        print("<cmd:teroff> - Prints nothing when program is terminated")    

    elif user_input == "<cmd:help->":

        print("<cmd:help-> - Defines the selected function")

    elif user_input == "<cmd:help-verbose>":

        print("<cmd:verbose> - Goes itp verbose mode")

    elif user_input == "<cmd:help-ulog>":

        print("<cmd:ulog> - Prints the update log")

    elif user_input == "<cmd:help-cmem>":

        print("<cmd:cmem> - Prints the entire memory")

    elif user_input == "<cmd:help-clog>":

        print("<cmd:clog> - Prints the whole conversation")

    elif user_input == "<cmd:help-clearm>":

        print("<cmd:clearm> - Clears the memory")

    elif user_input == "<cmd:help-clearc>":

        print("<cmd:clearc> - Clears the chat-logs")

    elif user_input == "<cmd:help-ver>":

        print("<cmd:ver> - Shows the version you are using")

    elif user_input == "<cmd:help-tutor>":

        print("<cmd:tutor> - Enters tutorial mode")

    elif user_input == "<cmd:help-perm>":

        print("<cmd:perm> - Edit your account permissions")

    elif user_input == "<cmd:help-py>":

        print("<cmd:py> - Allows python code to be executed")

    else:

        print("FATAL ERROR!")


def mem():
    
    Variables.hashed_pass2.clear()
    Variables.hashed_pass3.clear()
    Variables.vocabp.clear()
    Variables.memp.clear()
    Variables.vocablines.clear()
    Variables.memlines.clear()
    Variables.clogp.clear()
    Variables.illegal_chars.clear()

    global user_input

    if user_input == "<cmd:cmem>":

        user2 = input("Enter your username : ").strip()
        pass2 = input("Enter your password : ").strip()

        for ch in pass2:

            try:

                Variables.hashed_char = encrypter.get(ch)
                Variables.hashed_pass2.append(Variables.hashed_char)

            except Exception:

                Variables.illegal_chars.append(ch)

            
        if len(Variables.illegal_chars) != 0 :

            print("Wrong username or password!")
            Variables.illegal_chars.clear()
            return True

        elif len(Variables.illegal_chars) == 0:

            Variables.hashed_pass3 = ''.join(Variables.hashed_pass2)

            with open("user.txt", "r") as userfile, open("pass.txt", "r") as passfile:

                userlines = [line.strip() for line in userfile]
                passlines = [line.strip() for line in passfile]

                if user2 in userlines:

                    user_index = userlines.index(user2)
                    passchecker = passlines[user_index]
                    
                    if Variables.hashed_pass3 == passchecker:

                        print("Access allowed. Printing memory.")

                        with open("RuskVocab.txt", "r") as vocab, open("RuskMemory.txt","r") as mem:

                            Variables.vocablines = [line.strip() for line in vocab]
                            Variables.memlines = [line.strip() for line in mem]

                            for line in vocab:

                                Variables.vocabp.append(line)

                            for line in mem:

                                Variables.memp.append(line)

                            print("Bot Vocabulary : ")
                            print(f"{'\n'.join(Variables.vocabp)}")
                            print("\n")
                            print("Bot Memory : ")
                            print(f"{'\n'.join(Variables.memp)}")
                        
                    else:

                        print("Wrong username or password!")
                else:
                    print("Wrong username or password!")


    elif user_input == "<cmd:clearm>":
        
        user3 = input("Enter your username : ").strip()
        pass3 = input("Enter your password : ").strip()

        for ch in pass3:

            try:

                Variables.hashed_char = encrypter.get(ch)
                Variables.hashed_pass2.append(Variables.hashed_char)

            except Exception:

                Variables.illegal_chars.append(ch)

            
        if len(Variables.illegal_chars) != 0 :

            print("Wrong username or password!")
            Variables.illegal_chars.clear()
            return True

        elif len(Variables.illegal_chars) == 0:

            Variables.hashed_pass3 = ''.join(Variables.hashed_pass2)

            with open("user.txt", "r") as userfile, open("pass.txt", "r") as passfile:

                userlines = [line.strip() for line in userfile]
                passlines = [line.strip() for line in passfile]

                if user3 in userlines:

                    user_index = userlines.index(user3)
                    passchecker = passlines[user_index]
                    
                    if Variables.hashed_pass3 == passchecker:

                        print("Access allowed.")
                        print("WARNING! THIS COMMAD WILL ERASE ALL CHATBOT MEMORY. THIS ACTION CANNOT BE UNDONE AND DATA WILL BE IMPOSSIBLE TO GET BACK.")

                        allowchecker = input("Do you want to continue? y/n - ")

                        if allowchecker == "n":

                            print("Aborting memory deletion")

                        elif allowchecker != "y":

                            print("Invalid expression! Aborting process")

                        elif allowchecker == "y":

                            with open("RuskVocab.txt", "w") as vocab, open("RuskMemory.txt", "w") as mem:

                                print("All memory is wiped")

                    else:

                        print("Wrong username or password!")
                else:
                    print("Wrong username or password!")

def chatLogs():

    Variables.hashed_pass2.clear()
    Variables.hashed_pass3.clear()
    Variables.vocabp.clear()
    Variables.memp.clear()
    Variables.vocablines.clear()
    Variables.memlines.clear()
    Variables.clogp.clear()
    Variables.illegal_chars.clear()

    global user_input

    if user_input == "<cmd:clog>":

        user4 = input("Enter your username : ").strip()
        pass4 = input("Enter your password : ").strip()

        for ch in pass4:

            try:

                Variables.hashed_char = encrypter.get(ch)
                Variables.hashed_pass2.append(Variables.hashed_char)

            except Exception:

                Variables.illegal_chars.append(ch)

            
        if len(Variables.illegal_chars) != 0 :

            print("Wrong username or password!")
            Variables.illegal_chars.clear()
            return True

        elif len(Variables.illegal_chars) == 0:

            Variables.hashed_pass3 = ''.join(Variables.hashed_pass2)

            with open("user.txt", "r") as userfile, open("pass.txt", "r") as passfile:

                userlines = [line.strip() for line in userfile]
                passlines = [line.strip() for line in passfile]

                if user4 in userlines:

                    user_index = userlines.index(user4)
                    passchecker = passlines[user_index]
                    
                    if Variables.hashed_pass3 == passchecker:

                        print("Access allowed. Printing memory.")

                        with open("RuskVocab.txt", "r") as vocab, open("RuskMemory.txt","r") as mem:

                            Variables.vocablines = [line.strip() for line in vocab]
                            Variables.memlines = [line.strip() for line in mem]

                            for line in vocab:

                                Variables.vocabp.append(line)

                            for line in mem:

                                Variables.memp.append(line)

                            print("Bot Vocabulary : ")
                            print(f"{'\n'.join(Variables.vocabp)}")
                            print("\n")
                            print("Bot Memory : ")
                            print(f"{'\n'.join(Variables.memp)}")
                        
                    else:

                        print("Wrong username or password!")
                else:
                    print("Wrong username or password!")


    elif user_input == "<cmd:clearc>":
        
        user5 = input("Enter your username : ").strip()
        pass5 = input("Enter your password : ").strip()

        for ch in pass5:

            try:

                Variables.hashed_char = encrypter.get(ch)
                Variables.hashed_pass2.append(Variables.hashed_char)

            except Exception:

                Variables.illegal_chars.append(ch)

            
        if len(Variables.illegal_chars) != 0 :

            print("Wrong username or password!")
            Variables.illegal_chars.clear()
            return True

        elif len(Variables.illegal_chars) == 0:

            Variables.hashed_pass3 = ''.join(Variables.hashed_pass2)

            with open("user.txt", "r") as userfile, open("pass.txt", "r") as passfile:

                userlines = [line.strip() for line in userfile]
                passlines = [line.strip() for line in passfile]

                if user5 in userlines:

                    user_index = userlines.index(user5)
                    passchecker = passlines[user_index]
                    
                    if Variables.hashed_pass3 == passchecker:

                        print("Access allowed.")
                        print("WARNING! THIS COMMAD WILL ERASE ALL THE CHATLOGS. THIS ACTION CANNOT BE UNDONE AND DATA WILL BE IMPOSSIBLE TO GET BACK.")

                        allowchecker = input("Do you want to continue? y/n - ")

                        if allowchecker == "n":

                            print("Aborting memory deletion")

                        elif allowchecker != "y":

                            print("Invalid expression! Aborting process")

                        elif allowchecker == "y":

                            with open("conversationlog.txt", "w") as chat:

                                print("All memory is wiped")

                    else:

                        print("Wrong username or password!")
                else:
                    print("Wrong username or password!")

def AboutBot():

    Variables.hashed_pass2.clear()
    Variables.hashed_pass3.clear()
    Variables.vocabp.clear()
    Variables.memp.clear()
    Variables.vocablines.clear()
    Variables.memlines.clear()
    Variables.clogp.clear()
    Variables.illegal_chars.clear()

    global user_input

    if user_input == "<cmd:ver>":

        print(f"You are using {Variables.ver}")
    
    elif user_input == "<cmd:ulog>":

        print("Updates:\n")
        print(f"{Variables.updates1}\n")
        print(f"{Variables.updates2}\n")
        print(f"{Variables.updates3}\n")
        print(f"{Variables.updates4}\n")

    else:

        print("FATAL ERROR")

def permissions():

    global vc, allowpy, allowpyexe, user_input

    Variables.hashed_pass2.clear()
    Variables.hashed_pass3.clear()
    Variables.vocabp.clear()
    Variables.memp.clear()
    Variables.vocablines.clear()
    Variables.memlines.clear()
    Variables.clogp.clear()
    Variables.illegal_chars.clear()


    print("Permissions:")
    print("\n")
    print(f"Voice-chat - {vc}")
    print("\n")
    print(f"Allowpy - {allowpy}")
    print("\n")
    print(f"AllowpyExe - {allowpyexe}")

    perm_input = input(">> ").lower()

    if perm_input == "vc --y":

        vc = "y"
        print("Action done")

    elif perm_input == "allowpy --y":

        allowpy = "y"
        print("Action done")

    elif perm_input == "allowpyexe --y":

        allowpyexe = "y"
        print("Action done")

    elif perm_input == "vc --n":

        vc = "n"
        print("Action done")

    elif perm_input == "allowpy --n":

        allowpy = "n"
        print("Action done")

    elif perm_input == "allowpyexe --n":

        allowpyexe = "n"
        print("Action done")

    else:
        print("Illegal expression! Exiting permissions")


def pyexe():

    Variables.hashed_pass2.clear()
    Variables.hashed_pass3.clear()
    Variables.vocabp.clear()
    Variables.memp.clear()
    Variables.vocablines.clear()
    Variables.memlines.clear()
    Variables.clogp.clear()
    Variables.illegal_chars.clear()

    global user_input

    user6 = input("Enter your username : ").strip()
    pass6 = input("Enter your password : ").strip()

    for ch in pass6:

        try:

            Variables.hashed_char = encrypter.get(ch)
            Variables.hashed_pass2.append(Variables.hashed_char)

        except Exception:

            Variables.illegal_chars.append(ch)

            
    if len(Variables.illegal_chars) != 0 :

            print("Wrong username or password!")
            Variables.illegal_chars.clear()
            return True

    elif len(Variables.illegal_chars) == 0:

            Variables.hashed_pass3 = ''.join(Variables.hashed_pass2)

            with open("user.txt", "r") as userfile, open("pass.txt", "r") as passfile:

                userlines = [line.strip() for line in userfile]
                passlines = [line.strip() for line in passfile]

                if user6 in userlines:

                    user_index = userlines.index(user6)
                    passchecker = passlines[user_index]
                    
                    if Variables.hashed_pass3 == passchecker:

                            warnpy = input("WARNING! UNSUPERVISED OR CARELESS USE OF THIS COMMAND CAN POSSIBLE DELETE IMPORTANT FILES ON YOUR REAL SYSTEM. DATA RECOVERY WILL NOT BE POSSIBLE. DO YOU WISH TO CONTINUE? PROCEED WITH ABSOLUTE CAUTION. y/n - ")

                            if warnpy == "y" and allowpy == "y" and allowpyexe == "y":

                                pycmd = input(">>> ")

                                try:
                                    exec(pycmd)

                                except Exception:

                                    print("INCORRECT PROGRAM!!!")

                            if warnpy == "y" and allowpy != "y" and allowpyexe != "y":

                                print("Access denied. Exiting permissions")

                            elif warnpy == "n":

                                print("Exiting Python Runner")

                            else:
                                
                                print("Invalid expression! Aborting process")

                    else:

                        print("Wrong username or password!")

                else:
                    
                    print("Wrong username or password!")

def clsexe():

    Variables.hashed_pass2.clear()
    Variables.hashed_pass3.clear()
    Variables.vocabp.clear()
    Variables.memp.clear()
    Variables.vocablines.clear()
    Variables.memlines.clear()
    Variables.clogp.clear()
    Variables.illegal_chars.clear()


    global user_input

    os.system('cls' if os.name == "nt" else 'clear')




while True:

    user_input = input("> ").strip()

    if user_input in Variables.all_cmds:

        if user_input in Variables.ter_dict:

            should_stop = TerminaTer()

            if should_stop:
                break

        elif user_input in Variables.help_dict:

            helper()

        elif user_input in Variables.abtbot_dict:

            AboutBot()

        elif user_input in Variables.mem_dict:

            mem()

        elif user_input in Variables.chatlog_dict:

            chatLogs()

        elif user_input in Variables.perm_dict:

            permissions()

        elif user_input in Variables.pyexe_dict:

            pyexe()

        elif user_input in Variables.cls_dict:

            clsexe()
        else:

            print("Illegal command!")

    else:

        print("Illegal command!")