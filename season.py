import requests
from bs4 import BeautifulSoup


def get_weather(city_id):
    url = "http://www.weather.com.cn/weather/{}.shtml".format(city_id)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    dates = soup.find_all('h1')
    date_time = []  # 存放七天内的日期
    for i in dates:
        date = str(i)[7:9]
        date_time.append(date)
    date_time = date_time[:][:7]
    msg = soup.find_all('p', class_="wea")
    description = []  # 存放天气的描述信息
    for i in msg:
        desc = i.string
        description.append(desc)
    msg2 = soup.find_all('p', class_="tem")
    max_tem = []  # 存放当天的最高气温
    min_tem = []  # 存放当天的最低气温
    for i in msg2:
        s = i.find_all('span')
        for x in s:
            max_tem.append(x.string)
        z = i.find_all('i')
        for y in z:
            min_tem.append(y.string)

    wins = []  # 用于存储风向
    win_power = []  # 用于存储风力
    msg3 = soup.find_all('p', class_='win')
    for i in msg3:
        for x in i.find_all('span'):
            wins.append(x.get('title'))
        for y in i.find_all('i'):
            win_power.append(y.string)
    num = 0
    for i in wins[:]:
        if num % 2 == 1:
            wins.remove(i)
        num += 1
    weather = []
    a = 0
    for _ in range(7):
        msg = tuple((date_time[a],description[a],min_tem[a],max_tem[a],wins[a],win_power[a]))
        weather.append(msg)
    return weather
