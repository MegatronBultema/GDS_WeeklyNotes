from pymongo import MongoClient
from pprint import pprint
import spacy
from spacy.en import English
#from nltk.corpus import stopwords
import nltk
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
parser = English()
import sys
from string import punctuation
import re
from string import printable
import csv, re, sys, spacy
import numpy as np


def load_data():
    client = MongoClient()
    db = client.nyt_dump
    coll = db.articles
    return coll


def clean_data(coll):
    listdoc = []
    for document in coll.find().limit(2):
        a = document['content']
        text = ' '.join(a)
        text = text.replace('â', '')
        text = text.replace('Ã´', '')
        text = text.replace('Ã¢', '')
        text = text.replace('Ã©', '')
        text = text.replace('Ã§', '')
        text = text.replace("\n", " ").replace("\r", " ")
        parsed_text = parser(text)
        #text2 = ''.join([i if ord(i) < 128 else ' ' for i in text])
        listdoc.append(parsed_text)
    return listdoc

def lematize_string(doc, stop_words):
    if sys.version_info.major == 3:
        PUNCT_DICT = {ord(punc): None for punc in punctuation}
        doc = doc.translate(PUNCT_DICT)
    else:
        doc = unicode(doc.translate(None,punctuation))

    clean_doc = ""
    for char in doc:
        if char in printable:
            clean_doc += char
    return clean_doc
