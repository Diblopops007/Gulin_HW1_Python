# Lesson 10 — Allure Pytest

Проект содержит UI-тесты на Selenium с интеграцией **Allure** для
формирования наглядных отчётов.



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

