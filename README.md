# Финальный проект спринта: Проект «API для Yatube»

## Описание проекта
API Yatube предоставляет полный функционал для работы с публикациями, комментариями, группами и подписками. Реализована JWT-аутентификация для безопасного доступа к функциям платформы.

## Использованные технологии
* Python 3.9+
* Django 3.2
* Django REST Framework 3.12
* Simple JWT 4.7
* Djoser 2.1

## Установка

### Клонировать репозиторий и перейти в него в командной строке:
```python
git clone https://github.com/SergeiCherk/api_final_yatube.git

cd api_final_yatube
```
### Создание виртуального окружения
```python
python -m venv venv

source venv\Scripts\activate
```
### Установка зависимостей
```python
pip install --upgrade pip

pip install -r requirements.txt
```
### Выполнить миграции
```python
python manage.py migrate
```
### Создание суперпользователя
```python
python manage.py createsuperuser
```
### Запуск сервера
```python
python manage.py runserver
```
### Проект будет доступен по адресу: http://127.0.0.1:8000/

## Документация API
После запуска сервера документация API доступна по адресу:
Redoc: http://127.0.0.1:8000/redoc/

## Автор
Проект выполнен в рамках курса Backend-разработки Яндекс.Практикум

Черкасов Сергей, студент 76 когорты Факультета Бэкэнд-разработки
