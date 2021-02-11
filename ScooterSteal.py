import time
import json
import os
import array as arr

from m365py import m365py
from m365py import m365message
from bluepy.btle import Scanner

# callback for received messages from scooter
def handle_message(m365_peripheral, m365_message, value):
    print(json.dumps(value, indent=4))

""" Scans for available devices. """
scan = Scanner()
sec = 5
print("Scanning for %s seconds" % sec)
devs = scan.scan(sec)
print("Unlockable Scooters found:")
for dev in devs:
    localname = dev.getValueText(9)
    if localname and localname.startswith("MIScooter"):
        print("%s" % (dev.addr))
        scooter_mac_address = dev.addr
        scooter = m365py.M365(scooter_mac_address, handle_message)
        scooter.connect()
        print("Connected to Scooter")
        scooter.request(m365message.turn_off_lock)
        print("Unlocked scooter")
        time.sleep(1)
        scooter.disconnect()
        print("Disconnected from Scooter")
    else:
        print("No more scooters found")
print("No more scooters in range. Shutting down.")