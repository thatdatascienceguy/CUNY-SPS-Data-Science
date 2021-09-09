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