
import time

def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    time.sleep(sleep_time)
    print('OK {}'.format(url))

def main(urls):
    for url in urls:
        crawl_page(url)

main(['url_1', 'url_2', 'url_3', 'url_4'])

import asyncio_demo

async def crawl_page_async(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))

async def main_async(urls):
    for url in urls:
        await crawl_page_async(url)

asyncio.run(main_async(['url_1', 'url_2', 'url_3', 'url_4']))
