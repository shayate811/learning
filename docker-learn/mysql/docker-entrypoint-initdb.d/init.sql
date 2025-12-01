create database mydb;

use mydb;

create table tasks (
    id int primary key auto_increment,
    title varchar(255) not null,
    created_at timestamp not null default current_timestamp
);

insert into tasks (title) values
('フロントエンド実装'),
('バックエンド実装'),
('デプロイ設定');

create user 'myuser'@'%' identified with mysql_native_password by 'password';

grant select, insert, update, delete on mydb.* to 'myuser'@'%';