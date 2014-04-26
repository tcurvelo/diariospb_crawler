from diarios.items import DiariosItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.spiders import Rule
from scrapy.http import Request
from scrapy.selector import Selector


class DiarioPbSpider(CrawlSpider):
    name = 'diario-pb'
    allowed_domains = ['paraiba.pb.gov.br']
    start_urls = ['http://www.paraiba.pb.gov.br/diario-oficial']

    rules = (
        Rule(
            SgmlLinkExtractor(restrict_xpaths='//*[@id="busca_result"]/*/h3'),
            callback='parse_item'
        ),
    )

    def parse_item(self, response):
        sel = Selector(response)
        links = sel.xpath('//*[@id="conteudo-interna"]/*/a')

        for link in links:
            url = link.xpath('@href').extract()[0]
            if url.endswith(".pdf"):
                yield DiariosItem(
                    title=link.xpath('text()').extract(),
                    url=url
                )
            else:
                yield Request(url, callback=self.parse_item)
