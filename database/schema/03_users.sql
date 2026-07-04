use warehouse_db;

create table users (
    id int auto_increment primary key,
    role_id int not null,
    full_name varchar(100) not null,
    username varchar(50) not null unique,
    email varchar(255) not null,
    password varchar(255) not null,
    phone varchar(20),
    avatar varchar(255),
    status tinyint default 1,
    last_login datetime null,
    created_at timestamp default current_timestamp,
    updated_at timestamp default current_timestamp
        on update current_timestamp,

    constraint fk_user_role
        foreign key(role_id)
        references roles(id)
);