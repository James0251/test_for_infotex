import requests
from bs4 import BeautifulSoup

company_id = input('Введите ссылку на компанию или ее ID: ')
try:
    test_for_int = int(company_id)
    url = 'https://www.list-org.com/company/'+company_id
except:
    url = company_id

user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0', 'referer':'https://list-org.com'}
session = requests.session()
company_page = session.get(url, headers = user_agent)

soup = BeautifulSoup(company_page.text, 'lxml')
legal_name = soup.find('a', class_='upper').text
director = soup.find_all('a', class_='upper')[1].text
registration_date = soup.find('table', class_='tt').find_all('td')[-3].text
status = soup.find('table', class_='tt').find_all('td')[-1].text
inn = soup.find('table', class_='tt').find_all('td')[3].text.split('/')[0].strip()
kpp = soup.find('table', class_='tt').find_all('td')[3].text.split('/')[1].strip()
ogrn = soup.find_all('div', class_='c2m')[2].find_all('p')[3].text.split(':')[1].strip()

data = {'legal_name':legal_name,
        'director':director,
        'registration_date':registration_date,
        'status':status,
        'inn':inn,
        'kpp':kpp,
        'ogrn':ogrn}

file = open('company.csv','a')
file.write(data['legal_name'] + ';')
file.write(data['director'] + ';')
file.write(data['registration_date'] + ';')
file.write(data['status'] + ';')
file.write(data['inn'] + ';')
file.write(data['kpp'] + ';')
file.write(data['ogrn'] +'\n')
file.close()
