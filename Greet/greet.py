import argparse
from datetime import datetime, date

#parser = argparse.ArgumentParser(description="Greet Someone")
#parser.add_argument('--name', type=str, help='Name of the person', required=True)
#parser.add_argument('--age', type=int, help='Age of the person') 

#args = parser.parse_args()

#print(f"Hello, {args.name} !")
#if(args.age):
#    print(f"You are {args.age} years old")


# Custom funstion to parse the date string
def valid_date(s):
    try:
        return datetime.strptime(s, "%m-%d-%Y")
    except ValueError:
        raise argparse.ArgumentTypeError(f"Not a valid date : '{s}'. Use MM-DD-YYYY format")



name = input("Enter your name: ")
dob = valid_date(input("Enter your date of birth in MM-DD-YYYY format: "))

dateOfBirth = dob.date()
today = date.today()

age = today.year - dateOfBirth.year

if(today.month, today.day) < (dateOfBirth.month, dateOfBirth.day):
    age-=1


print(f"Your name is {name} ")
print(f"Your age is {age} ")
