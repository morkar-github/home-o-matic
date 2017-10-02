import HMC5883L
import GasCounterDAO
import time

class GasCounter:
    def __init__(self, counterValue):
        self.hmc5883l = HMC5883L.HMC5883L()
        self.database = GasCounterDAO.GasCounterDAO()
        self.counterValue = counterValue # initial value
        self.threshold = 600
        self.thresholdHysteresis = 100
        self.step = 0.01 # Amount to increase the counter at each trigger event
        
    def loop(self):
        state = 0 # initial state
        timestamp = time.time()
                
        while(1 == 1):
        	oldState = state
                x,y,z = self.hmc5883l.getSensorData()
                self.database.saveSensorData(x, y, z)
                           
                magnitude = x # currently, we only use x
                                
                if magnitude > self.threshold + self.thresholdHysteresis:
                    state = 1
                elif magnitude < self.threshold - self.thresholdHysteresis:
                    state = 0
                                                
                if oldState == 0 and state == 1: # detected
                    self.counterValue += self.step
                    self.database.saveGasConsumption(self.step)
                    self.database.saveGasCounterValue(self.counterValue)
                    timestamp = time.time()
                elif time.time() - timestamp > 3600: #at least one update per hour
                    self.database.saveGasCounterValue(self.counterValue)
                    timestamp = time.time()
                                                                        
                    time.sleep(1)
