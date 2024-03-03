RainSum = 0
radio.set_group(49)
weatherbit.start_wind_monitoring()
weatherbit.start_rain_monitoring()
ResetCount = 0

def on_forever():
    global ResetCount, RainSum
    weatherbit.start_weather_monitoring()
    radio.send_value("TempC", weatherbit.temperature())
    basic.pause(200)
    radio.send_value("Humidity", weatherbit.humidity())
    basic.pause(200)
    radio.send_value("Pressure", weatherbit.pressure())
    basic.pause(200)
    radio.send_value("Rain", weatherbit.rain())
    basic.pause(200)
    radio.send_value("WindSpeed", weatherbit.wind_speed())
    basic.pause(200)
    if weatherbit.wind_direction() == "N":
        radio.send_value("WindDir", 1)
    elif weatherbit.wind_direction() == "NE":
        radio.send_value("WindDir", 2)
    elif weatherbit.wind_direction() == "E":
        radio.send_value("WindDir", 3)
    elif weatherbit.wind_direction() == "SE":
        radio.send_value("WindDir", 4)
    elif weatherbit.wind_direction() == "S":
        radio.send_value("WindDir", 5)
    elif weatherbit.wind_direction() == "SW":
        radio.send_value("WindDir", 6)
    elif weatherbit.wind_direction() == "W":
        radio.send_value("WindDir", 7)
    elif weatherbit.wind_direction() == "NW":
        radio.send_value("WindDir", 8)
    else:
        radio.send_value("WindDir", 0)
    ResetCount += 1
    if RainSum == 10:
        pass
    RainSum = weatherbit.rain()
    basic.pause(60000)
basic.forever(on_forever)
