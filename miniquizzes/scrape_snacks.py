import requests
import bs4
import json
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, CollectionInvalid
import datetime as dt
from bs4 import BeautifulSoup

base_url = 'http://www.snackdata.com'
#<a href = "/corn_dog"

# Define the MongoDB database and table
db_cilent = MongoClient()
db = db_cilent['snack']
table = db['meta_snack']

#link = 'https://www.facebook.com/rsrc.php/v3ibIg4/yb/l/en_US/nQadBcJ-IAL.js'
# Query the NYT API once
def single_query(link):
    response = requests.get(link)
    if response.status_code != 200:
        print 'WARNING', response.status_code
    else:
        return response

def get_items(list_items):
    links =[]
    for li in list_items:
        links.append(li.a['href'])
    return links

def loop(link):
    for item in link:
        url_snack = base_url + item
        req_snack = requests.get(url_snack)
        soup_snack = BeautifulSoup(req_snack.text, 'html.parser')
        name_number = soup_snack.select('h4')[0].text.encode("ascii", "ignore")
        snack_number = name_number.split()[0]
        snack_name = ' '.join(name_number.split()[1:])
        #print(snack_number, snack_name)
        tab = soup_snack.find_all('div',attrs = {"class": "data clearfix"})
        tab_dd = tab[0].find_all('dd')
        flavor = tab_dd[0].text.strip().split(',u')
        cusine = tab_dd[1].text.strip()
        series = tab_dd[2].text.strip().split(',')
        print(snack_number, snack_name)
        print(flavor, cusine)



if __name__ == '__main__':
    response = single_query(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    list_items = soup.select("ol li")
    links = get_items(list_items)
    loop(links[:3])
    # in terminal start mongo damin then in a new terminal run mongo then start it up and create db and table
    #show dbs
    #use name_database
    #db.createCollection(collection)
    #db.collection.function()
