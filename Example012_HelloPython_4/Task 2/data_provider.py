from random import randint as rnd

def get_temperature(sensor):
    return rnd(-20, 0) if sensor else rnd(0, 20)

def get_pressure(sensor):
    if sensor:
        return rnd(720, 750)
    else:
        return rnd(750, 770)

def get_wind_speed(sensor):
    if sensor == 1:
        return rnd(0,30)
    else:
        return rnd(30,50)
    
def data_collection(sensor = 1):
    return (get_temperature(sensor), get_pressure(sensor), get_wind_speed(sensor))
