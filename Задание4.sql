/*
4. Задача БД - результат представить в виде SQL запросов в любом текстовом редакторе

4.1 Объединить таблицы
4.2 Объединить таблицы по таблице Заказчики
4.3 Объединить таблицы по таблице Города
*/

create table City(
    id SERIAL PRIMARY KEY,
    name varchar(255)
);

create table  Customers(
    id SERIAL PRIMARY KEY,
    name varchar(255),
    id_city integer REFERENCES City(id) ON DELETE RESTRICT ON UPDATE RESTRICT
);

insert into City(name) values
    ('Москва')
    ,('Санкт-Петербург')
    ,('Пермь')
    ,('Воронеж')
    ,('Липецк')
;

insert into Customers(name, id_city) VALUES
    ('Иванов Т.М.',3)
    ,('Пановко И.Т.',2)
    ,('Черненко И.А.',3)
    ,('Пановко А.И.',2)
    ,('Иванова А.И.',1)
;

--? 4.1 (По какому правилу их объединить в этом пункт ?)

-- 4.2
select * from Customers
join City C on Customers.id_city = C.id;

-- 4.3
select * from City
join Customers C on City.id = C.id_city


