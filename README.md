# Hook-Production-Task

Тестовое задание компании Hook Production.


## Особенности

- Присутствует CI
- Бизнес логика покрыта тестами
- БД Postgres
- `spinwheel/settings/storage.py` - настройки бд и статичных файлов

Приложение `roulette`:
- `roulette/services.py` - бизнес логика
- `roulette/repositories.py` - доступ к данным
- `roulette/viewsets.py` - `SpinWheelViewSet` с 3-мя эндпоинтами для получения/отправки данных

## Установка и запуск

- Создайте файл `.env` и скопируйте в него содержимое файла `.env.sample`:

Для **Linux**:
```
cp .env.sample .env
```

Для **Windows**:
```
copy .env.sample .env
```

- Запуск
```
docker-compose up django
```

- Тесты
```
docker-compose up test
```

- Заполнить базу
```
docker-compose up filldb
```

В результате будут созданы 3 пользователя (User), 2 раунда (Round) и 12 вращений (Spin).

Доступ к учетной записи суперпользователя:
- Логин: `admin`
- Пароль: `12345`

Данные других пользователей:

**test1**
- Логин: `test1`
- Пароль: `123123123Aa`

**test2**
- Логин: `test2`
- Пароль: `123123123Aa`

## Эндпоинты
- `/api/spinwheel/get_current_round` - `GET`. Получить текущий раунд. Если раунд закончился, создать и вернуть новый
- `/api/spinwheel/get_stats` - `GET`. Получить статистику согласно заданию
- `/api/spinwheel/make_spin/` - `POST`. Отправляет `id` раунда и совершает прокрутку
