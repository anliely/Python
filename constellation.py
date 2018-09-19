import requests
from bs4 import BeautifulSoup

def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    response = requests.get(url,headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    return html

def get_url():
    month = int(input("请输入月份"))
    day = int(input("请输入日期"))
    url = 'https://www.d1xz.net/astro/xingzuochaxun/%d-%d.aspx' % (month, day)
    html = get_html(url)
    soup = BeautifulSoup(html,'lxml')
    html2 = soup.find('span', style="color:red")
    html = html2.a['href']
    return html

def get_text():
    html = get_url()
    response = get_html(html)
    soup = BeautifulSoup(response,'lxml')
    Introduction = soup.find('p',class_="txt")
    label = soup.find_all('span',class_="left fl")
    content = soup.find_all('span',class_='right fr')
    left = []
    right = []
    for i in label:
        left.append(i.string)
    for j in content:
        right.append(j.string)
    message = zip(left,right)
    return message


if __name__=='__main__':
    get_text()
