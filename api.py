from mtgsdk import Card
from mtgsdk import Set
from pprint import pprint
from db_provider import insert_card
import json

from json import JSONEncoder
class MyEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__

def get_cards():

    try:
        cards = Card.where(supertypes='legendary').where(subtypes='vampire').all()
        #return cards

        res = []
        index = 0
        insert_card({"name":"test"})
        for card in cards:

            js = MyEncoder().encode(card)

            index+=1
            colors = ', '.join(card.colors)
            types = ', '.join(card.types)
            subtypes = ', '.join(card.subtypes)
            
            res.append("%3d. Name: %-30s csc: %2d =>%15s colors: %-20s [p/t]: %2s/%-2s rarity: %13s types: %10s subTypes: %20s" 
                % (index, card.name, card.cmc, card.mana_cost, colors, card.power, card.toughness, card.rarity, types, subtypes))

        return res

    except Exception as ex:
        print('Exception occured {0}'.format(ex))

if __name__ == '__main__':
    pprint(get_cards())
