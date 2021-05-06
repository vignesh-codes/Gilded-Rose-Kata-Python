'''
Four Special Items - Aged Brie, Sulfurus, Backstage and Conjured and Normal Items

1. Quality Deecreses by 1. Data passed -> decreses by 2 (DONE)
2. Quality can never be negative (DONE)
3. Quality can never by more than 50 for normal items (DONE)
4. If Aged Brie -> quality increases by 1 (DONE)
5. If Sulfuras -> quality is same (DONE)
6. If Backstage -> quality increases by 1. 10 or less -> increase by 2. 5 or less -> increase by 3
Backstage -> 0 after day=0 (DONE)
7. Conjured Mana Cake -> drops by 2 and drops by 4 when sell_in<0 (DONE)
'''
'''
ASSUMPTIONS:
1. The string is default the same. And if needed to trim the first few letters to look for special items, it can be done using regex. 
2. The quality and sell_in day behaviour is constant. If they are need to be maintained in a way that it can be changed easily next time, we can maintain them in config.yaml file. Having three fields: 
    sell_in_decrement: 1
    quality_increment: 1
    quality_decrement: 1

'''

'''
Explanation:
We maintain conditions for special items. 

- Backstage Passes Similar to Aged Brie quality change. So we use same if condition to deduct quality by 1
first and then if it is found to be backstage.. then deduct the quality again based on sell_in and quality boundaries as defined

- We maintain a seperate if condition for Sulfuras and Conjured special items

- If the item name is not found to be special then proceed with normal quality detuction based on defined sell_in

'''

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            #If the current item is Aged Brie or Backstage passes to a TAFKAL80ETC concert
            if item.name == "Aged Brie" or item.name == "Backstage passes to a TAFKAL80ETC concert":
                #Execute the following only if the item's Quality is withint the defined bounday 0 to 50
                if 0<=item.quality<50:
                    #increment for all item
                    item.quality += 1
                    #if it is Backstage passes to a TAFKAL80ETC concert, increment again
                    if item.name == "Backstage passes to a TAFKAL80ETC concert" and 6<=item.sell_in<=10 and 0<=item.quality<50:
                        item.quality +=1
                    elif item.name == "Backstage passes to a TAFKAL80ETC concert" and item.sell_in<=5 and 0<=item.quality<50:
                        item.quality +=2
                else:
                    pass
                #If the sell_in is <=0, make the quality as 0
                if item.name == "Backstage passes to a TAFKAL80ETC concert" and item.sell_in<=0:
                        # Handling a minor bug
                        item.quality = -1
            
            #Handle the Sulfuras, Hand of Ragnaros item
            elif item.name == "Sulfuras, Hand of Ragnaros":
                item.sell_in += 1
            
            #Handle the Conjured Mana Cake only if the quality is within the defined boundary
            elif item.name == "Conjured Mana Cake" and 0<item.quality<50:
                item.quality -= 2
                #if the sell_in is less than 0, increment again 
                if item.sell_in <=0:
                    item.quality -= 2
            
            #Handle the Normal Items Cake
            else:
                #Handle only if the quality is within the boundary
                if 0<=item.quality<50:
                    item.quality -= 1
                    #if the sell_in is less than 0, increment again 
                    if item.sell_in <=0:
                        item.quality -= 1
            #To cover the edge case of quality decrememented from 0 to -1
            if item.quality<=0:
                item.quality = 0

            #Decrement the sell_in for this iteration irrespective of what item it is
            item.sell_in -= 1
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
