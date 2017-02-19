from flask import Flask
from pyA20.gpio import gpio
from pyA20.gpio import port

app = Flask(__name__)

led = port.PA12
gpio.init()
gpio.setcfg(led, gpio.OUTPUT)

@app.route('/hello')
def hello():
	gpio.output(led, 1)
	return 'Hello Orange Pi Zero!'

@app.route('/bye')
def bye():
	gpio.output(led, 0)
	return 'Bye Bye!'

app.run(host='0.0.0.0', port=80)

