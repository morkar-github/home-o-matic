#this will be the home-o-matic master


def main():
    #initialize database

    #initialize gascounter
    GasCounter gasCounter(gasDAO)

    #initialize weather sensor
    OpenWeather openWeather(weatherDAO)
