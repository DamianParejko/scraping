import sys
sys.path.append('src')

from scraper import Scraper

def main():
    blog_url = 'https://blog.hubspot.com/'

    scraper = Scraper(blog_url)
    articles_url = scraper.get_articles()

    for index, url in enumerate(articles_url):
        print('Artykuł:', url)
        article = scraper.parse_article(url)
        if article:
            print(article)
        if index < len(articles_url) - 1:
            print('-' * 40)

if __name__ == '__main__':
    main()