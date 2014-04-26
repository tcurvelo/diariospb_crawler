from scrapy.item import Item, Field


class DiariosItem(Item):
    title = Field()
    url = Field()
    files = Field()
