for numbers in range (1,21):
    if numbers == 4 or numbers == 13:
        print(f"{numbers} is unlucky")
    elif numbers % 2 ==0:
        print(f"{numbers} is even") 
    else:
        print(f"{numbers} is odd")
        