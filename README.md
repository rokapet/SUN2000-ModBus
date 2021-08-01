# SUN2000-ModBus

## Original script taken from:
[https://github.com/basking-in-the-sun2000/solar-logger](https://github.com/basking-in-the-sun2000/solar-logger)

## Customize your config.py
 - inverter_ip: Set to the IP of your inverter
 - inverter_port: ModBus port is 502
 - slave: For Huawei inverters, it is 0x00
 - latitude: Western values are positive, eastern values are negative.
 - logitude: Northern values are positive, southern values are negative.
 - tilt: The slope of your rooftop.
 - azimuth: The facing of your panels.

## Usage
Add the config in userparams into the configuration of Zabbix Agent on a client, or on Zabbix Server.
Create a trapper item in Zabbix, with the appropriate run schedule.
Create a Zabbix client with the IP of your inverter, and assign the ModBus template to it.
