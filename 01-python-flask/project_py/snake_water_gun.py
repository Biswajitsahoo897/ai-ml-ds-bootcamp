
# import random

# # Game choices
# choices = ['Snake', 'Water', 'Gun']

# # Get user choice
# user_choice = input("Enter your choice (Snake, Water, Gun): ").capitalize()

# # Check if the user choice is valid
# if user_choice not in choices:
#     print("Invalid choice!")
# else:
#     # Generate computer choice
#     computer_choice = random.choice(choices)
    
#     # Determine the winner
#     if user_choice == computer_choice:
#         result = "It's a tie!"
#     elif (user_choice == 'Snake' and computer_choice == 'Water') or \
#          (user_choice == 'Water' and computer_choice == 'Gun') or \
#          (user_choice == 'Gun' and computer_choice == 'Snake'):
#         result = "You win!"
#     else:
#         result = "Computer wins!"

#     # Display the choices and result
#     print(f"Your choice: {user_choice}")
#     print(f"Computer's choice: {computer_choice}")
#     print(result)

import random
comp=random.randint(1,3)
print('USER SELECTION:')
print("1 for Snake , 2 for Water & 3 for Gun: ")
user=int(input("Enter Your choice : "))
if (user==comp):
    print("It's a tie!")
if user>3:
    print("Invalid!!")
else:    
    if(user==1 and comp==2):
        print('Congratulations!!! You Win') 
        
    elif(user==2 and comp==3) :
        print("Congratulations!!! You win")
    elif(user==3 and comp==1) :
        print("Congratulations!!! You Win")

    else:
        print("Computer Wins!!....")     
    print(f"Your choose   :{user} ")
    print(f"Computer choose :{comp} ")
    
    
print("Thank You!!")