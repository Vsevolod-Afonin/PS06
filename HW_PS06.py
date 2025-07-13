'''Попробуйте спарсить данные с сайта divan.ru, как в прошлом домашнем задании (можно использовать либо Scrapy, либо selenium),
 но теперь ещё и сохраните информацию в csv файл.
К дз прикрепляем ссылку на репозиторий с файлом csv и кодом.'''
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://www.divan.ru/category/divany-i-kresla'
driver.get(url)
time.sleep(1)

divans = driver.find_elements(By.CLASS_NAME, 'LlPhw')

parsed_data = []

for divan in divans:
    try:
        name = divan.find_element(By.CLASS_NAME, 'lsooF').text
        price = divan.find_element(By.CLASS_NAME, 'pY3d2').text
        link = divan.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8').get_attribute('href')
    except:
        print('Произошла ошибка при парсинге!')
        continue
    parsed_data.append([name, price, link])

print(parsed_data)
driver.quit()

with open('divan.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Названия дивана', 'Цена', 'Ссылка на товар'])
    writer.writerows(parsed_data)
