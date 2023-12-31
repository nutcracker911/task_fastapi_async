[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Task+FastAPI+Async)](https://git.io/typing-svg)

Данный проект разработан для осуществления асинхронного получения данных для последующей последовательной обработки.

## Запуск

В проекте имеется готовое виртуальное окружение, которое содержит в себе Python 3.11 и версию библиотеки FastAPI 0.97.0

Для запуска вирутального окружения необходимо активировать коружения командой:

```
source task_fastapi_async/myenv/bin/activate
```

Для запуска сервера FastAPI введите команду:

```
python3 task_fastapi_async/test_task/main.py
```

В проекте также присутствует блок кода отвечающий за проверку сервера, который создает асинхронную сессию для отправки 3 http запросов на сервер. По результату запроса сервер получает ответ в виде времени задержки обработки сервером. Для запуска теста воспользуйтесь следующей командой:

```
python3 task_fastapi_async/test_task/test_main.py
```


