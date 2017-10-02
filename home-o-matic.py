from threading import Thread
import Weather
import GasCounter

#this will be the home-o-matic master
if __name__ == "__main__":
	print "Initializing..."
	#gas
	print "HMC5883L GasCounter..."
    	gasCounter = GasCounter.GasCounter(22519.36)
	print "Starting loop..."
	gasCounterThread = Thread(target = gasCounter.loop)
	gasCounterThread.start()
	print "done!"	

	#weather
    	print "TemperatureFetcher..."
	weather = Weather.TemperatureFetcher(3)
	print "Starting loop..."
	weatherThread = Thread(target = weather.loop)
    	weatherThread.start()
	print "done!"

	gasCounterThread.join()
	weatherThread.join()

