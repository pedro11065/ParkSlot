
CREATE TABLE parkslot_historic(
    id UUID primary KEY,
    plate VARCHAR(8),
    custumer_name VARCHAR(40),
    entry_time time,
    entry_date date,
    exit_time time,
    exit_date date,
    paid FLOAT);

CREATE TABLE parkslot_now(
    id UUID primary KEY,
    plate VARCHAR(8),
    custumer_name VARCHAR(40),
    entry_time time,
    entry_date date);

CREATE TABLE users(
    id UUID PRIMARY KEY,
    cpnj INTEGER,
    fullname VARCHAR(40),
    email VARCHAR(40),
    password VARCHAR(40)
)




