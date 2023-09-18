import scrapy 
from number_parser import parse_number
import re



class BookSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['https://books.toscrape.com/catalogue/category/books_1/page-4.html']
    processed_pages = 0


    @staticmethod
    def to_int(x):
        try:
            match = re.search(r'(?:star-rating)(.*)', x)
            if match:
                x = match.group(1).strip()
            return parse_number(x)
        except:
            return 0
        

    def parse(self, response):
        """
        @url https://books.toscrape.com/catalogue/category/books_1/page-4.html
        @valid title price rating img
        """
        for book in response.xpath("//article[@class='product_pod']"):
            yield dict(
                title=book.xpath('.//a[@title]/@title').get(),
                price=book.xpath(".//p[@class='price_color']/text()").get(),
                rating=self.to_int(book.xpath(".//p[contains(@class, 'star-rating')]/@class").get()),
                img=book.xpath("./div/a/@href").get()
            )
            print('-------------------')

        if self.processed_pages < 5:
            self.processed_pages += 1
            next_page = response.css('li.next a::attr(href)').get()
            if next_page:
                yield response.follow(next_page, callback=self.parse)


