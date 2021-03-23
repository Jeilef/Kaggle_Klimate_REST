import unittest

from database_connector import DatabaseConnector


class TestDatabaseConnector(unittest.TestCase):
    def setUp(self) -> None:
        self.db = DatabaseConnector()

    def testUpdate(self):
        self.db.updateTemperatureForCityAndDate("Zwolle", "1783-10-01", 2, 5)

    def testTopTempleratures(self):
        results = self.db.topNTemperaturesForCity("Zwolle", 10)
        print(results)
