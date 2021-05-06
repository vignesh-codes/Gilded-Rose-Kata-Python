# -*- coding: utf-8 -*-
import unittest

from new import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_Aged_Brie(self):
        items = [Item("Aged Brie", 5, 40)]
        new = GildedRose(items)
        new.update_quality()
        # self.assertEquals("foo", items[0].name)
        # self.assertEquals(int(-1), items[0].sell_in)
        self.assertEquals(int(41), items[0].quality)

    def test_normal_p(self):
        items = [Item("normalp", 5, 10)]
        new = GildedRose(items)
        new.update_quality()
        self.assertEquals(int(9), items[0].quality)

    def test_normal_n(self):
        items = [Item("normaln", -5, 10)]
        new = GildedRose(items)
        new.update_quality()        
        self.assertEquals(int(8), items[0].quality)

    def test_conjured(self):
        items = [Item("Conjured Mana Cake", 5, 10)]
        new = GildedRose(items)
        new.update_quality()       
        self.assertEquals(int(8), items[0].quality)

    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        new = GildedRose(items)
        new.update_quality()       
        self.assertEquals(int(80), items[0].quality)

    def test_backstage1(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 10)]
        new = GildedRose(items)
        new.update_quality()       
        self.assertEquals(int(11), items[0].quality)

    def test_boundary(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        new = GildedRose(items)
        new.update_quality()      
        self.assertEquals(int(50), items[0].quality)

    def test_backstage2(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 9, 10)]
        new = GildedRose(items)
        new.update_quality()        
        self.assertEquals(int(12), items[0].quality)

    def test_backstage3(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)]
        new = GildedRose(items)
        new.update_quality()        
        self.assertEquals(int(13), items[0].quality)
    
    

if __name__ == '__main__':
    unittest.main()
