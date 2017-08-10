from urllib import request

# downloading files from the web using the url
print('Input the file url o download..')
print('--------------------------------')

file_url = input()


def download_file(url_file):
    res = request.urlopen(url_file)
    file = res.read()               # read the data
    file_txt = str(file)            # convert the data to string
    lines = file_txt.split('\n')
    location = r'file.txt'          # give the save file a name

    # read and write to file
    fx = open(location, 'w')

    # a loop to write to the file line by line
    for line in lines:
        fx.write(line + '\n')

    fx.close()

print('Downloading file.....')

# call the function to download file
download_file(file_url)

print('Download complete')
