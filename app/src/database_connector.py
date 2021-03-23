import mysql.connector as con


class DatabaseConnector:
    def __init__(self):
        self.con = con.connect(host="localhost",
                               port="3306",
                               user="root",
                               password="1234",
                               database="temperatures")

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

    def topNTemperaturesForCity(self, city, number_of_results):
        cursor = self.con.cursor()
        sql = f"""SELECT *
                FROM GlobalLandTemperatureByCity    
                WHERE city LIKE "{city}" 
                ORDER BY AverageTemperature DESC
                LIMIT {number_of_results}  """
        cursor.execute(sql)
        return cursor.fetchall()
