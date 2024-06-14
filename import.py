import psycopg2
import os
import fileinput
import mysql.connector

# Підключення до бази даних
conn = psycopg2.connect(
    host="localhost",
    database="db_lab3_",
    user="yakimov",
    password="1029nRiEg3847",
    port="5432"
)
cur = conn.cursor()

# Виконання команди COPY
with open('import.csv', 'w') as f:
    cur.copy_expert("COPY weather TO STDOUT WITH CSV HEADER", f)

# Закриття з'єднання
cur.close()
conn.close()

os.system("liquibase --url=jdbc:postgresql://localhost:5432/db_lab3_ --username=yakimov --password=1029nRiEg3847 --driver=org.postgresql.Driver --changeLogFile=changelog-liquibase.xml generateChangeLog")

id_ = []

with open("changelog-liquibase.xml", "r") as f:
    filedata = f.read()
    id_ = filedata.split("\n")
    id_ = id_[2]

filedata = filedata.replace('MY_ENUM', "ENUM ('S', 'WSW', 'NNW', 'W', 'N', 'SSE', 'SW', 'ENE', 'WNW', 'NW', 'SSW', 'E', 'SE', 'NNE', 'ESE', 'NE')")
filedata = filedata.replace('<column name="last_updated" type="TIMESTAMP WITHOUT TIME ZONE">', '<column name="last_updated" type="DATETIME DEFAULT \'0000-00-00 00:00\'">')

with open('changelog-liquibase.xml', 'w') as file:
    file.write(filedata)

lines = []

with open("changelog-import.xml", "r") as f:
    filedata = f.read()
    lines = filedata.split("\n")
    lines = lines[2]

filedata = filedata.replace(lines, id_)

with open('changelog-import.xml', 'w') as file:
    file.write(filedata)

os.system("liquibase --url=jdbc:mysql://localhost:3306/new_schema --username=yayak --password=1432mWeO8567 --driver=com.mysql.cj.jdbc.Driver --changeLogFile=changelog-liquibase.xml update")

os.system("liquibase --url=jdbc:mysql://localhost:3306/new_schema --username=yayak --password=1432mWeO8567 --driver=com.mysql.cj.jdbc.Driver --changeLogFile=changelog-import.xml update")
