# Python program to find Cumulative sum of a list
# Input : list = [10, 20, 30, 40, 50]
# Output : [10, 30, 60, 100, 150]
# list = [10, 20, 30, 40, 50]
# list_1=[]
# a=0
# for i in range(len(list)):
#     a+=list[i]
#     list_1.append(a)
# print(list_1)



# this is the code for the finding the Nth lagest element
# def Nmaxelements(list1, N):
# 	final_list = []

# 	for _ in range(0, N):
# 		max1 = 0
# 		for j in range(len(list1)):
# 			if list1[j] > max1:
# 				max1 = list1[j]
# 		list1.remove(max1)
# 		final_list.append(max1)
		
# 	print(final_list)
# list1 = [2, 6, 41, 85, 0, 3, 71, 6, 10]
# N = 4
# Nmaxelements(list1, N)








# this should be the output
# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]
# list_2 till the one digit number we got [5, 4, 8, 7, 5]
list=[23,67,98,34,5]
new_list=[]
# n=1
# new=0
for n in list:
    new=0
    while n>0:
        new+=n%10
        n//=10
        # new=n+new
    new_list.append(new)
print(new_list)


# this one will iterate till the sum of the digit is not a single digit number 
# list = [23, 67, 98, 34, 5]
# new_list = []

# for num in list:  # Iterate over each number in the list
#     while num >= 10:  # Repeat until the number is a single digit
#         new = 0
#         while num > 0:
#             new += num % 10  # Add the last digit of the number
#             num = num // 10  # Remove the last digit from the number
#         num = new  # Update num to be the sum of its digits
#     new_list.append(num)

# print(new_list)
# import requests

# # URL to fetch
# url = "http://data.pr4e.org/intro-short.txt"

# # Send a HEAD request to fetch only the headers
# response = requests.head(url)

# # Print the relevant headers
# print("Last-Modified:", response.headers.get("Last-Modified"))
# print("ETag:", response.headers.get("ETag"))
# print("Content-Length:", response.headers.get("Content-Length"))
# print("Cache-Control:", response.headers.get("Cache-Control"))
# print("Content-Type:", response.headers.get("Content-Type"))


# import urllib.request
# from bs4 import BeautifulSoup

# # Function to find and follow links
# def follow_links(url, count, position):
#     for i in range(count):
#         print("Retrieving:", url)
#         html = urllib.request.urlopen(url).read()
#         soup = BeautifulSoup(html, 'html.parser')

#         # Find all the anchor tags
#         tags = soup('a')

#         # Get the link at the specified position (position is 1-based)
#         url = tags[position - 1].get('href', None)
        
#     print("Retrieving:", url)
#     return url

# # Main program
# start_url = "http://py4e-data.dr-chuck.net/known_by_Gus.html"
# count = 7  # Number of times to repeat
# position = 18  # Position to follow

# # Follow the links and print the final name
# final_url = follow_links(start_url, count, position)

# # Extract and print the last name from the URL
# last_name = final_url.split('_')[-1].split('.')[0]
# print("The answer to the assignment for this execution is:", last_name)



# import urllib.request
# import xml.etree.ElementTree as ET

# # Function to fetch XML data and compute the sum of <count> values
# def get_sum_from_xml(url):
#     print("Retrieving", url)
#     # Fetch the XML data from the URL
#     data = urllib.request.urlopen(url).read()
#     print("Retrieved", len(data), "characters")
    
#     # Parse the XML data
#     tree = ET.fromstring(data)
    
#     # Extract all <count> elements
#     counts = tree.findall('.//count')
    
#     # Compute the sum of the <count> values
#     total_sum = sum(int(count.text) for count in counts)
    
#     # Print the results
#     print("Count:", len(counts))
#     print("Sum:", total_sum)

# # Main Program
# url = input("Enter location: ")
# get_sum_from_xml(url)


# import urllib.request
# import json

# # Function to fetch JSON data and compute the sum of 'count' values
# def get_sum_from_json(url):
#     print("Retrieving", url)
#     # Fetch the JSON data from the URL
#     data = urllib.request.urlopen(url).read()
#     print("Retrieved", len(data), "characters")
    
#     # Parse the JSON data
#     info = json.loads(data)
    
#     # Extract all 'count' values and compute the sum
#     total_sum = sum(item['count'] for item in info['comments'])
    
#     # Print the results
#     print("Count:", len(info['comments']))
#     print("Sum:", total_sum)

# # Main Program
# url = input("Enter location: ")
# get_sum_from_json(url)


# import urllib.request, urllib.parse
# import json

# def get_plus_code(location):
#     base_url = "http://py4e-data.dr-chuck.net/opengeo?"
    
#     # URL encode the location to pass as a query parameter
#     params = {'q': location}
#     url = base_url + urllib.parse.urlencode(params)
    
#     print("Retrieving", url)
    
#     # Fetch the JSON data from the URL
#     response = urllib.request.urlopen(url)
#     data = response.read().decode()
    
#     print("Retrieved", len(data), "characters")
    
#     # Print the JSON data for debugging
#     # print(data)
    
#     # Parse the JSON data
#     try:
#         js = json.loads(data)
#     except Exception as e:
#         print("Error parsing JSON:", e)
#         return

#     # Navigate the JSON structure to find the 'plus_code' in 'features'
#     if 'features' in js and len(js['features']) > 0:
#         properties = js['features'][0].get('properties', {})
#         plus_code = properties.get('plus_code')
#         if plus_code:
#             print("Plus code:", plus_code)
#         else:
#             print("Plus code not found in the response.")
#     else:
#         print("Plus code not found in the response.")

# # Main Program
# location = input("Enter location: ")
# get_plus_code(location)



import urllib.request
from bs4 import BeautifulSoup

# Function to scrape numbers from the given URL
def scrape_numbers(url):
    # Open the URL and read the HTML
    response = urllib.request.urlopen(url)
    html = response.read()
    
    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find all <span> tags
    tags = soup.find_all('span', class_='comments')
    
    total_sum = 0
    count = 0
    
    # Loop through the tags and extract the numbers
    for tag in tags:
        number = int(tag.contents[0])  # Get the content of the <span> tag
        total_sum += number  # Add the number to the total sum
        count += 1  # Increment the count

    return count, total_sum

# Main program execution
if __name__ == "__main__":
    url = input("Enter - ")
    count, total_sum = scrape_numbers(url)
    print("Count", count)
    print("Sum", total_sum)



