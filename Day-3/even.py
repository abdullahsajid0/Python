def Even(num):
    if num % 2 ==0:
        return True
    else:
        return False
    
while True:
    try:
        num= int(input("Enter the Number: "))
        break
    except:
        print("Invalid Input! Try Again! ")

result=Even(num)
if result:
    print(f"The Number {num} is Even.")
else:
        print(f"The Number {num} is Odd.")