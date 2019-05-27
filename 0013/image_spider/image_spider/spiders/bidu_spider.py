import scrapy
import urllib

cnt = 0

class BiduSpider(scrapy.Spider):
    name = 'biduspider'

    def start_requests(self):
        urls = [
            'http://tieba.baidu.com/f?kw=%E6%9D%89%E6%9C%AC%E6%9C%89%E7%BE%8E'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.get_pages)

    def get_pages(self, response):
        l = response.xpath('//*[@id="frs_list_pager"]/a')
        for i, item in enumerate(l):
            if i < 2:
                continue
            if i > 9:
                break
            x = 'http:'+item.xpath('@href').get()
            yield scrapy.Request(url=x, callback=self.parse)

    def parse(self, response):
        # //*[@id="thread_list"]/li[1]/div/div[2]/div[1]/div[1]
        base_url = 'http://tieba.baidu.com'
        l = response.xpath('//*[@id="thread_list"]/li')
        for item in l:
            x = item.xpath('./div/div[2]/div[1]/div[1]/a/@href').get()
            url = base_url + x
            yield scrapy.Request(url=url, callback=self.parse2)

    @staticmethod
    def filter_fun(x):
        if x.endswith('jpg') or x.endswith('png') or x.endswith('jpeg'):
            if 'static' not in x:
                return True
        return False

    def parse2(self, response):
        l = response.xpath('//*[@id="j_p_postlist"]/div')
        for item in l:
            r = item.xpath('.//img/@src').getall()
            r = list(filter(self.filter_fun, r))
            print(r)
            for x in r:
                global cnt
                save_path = './tmp/{}.jpg'.format(cnt)
                urllib.request.urlretrieve(x, save_path)
                cnt += 1


