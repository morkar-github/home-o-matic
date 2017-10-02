from influxdb import InfluxDBClient
import HMC5883L
import time

class GasCounterDAO:
    	def __init__(self):
        	self._gasData 		= InfluxDBClient(database="gas")
        	self._sensorData	= InfluxDBClient(database="GasMagnetometer")
        
	def saveSensorData(self, x, y, z):
        	json = [{"measurement": "magnetometer", "fields":{"x": float(x), "y": float(y), "z": float(z)}}]
        	self._sensorData.write_points(json)

	def saveGasConsumption(self, value):
    		json = [{"measurement": "consumption", "fields": {"value": float(value)}}]
		self._gasData.write_points(json)
         
        def saveGasCounterValue(self, value):
            	json = [{"measurement": "counter", "fields":{"value": float(value)}}]
		self._gasData.write_points(json)
