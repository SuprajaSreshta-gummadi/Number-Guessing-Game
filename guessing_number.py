import random
number= random.randint(1,100)
while True:
    try:
        guess =int(input('guess the number in between 1 to 100:'))

        if number < guess:
            print("its too high")
        elif number > guess:
            print("its too lower")
        else:
            print("Well done,you guess correct number")
            break
    except ValueError:
        print("please enter a valid number:")
    
