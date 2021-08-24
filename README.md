# Kinopoisk rates
Приложение для загрузки информации о фильмах и оценках с кинопоиска в базу данных.

## Рекомендации по настройке
1. Загрузить и установить [Python 3.9](https://www.python.org/)
2. Загрузить и установить [Docker](https://www.docker.com/)
3. Клонировать репозиторий ```git clone https://github.com/Aigul9/kinopoisk-rates.git```
4. Установить зависимости: ```pip install -r requirements.txt```
5. Проинициализировать переменные окружения в файле ```.env_template``` и переименовать его в ```.env```

## Запуск
1. Запустить postgres в контейнере: ```docker-compose up```
2. Запустить скрипт ```main.py```