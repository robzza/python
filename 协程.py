import requests
from lxml import etree
import time
import pandas
import aiohttp
import asyncio
all_list=[]
star=time.time()
async def download(i):
    print(f'正在爬取： {i}页')
    url = f'http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml'
    async with aiohttp.ClientSession() as session:
        async  with session.get(url) as resp:
            tree = etree.HTML(await resp.text())
            tree = tree.xpath('/html/body/div[2]/div[4]/div[1]/table/tr')[1:]
            print(f'爬取成功： {i}页')
            for j in tree:
                content = j.xpath('./td//text()')
                all_list.append(content)

async def main():
    task=[asyncio.create_task(download(i)) for i in range(1,1001)]
    await asyncio.wait(task)
if __name__ == '__main__':
    asyncio.run(main())
    print('爬取时间：',time.time()-star,'秒')
    df = pandas.DataFrame(all_list,columns=['品名','最低价','品均价','最高价','规格','单位','发布日期'])
    df.to_csv('./xindadi.csv',index=False,encoding='utf-8_sig')
