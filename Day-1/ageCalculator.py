print("This program calculates your age you just have to enter your date of birth.")
from datetime import date
def CalculateAge(birthdate):
    today = date.today()
    age = today.year - birthdate.year -((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
day = int(input("Enter the day you were born (1-31): " ))
month = int(input("Enter the month you were born (1-12): "))
year = int(input("Enter the year you were born (xxxx): "))
birthdate = date(year,month,day)
age = CalculateAge(birthdate)
print(f"You are {age} years Old")
