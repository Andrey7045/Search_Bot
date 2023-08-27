# Search_Bot
Мы разработали чат-бота с использованием машинного обучения и оптимизированного расширенного алгоритма Шинглов для помощи в решении вопросов по работе у сотрудников МФЦ.
Используемые алгоритмы разных уровней сложностей взаимодополняют друг друга, повышая точность при синтаксическом, лексическом анализе, а также ускоряют работу программы относительно сложности запроса.
На фреймворке python-flask написали API обработку на linux-сервере.
Такая структура построения поможет легко интегрировать систему обработки в любой другой сервис.

# ДЕМО
http://82.146.49.131:8087

# Архитектура
На фреймворке python-flask написал API обработки на своем linux-сервере. Написал фронтэнд на html и js. Фронт отправляет POST запрос, а сервер обрабатывает.
Такая структура построения поможет легко интегрировать систему обработки в любой другой сервис. В дальнейшем буду оптимизировать обработку за счёт многопоточности для сокращения времени обработки. Буду создавать удобный интерфейс запросов, админ-панель редактирования БД, систему получения ответов от модели offline GPT, построенной на основе текстов БД, для более глубокого анализа тем запросов.
Также сервер будет добавлен в docker и github для быстрого разворачивания и удобства.

# Исправление ошибок
Если не работает библиотека scikit-learn:
https://stackoverflow.com/questions/30766274/error-importing-scikit-learn-modules

Сайт для перевода Excel-файлов в JSON-файлы:
https://products.aspose.app/cells/ru/conversion/excel-to-json


## Разработчики
Команда SpecTraite
-> Ратушняк Иван
-> Молозаев Алексей
-> Герел Турбеева
