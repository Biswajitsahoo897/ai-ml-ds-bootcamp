import os

# Create the main folder if it does not exist
if not os.path.exists("/01-python-flask/os_modules-inpython"):
    os.mkdir("01-python-flask/os_modules-inpython/Data_folder")

# Create 10 subdirectories inside the "data_folder" and remember we have to give that data_folder/day 
for i in range(10):
    os.mkdir(f"01-python-flask/os_modules-inpython/Data_folder/day_{i+1}")
