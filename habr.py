import requests
from bs4 import BeautifulSoup

count = int(input("Введите количество постов: "))
parse_page = ''

if count % 20 == 0:
    pages_to_parse = count//20
else:
    pages_to_parse = count//20 + 1

for i in range (1, pages_to_parse+1):
    url = 'https://habr.com/ru/top/yearly/page' + str(i)
    r = requests.get(url)
    parse_page += r.text.replace('</html>', '')

soup = BeautifulSoup(parse_page, 'lxml')

for i in range (0, count):
    post_title = soup.find_all('a', class_='post__title_link')[i].text
    post_text = BeautifulSoup(str(soup.find_all('div', class_='post__text')[i]).replace('<br/>','').replace('\r\n',' ').replace('\n',' '),'lxml').text
    post_date = soup.find_all('span', class_='post__time')[i].text
    post_author = soup.find_all('span', class_='user-info__nickname')[i].text

    file = open('habr.csv', 'a')
    file.write(post_title + ';')
    file.write(post_text + ';')
    file.write(post_date + ';')
    file.write(post_author + '\n')
    file.close()
