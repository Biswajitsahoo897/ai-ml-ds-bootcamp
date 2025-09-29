import os


if not os.path.exists("data_folder"):
    os.mkdir("data_folder")


for i in range(100):
    os.rename(f"data_folder/day {i+1}", f"data_folder/Tutorial {i+1}")
# os.rename(source , destination )


