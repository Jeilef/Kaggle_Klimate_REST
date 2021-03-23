DROP SCHEMA IF EXISTS temperatures;
CREATE SCHEMA temperatures;
USE temperatures;
CREATE TABLE GlobalLandTemperatureByCity(
    dt DATE,
    AverageTemperature FLOAT,
    AverageTemperatureUncertainty FLOAT,
    city VARCHAR(64),
    country VARCHAR(64),
    latitude VARCHAR(16),
    longitude VARCHAR(16),
    KEY (dt, city)
);
CREATE Or replace USER temperatureapp IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON * TO temperatureapp;
LOAD DATA LOCAL INFILE 'app/src/db/GlobalLandTemperaturesByCity.csv'
INTO TABLE GlobalLandTemperatureByCity fields terminated by ',' LINES TERMINATED BY '\r'