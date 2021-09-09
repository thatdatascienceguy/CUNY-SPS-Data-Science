/* Create Data Science database */
DROP DATABASE if exists data_science;

CREATE DATABASE data_science;
/* Use Data Science database */
USE data_science;

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



/* Insert Transactions in data_science.transactions table */
INSERT INTO transactions (SKILL_ID, TX_DATE) values (1, STR_TO_DATE('10/15/2016', '%m/%d/%Y'));
INSERT INTO transactions (SKILL_ID, TX_DATE) values (1, STR_TO_DATE('10/16/2016', '%m/%d/%Y'));





