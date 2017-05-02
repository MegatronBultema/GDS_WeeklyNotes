from pymongo import MongoClient
from bs4 import BeautifulSoup
import urllib

client = MongoClient()
# Access/Initiate Database
db = client['test_database']
# Access/Initiate Table
tab = db['test_table']
#db.tab.insert({'_id':1})
db.tab.insert({ 'item': "canvas", 'qty': 100, 'tags': ["cotton"]})
db.tab.update({'tags': ["cotton"]}, {'tags': ["fabric"]})

from pprint import pprint

cursor = db.tab.find({})
for document in cursor:
    pprint(document)

#$('.sresult.lvresult.clearfix.li')

soup = BeautifulSoup(open('/Users/DataScience/Documents/GDS_WeeklyNotes/week5/MongoFolder/web-scraping/data/ebay_shoes.html'))
#test = soup.find_all(class_='sresult lvresult clearfix li')
test = soup.find_all(class_="lvpic pic img left")

images = []
for i in soup.find_all(class_="lvpic pic img left"):
    images.append(i.img['src'])

for num, i in enumerate(images):
    a = i.strip('./')
    obj = urllib.urlopen('{0}{1}'.format('file:///Users/DataScience/Documents/GDS_WeeklyNotes/week5/MongoFolder/web-scraping/data/',a))

    #touch 'data/{0}'.format(a)
    filename =  open('/Users/DataScience/Documents/GDS_WeeklyNotes/week5/MongoFolder/web-scraping/test/{}'.format(a), 'wb')
    filename.write(obj.read())
