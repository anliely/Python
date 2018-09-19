import requests
from bs4 import BeautifulSoup

def bd_bk():
    messge = input("输入需要百度的信息:")
    url = 'https://www.baidu.com/s?wd=' + messge
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

    response = requests.get(url, headers=headers)
    try:
        html = response.text
    except AttributeError as e:
        return "搜索的选项不存在"
    html1 = html.split('<h3 class="t c-gap-bottom-small">')
    try:
        html2 = html1[1].split('<a href="')
    except IndexError as e:
        return "错误的搜索方式"
    url2 = html2[1].split("\"")[0]
    wangzhi = requests.get(url2, headers=headers)
    wangzhi.encoding='utf-8'
    new_html = wangzhi.text
    soup = BeautifulSoup(new_html, 'lxml')
    soup_text = soup.find('div', class_="lemma-summary")
    try:
        message = soup_text.text.strip()
    except AttributeError as e:
        return "该搜索项不存在"
    msg = message.split('\n')
    x = 0
    for i in msg[:]:
        if x % 2 == 1:
             msg.remove(i)
        x += 1
    last_msg = ''.join(msg)
    return last_msg

print(bd_bk())
