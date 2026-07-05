use warehouse_db;

insert into role_permissions

(role_id, permission_id)

select

1,
id

from permissions;