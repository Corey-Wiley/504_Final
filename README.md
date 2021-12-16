# 504_Final
HHA 504 Final Assignment

1.Using Microsoft Azure create and deploy 2 virtual machines, give them 2 
different distinguishable names (ex. Master/Slave) – use Ubuntu Server 20.04 
LTS -Gen2, create both virtual machines with a user name and password with port 
22 open

2.After creating and deploying both machines, create a new inbound port rule 
so that they are both MYSQL compatible (port 3306)

3.In your computer terminal connect to both virtual machines in two different 
tabs using the following command – [ssh username@IPaddress] 
(ex. ‘corey@12.34.56.78’), when prompted say yes and enter the password

4.Update both virtual machines with the following command – 
[sudo apt – get update]

5.Install MYSQL on both virtual machines using the following command – 
[sudo apt install mysql – server mysql – client], once installed open MYSQL 
with the following command – [sudo mysql]

6.On the first virtual machine create a user name for MYSQL using the 
following command – [create user ‘dba’@’%’ indentified by ‘ahi2021’] 
(in this example the user name is ‘dba’ and the password is ‘ahi2021’)

7.Grant the new user privileges with the following command – 
[grant all privileges on *.* to 'dba'@'%' with grant option]

8.Create a new database in MYSQL named e2e with the following command – [
create database e2e], confirm it was created with the following command – [show databases]

9.Using a jupyter notebook connect to MYSQL via the first virtual machine that 
was created (refer to script 'fludata.py' found within repo)

10.After connecting to MYSQL via a jupyter notebook, upload a dataset into our 
MYSQL database code (refer to script 'fludata.py' found within repo) 

11.After most likely receiving an error message, go back to the terminal and 
update the configuration settings within MYSQL on the first virtual machine with 
the following command – [sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf], update 
the bind address to 0.0.0.0, server id to 1, log_bin to ‘/var/log/mysql/mysql-bin.log’, 
binlog_do_db to ‘e2e’, then save using CTRL+O and exit using CTRL+X

12.Restart MYSQL within the first virtual machine with the following command – 
[/etc/init.d/mysql restart], then go back into jupyter notebook and re-run the 
codes from step 9 & 10

13.Confirm the fludata table was inserted into the MYSQL database with the 
following commands in order [show databases; , use e2e; , show tables;], 
fludata should be there

14.On the first virtual machine create a dump or backup file of the database 
using the following command – [sudo mysqldump e2e > e2e.sql] , then restart 
MYSQL with the command – [sudo service mysql restart]

15.Jump back into mysql with the command [sudo mysql] and grant replication 
privileges with the following command – 
[grant replication slave on *.* to 'replica_user'@'%' identified by 'replica_user';], 
which is essentially saying give this user named ‘replica_user’ slave privileges, 
then use the command [flush privileges] to confirm

16.Use the following commands to confirm the database and table are properly 
configured – [use e2e; , flush tables with read lock;]

17.Using SCP (secure copy paste) on the first virtual machine, send the database 
over to the second virtual machine we created using the following command 
[scp e2e.sql, user@ipaddress: /home/user]

18.Confirm the file was sent to the second virtual machine by logging back into 
MYSQL with the ‘replica_user’ username and password and then using the following 
commands – [show databases; , use e2e; , show tables;]

19.Create a trigger within the table ‘fludata’ using SQL Workbench 
(refer to script 'h1ni_trigger' within repo)
 
20.Confirm the trigger was created with the following query within 
SQL Workbench – [show triggers;]

