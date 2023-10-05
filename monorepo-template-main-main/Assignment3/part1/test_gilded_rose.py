# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_standard_item_before_sell_by_date(self):
        items = [Item("item", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(9, items[0].quality)

    def test_standard_item_passed_sell_by_date(self):
        items = [Item("item", -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_aged_brie(self):
        items = [Item("Aged Brie", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(11, items[0].quality)

    def test_backstage_passes_normal(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(11, items[0].quality)

    def test_backstage_passes_less_than_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 9, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].sell_in)
        self.assertEqual(12, items[0].quality)

    def test_backstage_passes_less_than_5_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].sell_in)
        self.assertEqual(13, items[0].quality)

    def test_backstage_passes_after_the_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_conjured_item_before_sell_by_date(self):
        items = [Item("Conjured", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_conjured_item_after_sell__by_date(self):
        items = [Item("Conjured", -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(6, items[0].quality)


if __name__ == '__main__':
    unittest.main()
