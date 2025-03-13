import scrapy


class BooksItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    _id = scrapy.Field()

