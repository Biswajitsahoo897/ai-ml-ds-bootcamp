import os

# Create the main folder if it does not exist
if not os.path.exists("data_folder"):
    os.mkdir("data_folder")

# Create 100 subdirectories inside the "data_folder" and remember we have to give that data_folder/day 
for i in range(100):
    os.mkdir(f"data_folder/day {i+1}")
