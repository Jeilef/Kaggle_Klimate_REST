from flask import Flask, render_template, request
import datetime

from database_connector import DatabaseConnector

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_home():
    print("get home")
    top_cities = []
    bottom_cities = []
    if request.method == 'POST':
        print("received post")
        print(request.form)
        db = DatabaseConnector()
        if 'new-city' in request.form.keys():
            create_entry(db)

        if 'selected-city' in request.form.keys():
            update_entry(db)

        if 'num-results' in request.form.keys():
            fetch_results(bottom_cities, db, top_cities)

    return render_template('home.html', top_cities=top_cities, bottom_cities=bottom_cities)


def fetch_results(bottom_cities, db, top_cities):
    num_results = request.form['num-results']
    from_date = request.form['from-date']
    to_date = request.form['to-date']
    if not num_results:
        num_results = 5
    if not to_date:
        to_date = datetime.date.today()
    # fetch top temperatures
    result = db.topNTemperaturesForCity(num_results, from_date, to_date)
    for row in result:
        top_cities.append(serialize_row(row))
    # fetch lowest temperatures
    result_low = db.bottomNTemperaturesForCity(num_results, from_date, to_date)
    for row in result_low:
        bottom_cities.append(serialize_row(row))


def update_entry(db):
    city = request.form['selected-city']
    date = datetime.date.fromisoformat(request.form['selected-date'])
    temperature = request.form['average-temp']
    uncertainty = request.form['average-uncertainty']
    db.updateTemperatureForCityAndDate(city, date, temperature, uncertainty)


def create_entry(db):
    city = request.form['new-city']
    date = request.form['new-date']
    temp = request.form['new-temp']
    uncertainty = request.form['new-average-uncertainty']
    country = request.form['new-country']
    lat = request.form['new-lat']
    lon = request.form['new-lon']
    db.createNewEntry(date, temp, uncertainty, city, country, lat, lon)


def serialize_row(row):
    serialized_row = [f"{row[0].day}.{row[0].month}.{row[0].year}"]
    serialized_row.extend(row[1:])
    return serialized_row


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
