import urllib.request
import random

def download_image(url):
    img_name=random.randrange(100,500)
    full_name = str(img_name)+'.jpg'
    urllib.request.urlretrieve(url,full_name)
    
    download_image('https://www.worldatlas.com/r/w728-h425-c728x425/upload/09/04/49/untitled-design-374.jpg')