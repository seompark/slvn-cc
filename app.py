from flask import Flask, jsonify, request, render_template
from sds011 import SDS011
import os
import time

# dust_sensor = SDS011('COM7')

app = Flask(__name__)
# dust_sensor.sleep(sleep=False)


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/api', methods=['GET'])
def status():
   # dust = dust_sensor.query()
    dust = ['45', '59']
    return jsonify({
        'pm10': dust[0],
        'pm25': dust[1]
    })


if __name__ == '__main__':
    app.run(debug=True)
