# api_final
Версия 2.0 проекта api_yatube. 

Описана новая модель Follow, в которой два поля — user (кто подписан) и following (на кого подписан). Для этой модели описан эндпоинт /follow/ и два метода:
GET — возвращает все подписки пользователя, сделавшего запрос. Возможен поиск по подпискам по параметру search
POST — подписать пользователя, сделавшего запрос на пользователя, переданного в теле запроса. При попытке подписаться на самого себя, пользователь получает информативное сообщение об ошибке. Проверка осуществляется на уровне API.
Анонимный пользователь на запросы к этому эндпоинту получает ответ с кодом 401 Unauthorized.


## Запуск проекта
1. Клонирование репозитория
```
git clone git@github.com:ваш-аккаунт-на-гитхабе/api_final_yatube.git
```

Откройте в своем редакторе кода локальный проекта из репозитория GitHub, клонированного ранее

2. Развертывание в репозитории виртуального окружения
```
python3 -m venv venv
```
3. Запуск виртуального окружения
```
source venv/Scripts/activate
```
4. Установка зависимостей в виртуальном окружении
```
pip install -r requirements.txt
```

5. Выполнение миграций
```
python manage.py migrate
```

6. Запуск проекта
```
python manage.py runserver
```

## Документация

Когда вы запустите проект, по адресу http://127.0.0.1:8000/redoc/ будет доступна документация для API Yatube

## Технологии
- Python3
- Django REST Framework
- API REST
- Postman
- SQLite3
- Simple-JWT