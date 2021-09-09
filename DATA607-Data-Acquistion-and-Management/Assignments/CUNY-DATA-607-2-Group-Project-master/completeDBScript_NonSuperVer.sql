/* Create Data Science database */
DROP DATABASE if exists data_science_wordver;

CREATE DATABASE data_science_wordver;
/* Use  data_science_wordSuperVer */
USE data_science_wordver;

/* Drop all data_science database tables */
/*DROP TABLE data_science.category;
DROP TABLE data_science.skill;
DROP TABLE data_science.skill_category_map;
DROP TABLE data_science.transactions;*/
/* Create data_science.category table */
CREATE TABLE category
(
	ID INT(5) NOT NULL AUTO_INCREMENT,
	CATEGORY_NAME VARCHAR(100),
	PRIMARY KEY (ID)
);
/* Create data_science.skill table 
changed to have foriegn key to category table...assumption is each skill 
must have a category even if it is the unknown*/
CREATE TABLE skill
(
        ID INT(5) NOT NULL AUTO_INCREMENT,
        CAT_ID INT(5) NOT NULL,
        SKILL_NAME VARCHAR(100),
        FOREIGN KEY (CAT_ID)
			REFERENCES category(ID),
	PRIMARY KEY (ID)
);


/* Create data_science.skill_category_map table 
with foreign key in skill to category, not sure this table is needed*/

/*CREATE TABLE skill_category_map
(
	SKILL_ID INT(5) NOT NULL,        
	CATEGORY_ID INT(5) NOT NULL
);*/

/* Create data_science.transactions table */
CREATE TABLE transactions (
    ID INT(5) NOT NULL AUTO_INCREMENT,
    SKILL_ID INT(5) NOT NULL,
    TX_DATE DATETIME NOT NULL,
    FOREIGN KEY (SKILL_ID)
        REFERENCES skill (ID),
    PRIMARY KEY (ID)
);

create table skill_counts (
	ID INT(5) NOT NULL AUTO_INCREMENT,
    SKILL_ID INT(5) NOT NULL, 
    SKILL_CNT INT(10) NOT NULL,
    FOREIGN KEY (SKILL_ID)
        REFERENCES skill (ID),
    PRIMARY KEY (ID)
);


/* Initialize auto increment value to 1 */
ALTER TABLE category AUTO_INCREMENT=1;
/* Initialize auto increment value to 1 */
ALTER TABLE skill AUTO_INCREMENT=1;
/* Initialize auto increment value to 1 */
ALTER TABLE transactions AUTO_INCREMENT=1;

/* Populate data_science.category table */
INSERT INTO category(CATEGORY_NAME) VALUES ('Unknown');
INSERT INTO category(CATEGORY_NAME) VALUES ('Programming Languages');
INSERT INTO category(CATEGORY_NAME) VALUES ('Machine Learning');
INSERT INTO category(CATEGORY_NAME) VALUES ('Data Mining');
INSERT INTO category(CATEGORY_NAME) VALUES ('Data Visualization');
INSERT INTO category(CATEGORY_NAME) VALUES ('Databases');
INSERT INTO category(CATEGORY_NAME) VALUES ('Big Data Frameworks');
INSERT INTO category(CATEGORY_NAME) VALUES ('Probability and Statistics');
INSERT INTO category(CATEGORY_NAME) VALUES ('Generic');
INSERT INTO category(CATEGORY_NAME) VALUES ('Education');
INSERT INTO category(CATEGORY_NAME) VALUES ('Operating Systems');

/* Populate data_science.skill table */
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (2,'Java');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (2,'R');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (2,'Scala');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (2,'Python');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (2,'C');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (2,'C++');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (2,'SAS');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (3,'Natural Language Processing');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (3,'scikit-learn');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (3,'Text Mining');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (3,'Text Analytics');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (5,'Tableau');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (5,'D3.js');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (5,'FusionCharts');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (5,'Charts.js');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (5,'Google Charts');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (5,'Highcharts');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (5,'Leaflet');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (5,'dygraphs');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (5,'Datawrapper');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (5,'QlikView');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (5,'Plotly');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (6,'MySQL');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (6,'Oracle');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (6,'NoSQL');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (6,'MongoDB');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (6,'Cassandra');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (6,'Redis');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (6,'SQL');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (6,'Postgres');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (6,'HBase');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (6,'Elastic');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (7,'Hadoop');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (7,'Hive');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (7,'Mahout');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (7,'Pig');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (7,'Spark');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (7,'Tez');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (7,'Zookeeper');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (7,'Avro');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (7,'Ambari');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (7,'Chukwa');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (7,'Apache Storm');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (7,'Apache Kafka');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (8,'Naive Bayes Classifier');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (8,'Inferential Statistics');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (8,'Descriptive Statistics');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (8,'Regression Analysis');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (8,'Time Series Analysis10	Unix');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (11,'Linux');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (11,'Mac');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (11,'Windows');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (10,'B.S Computer Science');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (10,'B.S Statistics');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (10,'B.S Mathematics');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (10,'B.S Applied Mathematics');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (10,'B.S Economics');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (10,'B.S Physics');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (10,'M.S Computer Science');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (10,'M.S Statistics');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (10,'M.S Mathematics');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (10,'M.S Applied Mathematics');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (10,'M.S Operations Research');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (10,'M.S Quantitative Finance');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (9,'Web Analytics');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (9,'Predictive Analytics');
INSERT INTO skill(CAT_ID, SKILL_NAME) VALUES (9,'ETL');

DELIMITER //




drop procedure if exists sp_insert_category//

