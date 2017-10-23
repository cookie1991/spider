import os
import requests
from bs4 import BeautifulSoup


class Spider:

    def __init__(self):
        self.servername = 'http://www.biqukan.com'
        self.target = 'http://www.biqukan.com/1_1094/'
        self.titles = []
        self.urls = []
        self.comments = []
        self.nums = 0

    def get_urls(self):
        req = requests.get(url=self.target)
        html = req.text
        bf = BeautifulSoup(html, 'html.parser')
        div = bf.find_all('div', class_='listmain')
        bf_div = BeautifulSoup(str(div), 'html.parser')
        urls = bf_div.find_all('a')
        self.nums = len(urls[15:])
        for url in urls[15:]:
            self.titles.append(url.string)
            self.urls.append(self.servername + url.get('href'))

    def get_comment(self, urls):
        for url in urls:
            req = requests.get(url=url)
            html = req.text
            bf = BeautifulSoup(html, 'html.parser')
            comments = bf.find_all('div', class_='showtxt')
            for comment in comments:
                self.comments.append(comment.text.replace('\xa0'*8, '\n'))


if __name__ == '__main__':
    spider = Spider()
    spider.get_urls()
    spider.get_comment(spider.urls)

    f = open('d:/Users/liujuna/Desktop/test.txt', 'wb')
    num = 0
    for comment in spider.comments:
        f.write(spider.titles[num].encode('UTF-8'))
        f.write('\n'.encode('UTF-8'))
        f.write(str(comment).encode('UTF-8'))
        num += 1
    f.close()
