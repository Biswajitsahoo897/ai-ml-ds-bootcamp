# user_input=int(input("Enter the nth number :"))
# def fibo(x):
#     if x==1:
#         return 0
#     elif x==2:
#         return 1
#     else:
#         return fibo(x-1)+fibo(x-2)
    

# print(fibo(user_input))


# f0=0
# f1=1
# # def fibo(x):
# n=int(input("Enter how terms you want to print:"))
# print(f0,f1,end=" ")
# for _ in range(2,n):
#     f_next=f0+f1
#     print(f_next,end=" ")
#     f0=f1
#     f1=f_next

        
# writing a program for the prime number or not , or to print the numbers defined range by the user:
# list_prime=[]
# for i in range(2,100):
#     flag=True
#     for j in range(2,int(i/2)+1):
#         if i%j==0:
#             flag=False
#             break
#     if flag:
#         list_prime.append(i)
    
# print(list_prime)
# print(len(list_prime))

# this is the program to print the ASCII value of character
# a=input("Enter here:")
# b=ord(a)
# print(b)


# this is the code for the append the first two terms to last two
# arr = [12, 40, 3, 6, 11, 90]
# a = len(arr)
# print(a)
# for i in range(2):  # Loop twice to remove the first two elements
#     first_element = arr[0]  # Get the first element
#     arr.remove(first_element)  # Remove it from the list
#     arr.append(first_element)  # Append it to the end of the list

# print(arr)

# this is the code for the second largest element in the list
list_1=[89,10,26,39,4,100,74,22,51]
largest=-100000
for i in range(len(list_1)):
    if largest < list_1[i]:
        largest=list_1[i]

    else:
        continue 
print(f"The first largest number is :{largest}")
largest_1=-100000
list_1.remove(largest)
for i in range(len(list_1)):
    if largest_1 < list_1[i]:
        largest_1=list_1[i]

# print(list_1)#remove the largest element because of the convient for the user
print(f"The second largest number is :{largest_1}")