create procedure sp_insert_category (IN cat varchar(100))

	begin
		if not exists(select category_name from category as c where c.CATEGORY_NAME = cat)
			then insert into category(CATEGORY_NAME) value (cat) ;
		end if;
end//


drop procedure if exists sp_insert_skill//

create procedure sp_insert_skill 
		(in s_name varchar(100),
         in cat varchar(100))
	begin
		declare c_id int(5);
		
		#if cat not passed in, then default to "unknown"
		if cat = '' then set cat = 'Unknown'; end if;  
		
		set c_id = (select id from category c where c.CATEGORY_NAME = cat);
		
		if(isnull(c_id))
			then insert into CATEGORY(CATEGORY_NAME) value (CAT);
			set c_id = (select id from category c where c.CATEGORY_NAME = cat);
		END IF;
		
		if not exists(select skill_name from skill as s
										inner join category c
										on c.ID = s.CAT_ID    
					  #where c.ID = c_id   #we might/might not want skill to be in more than one category but will blow up elsewhere if we do that currently
					#	and S.skill_name = s_name)						
                    where S.skill_name = s_name)						
			then insert into skill(cat_id, skill_name) values (c_id, s_name) ;
		end if;
	end//


drop procedure if exists sp_insert_transaction_by_id//

create procedure sp_insert_transaction_by_id
				(in s_id int(5))
	#assumes skill_id exists, if not will insert nada, caller beware				 
	begin
		set s_id = (select id from skill where id = s_id);
		
		if (not isnull(s_id))
		then
			insert into transactions(skill_id, tx_date) values(s_id, now());
		end if;
	end//
                 
drop procedure if exists sp_insert_transaction_by_name//

create procedure sp_insert_transaction_by_name
				(in s_name varchar(100))			

	begin
		#assumes skill_id exists, if not will insert nada, caller beware
		declare s_id int(5);
		
		set s_id = (select id from skill where skill_name = s_name);
		
		if (not isnull(s_id))
			then insert into transactions(skill_id, tx_date) values(s_id, now());
		end if;
	end//

drop procedure if exists sp_upsert_skill_counts//

create procedure sp_upsert_skill_counts
					(in s_name varchar(100),
                     in s_count int(10))

	begin
		#assumes skill_id exists, if not will insert nada, caller beware
                
		declare s_id int(5);
		
		set s_id = (select id from skill where skill_name = s_name);
        if (not isnull(s_id))
			then
				if (select exists (select * from skill_counts s where s.skill_id = s_id))
					then						
						update skill_counts sc
						set  sc.skill_cnt = s_count
						where sc.skill_id = s_id;
				 else					
					insert into skill_counts(skill_id, skill_cnt) values(s_id, s_count);
                 end if;		
			
		end if;
    
    end;



drop procedure if exists sp_get_category//

create procedure sp_get_category (IN cat varchar(100))

begin
	if (cat = "")
	then select c.ID, c.CATEGORY_NAME from category as c;
    else
		select c.ID, c.CATEGORY_NAME from category as c
			where c.CATEGORY_NAME = cat;
	end if;
end//

drop procedure if exists sp_get_skill//

create procedure sp_get_skill (IN skillName varchar(100))

begin
	if (skillName = "")
	then select s.ID, s.CAT_ID, s.SKILL_NAME from skill as s;
    else
		select s.ID, s.CAT_ID, s.SKILL_NAME from skill as s
			where s.SKILL_NAME = skillName;
	end if;
end//

drop procedure if exists sp_get_skillByID//

create procedure sp_get_skillByID (IN skillID int(5))

begin	
		select s.ID, s.CAT_ID, s.SKILL_NAME from skill as s
			where s.id = skillID;	
end//

drop procedure if exists sp_get_skill_counts//

create procedure sp_get_skill_counts (IN skillID int(5),
									  IN skillName varchar(100),
                                      IN catg varchar(100))

begin	
		select s.ID, s.skill_name, sc.skill_cnt from skill_counts as sc
			inner join skill s 
				on s.id = sc.skill_id
			inner join category c
				on s.CAT_ID = c.id
			where (isnull(skillid) or s.id = skillID)
				and (isnull(skillName) or s.skill_name = skillName)
                and (isnull(catg) or c.category_name = catg);		
end//


DELIMITER //

USE data_science//


drop procedure if exists sp_get_category//

create procedure sp_get_category (IN cat varchar(100))

begin
	if (cat = "")
	then select c.ID, c.CATEGORY_NAME from category as c;
    else
		select c.ID, c.CATEGORY_NAME from category as c
			where c.CATEGORY_NAME = cat;
	end if;
end//

drop procedure if exists sp_get_skill//

create procedure sp_get_skill (IN skillName varchar(100))

begin
	if (skillName = "")
	then select s.ID, s.CAT_ID, s.SKILL_NAME from skill as s;
    else
		select s.ID, s.CAT_ID, s.SKILL_NAME from skill as s
			where s.SKILL_NAME = skillName;
	end if;
end//

drop procedure if exists sp_get_skillByID//

create procedure sp_get_skillByID (IN skillID int(5))

begin	
		select s.ID, s.CAT_ID, s.SKILL_NAME from skill as s
			where s.id = skillID;	
end//

drop procedure if exists sp_get_skill_counts//

create procedure sp_get_skill_counts (IN skillID int(5),
									  IN skillName varchar(100),
                                      IN catg varchar(100))

begin	
		select s.ID, s.skill_name, sc.skill_cnt from skill_counts as sc
			inner join skill s 
				on s.id = sc.skill_id
			inner join category c
				on s.CAT_ID = c.id
			where (isnull(skillid) or s.id = skillID)
				and (isnull(skillName) or s.skill_name = skillName)
                and (isnull(catg) or c.category_name = catg);		
end//
















