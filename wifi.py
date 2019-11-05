import config
import network
import time


def connect_to_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('[WIFI] connecting to {}..'.format(config.wifi_ssid), end='')
        sta_if.active(True)
        sta_if.ifconfig((config.ip, '255.255.255.0', config.router, config.router))
        sta_if.connect(config.wifi_ssid, config.wifi_password)
        while not sta_if.isconnected():
            print('.', end='')
            time.sleep(1)
        else:
            print('\n[WIFI] Connected!')
            print('[WIFI] IP: {}'.format(sta_if.ifconfig()[0]))
