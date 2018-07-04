create database if not exists  simple;

use simple;

create table tb_user (
	user_id BIGINT AUTO_INCREMENT,
	user_username VARCHAR(500) NULL,
	user_password VARCHAR(500) NULL,
	PRIMARY KEY (user_id)
);

delimiter //
create procedure sp_createUser(
in p_username varchar(500),
in p_password varchar(500)
)
begin
	if (select exists (select * from tb_user where user_username = p_username) ) then
		select 'Username Exists !!';
	else
		insert into tb_user (user_username, user_password) values (p_username, p_password);
	end if;
end//

delimiter ;

