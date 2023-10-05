class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

# Design pattern: Strategy Pattern
class ItemUpdater:
    def __init__(self, item):
        self.item = item

    def update_quality(self):
        pass

class StandardItemUpdater(ItemUpdater):
    def update_quality(self):
        decrement = 1
        if 'conjured' in self.item.name.lower():
            decrement *= 2
        if self.item.sell_in <= 0:
            decrement *= 2
        self.item.quality = max(0, self.item.quality - decrement)
        self.item.sell_in -= 1

class AgedBrieItemUpdater(ItemUpdater):
    def update_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1
        self.item.sell_in -= 1

class BackstageUpdater(ItemUpdater):
    def update_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1
            if self.item.sell_in < 11 and self.item.quality < 50:
                self.item.quality = min(self.item.quality + 1, 50) 
            if self.item.sell_in < 6 and self.item.quality < 50:
                self.item.quality = min(self.item.quality + 1, 50) 
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.item.quality = 0

class GildedRose(object):
    def __init__(self, items):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater = self.get_item_updater(item)
            updater.update_quality()

    def get_item_updater(self, item):
        if item.name == "Aged Brie":
            return AgedBrieItemUpdater(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstageUpdater(item)
        else:
            return StandardItemUpdater(item)
