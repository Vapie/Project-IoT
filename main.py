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

#a faire antidatage + calcul dynamique du sleep de fin
print("start")

"""ssid = 'AndroidAP4979'
pass = 'e2810218cd5d'
ssid="Livebox-fd84"
password="EDCE75E392ECDDD3F25ECCF7C4"
"""
ssid="aaaa"
password="yoyoyoyo"
Org_Id = "t8jaol"


def push_data(list_histo_alti,altitude,str_date,client):
    try:
        client.publish(topic="iot-2/evt/status/fmt/json", msg="{\"altitude\":\""+str(altitude)+"\",\"heure\":\""+str(str_date)+"\"}")
        print("push"+str_date)

    except:
       list_histo_alti = add_data_to_histo(list_histo_alti,altitude,str_date)
       print("merd" + str(list_histo_alti))
    finally:
        try:
            print(len(list_histo_alti))
            if len(list_histo_alti)>0:
                list_histo_alti = push_histo_data(list_histo_alti,client)
        except:
            print("pas pu push l'histo")
        return list_histo_alti
    #client.publish(topic="iot-2/evt/status/fmt/json", msg="{\"altitude\":\""+str(altitude)+"\",\"heure\":\""+"le "+str(date[2])+"/"+str(date[1])+"/"+str(date[0]) +" a " + str(date[4]) +"h"+str(date[5])+"\"}")

def push_histo_data(list_histo_alti,client):
    #try:

    for historized_data in list_histo_alti:
        print(str(historized_data))
        altitude = historized_data[0]
        str_date = historized_data[1]

        client.publish(topic="iot-2/evt/status/fmt/json", msg="{\"altitude\":\""+str(altitude)+"\",\"heure\":\""+str(str_date)+"\"}")

        list_histo_alti.remove(historized_data)
        print("yoyoyo")
        print(historized_data+"pushhisto")
    #except:
    #   print("merd" + str(list_histo_alti))
    #finally:
    return list_histo_alti

def try_to_connect(ssid,password,rtc):
    try:
        nets = wlan.scan()
        #print("les nets: " + str(nets))
        for net in nets:
            print("try")
            if net.ssid == ssid:
                print('Network found!')
                wlan.connect(net.ssid, auth=(net.sec, password), timeout=5000)
                if not wlan.isconnected():
                    utime.sleep(10)
                else:
                    print("connected to network")
                    return try_to_sync_clock(rtc)
                return False
    except:
        return False

def add_data_to_histo(list_histo_alti,altitude,str_date):
    list_histo_alti.append([str(altitude),str_date])
    return list_histo_alti

def try_to_sync_clock(rtc):
    try:
        t = ntptime.time()
        #différence de
        t=utime.ticks_add(t,-79200)
        tm = utime.gmtime(t)
        rtc.init((tm[0]+30, tm[1], tm[2], tm[3] , tm[4] , tm[5], 0, 0))
        return True
    except:
        return False




wlan = WLAN(mode=WLAN.STA)
try_to_connect(ssid,password,RTC())

if not wlan.isconnected():
    print("merd")
def test():
    client = MQTTClient("d:"+Org_Id+":Pycom:123456", Org_Id +".messaging.internetofthings.ibmcloud.com",user="use-token-auth", password="Co_q7SzBQgSDO1Y-gW", port=1883)
    client.connect()
    client.publish(topic="iot-2/evt/status/fmt/json", msg="{\"altitude\":\"test\",\"heure\":\"test\"}")
test()
"""
"""
client = None
py = Pysense()
list_histo_alti = []
rtc = RTC()
clock_has_been_synced=False
clock_is_synced = False
client_is_connected = False
wlan = WLAN(mode=WLAN.STA)
clock_is_synced = try_to_connect(ssid,password,rtc)
count = 0
client = MQTTClient("d:"+Org_Id+":Pycom:123456", Org_Id +".messaging.internetofthings.ibmcloud.com",user="use-token-auth", password="Co_q7SzBQgSDO1Y-gW", port=1883)

while True:
    if clock_is_synced :
        clock_has_been_synced = True
    if not client_is_connected and clock_has_been_synced:
        client = MQTTClient("d:"+Org_Id+":Pycom:123456", Org_Id +".messaging.internetofthings.ibmcloud.com",user="use-token-auth", password="Co_q7SzBQgSDO1Y-gW", port=1883)
        client.connect()
        client_is_connected = True
    altitude = str(MPL3115A2(py, mode=ALTITUDE).altitude())

    if(clock_has_been_synced):
        date = rtc.now()
        str_date ="le "+str(date[2])+"/"+str(date[1])+"/"+str(date[0]) +" a " + str(date[3]) +"h"+str(date[4])
    else:
        str_date = count

    if wlan.isconnected() and not clock_has_been_synced:
        #on sync la clock
        clock_is_synced = try_to_sync_clock(rtc)
        if clock_has_been_synced :
            #on push les données
            list_histo_alti = push_data(list_histo_alti,altitude,str_date,client)
            print("try push tf")
        else:
            #on historise les données
            print("histo")
            add_data_to_histo(list_histo_alti,altitude,str_date)

    elif wlan.isconnected() and clock_has_been_synced:
        #on push juste les données
        list_histo_alti = push_data(list_histo_alti,altitude,str_date,client)

    else:

        list_histo_alti = add_data_to_histo(list_histo_alti,altitude,str_date)
        clock_is_synced = try_to_connect(ssid,password,rtc)
        print(str(list_histo_alti))
        #on historise et on essaie de se connecter
    utime.sleep(10)
    count+=1












"""
while True:
    rtc = RTC()
    utime.sleep(1)
    print(rtc.now())
"""







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
