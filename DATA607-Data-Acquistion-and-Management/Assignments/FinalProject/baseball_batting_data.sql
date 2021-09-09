use stats;
select b.playerID, b.yearID, b.teamID, b.G, b.AB, b.R, b.H, b.2B, b.3B, b.HR, b.RBI, b.SB, b.CS, b.BB, b.SO, m.nameFirst, m.nameLast, m.nameGiven, m.bats, m.throws, m.debut, m.finalGame
from batting b inner join stats.master m
on b.playerID = m.playerID;