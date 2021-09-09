drop database if exists surveys;
create database surveys;
use surveys;

create table movie
(
	mID int primary key auto_increment,
    moviename varchar(100)
);

create table person
(
	pID int primary key auto_increment,
    pname varchar(30)
);

# Many to Many table

create table movie_rating
(
	mpID int primary key auto_increment,
    mID int,
    pID int,
    rating smallint,
    foreign key (pID) references person(pID),
    foreign key (mID) references movie(mID)
);

insert into movie(moviename) values
("Suicide Squad"),
("Sasuage Party"),
("Sully"),
("War Dogs"),
("Bad Moms"),
("Southside With you");

insert into person(pname) values
("Jonathan"),
("Will"),
("Horace"),
("Waqas"),
("Laura"),
("Philip"),
("Travis"),
("Solomon"),
("Eric");

insert into movie_rating(mID,pID,rating) values
(1,2,5),
(1,5,1),
(4,8,3),
(6,5,5),
(3,5,5),
(2,8,4),
(2,6,4),
(5,1,1),
(2,1,5),
(4,4,4);

# See who has rated which movies
#select pname as Person, moviename, rating from person p
#inner join movie_rating mr
#on p.pID = mr.PID
#	inner join movie m
#    on m.MID = mr.MID;