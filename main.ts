let RainSum = 0
let ResetCount = 0
radio.setGroup(49)
basic.forever(function () {
    radio.sendValue("TempC", 0)
    basic.pause(200)
    radio.sendValue("Humidity", 0)
    basic.pause(200)
    radio.sendValue("Pressure", 0)
    basic.pause(200)
    radio.sendValue("Rain", 0)
    basic.pause(200)
    radio.sendValue("WindSpeed", 0)
    basic.pause(200)
    if ((0 as any) == ("N" as any)) {
        radio.sendValue("WindDir", 1)
    } else if ((0 as any) == ("NE" as any)) {
        radio.sendValue("WindDir", 2)
    } else if ((0 as any) == ("E" as any)) {
        radio.sendValue("WindDir", 3)
    } else if ((0 as any) == ("SE" as any)) {
        radio.sendValue("WindDir", 4)
    } else if ((0 as any) == ("S" as any)) {
        radio.sendValue("WindDir", 5)
    } else if ((0 as any) == ("SW" as any)) {
        radio.sendValue("WindDir", 6)
    } else if ((0 as any) == ("W" as any)) {
        radio.sendValue("WindDir", 7)
    } else if ((0 as any) == ("NW" as any)) {
        radio.sendValue("WindDir", 8)
    } else {
        radio.sendValue("WindDir", 0)
    }
    ResetCount += 1
    if (RainSum == 10) {
    	
    }
    RainSum = 0
    basic.pause(60000)
})
