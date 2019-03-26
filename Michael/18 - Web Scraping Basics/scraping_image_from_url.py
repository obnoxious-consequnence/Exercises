import bs4
import os
import sys
import requests
import urllib.request as req

if __name__ == '__main__':

    def collect_img_links(url):
        r = requests.get(url)
        r.raise_for_status()
        soup = bs4.BeautifulSoup(r.text, 'html5lib')
        
        return [img.get('src') for img in soup.select('img') 
                if img.get('src').startswith('http')]


    def download_imgs(links, out_folder="./images/"):
        count = 0
        for l in links:
            count += 1
            req.urlretrieve(l, out_folder + str(count) + '.PNG' )
            
            
    links = collect_img_links('https://www.google.dk/search?site=&tbm=isch&source=hp&biw=1163&bih=812&q=minions&oq=minions')
    download_imgs(links)