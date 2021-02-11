# ScooterSteal

A script to scan for nearby Xiaomi m365 scooters and unlock them if they are locked.
Will work best with scooters on 1.3.8 firmware.
(pretty much any modified firmware as this is the most compatible)
.
A good platform for this attack is a Raspberry Pi broadcasting a WiFi hotspot, or a cron job if you want to unlock all scooters in your path.

Please do not target scooters without the express consent of the users targeted.
I do not take any responsibility for your actions.

## Installation of pip and modules

```sh
sudo apt-get install python-pip libglib2.0-dev
```

```sh
sudo pip install bluepy
```

```sh
sudo pip install git+https://github.com/AntonHakansson/m365py.git#egg=m365py
```

## Find MAC address of your scooter

You'll need to find the MAC Address of your scooter. 
Using the m365py module, you can find the MAC Addresses of all nearby scooters:

```sh
sudo python -m m365py
```

Clone the Repository:
```sh
git clone https://github.com/NickJongens/ScooterJam.git
```


## Start the script - could be run as a cron job etc:
```sh
sudo python ScooterSteal.py
```



## Credits

Anton Hakansson

https://github.com/AntonHakansson

Ian Harvey

https://github.com/IanHarvey
