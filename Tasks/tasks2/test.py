"""
3.2 `tasks2`: создание функции для задачи "Имя файла"

Задача: Имя файла

Фирма для названия файлов всегда использует одинаковую
длину. Длина определяется исходя из самого длинного
названия, передаваемого в списке. Важно, в название файла
не должны дублироваться символы. Если строка короче
самой длинной, необходимо дополнить нижним
подчеркиванием до необходимого размера.
"""


import pprint


def rename_files(list_dir: list):
    max_length = len(max(list_dir, key=len))

    res_set = set()
    for filename in list_dir:
        new_filename = filename.replace(
            ' ', '_').replace('-', '_').replace('.', '_')
        if len(new_filename) < max_length:
            new_filename = new_filename + '_' * \
                (max_length - len(new_filename))
        res_set.add(new_filename)

    pprint.pprint(res_set)


if __name__ == "__main__":
    # Список файлов
    list_dir = [
        'AnyDask.desktop', 'DBeaver.desktop', 'freetube.desktop', 'krdc.desktop', 'Pycharm.desktop', 'code.desktop',
        'Goland', 'syncthing.desktop', 'Cilion', 'MagicaVoxel.desktop', 'blender.desktop',
        'Remmina.desktop', 'lunacy.desktop', 'peek.desktop', 'steam.desktop', 'Obsidian.desktop'
        'DataGrip.desktop', 'godot.desktop', 'fsearch.desktop', 'krdc2.desktop'        #
        # Дубликаты
        ,  'webstorm.desktop',  'webstorm.desktop',  'webstorm.desktop',  'webstorm.desktop'
    ]
    rename_files(list_dir)

"""
Так как это задача мне показалась шаблонной, я решил, в познавательных целях, воспользоваться ChatGPT, и немного поправить его ответ.

Весь ответ его выглядел так:

Для решения данной задачи можно использовать следующий алгоритм:

1. Найти самое длинное название в списке файлов.
2. Определить его длину.
3. Пройти по всем названиям файлов и проверить каждое на наличие повторяющихся символов.
4. Если найдены повторяющиеся символы, заменить их на нижнее подчеркивание.
5. Если длина текущего названия меньше самого длинного, дополнить его нижним подчеркиванием до нужной длины.
6 .Сохранить новое название файла.

Пример реализации данного алгоритма на языке Python:

```python
import os

def rename_files(directory):
    filenames = os.listdir(directory)
    max_length = len(max(filenames, key=len))

    for filename in filenames:
        new_filename = filename.replace(' ', '_').replace('-', '_').replace('.', '_')
        if len(new_filename) < max_length:
            new_filename = new_filename + '_' * (max_length - len(new_filename))
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
```

В данном примере мы используем модуль os для работы с файловой системой. 
Функция os.listdir(directory) возвращает список файлов в указанной директории. 
Мы находим самое длинное имя файла, затем проходим по списку файлов, заменяем все повторяющиеся символы на нижнее подчеркивание, 
дополняем название файла до нужной длины и сохраняем новое название с помощью функции os.rename(). 
Обратите внимание, что в примере мы заменяем пробелы, дефисы и точки на нижнее подчеркивание, 
чтобы избежать возможных проблем с именами файлов на разных операционных системах.

"""
