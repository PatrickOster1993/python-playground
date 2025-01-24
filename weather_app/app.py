from flask import Flask, render_template, request
from weather_client import WeatherClient

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    client = WeatherClient()
    
    try:
        client.fetch_data(city)
        return render_template('results.html', 
                            city=city,
                            data=client.data_dict,
                            plot=client.generate_plot())
    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)