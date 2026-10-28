# Telegram Bot Template (aiogram 3)

Шаблон бота с опциональным прокси для работы из России.

## Запуск

1. Скопировать `.env.example` → `config/.env`, заполнить `BOT_TOKEN`.
2. Установить зависимости: `pip install -r requirements.txt`.

### Локально в РФ (через прокси)
1. В `config/.env` указать `PROXY_URL=http://127.0.0.1:8080` и `WORKER_HOST=...workers.dev`.
2. Окно 1: `tgwsapiproxy --worker-host ...workers.dev`
3. Окно 2: `python main.py`

### На зарубежном сервере (без прокси)
1. В `config/.env` убрать/закомментировать `PROXY_URL`.
2. `python main.py`