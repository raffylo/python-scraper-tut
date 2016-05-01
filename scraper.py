from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv

base_url = ("http://ph.phonebooky.com/blog/20-restaurants-won-2015/")

soup = BeautifulSoup(urlopen(base_url).read(), "lxml")

f = csv.writer(open("phonebooky.csv", "w"))
f.writerow(["address"])

blockquote = soup.findAll("blockquote")
  
for block in blockquote:
    address = block.contents[0]

    f.writerow([address])

    #output.writerow([address])

#print "Done writing file"
