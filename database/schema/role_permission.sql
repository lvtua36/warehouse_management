use warehouse_db;

create table role_permissions(
    role_id int not null,
    permission_id int not null,
    primary key(role_id, permission_id),

    constraint fk_role_permission_role
    foreign key(role_id)
    references roles(id),

    constraint fk_role_permission_premission
        foreign key(permission_id)
        references permissions(id)
);