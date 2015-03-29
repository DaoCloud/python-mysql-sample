This sample demonstrates how to setup continuous integration for a Python+MySQL project.

This sample is built for DaoCloud, a docker based continuous integration and deployment platform.

## Default DB Connection
# MYSQL_USERNAME=root
# MYSQL_PASSWORD # empty string
# MYSQL_PORT_3306_TCP_ADDR=localhost
# MYSQL_PORT_3306_TCP_PORT=3306
# MYSQL_INSTANCE_NAME=daocloud

## Run Container
docker run --link your_mysql:mysql -p 3000:3000 python-mysql-sample
