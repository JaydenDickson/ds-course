import math


def main(): 
    #   Format first prompt
    user_prompt = """
    Please choose from the following options: 

    Investment  - To calculate the amount of interest you'll earn on your investment.
    Bond        - To calculate the amount you'll have to pay on a home loan.

    Enter either 'investment' or 'bond' to proceed: 
    """
    #   Prompt user for calculation type
    calculation_type = input(user_prompt)
    #   "Clean" string of caps and whitespace
    clean_calculation_type = "".join(calculation_type.lower().split())
    #   ----------BONDS----------
    if clean_calculation_type == "bond": 
        present_value = float(input("What is the present value of the house?: "))
        interest_rate = float(input("What is the interest rate?: "))
        time = float(input("Over how many months do you plan to repay the bond?: "))
        total_amount = ((interest_rate/(100*12))*(present_value))/(1 - (1+(interest_rate/(100*12)))**(-time))
        print(f"Your monthly repayment will be: {total_amount:.2f}") #Print monthly repayment with 2 decimal places
    #   ----------INVESTMENTS----------
    elif clean_calculation_type == "investment": 
        amount = float(input("How much money are you depositing?: "))
        interest_rate = float(input("What is the interest rate?: "))
        time = float(input("How many years do you plan on investing?: "))
        interest_type = input("Do you want simple or compound interest. Please enter ''simple'' or ''compound'': ")
        clean_interest_type = "".join(interest_type.lower().split())

        if clean_interest_type == "compound": 
            total_amount = amount* math.pow((1+(interest_rate/100)),time)
            print(f"Your total investment value will be: {total_amount:.2f}") #Print total amount with 2 decimal places
        elif clean_interest_type == "simple": 
            total_amount = amount*(1 + (interest_rate/100)*time)
            print(f"Your total investment value will be: {total_amount:.2f}") #Print total amount with 2 decimal places
        else:
            print("Please try again and enter either 'simple' or 'compound' to proceed.")
            return
    else: 
        print("Please try again and enter either 'investment' or 'bond' to proceed.")
        return  
        
if __name__ == "__main__": 
    main()
