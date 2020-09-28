import time
import utime
import pycom
from pysense import Pysense
from MPL3115A2 import MPL3115A2, ALTITUDE
from machine import RTC
import machine
import ntptime
from mqtt import MQTTClient
from network import WLAN


wlan = WLAN(mode=WLAN.STA)

print("start")
nets = wlan.scan()
print("les nets: " + str(nets))
for net in nets:
    if net.ssid == 'AndroidAP4979':
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, 'e2810218cd5d'), timeout=5000)
        while not wlan.isconnected():
            utime.sleep(3)
        print('WLAN connection succeeded!')
        break
Org_Id = "t8jaol"
client = MQTTClient("d:"+Org_Id+":Pycom:123456", Org_Id +".messaging.internetofthings.ibmcloud.com",user="use-token-auth", password="Co_q7SzBQgSDO1Y-gW", port=1883)

client.connect()
print("Connected to Watson IoT!")

while True:
     print("Sending ON")
     client.publish(topic="iot-2/evt/status/fmt/json", msg="{\"d\":\"ON\"}")
     time.sleep(10)
     print("Sending OFF")
     client.publish(topic="iot-2/evt/status/fmt/json", msg="{\"d\":\"OFF\"}")
     time.sleep(10)



"""from network import WLAN
import time
import utime
import pycom
from pysense import Pysense
from MPL3115A2 import MPL3115A2, ALTITUDE
from machine import RTC
import machine
import ntptime

wlan = WLAN(mode=WLAN.STA)

print("start")
nets = wlan.scan()
print("les nets: " + str(nets))
for net in nets:
    if net.ssid == 'AndroidAP4979':
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, 'e2810218cd5d'), timeout=5000)
        while not wlan.isconnected():
            utime.sleep(3)
        print('WLAN connection succeeded!')
        break
rtc = RTC()
t = ntptime.time()
tm = utime.gmtime(t)
rtc.init((tm[0]+30, tm[1]-1, tm[2], tm[6] , tm[3]+2 , tm[4], tm[5], 0))
py = Pysense()

mp = MPL3115A2(py, mode=ALTITUDE)

r = rtc.now()
print("le "+str(r[2])+"/"+str(r[1])+"/"+str(r[0]) +" a " + str(r[4]) +"h"+str(r[5])+" a l'altitude " + str(mp.altitude()))

"""










"""
rtc = RTC()
print(rtc.now())
rtc.ntp_sync("https://www.impots.gouv.fr/portail/")
print(rtc.now())

wlan.disconnect()
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
