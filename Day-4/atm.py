def withdrawel(balance,amount):
    if amount > balance:
        print("Your Balance is inefficient")
    else:
        balance-=amount
        print(f"Please recieve your Rs:{amount} and Your Remaining Balance is {balance} ")
    return balance


a=-1
balance=5000
while True:  
    while True: 
        try:
            a=int(input( "Welcome to the Sajid's ATM. Select the option from Below (ie 1,2 3) \n1. Check Balance \n2. Withdraw Money \n 3. Exit \nYour Choice:  "))
            break
        except:
            
            print("Invalid input please Enter number")
    
    if a == 1:
        print(f"Your Balance is {balance}")
    elif a == 2:
        while True:
            try:
                amt= int(input("Enter the Number: "))
                if amt % 500!=0:
                    raise Exception("Please Enter the amount In 500 or 1000 Multiple ")
                break
            except ValueError:
                print("Invalid Input! Try Again! ")
            except Exception as e:
                print(e)
        balance= withdrawel(balance,amt)
    elif a==3:
        print("Thank You for choosing Our Service")
        break
    
    else:
        print("Invalid choice! Please select 1, 2, or 3.")