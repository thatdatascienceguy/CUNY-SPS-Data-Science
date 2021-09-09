## bunch of helper functions to call procs to insert and retrieve rows from "data_science" db


#install.packages("RMySQL")
if (!require('RMySQL')) install.packages('RMySQL')
library('RMySQL')
library(stringr)

db_name <- 'data_science_wordver'


getDBConn <- function()
{
    db <- dbDriver("MySQL")

    dbConn <-dbConnect(db, user='root',password='boysqljh368',dbname= db_name,
                       host ='127.0.0.1')
    return(dbConn)
}


#if catName is "", then return all categories and ids
getCategorys <-function(catName)
{
    con <- getDBConn()
    cats <- dbGetQuery(con, str_c("CALL sp_get_category('", catName, "')"))
    dbDisconnect(con)
    return(cats)
}


#if skillName is "", then return all skills and ids

#skill can be skill id or skillname
getSkills <-function(skill)
{
    con <- getDBConn()
    if(is.numeric(skill))
    {
        skills <- dbGetQuery(con, str_c("CALL sp_get_skillByID('", skill, "')"))
    }
    else
    {
        skills <- dbGetQuery(con, str_c("CALL sp_get_skill('", skill, "')"))
    }
    dbDisconnect(con)
    return(skills)
}


#pass in skillID, skillName (one or other in skill param) or catg
#if "" passed into both variables, all skillcounts returned
getSkillCounts <- function(skill, catg)
{
    con <- getDBConn()
    
    if(is.numeric(skill))
    {
        if(catg == '')
        {
            skills <- dbGetQuery(con, str_c("CALL sp_get_skill_counts(", skill, ", null, null)"))
        }
        else
        {
            skills <- dbGetQuery(con, str_c("CALL sp_get_skill_counts(", skill, ", null, '", catg, "')"))
        }
        
    }
    else if (skill != "")
    {
        if(catg == '')
        {
            skills <- dbGetQuery(con, str_c("CALL sp_get_skill_counts(null, '", skill, "', null)"))
        }
        else
        {
            skills <- dbGetQuery(con, str_c("CALL sp_get_skill_counts(null, '", skill, "', '", catg, "')"))
        }
    }
    else
    {
        skills <- dbGetQuery(con, "CALL sp_get_skill_counts(null, null, null)")
    }
    
    
    dbDisconnect(con)
    return(skills)
    
}


insCategoryDB <-function(catg)
{
    con <- getDBConn()
    dbGetQuery(con, str_c("CALL sp_insert_category ('", catg, "');"))
    dbDisconnect(con)
}

insSkillCatDB <- function(skill, catg)
{
    con <- getDBConn()
    dbGetQuery(con, str_c("CALL sp_insert_skill ('", skill, "', '", catg, "');"))
    dbDisconnect(con)
    return()
}

insSkillNoCatDB <- function(skill)
{
    con <- getDBConn()
    dbGetQuery(con, str_c("CALL sp_insert_skill ('", skill, "', '' );"))
    dbDisconnect(con)
    return()
}



insTransactionByNameDB <- function(skillName)
{
    
    con <- getDBConn()
    if(as.character(getSkills(skillName)[3]) != toupper(skillName))
    {
        return(FALSE)
    }
    else
    {
        dbGetQuery(con, str_c("CALL sp_insert_transaction_by_name ('", skillName, "');"))   
        dbDisconnect(con)
        return(TRUE)
    }
}

insTransactionByIdDB <- function(skillID)
{
    con <- getDBConn()
    if(as.character(getSkills(skillID)[1]) != skillID)  ##can't insert a skill, that doesn't yet exist, don't know catg
    {
        return(FALSE)
    }
    dbGetQuery(con, str_c("CALL sp_insert_transaction_by_id (", skillID, ");"))   
    dbDisconnect(con)
    return(TRUE)
}

#this inserts a transaction with skill and catg, 
#NOTE, skill and catg do not need to yet exist, they will be inserted as needed
insTransactionByNameCatDB <- function(skill, catg)
{
    
    con <- getDBConn()
    if(as.character(toupper(getCategorys(catg)[2])) != toupper(catg))
    {
        insCategoryDB(catg)
    }
    if(as.character(toupper(getSkills(skill)[3])) != toupper(skill))
    {
        insSkillDB(skill, catg)
    }
    insTransactionByNameDB(skill)

}

upsertSkillCount <- function(skill, sCount)
{
    con <- getDBConn()
    dbGetQuery(con, str_c("CALL sp_upsert_skill_counts ('", skill, "',", sCount, ");"))   
    dbDisconnect(con)
}






