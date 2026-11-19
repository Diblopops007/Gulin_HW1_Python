# Lesson 10 — Allure + Selenium Pytest

Проект содержит UI-тесты на Selenium с интеграцией **Allure** для
формирования наглядных отчётов.

## Требования

- Python 3.10+
- Google Chrome / Mozilla Firefox


## Запуск тестов и формирование отчёта

Запуск из корня проекта:

```
pytest lesson_10 --alluredir=lesson_10/allure-results
```

После выполнения в папке `lesson_10/allure-results` появятся
JSON-файлы с результатами.

## Просмотр отчёта

```
allure serve lesson_10/allure-results
```

Команда автоматически сгенерирует HTML-отчёт во временной папке
и откроет его в браузере.



## Разметка Allure

В тестах использованы:

- `@allure.feature` — модуль/фича;
- `@allure.title` — заголовок теста;
- `@allure.description` — описание;
- `@allure.severity` — важность (`CRITICAL`, `NORMAL`);
- `with allure.step("...")` — шаги теста.

