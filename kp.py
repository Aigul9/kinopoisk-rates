import csv
import errno
import json
import logging
import os
import requests
from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join


logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s - %(filename)s:%(lineno)s:%(funcName)s()',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def extract_data(user_id, page_no):
    """Парсит данные с персональной страницы."""
    url = f'https://www.kinopoisk.ru/user/{user_id}/votes/list/ord/date/page/{page_no}/#list'
    page = requests.get(url)
    logger.info(page.status_code)
    soup = BeautifulSoup(page.content, 'html.parser')
    items = soup.find_all('div', {'class': 'item'})
    while page.status_code == 200 and len(items) == 0:
        logger.info('loading...')
        logger.info(soup)
        exit()
    for item in items:
        num = item.find('div', {'class': 'num'}).text
        href = item.find('a', href=True)['href']
        name_rus = item.find('div', {'class': 'nameRus'}).text
        name_eng = item.find('div', {'class': 'nameEng'}).text
        rating_data = item.find('div', {'class': 'rating'})
        try:
            rating = rating_data.find('b').text
        except AttributeError:
            rating = 'n/a'
            logger.error(f'{name_rus}')
        try:
            duration = rating_data.find_all('span')[1].text
        except IndexError:
            duration = 'n/a'
            logger.error(f'{name_rus}')
        try:
            votes = int(rating_data.find_all('span')[0].text[1:-1].replace(' ', ''))
        except ValueError:
            duration = rating_data.find_all('span')[0].text
            votes = 'n/a'
            logger.error(f'{name_rus}')
        date = item.find('div', {'class': 'date'}).text
        my_vote = item.find('div', {'class': 'vote'}).text
        yield num, href, name_rus, name_eng, rating, votes, duration, date, my_vote


def get_pages(count):
    """Возвращает количество страниц для парсинга."""
    default_count = 50
    return round(count / default_count)


def save(page_no, data):
    """Сохраняет данные в файл."""
    mkdir_p('data/')
    with open(f'data/{page_no}.tsv', 'w', encoding='utf-8', newline='') as file:
        w = csv.writer(file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_NONE, escapechar='\\')
        w.writerow(['num', 'href', 'nameRus', 'nameEng', 'rating', 'votes', 'duration', 'date', 'my_vote'])
        for v in data:
            w.writerow([*v])


def load_data(path):
    """Загружает данные из файла."""
    with open(f'{path}.tsv', 'r', encoding='utf-8') as f:
        return [line.rstrip().split('\t') for line in f.readlines()][1:]


def get_movie_attr(href):
    """Возращает тип: фильм или сериал - и его id."""
    href = href.split('/')
    return href[1], href[2]


def extract_data_api(movie_id, api_key):
    """Получает дополнительные данные по фильму из api."""
    url = f'https://kinopoiskapiunofficial.tech/api/v2.1/films/{movie_id}?' \
          f'append_to_response=BUDGET&' \
          f'append_to_response=RATING&' \
          f'append_to_response=REVIEW&'
    headers = {'content-type': 'application/json', 'X-API-KEY': api_key}
    r = requests.get(url, headers=headers)
    return json.loads(r.content.decode('utf-8'))


def files_in_dir(path):
    """Формирует список файлов с директории."""
    return [f for f in listdir(path) if isfile(join(path, f))]


def load_games(path):
    """Считывает данные из массива файлов."""
    files = files_in_dir(path)
    data = []
    for f in files:
        logger.info(f[:-4])
        data.extend(load_data(f'{path}{f[:-4]}'))
    return data


def mkdir_p(path):
    """Создает директорию data/ для сохранения выгрузок с оценками."""
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
