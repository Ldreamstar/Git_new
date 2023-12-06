import requests
from bs4 import BeautifulSoup
import csv
import re


def get_sina_news():
    try:
        url = 'https://news.sina.com.cn/world'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        }

        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.text, 'html.parser')

        # 获取所有新闻项：在 BeautifulSoup 对象 soup 中查找所有带有类名以 "news-item" 开头的 <div> 元素，并将它们存储在名为 news_items 的结果集合中
        news_items = soup.find_all('div', class_=re.compile(r'^news-item'))

        # 存储新闻信息的列表
        news_data = []

        for item in news_items:
            try:
                # 提取新闻主题、时间、摘要等信息，具体选择可能需要根据实际情况调整
                title = item.find('h2').text.strip()
                time = item.find('div', class_='time').text.strip()

                # 将信息存储为字典
                news_data.append({
                    'title': title,
                    'time': time,
                })
            except Exception as e:
                print(f"Error extracting news item: {e}")

        return news_data
    except Exception as e:
        print(f"Error fetching Sina news: {e}")
        return []


def save_to_csv(news_data, filename='sina_news.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'time', 'summary']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in news_data:
            writer.writerow(row)


# 获取新浪网最近一天的新闻数据
sina_news_data = get_sina_news()

# 存储为 CSV 文件
save_to_csv(sina_news_data)

print('新闻数据已成功抓取并保存为 CSV 文件: sina_news.csv')
