1. Необходимо создать класс «Technic» с тремя параметрами:
название, цена, наличие (True, False). С помощью тернарного
оператора по цене определить товар в категорию
«Бюджетный» / «Дорогой».
*Важно, необходимо ограничить добавление других наборов
атрибутов и методов.

2. На основе предыдущего задания необходимо выполнить
сравнение строк «Названия техники» по количеству символов,
неиспользованный скрипт закомментировать.
*воспользоваться магическими методами;
** воспользоваться декоратором.

3. Создать пакет `Tasks` состоящиё из трех подпакеов: `tasks1`,`tasks2`,`tasks3`, в каждом из них необходимо создать файл `test.py`

    3.1. `tasks1`: создать функцию для задачи "Сервисный центр"

    Задача: Сервесный центр

    В базе даннхы сервесного центра хранятся информация о списке клиентов. Данные о технике и их владельцах
    записаны в формате "Название техники, цена ремонта, Имя владельца, телфон владельца"

    ```python
    technic = [('Ноутбук', 1500, 'Татьяна', '89002001020'),
    ('Смартфон', 500, 'Анна', '89202202325'),
    ('Проектор ', 300, 'Андрей', '89505205656'),
    ('Принтер', 750, 'Игорь', '89303303236'),
    ('Планшет', 2300, 'Игорь', '89303303236'),
    ('Смартфон', 1000, 'Андрей', '89505205656'),
    ('Ноутбук', 4800, 'Татьяна', '89002001020'),
    ('Наушники', 780, 'Марина', '89562002350'),
    ('Сканер', 550, 'Сергей', '89808564559'),
    ('Планшет', 1200, 'Анна', '89202202325'),
    ('Ноутбук', 1100, 'Игорь', '89303303236'),
    ('Смартфон', 3500, 'Татьяна', '89002001020')]
    ```

    Имена некоторых клиентов поаторяються, так как обращались в сервис несколько раз.
    Необходимо оптимизировать хранение данных таким образом, чтобы для каждого клиента при ввыоде на печать данных о всеё технике отображались в одной строке

    ```
    Татьяна 89002001020: Ноутбук - 1500; Ноутбук - 4800;
    Смартфон - 3500
    Анна 89202202325: Смартфон - 500; Планшет - 1200
    Андрей 89505205656: Проектор - 300; Смартфон - 1000
    Игорь 89303303236: Принтер - 750; Планшет - 2300; Ноутбук

    - 1100
    Марина 89562002350: Наушники - 780
    Сергей 89808564559: Сканер - 550
    ```

    3.2 `tasks2`: создание функции для задачи "Имя файла"

    Задача: Имя файла

    Фирма для названия файлов всегда использует одинаковую
    длину. Длина определяется исходя из самого длинного
    названия, передаваемого в списке. Важно, в название файла
    не должны дублироваться символы. Если строка короче
    самой длинной, необходимо дополнить нижним
    подчеркиванием до необходимого размера.

    3.3 `tasks3`: Итоговая задача - вызвать функции с задачами 3.1 и 3.2

4. Задача БД - результат представить в виде SQL запросов в любом текстовом редакторе

    4.1 Объеденить таблицы
    4.2 Объеденить таблицы по таблице Заказчики
    4.3 Объеденить таблицы по таблице Города
