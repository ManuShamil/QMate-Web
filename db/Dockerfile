FROM mysql

WORKDIR .

COPY database.sql ./

RUN service mysqld start

RUN mysql -u root -p${MYSQL_ROOT_PASSWORD} < database.sql
