FROM mysql

WORKDIR .

COPY database.sql ./

RUN mysql -u root -p${MYSQL_ROOT_PASSWORD} < database.sql
