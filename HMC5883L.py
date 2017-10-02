import smbus
import math
import os
import re

class HMC5883L:
	#constructor
	def __init__(self):
		self.bus = smbus.SMBus(1)
		self.address = 0x1e

		self.write_byte(0, 0b01110000) # Rate: 8 samples @ 15Hz
		self.write_byte(1, 0b11100000) # Sensor field range: 8.1 Ga
		self.write_byte(2, 0b00000000) # Mode: continuous sampling

	def getSensorData(self):
		data = self.read_data()
		x = self.convert(data, 3) # x
		y = self.convert(data, 7) # y
		z = self.convert(data, 5) # z

		return x,y,z

	# Read block data from HMC5883
	def read_data(self):
  		return self.bus.read_i2c_block_data(self.address, 0x00)

	# Convert val to signed value
	def twos_complement(self, val, len):
  		if (val & (1 << len - 1)):
    			val = val - (1<<len)
  		return val

	# Convert two bytes from data starting at offset to signed word
	def convert(self, data, offset):
  		return self.twos_complement(data[offset] << 8 | data[offset+1], 16)

	# Write one byte to HMC5883
	def write_byte(self, adr, value):
  		self.bus.write_byte_data(self.address, adr, value)


