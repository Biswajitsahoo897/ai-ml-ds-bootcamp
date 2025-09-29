# def double(x):
#     return x*2
# d=double(3)
# print(d)


# # this the use of lambda funtion 
# def appl(funx, value):
#     return 8+ funx(value)
# double=lambda c: c*4
# cube=lambda c:c*c*c
# avg_of_multi=lambda c,b,d:(c+b+d)/3 
# print(double(4))
# print(cube(4))
# print(avg_of_multi(4,5,6))
# # this means value=3 but funx is same AS  double here so  funx(3) which is 12 and 12+8 =20 (Ans)
# print(appl( double, 3))
# print(appl( lambda c:c*c , 3))


# numbers=[1,2,3,4,5]
# for num in numbers:
#     if(num%2==0):
#         print(num)

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Get only the even numbers using the filter function
evens = filter(lambda x: x % 2 == 0, numbers)

# Print the even numbers
print(list(evens))



