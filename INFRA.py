from flask import Flask
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['DataCollectionXYZ']
app = Flask(__name__)
