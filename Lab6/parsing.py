print('HTML - ТЕГИ:')
from bs4 import BeautifulSoup
import requests 
with open("news.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml') 
    for child in soup.recursiveChildGenerator():
        
        if child.name:
            print(child.name)
print("")
print('')
print('ПОСИЛАННЯ В КОДІ:')
print('')
def get_links(url):
    from bs4 import BeautifulSoup as soup
    import requests 
    result = requests.get(url)
    page = result.text
    doc = soup(page, features='html.parser')
    links = [element.get('href') for element in doc.find_all('a')]
    return links

urls = ['https://kyiv.24tv.ua/aeroportu-borispolya-utvorilas-velika-svizhi-novini-borispolya_n1457447']

for url in urls:
    print('Links in', url)
    for num, link in enumerate(get_links(url), start=1):
        print(num, link)
    print()