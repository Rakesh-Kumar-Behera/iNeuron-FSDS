-- Active: 1685081069660@@127.0.0.1@3306@Test
CREATE TABLE t1(x1 VARCHAR(40), x2 INT , x3 VARCHAR(60) , x4 VARCHAR(90));

select * from t1;

insert INTO t1 VALUES('raka' , 234 , 'kumar' , 'iNeuron');

CREATE Table fsds (student_name VARCHAR(50) , email_id VARCHAR(90) , phone_number INT);

select * FROM fsds;

INSERT INTO fsds VALUES('Rakesh' , 'raka@ineuron.ai' , 987678);

INSERT INTO fsds VALUES('Mukesh' , 'Muka@ineuron.ai' , 887678) , ('yash' , 'yas@ineuron.ai' , 897678) , ('Nachi' , 'nachi@ineuron.ai' , 889678) , ('Abhi' , 'abhi@ineuron.ai' , 887978);

SHOW DATABASES;

use fsds_db;

select * from fsds1;
