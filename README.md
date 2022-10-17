## Тестовое задание для Product Lab

# Задание часть 1:

файл в корневой папке ```friends.py```

#### как запустить:
```
python3 friends.py
```
Как запустите скрипт, он ничего не выведет, это значит что он выполнится успешно (это на поиск связей у пользователей в сети). 


---

#### как запустить (linux/macos):

в корневой папке с проектом запускаем терминал и пишем комманды:
```

1) python3 -m venv venv

2) source venv/bin/activate

3) pip install -r requirements.txt
```

первые три комманды создатут виртуальное окружение, и установят библиотеки

Дальше нужно установить playwright (симулятор браузера), оно устанавливается ГЛОБАЛЬНО на компьютер, это не библиотека.

```
4) install playwright
```

удалить после теста можно, uninstall playwrigth

дальше запускаем сервер
```
5) python manage.py runserver 0.0.0.0:8000
```
---

проект запустится по адресу https://127.0.0.1:8000/

API доступно по адресу:
http://127.0.0.1:8000/product/
на API можно посылать только POST запрос!

в API можно посылать два поля: 
1) ```article``` - id товара на wildberries
2) ```excel``` - файл с расширением .xlsx (в корневой папке лежит excel_example.xlsx который можно загрузить для теста)

<img width="634" alt="instruction" src="https://user-images.githubusercontent.com/72818824/196244989-8911658e-977f-41c8-9024-eb49e6d5311c.png">

---

