# Приложение для определения заполненных форм

## Технологии:
 ![Python](https://img.shields.io/badge/-Python-464646??style=flat-square&logo=Python)
 [![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
 ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
 ![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)

___
## Как запустить проект

Клонируйте репозиторий, перейдите в папку, установите docker и docker-compose если нужно.
Запустить приложения в контейнерах:
```
docker compose up
```
или для запуска в фоном режиме:
```
docker compose up -d
```
запустить скрипт для тестовых запросов в терминале docker:
```
python script.py
```
#### Остановить контейнер:
```
docker compose stop
```
#### Удалить контейнер:
```
docker compose down
```

___
## Доступ к сервису:
Сервис будет доступен по адресу http://localhost/

Документация по API доступна по адрессу: http://localhost:8000/docs#/

___
### Автор
Belousov Evgeniy