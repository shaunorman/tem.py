# tem.py
Micropython temperature station.

Considering I develop in Python for my every day job I thought I should try micropython instead of doing all my work in Arduino's version of C.

Basically, this was to see how I could creata a basic IoT device which
1. Connected to wifi.
2. Read in the temperature and humidity from the DHT22 sensor
3. Posted it to the MQTT server.
4. repeat!

Seems it was quite easy once I got the hang of the process of uploading your project to the device using [mpfshell.](https://github.com/wendlers/mpfshell)


One of the things I love about the micropython base is the amount of modules built into it as standard making things a lot easier. Plus, the ability to get a REPL prompt either via USB or the [web](http://micropython.org/webrepl/).
