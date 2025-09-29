import random 
def is_win(player, opponent):
    if player=='r' and opponent=='s':
        print(f"computer chose:{opponent}")
        print("Ya! You win")
    elif player=='r' and opponent=='p':
        print(f"computer chose:{opponent}")
        print("computer wins!")
    elif player=='s' and opponent=='p':
        computer_chose(opponent)
        print("Ya! you win")
    else:
        print(f"computer chose:{opponent}")
        print(" computer wins!")
def computer_chose(opponent):
    print(f"computer chose:{opponent}")
def user():
    x=input("Enter your choice(r->rock,p->paper,s->scissor):").lower()
    let_com=random.choice(['r','p','s'])
    if let_com==x:
        print("tie")
    else:
        is_win(x,let_com)
        
user()

