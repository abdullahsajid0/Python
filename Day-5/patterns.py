
def squarestar(num):
    print("This is the Square star pattern: \n")
    for i in range(num):  # Loop for rows
        for j in range(num):  # Loop for columns
            print("*", end=" ") 
        print() 
        
def rectangleStar(num):
    print("This is the Rectangle star pattern: \n")
    for i in range(num//2):  # Loop for rows
        for j in range(num):  # Loop for columns
            print("*", end=" ") 
        print() 

def leftAlignStar(num):
    print("This is the Left Aligned Star\n")
    for i in range(1,num+1):  # Loop for rows
        for j in range(i):  # Loop for columns
            print("*", end=" ") 
        print() 


def invleftAlignStar(num):
    print("This is the Inverse Left Aligned Star\n ")
    for i in range(num,0,-1):  # Loop for rows
        for j in range(i):  # Loop for columns
            print("*", end=" ") 
        print() 
        

def centerstar(num):
    print("This is the Centered Star\n ") 
    # for i in range(1, num + 1):  
    #     for j in range(num - i):  # Print spaces for alignment
    #         print(" ", end=" ")  
    #     for k in range(2 * i - 1):  # Print stars
    #         print("*", end=" ")
    #     print()  # Move to the next line

    for i in range(1, num + 1):
        print("  " * (num - i) + "* " * (2 * i - 1))

def invcenterstar(num):
    print("This is the Centered Star\n ") 
    # for i in range(num,0,-1):  
    #     for j in range(num - i):  # Print spaces for alignment
    #         print(" ", end=" ")  
    #     for k in range(2 * i - 1):  # Print stars
    #         print("*", end=" ")
    #     print()  # Move to the next line
    for i in range(num , 0, -1):
        print("  " * (num - i) + "* " * (2 * i - 1))

def diamondshape(num):
    print("This is the Centered Star\n")

    # Top half
    for i in range(1, num + 1):
        print("  " * (num - i) + "* " * (2 * i - 1))

    # Bottom half
    for i in range(num - 1, 0, -1):
        print("  " * (num - i) + "* " * (2 * i - 1))

def hollowSquare(num):
    print("This is the This is the Hollow Square\n")
    for i in range(num):
        for j in range(num):
            if i==0 or i==num-1 or j==0 or j==num-1 :
                print("*",end=" ")
            else:
                print(" ", end=" ")
        print()
def hollowTriangle(num):
    print("This is the This is the Hollow Triangle\n")
    for i in range(1, num + 1):
        # Print leading spaces
        for j in range(num - i):
            print(" ", end=" ")

        # Print stars and spaces
        for k in range(1, 2 * i):
            if k == 1 or k == 2 * i - 1 or i == num:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


while True:
    try:
        a= int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid Input! Please enter numbers only.")

squarestar(a)
rectangleStar(a)
leftAlignStar(a)
invleftAlignStar(a)
centerstar(a)
invcenterstar(a)
diamondshape(a)
hollowSquare(a)
hollowTriangle(a)