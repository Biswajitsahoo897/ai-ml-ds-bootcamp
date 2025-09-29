import random
def user_guess(x):
    random_num=random.randint(1,x)
    guess=0
    while guess!=random_num:
        guess=int(input(f"Guess a number between 1 and {x} : "))
        if guess<random_num:
            print("Try again ,Too Low a little higher")
        elif guess>random_num:
            print("Try again ,Too high a little low")
    print(f"Ya congrats . You have guessed the number correctly!!!")
user_guess(20)
def computer_guess(x):
    low=1
    high=x
    feedback=""
    while feedback!='c':
        Guess=random.randint(low,high)
        feedback=input(f"Is{Guess} too high (H),too low(L) or correct(C)?").lower()
        if feedback=='h':
            high=Guess-1
        elif feedback=='l':
            low=Guess+1
    print(f"Ya!! The computer guessed ur {Guess} number correctly!")
computer_guess(20)
    