from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.Mtg

def insert_card(card):
    db.cards.insert(card)
    