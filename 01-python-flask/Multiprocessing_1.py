# this is the first code for the 

# import multiprocessing
# import requests

# def download_file(url, name):
#     response=requests.get(url)
#     open(f"image_files_multi/Image_{name}.jpg","wb").write(response.content)
#     return

# url="https://picsum.photos/200/300"

# pros=[]
# if __name__=="__main__":
#     for i in range(5):
#         # download_file(url,i)
#         p=multiprocessing.Process(target=download_file ,args=[url,i])
#         p.start()
#         pros.append(p)

# for p in pros:
#     p.join()










## second using the threadpool executor and map function
# from concurrent.futures import ThreadPoolExecutor
# import concurrent
# import concurrent.futures
# import requests

# def download_file(url, name):
#     print(f"started dowloading {name}")
#     response=requests.get(url)
#     open(f"image_files_multi/Image_{name}.jpg","wb").write(response.content)
#     print(f"Finished dowloading {name}")
#     return

# url="https://picsum.photos/200/300"

# with concurrent.futures.ProcessPoolExecutor() as executor:
#     l=[i for i in range(10)]
#     l1=[url for i in range(10)]
#     results=executor.map(download_file,l1,l)
#     for r in results:
#         print(r)


import concurrent.futures
import requests
import os

# Create the directory if it doesn't exist
if not os.path.exists("image_files_multi"):
    os.makedirs("image_files_multi")

def download_file(url, name):
    print(f"Started downloading {name}")
    response = requests.get(url)
    open(f"image_files_multi/Image_{name}.jpg", "wb").write(response.content)
    print(f"Finished downloading {name}")
    return

url = "https://picsum.photos/200/300"

# Use ThreadPoolExecutor for I/O-bound tasks
with concurrent.futures.ThreadPoolExecutor() as executor:
    l = [i for i in range(10)]
    l1 = [url for _ in range(10)]
    results = executor.map(download_file, l1, l)

# Output the completion status
for r in results:
    print(r)



