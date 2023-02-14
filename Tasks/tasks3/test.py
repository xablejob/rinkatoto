import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.resolve()))

import tasks2
import tasks1

if __name__ == "__main__":

    # 3.1
    tasks1.test.optimize([
        ('Ноутбук', 1500, 'Татьяна', '89002001020'),
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
        ('Смартфон', 3500, 'Татьяна', '89002001020')
    ])

    # 3.2
    tasks2.test.rename_files([
        'AnyDask.desktop', 'DBeaver.desktop', 'freetube.desktop', 'krdc.desktop', 'Pycharm.desktop', 'code.desktop',
        'Goland', 'syncthing.desktop', 'Cilion', 'MagicaVoxel.desktop', 'blender.desktop',
        'Remmina.desktop', 'lunacy.desktop', 'peek.desktop', 'steam.desktop', 'Obsidian.desktop'
        'DataGrip.desktop', 'godot.desktop', 'fsearch.desktop', 'krdc2.desktop'        #
        # Дубликаты
        ,  'webstorm.desktop',  'webstorm.desktop',  'webstorm.desktop',  'webstorm.desktop'
    ])
