# SUN2000-ModBus


## WARNING
Huawei has taken the posibility for querying ModBus data over WiFi (at least over the home WiFi, no clue about through the hotspot of the inverter itself) away in recent firmware upgrades without any explanation, documentation or notice, which, in my opinion, was a rather unfriendly and rude act towards their customers. Guess they want to push people to buy the dedicated dongles to have the same functionality again. You could have disabled firmware updates beforehand to avoid this, but (as Huawei support was kind enough to explain) if a firmware update is considered of "Critial" importance, the inverter will apply it and upgrade itself anyway by design, regardless of whether the "Disable firmware upgrades" option is enabled or not, so naming this option as "Apply critical firmware upgrades only" would have been more straightforward... Anyway, the inverter does not allow connections on port 502 over WiFi anymore.

Shame!


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
 - Add the config in userparams into the configuration of Zabbix Agent on a client, or on Zabbix Server.
 - Create a trapper item in Zabbix, with the appropriate run schedule.
 - Create a Zabbix client with the IP of your inverter, and assign the ModBus template to it.
