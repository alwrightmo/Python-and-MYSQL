@echo off
echo Do you have the mysql-connector-python package installed?
set /p input=Enter y or n: 
If /I "%input%"=="n" goto n
if /I "%input%"=="y" goto y
:n
cd %~dp0
cd redistributables
start mysql-connector-python-8.0.24-windows-x86-64bit.msi
pause
cd %~dp0
:y

echo If the program crashes after this point you need to install python
echo 3.9.X to its default file location then reinstall the connector, 
echo or set a path variable to the mysql server bin folder
pause

set /p password=Enter password for root user: 
mysql -uroot -p%password% -e "CREATE DATABASE IF NOT EXISTS freshPrints"
mysql -uroot -p%password% freshPrints < freshPrints.sql
python freshPrints.py
mysqldump -uroot -p%password% freshPrints > freshPrints.sql
pause

