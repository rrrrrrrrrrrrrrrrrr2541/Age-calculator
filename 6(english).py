from datetime import datetime

def calcAge(birthYear, birthMonth, birthDay):
    today = datetime.today()
    print(today)
    age = today.year - birthYear - ((today.month, today.day) < (birthMonth, birthDay))
    return age

year = int(input('Enter birth year: '))
month = int(input('Enter birth month: '))
day = int(input('Enter birth day: '))
print('Your age is:', calcAge(year, month, day))
input()
