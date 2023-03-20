sex = input("What is your sex?\n=> ")
age = int(input("Enter your age: "))

if sex == 'man':
    if age <= 18:
        print(f"You're too young to enter man You're {age}")
    elif age < 21:
        print(f"You're {age} you can enter")
    else:
        print(f"In you go and take off your shoe man: age {age}")
elif sex == 'women':
    if age <= 18:
        print(f"You're too young to enter baby girl You're {age}")
    elif age < 21:
        print(f"You're {age} you can enter cute girl")
    else:
        print(f"Here your free 2 drink coupon and Here you go: age {age}")
else:
    print("You're gay!")
    if age <= 18:
        print(f"You're too young to enter mister or misses You're {age}")
    elif age < 21:
        print(f"You're {age} you can enter")
    else:
        print(f"You can enter Mister or Misses {age}")