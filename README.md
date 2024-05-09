# Сайт-опрос для собственников бизнеса

## Описание проекта

Сервис онбординга с учетом пользователя и динамическим отображением вопросов.

### Основной функционал проекта:

* Регистрация и аутентификация пользователя;
* Внесение ответов на вопросы, которые можно создавать и редактировать в админке.

### Основной стек технологий проекта:

python, django, sqlite, django rest framework

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:dariazueva/absolut_test.git
```

```
cd absolut_test
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/Scripts/activate
    ```

```
python -m pip install --upgrade pip
```

Создайте файл .env и заполните его своими данными по образцу файла env.example:

```
SECRET_KEY = 'ваш-секретный-ключ'
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt

```

Пройдите в директорию с файлом manage.py:
```
cd onboarding
```

Выполнить миграции:

```
python manage.py migrate
```

Загрузить фикстуры:

```
python manage.py load_fixture
```

Запустить проект:

```
python manage.py runserver
```

## Автор
Зуева Дарья Дмитриевна
Github https://github.com/dariazueva/