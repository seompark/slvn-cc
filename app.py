from flask import Flask, jsonify, request
from sds011 import SDS011
from adafruit_dht import DHT22
import board
import os

dust_sensor = SDS011(os.environ['SDS011_SERIAL_PORT'])
dht = DHT22(board.D18)

app = Flask(__name__)
dust_sensor.sleep(sleep=False)

@app.route('/', methods=['GET'])
def status():
  dust = dust_sensor.query()
  return jsonify({
    'temperature': dht.temperature,
    'humidity': dht.humidity,
    'pm10': dust[0],
    'pm2.5': dust[1]
  })

if __name__ == '__main__':
  app.run(debug=True)
