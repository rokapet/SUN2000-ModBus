#!/bin/bash

. /etc/zabbix/userparams/_config

python3 /etc/zabbix/userparams/huawei/scanner_2.py
zabbix_sender -z $ZABBIX_SERVER -p 10051 -i /tmp2/sun2000_min.txt

rm -f /tmp2/sun2000_min.txt