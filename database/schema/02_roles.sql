use warehouse_db;

create table roles (
    id int auto_increment primary key ,
    name varchar(50) not null unique,
    description varchar(255),
    status tinyint default 1,
    created_at timestamp default current_timestamp,
    updated_at timestamp default current_timestamp
        on update current_timestamp
);