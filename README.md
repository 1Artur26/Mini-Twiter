For the correct operation of the code, you need to install the following packages
Django 4.2.7
Pillow 10.1.0
pip 22.2.2
psycopg2-binary 2.9.9
To connect to the database, you need to create a database in Postgres with the following settings
'NAME': 'mini_twitter',
'USER': 'postgres',
'PASSWORD': 'qwerty1234',
'HOST': 'localhost',
'PORT': '5432'
or replace DATABASES settings in mini_twitter\mini_twitter\settings.py