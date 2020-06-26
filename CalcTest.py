from IPython.display import clear_output 

final_command = "INITIATE PROGRAM"

while final_command != "NO":
    
    option_chosen = int(0)
   
    print("Welcome to the Calculator!\n")
    print("Here's what you can do:\n 1. Perform a Calculation. \n 2. Solve a Quadratic Equation. \n")

    option_chosen = int(input("So what do you wanna do? 1 or 2? \nAnswer:")) 

    if option_chosen == 1:

        command = str(" ")
        Operations = []
        Answers = []

        initiate_response = "Hello! Welcome to the Calculator!"
        basic_instructions = "The basic operations to be used are listed below: \n '+' : Addition \n '-' : Subtraction \n '*' : Multiplication \n '/' : Division"
        exponential_instructions = "For Roots and Exponents use the double asterisks (**).\n For Example: \n 2**3 = 8 and 169**0.5 = 13"
        warning = "Be careful of the order of operations by using the parenthesis ()."

        print(initiate_response)
        print(basic_instructions)
        print(exponential_instructions)
        print(warning)

        while command != "EXIT":
    
            calculation_answer = float(0.0)
    
            calculation_query = input("\nEnter Your Query Please:\n")
            calculated_answer = str(eval(calculation_query))
    
            print("The Answer is: " + calculated_answer)
    
            Operations.append(calculation_query)
            Answers.append(calculated_answer)
    
            print('\n')
    
            command = str(input("Exit or Continue Program? \nEnter any key to continue or enter 'Exit' to Quit: "))
            command = command.upper()

        else:
    
            Index = 0
            Number = 1
            List_Size = len(Operations)
            print("The Total Calculations you did:\n")
        
            while Index < List_Size :
                print(f"{Number}.  {Operations[Index]} = {Answers[Index]} \n") 
                Index += 1
                Number += 1

            print('\n')
            print("Thanks for using the Calculation Program! :))")
            
            final_command = str(input("Do you want go back to Main Menue?\nWARNING: It will Erase all Data.\nSay 'Yes' or 'No': "))
            final_command = final_command.upper()

            if final_command == "YES":
                clear_output()
                continue

    elif option_chosen == 2:
        a = int (0)
        b = int (0)
        c = int (0)
        x1 = float(0)
        x2 = float(0)
        command = str("no")

        while command == "no":
    
            a = int(input("Enter the value of the co-efficient of x^2 =\t"))
            b = int(input("Enter the value of the co-efficient of x =\t"))
            c = int(input("Enter the value of the constant =\t"))

            x1 = (-b+((b**2)-4*a*c)**0.5) / (2*a)
            x2 = (-b-((b**2)-4*a*c)**0.5) / (2*a)

            print(f"The Value of the Variable 'x' can either be {x1} or {x2}")
    
            command = str(input("Exit Quadratic Calculator? Enter 'No' to continue, or any other key to Exit: "))
            command = command.lower()
        
        else:
            print("Thankyou for using the Quadratic Calculator Program :))")
            final_command = str(input("Do you want to go back to Main Menue?\nWARNING: It will Erase all Data.\nSay 'Yes' or 'No': "))
            final_command = final_command.upper()

            if final_command == "YES":
                clear_output()
                continue
    
    else:
        print("Invalid Choice!")

        final_command = str(input("Do you want to go back to Main Menue?\nWARNING: It will Erase all Data.\nSay 'Yes' or 'No': "))
        final_command = final_command.upper()

        if final_command == "YES":
            clear_output()
            continue


else:
    print("Thanks for using our Calculator Program. :))")