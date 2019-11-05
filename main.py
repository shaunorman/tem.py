import config
import dht
import json
import machine

from time import sleep
from umqtt.simple import MQTTClient
from wifi import connect_to_wifi

sensor = dht.DHT22(machine.Pin(5))

while True:
    connect_to_wifi()

    sensor.measure()
    payload = json.dumps({
        'temp': sensor.temperature(),
        'humidity': sensor.humidity()
    })

    client = MQTTClient('client.{}'.format(config.ip), config.server)
    client.connect()
    client.publish('/temp/test', payload)
    print('[MQTT] /temp/test: {}'.format(payload))

    # Wait another 5 minutes before sending the temp again.
    sleep(300)
