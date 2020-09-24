from network import WLAN
import time
import utime
import pycom
from pysense import Pysense
from MPL3115A2 import MPL3115A2, ALTITUDE
from machine import RTC
import machine

wlan = WLAN(mode=WLAN.STA)

nets = wlan.scan()
for net in nets:
    if net.ssid == 'aaaa':
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, 'yoyoyoyo'), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        break
"""
rtc = RTC()
print(rtc.now())
rtc.ntp_sync("https://www.impots.gouv.fr/portail/")
print(rtc.now())
#connexion au serveur pour mise a jour de l'heure
"""
"""
rtc.ntp_sync("pool.ntp.org")

rtc = RTC()
rtc.init((2014, 5, 1, 4, 13, 0, 0, 0))
print(rtc.now())

print(rtc.now())
# setup as a station
"""

"""
print("yo")
wlan = network.WLAN(mode=network.WLAN.STA)
wlan.connect('We need the Fi', auth=(network.WLAN.WPA2, 'ricardoo'))
while not wlan.isconnected():
    time.sleep_ms(50)
print(wlan.ifconfig())
"""

"""
voila comment récupérer l'altitude
py = Pysense()
mp = MPL3115A2(py, mode=ALTITUDE)

for i in range(100):
    print(str(now())+ str(mp.altitude()))
    utime.sleep(1)
"""

#test connection
# une connexion aété effextuée :


#si connecté

#si pas connecté


# now use socket as usual
