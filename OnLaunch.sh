#!/bin/bash
while true; do
exec IFACE=wlan0 OUTPUT=OUT.txt CHANNEL_HOP=1 ./sniff-probes.sh
python todb.py
done
