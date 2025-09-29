marks=[23,78,67,98,89,1,4,90]
index=0
for mark in marks:
    print(mark)
    if index==3:
        print(f"you are amazing , because u got {marks[index]}")
        # perfect use of f-string in thr enumerate funtion
    index+=1    



# Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango']
for index , value in enumerate( fruits, start=1):
    print(index, value)

    # for index, fruit in enumerate(fruits, start=1):
    # print(index, fruit)

    stre="hello world!!! this is python."
    for index , var in enumerate(stre, start=1):
        # if i want i can change start to 0 also 
        if var==" ":
            continue
        # skips the current iteration but break terminates the entire program
        print(index,':', var)