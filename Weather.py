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
