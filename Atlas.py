from bs4 import *
import requests as rq

def intro():
  print("############################    by semiromest      ##########################" + "\n" +
        "############################    Lib3rty0rD3ath     ##########################" + "\n" +
        "############################        ATLAS          ##########################")
intro()
url = input("Lütfen tarama yapmak istediğiniz websitesinin adresini başında https bulunarak yazınız : ")

requests = rq.get(url)
soup_vericek = BeautifulSoup(requests.text,"html.parser")
images = soup_vericek.find_all('img')
images_link= []

for image in images:
  resim = image['src']
  images_link.append(resim)

def svg_sil():
  svg_sil_list=[]
  for i in images_link:
    if i.startswith("http"):
      svg_sil_list.append(i)
  return svg_sil_list

images_link=set(svg_sil())

def size():
    for i in images_link:
      img_size = rq.get(i).content
      if (len(img_size) / 1024) > 100:
          print(i + " Bu resim dosyası optimize edilmeli")
size()

