DELIMITER //

USE data_science//


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
				  where c.ID = c_id
					and S.skill_name = s_name)						
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


