import network
import time
import utime
from pysense import Pysense
from MPL3115A2 import MPL3115A2, ALTITUDE
from machine import RTC

rtc = RTC()
print(rtc.now())
# setup as a station
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
#une connexion aété effextuée :


#si connecté

#si pas connecté


# now use socket as usual
