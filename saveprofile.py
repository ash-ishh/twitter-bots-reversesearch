import requests
import re

f = open("handles.txt")
handles = [line.strip() for line in f.readlines()]
f.close()
baseurl = "http://www.twitter.com/"
save_f = open("profilelinks.txt","w")


for handle in handles:
    url = baseurl + handle
    r = requests.get(url)
    text = r.text
    try:
        url_re = re.compile(r"https://pbs.twimg.com/profile_images/.*?jpg") #eg : https://pbs.twimg.com/profile_images/935474725270167552/eMMqO_PZ_400x400.jpg
        profile_url = url_re.findall(text)[0]
        save_f.write(profile_url)
        save_f.write("\n")
    except:
        pass
    print(profile_url)
save_f.close()

