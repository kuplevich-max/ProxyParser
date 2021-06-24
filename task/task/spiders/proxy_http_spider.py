import scrapy
from scrapy_splash import SplashRequest

class ProxyHttpSpider(scrapy.Spider):
    name = 'proxyhttp'
    allowed_domains = ['proxyhttp.net']
    start_urls = ['https://proxyhttp.net/free-list/anonymous-server-hide-ip-address#proxylist']
    custom_settings = {'FEED_URI': "proxy_http.json",
                       'FEED_FORMAT': 'json'}

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url)

    def parse(self, response, **kwargs):
        ip = response.css('table.proxytbl tr td.t_ip::text').getall()
        ports = [item.split('\n')[0] for item in response.css('table.proxytbl tr td.t_port::text').getall() if item[0] != '\n']
        rows = [(ip[i], ports[i]) for i in range(len(ip))]
        for row in rows:
            scraped_info = {
            'ip' : row[0],
            'port': row[1]
            }
            yield scraped_info
