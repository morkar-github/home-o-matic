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
