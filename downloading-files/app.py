from urllib import request

# downloading files from the web using the url
print('Input the file url o download..')
print('--------------------------------')

file_url = input()


def download_file(file_url):
    res = request.urlopen(file_url)
    file = res.read()       # read the data
    file_txt = str(file)    # convert the data to string
    lines = file_txt.split('\n')
