create database SupplyDB;
USE SupplyDB;

create table if not exists Suppliers (
    sid int auto_increment primary key,
    sname varchar(255),
    address varchar(255)
);

create table if not exists Parts (
    pid varchar(255) primary key,
    pname varchar(255),
    color varchar(255)
);

create table if not exists Catalog (
    sid int,
    pid varchar(255),
    cost double,
    primary key (sid, pid),
    foreign key (sid)
        references suppliers (sid)
        on update restrict
        on delete cascade,
    foreign key (pid)
        references parts (pid)
        on update restrict
        on delete cascade
);
