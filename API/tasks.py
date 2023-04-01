import requests
import json
from OpenChecker.celery import app
from .create_models import *
from .hh_data import get_pages
import webbrowser
import time


@app.task
def get_data():
    print('Start to add vacancies')
    for page in range(0, 20):
        jsObj = json.loads(get_pages(page))
        for vacancy_obj in jsObj['items']:
            try:
                req = requests.get(vacancy_obj['url'])
            except:
                print(vacancy_obj)
                continue
            data = req.content.decode()
            req.close()
            jsObj = json.loads(data)
            try:
                print('Error-' + jsObj['errors'][0]['value'])
                captcha_url = jsObj['errors'][0]['captcha_url'] + '&backurl=' + 'http://127.0.0.1:8000'
                webbrowser.open(captcha_url, new=0)
                print('Press enter co continue')
                input()
            except:
                pass
            create_vacancy(jsObj)
            time.sleep(0.25)
    print('Vacancies added successfully')


