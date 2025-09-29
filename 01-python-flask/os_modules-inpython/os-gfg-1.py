try:
    import os
    directory = "makenewdir"
    parent_dir = "D:/newpython"
    path = os.path.join(parent_dir, directory)

    os.mkdir(path)
    print(f"Directory {directory} created")

except FileExistsError:
    print("file already exists")    
# directory = "Geeks"
# parent_dir = "D:/newpython"
# mode = 0o666
# path = os.path.join(parent_dir, directory)
# os.mkdir(path, mode)
# print("Directory '% s' created" % directory)
