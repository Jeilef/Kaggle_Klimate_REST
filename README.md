# Temperature Analysis

## Requirements
- A working Docker installation

## Starting application
1. Setup database `docker run --name temperaturedb -p 3306:3306 -e MYSQL_ROOT_PASSWORD=mypass -d mariadb/server:10.4`
2. Run `docker-compose -d up`

## Design Decisions
- MariaDB as a nice database with a clean available docker image