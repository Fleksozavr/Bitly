# Обрезка ссылок с помощью Bitly

Этот код поможет вам сократить ссылку, и посмотреть количество переходов по ней.

### Как установить

Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Рекомендуется использовать [virtual/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.

Перед запуском программы не забудьте склонировать проект или скачать его архив. В папке с проектом не забудьте создать .env файл, где вы укажите ваш собственный токен Битли([создать Битли токен](https://bitly.com/pages/home))
```
bitly_token = "ваш токен"
```

### Как запустить файл

Для сокращения ссылки необходимо запустить файл, где в качестве аргумента будет ваша ссылка.
```
python main.py https://dvmn.org/modules/
```
Для подсчета переходов по ссылке Битли необходимо запустить файл, где в качестве аргумента будет ваш Битлинк:
```
python main.py https://bit.ly/3N9ThBf
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org)
