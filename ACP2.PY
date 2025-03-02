secret_num= 67
num =()
val = int(input("Enter your guess"))
while (True):
    if int(1) > secret_num:
        print ("Guess a lower number")
    if int(1) < secret_num:
        print("Guess a higher number")
    if int(1) == secret_num:
        print("Hurray! You guessed it.")
        break