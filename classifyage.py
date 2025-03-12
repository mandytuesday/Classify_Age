#classify_age(age)
def age():
    age = int(input("Enter your age:"))
    if age < 0:
        print("Invalid age! Enter a value between 0 and 100.")
    elif age <=12:
        print("You are a CHILD.")
    elif age <=19:
        print("You are a TEEN.")
    elif age <=64:
        print("You are an ADULT.")
    elif age >=65:
        print("You are a SENIOR.")
        
age()

while True:
    a = input("Run Again?:")
    if a == "yes":
        age()
        
    else:
        b = print("Program Done.")
        break