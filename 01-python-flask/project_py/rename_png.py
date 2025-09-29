import os
files=os.listdir("E:/TRIP_TO_DARJEELING")
i=1
for file in files:
    # if file.endswith(".jpg"):
    #     print(file)
    #     os.rename(f"E:/TRIP_TO_DARJEELING/{file}",f"E:/TRIP_TO_DARJEELING/ImagE_{i}.jpg")
    #     i=i+1
    if file.endswith(".MP4"):
        print(file)
        os.rename(f"E:/TRIP_TO_DARJEELING/{file}",f"E:/TRIP_TO_DARJEELING/Video_{i}.MP4")
        i=i+1
        print(file)
    # else:
    #     print("This is the else part of the file")
    #     print(file)
        

