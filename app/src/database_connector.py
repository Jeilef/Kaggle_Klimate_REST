import mysql.connector as con


class DatabaseConnector:
    def __init__(self):
        self.con = con.connect(host="localhost",
                               port="3306",
                               user="root",
                               password="1234",
                               database="temperatures")

    def createNewEntry(self, date, temp, uncertainty, city, country, lat, lon):
        cursor = self.con.cursor()
        if date and temp and uncertainty and city and country and lat and lon:
            sql = f"""INSERT INTO GlobalLandTemperatureByCity
                        VALUES ("{date}", "{temp}", "{uncertainty}", "{city}", "{country}", "{lat}", "{lon}")"""
            cursor.execute(sql)
            self.con.commit()

    def updateTemperatureForCityAndDate(self, city, date, average_temperature, average_uncertainty):
        cursor = self.con.cursor()
        if average_temperature:
            sql = f"""UPDATE GlobalLandTemperatureByCity
                    SET AverageTemperature = "{average_temperature}"
                    WHERE city LIKE "{city}"
                    AND dt = "{date}" """
            cursor.execute(sql)
            self.con.commit()

        if average_uncertainty:
            sql = f"""UPDATE GlobalLandTemperatureByCity
                        SET AverageTemperatureUncertainty = "{average_uncertainty}"
                        WHERE city LIKE "{city}"
                        AND dt = "{date}" """
            cursor.execute(sql)
            self.con.commit()

    def topNTemperaturesForCity(self,  number_of_results, from_date, to_date):
        cursor = self.con.cursor()
        sql = f"""SELECT *
                FROM GlobalLandTemperatureByCity    
                WHERE dt >= "{from_date}" AND dt <= "{to_date}"
                ORDER BY AverageTemperature DESC
                LIMIT {number_of_results}  """
        cursor.execute(sql)
        return cursor.fetchall()

    def bottomNTemperaturesForCity(self,  number_of_results, from_date, to_date):
        cursor = self.con.cursor()
        sql = f"""SELECT *
                FROM GlobalLandTemperatureByCity    
                WHERE dt >= "{from_date}" AND dt <= "{to_date}"
                ORDER BY AverageTemperature Asc
                LIMIT {number_of_results}  """
        cursor.execute(sql)
        return cursor.fetchall()
