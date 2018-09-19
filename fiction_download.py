import requests
from bs4 import BeautifulSoup
import os
from threading import Thread
import re


def get_soup(url):
    # 用来响应请求，并返回soup对象
    headers = { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
    response = requests.get(url,headers=headers)
    response.encoding='utf=8'
    response = response.text
    soup = BeautifulSoup(response, 'lxml')
    return  soup

def get_fiction(fic_name):
    # 获取搜索的小数的目录url
    url = "https://xiaoshuo.sogou.com/0_0_0_0_heat/?keyword={}".format(fic_name)
    soup = get_soup(url)
    html = soup.find('li',class_="fl clear")
    url = html.find('a',class_="btn btn-toc")
    url = url['href']
    return url,fic_name

def get_fiction_body(url):
    soup = get_soup(url)
    div = soup.find('div',id="contentWp")
    body = div.find_all('p')
    fiction = ''
    for i in body:
        fic = i.string
        if fic:
            fiction += '  ' + fic +  '\n'
    return fiction


def save_fiction(name,fiction,fic_name):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    name = re.sub(rstr, "_", name)  # 替换为下划线
    path = "E:\\fiction\\" + fic_name
    if not os.path.exists(path):
        os.mkdir(path)
    file_name = path + '\\' + name + '.txt'
    with open(file_name,'w',encoding='utf-8') as f:
        f.write(fiction)
        print(file_name,'下载完成')


def main(fic_name):
    url_list,fic_name = get_fiction(fic_name)
    base_url = 'https://xiaoshuo.sogou.com'
    url = base_url + url_list
    soup = get_soup(url)
    lst = soup.find_all('a',class_="text-ellips")
    for i in lst:
        # 获取到小说的url
        file_url = i['href']
        # 拼接小说的路径
        fic_url = base_url + file_url
        fiction = get_fiction_body(fic_url)
        name= i.find('span').string
        save_fiction(name,fiction,fic_name)

if __name__ == "__main__":
    fic_name = input("输入小说的名字:")
    main(fic_name)
