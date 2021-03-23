from flask import Flask, render_template, request
import datetime

from database_connector import DatabaseConnector

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_home():
    print("get home")
    top_cities = []
    if request.method == 'POST':
        print("received post")
        print(request.form)
        db = DatabaseConnector()
        if 'selected-city' in request.form.keys():
            city = request.form['selected-city']
            date = datetime.date.fromisoformat(request.form['selected-date'])
            temperature = request.form['average-temp']
            uncertainty = request.form['average-uncertainty']
            db.updateTemperatureForCityAndDate(city, date, temperature, uncertainty)

        if 'selected-city2' in request.form.keys():
            city = request.form['selected-city2']
            num_results = request.form['num_results']
            top_cities = db.topNTemperaturesForCity(city, num_results)

    return render_template('home.html', top_cities=top_cities)


if __name__ == '__main__':
    print("now")
    app.run(host="0.0.0.0", port=5000, debug=True)
