def filtered_user_input(user_input):
    allowed_chars = "0123456789.+-*/"
    filtered_ui = ""

    for ch in user_input:
        if ch in allowed_chars:
            filtered_ui+=ch
    
    spaces = ""
    ops = "+-*/."

    for ch in filtered_ui:
        if ch in ops:
            spaces+=(f" {ch} ")
        else:
            spaces+=ch

    return spaces

reserver_ops = ["+", "-", "*", "/", "add", "subtract", "multiply", "divide"]

while True:

    user_input = input("> ").lower()
    user_input_filtered = filtered_user_input(user_input)
    words = user_input.split()
    words2 = user_input_filtered.split()
    prod = 1
    numbers = []


    for word in words2:
        try:
            numbers.append(float(word))
        except ValueError:
            pass
        
           
    if len([op for op in reserver_ops if op in user_input]) > 1:
        print("I can only perform one operation at a time, pal.")
        continue

    elif "+" in words2 or "add" in words:
        if numbers:
            try:
                print("<Rusk-Bot> The sum is = ",sum(numbers))

            except ValueError:
                print("**ERROR IN INPUT**")


        else:
            print("You did not enter any number, pal.")
    

    elif "*" in words2 or "multiply" in words:
        
        if numbers:
        
            try:
                for number in numbers:
                    prod *= number
                print(f"<Rusk-Bot> The product is = {prod}")

            except ValueError:
                print("**ERROR IN INPUT**") 

        else:
            print("You did not enter any number, pal.")
    

    elif "-" in words2 or "subtract" in words or "minus" in words:
        
        if numbers and len(numbers) == 1:
            
                print(f"You only entered one number, pal. Enter more than one number for an arithmetic operation to be done. Not just {numbers}")
        
        elif len(numbers)>1:
            
            try:
                diff = numbers[0]
                
                for number in numbers[1:]:
                    diff -= number
                print(f"<Rusk-Bot> The difference is = {diff}")
            except ValueError:
                print("**ERROR IN INPUT**")
            

        
        else:

            print("You did not enter any number, pal.")
            


    elif "/" in words or "divide" in words:


        if numbers:   
            try:

                quo = numbers[0]
                for number in numbers[1:]:
                    quo /=number
                if len(numbers) == 2:
                    rem = numbers[0] % numbers[1]
                    print(f"<Rusk-Bot> The quotient is = {quo} and the remainder is approximately = {round(rem, 10)}")
                

                else:
                    print(f"<Rusk-Bot> The quotient is = {quo}")

            except ZeroDivisionError:
                print("You cannot divide by 0, pal.")
            
            except ValueError:
                print("**ERROR IN INPUT**")
            
        else:
            print("You did not enter any number, pal.")
        
    elif "square" in words:
        if "root" in words:
            if len(numbers) == 1:

                sqrt = numbers[0] ** 0.5
                print(f"The square root of {numbers[0]} is = {sqrt}")
            
            else:
                print("**ERROR IN INPUT**")
        else:

            if len(numbers) == 1:
                
                sq = numbers[0] * numbers[0]
                print(f"The square of {numbers[0]} = {sq}")

            else:
                print("**ERROR IN INPUT**")


    elif "cube" in words:
        if "root" in words:
            if len(numbers) == 1:

                curt = numbers[0] ** (1/3)
                print(f"The cube root of {numbers[0]} is = {curt}")
            
            else:
                print("**ERROR IN INPUT**")
        else:

            if len(numbers) == 1:
                
                cu = numbers[0] * numbers[0] * numbers[0]
                print(f"The cube of {numbers[0]} = {cu}")

            else:
                print("**ERROR IN INPUT**")
        
    elif len(numbers) == 0:
        print("I can only do arithmetic operations and basic squares, cubes and roots, pal.")