# Simple Calculator using argparse

import argparse
parser=argparse.ArgumentParser(description="Simple Calculator")
parser.add_argument("num1",type=float,help="first number")
parser.add_argument("num2",type=float,help="second number")
parser.add_argument("operation",choices=["add","mul","sub","div"] ,help="Operation to perform")

args=parser.parse_args()

if args.operation=="add":
    print(f"The addition of {args.num1} and {args.num2} is {args.num1+args.num2}")
elif args.operation=="mul":
    print(f"The multiplication of {args.num1} and {args.num2} is {args.num1*args.num2}")
elif args.operation=="sub":
    print(f"The subtraction of {args.num1} and {args.num2} is {args.num1-args.num2}")
elif args.operation=="div":
    print(f"The division of {args.num1} and {args.num2} is {args.num1/args.num2}")
else:
    print("Invalid operation!!!!!, Some Unknown error occurred")

# Dont run directly 
# python argparse_calculator.py 3 5 add
# output : => The addition  of 3.0 and 5.0 is 8.0