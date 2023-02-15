import requests
import json
import os
import time
import xlsxwriter
from tqdm import tqdm
from multiprocessing import Pool
import numpy as np
from datetime import date
import re

prof_roles = [156, 160,10, 12, 150, 25, 165, 34, 36, 73, 155, 96, 164, 104, 157, 107, 112, 113, 148, 114, 116, 121, 124,
              125, 126]

def get_pages(page=0, area=1679, prof_roles=prof_roles):
    """
    Создаем метод для получения страницы со списком вакансий.
    Аргументы:
        page - Индекс страницы, начинается с 0. Значение по умолчанию 0, т.е. первая страница
    """
    params = {
        'area': area,  # Поиск ощуществляется по вакансиям города Москва
        'page': page,  # Индекс страницы поиска на HH
        'per_page': 100,  # Кол-во вакансий на 1 странице
        'professional_role': prof_roles
    }

    req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
    data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
    req.close()
    return data


def save_pages():
    try:
        os.makedirs(f'./data/vacancies/{date.today()}')
        os.makedirs(f'./data/vacancies/{date.today()}/raw_data')
        os.makedirs(f'./data/vacancies/{date.today()}/prepared_data')
        os.makedirs(f'./data/vacancies/{date.today()}/result')
    except FileExistsError:
        pass
    for page in range(0, 20):
        jsObj = json.loads(get_pages(page))
        for v in jsObj['items']:
            # Обращаемся к API и получаем детальную информацию по конкретной вакансии
            try:
                req = requests.get(v['url'])
            except:
                print(v)
                continue
            data = req.content.decode()
            req.close()

            # Создаем файл в формате json с идентификатором вакансии в качестве названия
            # Записываем в него ответ запроса и закрываем файл
            vacancy_id = v['id']
            fileName = f'./data/vacancies/{date.today()}/raw_data/{vacancy_id}.json'
            f = open(fileName, mode='w', encoding='utf8')
            f.write(data)
            f.close()

            time.sleep(0.2)

    print('Вакансии собраны')







def get_experience(small_directory):
    list_of_candidates = []
    with tqdm(total=len(small_directory)) as pbar:
        for file in small_directory:
            try:
                f = open(f'./data/vacancies/{date.today()}/raw_data/{file}', encoding='utf8')
                jsonText = f.read()
                jsonObj = json.loads(jsonText)
            except UnicodeDecodeError:
                print(file)
                continue
            vacancy_id = jsonObj['id']
            url = jsonObj['alternate_url']
            title = jsonObj['name']
            company = jsonObj['employer']['name']
            prof_role = jsonObj['professional_roles'][0]['name']
            experience = jsonObj['experience']['id']
            specialization = jsonObj['specializations'][0]['profarea_name']
            try:
                salary_from = jsonObj['salary']['from']
                salary_to = jsonObj['salary']['to']
                currency = jsonObj['salary']['currency']
            except TypeError:
                salary_from = ''
                salary_to =''
                currency = ''
            descriptions = (re.sub(r'(\<(/?[^>]+)>)', '', jsonObj['description']))
            skills = []
            for skl in jsonObj['key_skills']:
                skills.append(skl['name'])
            skills = str(skills)
            list_of_candidates.append([vacancy_id, url, title, company, prof_role, experience, skills,
                                       specialization, salary_from, salary_to, currency, descriptions])
            pbar.update(1)
    return list_of_candidates


def save_bd(num_threads=1, filename=f'{date.today()}'):
    directory = os.listdir(f'./data/vacancies/{filename}/raw_data')
    workbook = xlsxwriter.Workbook(f'./data/vacancies/{filename}/prepared_data/DataFrame.xlsx', {'strings_to_urls': False})
    worksheet = workbook.add_worksheet()
    worksheet.write(f'A1', 'id')
    worksheet.write(f'B1', 'url')
    worksheet.write(f'C1', 'title')
    worksheet.write(f'D1', 'company')
    worksheet.write(f'E1', 'prof_role')
    worksheet.write(f'F1', 'experience')
    worksheet.write(f'G1', 'key_skills')
    worksheet.write(f'H1', 'specialization')
    worksheet.write(f'I1', 'salary_from')
    worksheet.write(f'J1', 'salary_to')
    worksheet.write(f'K1', 'currency')
    worksheet.write(f'L1', 'description')
    num_ex = 2
    list_of_files = np.array_split(directory, num_threads)
    with Pool(num_threads) as pool:
        for thread in pool.map(get_experience, list_of_files):
            for resume in thread:
                worksheet.write(f'A{num_ex}', resume[0])
                worksheet.write(f'B{num_ex}', resume[1])
                worksheet.write(f'C{num_ex}', resume[2])
                worksheet.write(f'D{num_ex}', resume[3])
                worksheet.write(f'E{num_ex}', resume[4])
                worksheet.write(f'F{num_ex}', resume[5])
                worksheet.write(f'G{num_ex}', resume[6])
                worksheet.write(f'H{num_ex}', resume[7])
                worksheet.write(f'I{num_ex}', resume[8])
                worksheet.write(f'J{num_ex}', resume[9])
                worksheet.write(f'K{num_ex}', resume[10])
                worksheet.write(f'L{num_ex}', resume[11])
                num_ex += 1
        workbook.close()


if __name__ == '__main__':
    save_pages()
    save_bd()


