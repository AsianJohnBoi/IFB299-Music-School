Database: music_school
User: root
Password: ifb299

Requirements:
- mySQL with mySQLWorkbench installed (make sure user or root password is 'ifb299')
- Django 2.0.3
- Python 3.6
- mysqlclient

1) Create an SQL database through the terminal.

type: 'mysql -u root -p' then enter your password. Once accepted, type 'CREATE DATABASE music_school'

Type in 'show DATABASES;' to verify that the database called 'music_school has been included.

2) You will also need to import the database tables for the website to use. Open up a new terminal. Make sure you're in the music_school directory ('cd project_code/music_school') then type in 'python3 manage.py makemigrations' then 'python3 manage.py migrate'. If you are getting an error, make sure you have done step 1 correctly and music_school database has been created.

3) Double check that the tables have been made by opening up the music_school database in mySQLWorkbench. If there are no connections, add a new one.

Connection name: music_school
hostname: localhost
port: 3306
username: root
Leave everything else by default

4) Now you are ready to run the website. Type 'python3 manage.py runserver' in the terminal window then go on a web browser and type in the URL '127.0.0.1:8000/'

