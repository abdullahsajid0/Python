def Grading(tm,om):
    percnt = (om*100)/tm
    if percnt > 80:
        grade="A"
    elif percnt >70:
        grade="B"
    elif percnt >60:
        grade="C"
    elif percnt >50:
        grade="D"
    else:
        grade=0
    return grade

while True:
    try:
        obtainedMarks= float(input("Enter your Obtained Marks : "))
        break
    except:
        print("Please Enter your Marks in Number (23,43): ")




while True:
    try:
        TotalMarks= float(input("Enter your Total Marks : "))
        break
    except:
        print("Please Enter your Marks in Number (23,43): ")

result = Grading(TotalMarks,obtainedMarks)
if result == 0:
    print("You Got Fail. Better luck next time!")
else:
    print(f"Your Grade is {result} ")
