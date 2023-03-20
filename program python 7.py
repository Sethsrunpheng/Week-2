o_year = int(input('Enter the year: '))
if o_year % 4 == 0:
    if o_year % 100 == 0:
        if o_year % 400 == 0:
            print(f'Leap year ({o_year})')
        else:
            print(f'Not leap year ({o_year})')
    else:
        print(f'Leap year ({o_year})')
else:
    print(f'Not a leap year ({o_year})')