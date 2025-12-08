# Python
def convert(unit,temp):
    if unit.lower() == "f":
        result=temp*9/5 + 32
    elif unit.lower() == "c":
        result =  (temp-32)*5/9
    else:
        return "Invalid unit! Please choose 'C' or 'F'."

    return result

s=input("what unit u want to convert Chose any option from below \n 1. f\n 2. c \n Your Answer:  ")
t= float(input("Enter the Temp Value: "))
print(convert(s,t))