create table parkslot_now
(id serial primary key,
plate varchar(7) unique,
custumer_name varchar(225),
entry_time varchar(5),
entry_date varchar(10));