import requests
import webbrowser
import os
import time

os.chdir("files")
files = os.listdir()
search_url = "http://www.google.hr/searchbyimage/upload"

for each_file in files:
    multipart = {"encoded_image" : (each_file , open(each_file,"rb")),"image_content":""}
    resp = requests.post(search_url,files=multipart,allow_redirects=False)
    fetch_url = resp.headers['location']
    webbrowser.open(fetch_url)
    time.sleep(1)
