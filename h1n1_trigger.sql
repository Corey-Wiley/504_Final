use e2e;
select * from fludata;

delimiter $$
create trigger h1n1_concern_trigger before insert on fludata
for each row 
begin
if new.h1n1_concern > 3 then
signal sqlstate '45000'
set message_text = 'H1N1 concern should be a numerical value between 0 and 3. Please try again.'
end if;
end; 
$$
delimiter;

show triggers;
