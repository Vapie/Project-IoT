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


print("start")


def push_data(list_histo_alti,altitude,date):
    if len(list_histo_alti)>0:
        push_histo_data(list_histo_alti)
    client.publish(topic="iot-2/evt/status/fmt/json", msg="{\"altitude\":\""+str(altitude)+"\",\"heure\":\""+"le "+str(date[2])+"/"+str(date[1])+"/"+str(date[0]) +" a " + str(date[4]) +"h"+str(date[5])+"\"}")

def push_histo_data(list_histo_alti):
    for historized_data in range():
        altitude = historized_data[0]
        date = historized_data[1]
        client.publish(topic="iot-2/evt/status/fmt/json", msg="{\"altitude\":\""+str(altitude)+"\",\"heure\":\""+"le "+str(date[2])+"/"+str(date[1])+"/"+str(date[0]) +" a " + str(date[4]) +"h"+str(date[5])+"\"}")

def try_to_connect(ssid,pass):
    nets = wlan.scan()
    #print("les nets: " + str(nets))
    for net in nets:
        if net.ssid == ssid:
            print('Network found!')
            wlan.connect(net.ssid, auth=(net.sec, pass), timeout=5000)
            for x in range(3)
                if not wlan.isconnected():
                    utime.sleep(3)
                else:
                    return try_to_sync_clock()
                    break
            return False

def add_data_to_histo(list_histo_alti,altitude,date):
    list_histo_alti.append[altitude,date]
    return list_histo_alti

def try_to_sync_clock():
    pass


clock_is_synced = False
wlan = WLAN(mode=WLAN.STA)
nets = wlan.scan()
clock_is_synced = try_to_connect('AndroidAP4979','e2810218cd5d')


py = Pysense()
rtc = RTC()
list_histo_alti = []

while True:
    altitude = MPL3115A2(py, mode=ALTITUDE).altitude()
    t = ntptime.time()
    tm = utime.gmtime(t)
    date = rtc.now()
    if wlan.connect() && not clock_is_synced:
        #on sync la clock
        clock_is_synced = try_to_sync_clock()
        if clock_is_synced :
            #on push les données
            push_data(list_histo_alti,altitude,date)
        else:
            #on historise les données
            add_data_to_histo(list_histo_alti,altitude,date)

    elif wlan.connect() && clock_is_synced:
        #on push juste les données
        push_data(list_histo_alti,altitude,date)

    else:
        add_data_to_histo(list_histo_alti,altitude,date)
        clock_is_synced = try_to_connect('AndroidAP4979','e2810218cd5d')
        #on historise et on essaie de se connecter


"""
#print("les nets: " + str(nets))
clock_is_synced = False
for net in nets:
    if net.ssid == 'AndroidAP4979':
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, 'e2810218cd5d'), timeout=5000)
        for x in range(3)
            if not wlan.isconnected():
                utime.sleep(3)
            else:
                clock_is_synced = True
                break
        print('WLAN connection succeeded!')
        break

"""

"""
rtc = RTC()
t = ntptime.time()
tm = utime.gmtime(t)
r = rtc.now()
rtc.init((tm[0]+30, tm[1]-1, tm[2], tm[6] , tm[3]+1 , tm[4], tm[5], 0))
print("Sending Altitude")
client.publish(topic="iot-2/evt/status/fmt/json", msg="{\"altitude\":\""+str(mp.altitude())+"\",\"heure\":\""+"le "+str(r[2])+"/"+str(r[1])+"/"+str(r[0]) +" a " + str(r[4]) +"h"+str(r[5])+"\"}")
time.sleep(60)
"""


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
