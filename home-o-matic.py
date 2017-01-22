#this will be the home-o-matic master

import smbus
import math
import os
import re

class HMC5883L:

	#constructor
	def __init__(self):
		self.bus = smbus.SMBus(1)
		self.address = 0x1e

		write_byte(0, 0b01110000) # Rate: 8 samples @ 15Hz
		write_byte(1, 0b11100000) # Sensor field range: 8.1 Ga
		write_byte(2, 0b00000000) # Mode: continuous sampling

	def getSensorData(self):
		data = read_data()
		x = convert(data, 3) # x
		y = convert(data, 7) # y
		z = convert(data, 5) # z

		return x,y,z

	# Read block data from HMC5883
	def read_data():
  		return bus.read_i2c_block_data(address, 0x00)

	# Convert val to signed value
	def twos_complement(val, len):
  		if (val & (1 << len - 1)):
    		val = val - (1<<len)
  		return val

	# Convert two bytes from data starting at offset to signed word
	def convert(data, offset):
  		return twos_complement(data[offset] << 8 | data[offset+1], 16)

	# Write one byte to HMC5883
	def write_byte(adr, value):
  		bus.write_byte_data(address, adr, value)


from influxdb import InfluxDBClient
import HMC5883L
import time

class GasCounterDAO:
	def __init__(self):
		self._gasData 		= InfluxDBClient(database="gas")
		self._sensorData	= InfluxDBClient(database="GasMagnetometer") 

	def saveSensorData(self, x, y, z):
    	json = 
    	[
      		{
      			"measurement": "magnetometer",
        		"fields": 
        		{
           			"x": float(bx),
                    "y": float(by),
                    "z": float(bz)
        		}
    		}
    	]
    
    	_sensorData.write_points(json)

    def saveGasConsumption(self, value):
    	json = 
    	[
    		{
        		"measurement": "consumption",
        		"fields": 
        		{
            		"value": float(value)
        		}
    		}
		]

		_gasData.write_points(json)

	def saveGasCounterValue(self, value):
      json = 
      [
      		{
      			"measurement": "counter",
        		"fields": 
        		{
           			"value": float(value)
        		}
    		}
      ]

      _gasData.write_points(json)

import HMC5883L
import GasCounterDAO

class GasCounter:
	def __init__(self, counterValue):
		self.hmc5883l = HMC5883L()
		self.database = GasCounterDAO()
		self.counterValue = counterValue # initial value
		self.threshold = 600
		self.thresholdHysteresis = 100
		self.step = 0.01 # Amount to increase the counter at each trigger event
	
	def loop(self):
		state = 0 # initial state
		timestamp = time.time()

		while(1 == 1):
			 oldState = state
			 x,y,z = hmc5883l.getSensorData()
			 database.saveSensorData(x, y, z)

			 magnitude = x # currently, we only use x

			 if magnitude > threshold + thresholdHysteresis:
			 	state = 1
			 elif magnitude < threshold - thresholdHysteresis:
			 	state = 0

			 if oldState == 0 and state == 1: # detected
			 	self.counterValue += self.step	
			 	database.saveGasConsumption(self.step)
				database.saveGasCounterValue(self.counterValue)  
  				timestamp = time.time()
  			elif time.time() - timestamp > 3600: #at least one update per hour
  				database.saveGasCounterValue(self.counterValue)
  				timestamp = time.time()

  			time.sleep(1)

class OpenWeather:
 	def __init__(self, apiKey):
 		self._apiKey = apiKey

 	def getTemperature():
 		response = requests.get('http://api.openweathermap.org/data/2.5/weather?id=2923544&units=metric&APPID=' + self._apiKey) #abcc6a6d692594e4c9524d7088d5184b
    	responseAsJson = response.json()
    	jsonNode = responseAsJson['main']
    	temperature     = float(jsonNode['temp'])
    	temperature_min = float(jsonNode['temp_min'])
    	temperature_max = float(jsonNode['temp_max']) 		

    	return temperature, temperature_min, temperature_max

from influxdb import InfluxDBClient

class WeatherDAO:
	def __init__(self):
		self._database = InfluxDBClient(database=databaseName)

	def saveTemperature(self, temperature, minimum, maximum):	
    	json = 
    	[
        	{
            	"measurement": "openweather",
            	"fields": 
            	{
                	"temperature": temperature,
                	"temperature_min": minimum,
                	"temperature_max": maximum
            	}
        	}
    	]
    	self._database.write_points(json)

class Weather:
	def __init__(self, updatesPerHour):
		self._updatesPerHour = updatesPerHour
		self._sensor = OpenWeather('abcc6a6d692594e4c9524d7088d5184b')
		self._dao = WeatherDAO()
		#nothing yet

 	def loop(self):
 		while(1 == 1):
 			try:
 				t, t_min, t_max = self._sensor.getTemperature()
 				self._dao.saveTemperature(t, t_min, t_max)
    			time.sleep(60*(60/self._updatesPerHour)) # get values twice per hour 
    		except Exception as unknownException:
				print unknownException.args
				print unknownException	

def __main__(self):
	#gas
	GasCounter gasCounter(counterValue)
	
	#weather
	Weather weather(3)


