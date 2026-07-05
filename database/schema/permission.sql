use warehouse_db;

create table premission(
    id int auto_increment primary key,
    code varchar(100) not null unique,
    name varchar(100) not null,
    description varchar(255),
    module varchar(50),
    status tinyint default 1,
    created_at timestamp default current_timestamp,
    updated_at timestamp default current_timestamp
        on update current_timestamp
);