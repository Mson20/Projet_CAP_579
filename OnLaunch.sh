#!/bin/bash
DATE=$(date +%d-%m-%Y).txt

exec IFACE=wlan0 OUTPUT=DATE CHANNEL_HOP=1 ./sniff-probes.sh
python todb.py