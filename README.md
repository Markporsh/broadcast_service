# Сервис управления рассылками

Сервис позволяет управлять рассылками сообщений для клиентов. 

## Функциональность

- Создание новой рассылки
- Просмотр созданных рассылок
- Запуск рассылки по списку клиентов на основе заданных фильтров

## Технологии

- Python 3.10
- Django 4.2.3
- Django Rest Framework
- SQLite

## Установка и запуск

Следуйте этим шагам для установки и запуска проекта:

1. Клонирование репозитория:
    ```bash
    git clone https://github.com/Markporsh/broadcast_service
    ```
2. Переход в директорию проекта:
    ```bash
    cd broadcast_service
    ```
3. Создание и активация виртуального окружения:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
4. Установка зависимостей:
    ```bash
    pip install -r requirements.txt
    ```
5. Применение миграций:
    ```bash
    python manage.py migrate
    ```
6. Запуск сервера:
    ```bash
    python manage.py runserver
    ```

## Тестирование API

Для проверки API используйте коллекцию Postman, которую вы найдете в файле `postman_collection.json` в корневом каталоге проекта.

## Документация

Полная документация доступна по адресу `http://localhost:8000/docs`.
