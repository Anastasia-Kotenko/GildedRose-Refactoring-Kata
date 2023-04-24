class GildedRose {
    public static final String AGED_BRIE = "Aged Brie";
    public static final String BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert";
    public static final String SULFURAS = "Sulfuras, Hand of Ragnaros";

    Item[] items;

    public GildedRose(Item[] items) {
        this.items = items;
    }

    public void updateQuality() {
        for (Item item: items) {
            updateItemQuality(item);
        }
    }

    private static void updateItemQuality(Item item) {
        if (!item.name.equals(AGED_BRIE) && !item.name.equals(BACKSTAGE_PASSES)) {
            if (!item.name.equals(SULFURAS)) {
                adjustQuality(item, -1);
            }
        } else {
            adjustQuality(item, 1);

            if (item.name.equals(BACKSTAGE_PASSES) && item.sellIn < 11 && item.sellIn < 6) {
                    adjustQuality(item, 1);
            }
        }

        if (!item.name.equals(SULFURAS)) {
            item.sellIn = item.sellIn - 1;
        }

        if (item.sellIn < 0) {
            handleExpired(item);
        }
    }

    private static void handleExpired(Item item) {
        if (!item.name.equals(AGED_BRIE)) {
            if (!item.name.equals(BACKSTAGE_PASSES) && !item.name.equals(SULFURAS)) {
                adjustQuality(item, -1);
            } else {
                item.quality = item.quality - item.quality;
            }
        } else {
            adjustQuality(item, 1);

        }
    }

    private static void adjustQuality(Item item, int adjustment) {
        int newQuality = item.quality + adjustment;
        boolean itsRange = newQuality <= 50 && newQuality >= 0;
        if (itsRange) {
            item.quality = newQuality;
        }
    }

    public Item[] getItems() {
        return items;
    }
}