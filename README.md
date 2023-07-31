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
- Postgres
- redis
- Celery

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
   
3. Создать файл .env:
    ```bash
    touch .env
    ```
   
4. Откройте созданный .env файл в текстовом редакторе и добавьте следующие строки:
   ```
   DATABASE_NAME=broadcast
   DATABASE_USER=broadcast_admin
   DATABASE_PASSWORD=admin123
   DATABASE_HOST=db
   DATABASE_PORT=5432
   ```
   
5. Запустите docker compose:
   ```bash
   docker-compose up --build -d
   ```
   
6. Проведите миграции в django контейнере:
   ```bash
   docker exec -it broadcast_service-web-1 python manage.py migrate
   ```

Далее вы можете воспользоваться тестовыми данными из data.json
   ```bash
   docker exec -it broadcast_service-web-1 python manage.py loaddata data.json
   ```

Либо используйте файл broadcast_requests.postman_collection.json в нем хранятся запросы для Postman
Чтобы использовать их, следуйте инструкции:
1. Откройте Postman.
2. Нажмите кнопку "Import" в верхнем левом углу интерфейса Postman.
3. В открывшемся диалоговом окне выберите "Upload Files" и выберите broadcast_requests.postman_collection.json
4. Нажмите "Open" или "Import", и ваша коллекция должна быть импортирована в Postman.

INFO

Для получения иформации о логах используйте 
   ```bash
      docker logs broadcast_service-web-1
   ```
   ```bash
      docker logs broadcast_service-celery-1
   ```

## Эндпоинты API

### Клиенты

1. **Создать нового клиента**

   POST /clients/

   Пример запроса:
   ```json
   {
       "phone_number": "71234567890",
       "mobile_operator_code": 10,
       "tag": "VIP"
   }
   ```
2. **Получить список всех клиентов**

   GET /clients/

3. **Получить информацию о конкретном клиенте**

   GET /clients/{id}/

4. **Обновить информацию о конкретном клиенте**

   PUT /clients/{id}/

   Пример запроса:
   ```json
   {
       "phone_number": "71234567890",
       "mobile_operator_code": 20,
       "tag": "Regular"
   }
   ```
5. **Удалить конкретного клиента**

   DELETE /clients/{id}/

### Рассылки

1. **Создать новую рассылку**
   
   POST /newsletters/

   
   Тело запроса:
   
   ```json
   {
       "start_date": "2023-07-30T10:00:00Z",
       "message_text": "This is a sample newsletter message.",
       "mobile_operator_code": 10,
       "tag": "VIP",
       "end_date": "2023-07-30T12:00:00Z"
   }
   ```

2. **Получить список всех рассылок**

   GET /newsletters/

3. **Получить информацию о конкретной рассылке**

   GET /newsletters/{id}/

4. **Обновить информацию о конкретной рассылке**

   PUT /newsletters/{id}/
   
   Тело запроса:
   
   ```json
   {
    "start_date": "2023-07-30T10:00:00Z",
    "message_text": "This is an updated newsletter message.",
    "mobile_operator_code": 10,
    "tag": "VIP",
    "end_date": "2023-07-30T12:00:00Z"
   }
   ```
5. **Удалить конкретную рассылку**

   DELETE /newsletters/{id}/

Не забудьте заменить {id} на соответствующий id рассылки, с которой вы хотите взаимодействовать.
