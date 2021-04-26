import requests
from lxml import etree
import time
import pandas
from concurrent.futures import ThreadPoolExecutor
all_list=[]
star=time.time()
def download(i):
    print(f'正在爬取： {i}页')
    url=f'http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml'
    resp = requests.get(url).text
    tree = etree.HTML(resp)
    tree = tree.xpath('/html/body/div[2]/div[4]/div[1]/table/tr')[1:]
    print(f'爬取成功： {i}页')
    for j in tree:
        content=j.xpath('./td//text()')
        all_list.append(content)


def main():
    with ThreadPoolExecutor(50) as t:
        for i in range(1,1001):
            t.submit(download,i)
if __name__ == '__main__':
    main()
    print('爬取时间：',time.time()-star,'秒')
    df = pandas.DataFrame(all_list,columns=['品名','最低价','品均价','最高价','规格','单位','发布日期'])
    df.to_csv('./xindadi.csv',index=False,encoding='utf-8_sig')
