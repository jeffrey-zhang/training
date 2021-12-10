import asyncio


async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))


async def main(urls):
    task = [asyncio.create_task(crawl_page(url)) for url in urls]
    await asyncio.gather(*task)


asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
