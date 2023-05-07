# -*- coding: utf-8 -*-
CONJURED = "Conjured Mana Cake"
BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
SLFURAS = "Sulfuras, Hand of Ragnaros"
AGED_BRIE = "Aged Brie"


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.UPDATE_ITEM_QUALITY(item)

    def UPDATE_ITEM_QUALITY(self, item):
        degrate = item.name != AGED_BRIE and item.name != BACKSTAGE and item.name != SLFURAS
        if degrate:
            self.ADJUST_QUALITY(-1, item)
        else:
            self.ADJUST_QUALITY(1, item)
            if item.name == BACKSTAGE:
                if item.sell_in < 11:
                    self.ADJUST_QUALITY(1, item)
                if item.sell_in < 6:
                    self.ADJUST_QUALITY(1, item)
        if item.name != SLFURAS:
            item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            self.HANDLE_EXPIRED(item)

    def HANDLE_EXPIRED(self, item):
        if item.name != AGED_BRIE:
            if item.name != BACKSTAGE:
                if item.name != SLFURAS:
                    self.ADJUST_QUALITY(-1, item)
            else:
                item.quality = item.quality - item.quality
        else:
            self.ADJUST_QUALITY(1, item)

    def ADJUST_QUALITY(self, adjustment, item):
        new_quality = item.quality + adjustment
        inRange = new_quality <= 50 and new_quality >= 0
        if inRange:
            item.quality = item.quality + adjustment


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
