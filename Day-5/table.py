# This program give us the full table by inputing the number 
def table(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")


while True:
    try:
        a= int(input("Enter the number: "))
        break
    except:
        print("Invalid Input! Please enter numbers only!!")
 
table(a)
#this is new
