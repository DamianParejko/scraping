import requests
from bs4 import BeautifulSoup
from analyzer import Analyzer

class Scraper:
    def __init__(self, url):
        self.url = url
    
    def get_articles(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            print("Error")
            return None

        articles_soup = BeautifulSoup(response.text, 'html.parser')

        articles = articles_soup.find_all('li', class_='blog-post-list-item', limit=3)

        links = []
    
        for article in articles:
            link = article.find('a')
            if link:
                href = link['href']
                links.append(href)
                
        return links

    def parse_article(self, article_url):
        response = requests.get(article_url)
        if response.status_code != 200:
            print("Error")
            return None

        article_soup = BeautifulSoup(response.text, 'html.parser')
        article_content = article_soup.find('div', class_='hsg-rich-text__wrapper')

        if article_content:
            text = article_content.text
            response_count_words = Analyzer.count_words(text) 
            response_count_letters = Analyzer.count_letters(text) 
            response_phrases = Analyzer.most_common_phrases(text)
            return f'{response_count_words}\n{response_count_letters}\n{response_phrases}'
        else: 
            return None