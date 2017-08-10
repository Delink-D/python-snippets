import random
import urllib.request


# function that allow a for a single parameter
def download(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpg'  # full name of the image
    urllib.request.urlretrieve(url, full_name)  # request using the urllib module

# allow user to input the url to download from
print("Input the url of image you want to download...")
print("----------------------------------------------")

userInput = input()  # save input to a variable

# call the function and pass in the users input
download(userInput)
