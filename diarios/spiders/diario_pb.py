from datetime import date
from dateutil.relativedelta import relativedelta
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

    def __init__(self, *args, **kwargs):
        super(DiarioPbSpider, self).__init__(*args, **kwargs)

        if all(
            True if param in kwargs else False
            for param in ['start_year', 'start_month', 'end_year', 'end_month']
        ):
            current = date(
                int(kwargs['start_year']),
                int(kwargs['start_month']),
                1
            )
            end = date(
                int(kwargs['end_year']),
                int(kwargs['end_month']),
                1
            )
            month = relativedelta(months=1)

            self.start_urls = []
            while current <= end:
                for base_url in DiarioPbSpider.start_urls:
                    self.start_urls.append(
                        '%s?mes=%d&ano=%d' % (
                            base_url, current.month, current.year
                        )
                    )
                current += month

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
