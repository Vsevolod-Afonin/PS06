import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'https://tomsk.hh.ru/vacancies/programmist'

driver.get(url)
time.sleep(0.1)

vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--n77Dj8TY8VIUF0yM')

parsed_data = []

for vacancy in vacancies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___tkzIl_6-0-0').text
        company = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___tkzIl_6-0-0').text
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___tkzIl_6-0-0').text
        link = vacancy.find_element(By.CSS_SELECTOR,  'span.magritte-text___tkzIl_6-0-0').text
    except:
        print('Произошла ошибка при парсинге')
        continue
    parsed_data.append([title, company, salary, link])

print(parsed_data)
driver.quit()

with open('hh.csv', 'w',newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'Зарплата', 'Ссылка на вакансию'])
    writer.writerows(parsed_data)