#!/bin/bash
while true; do
cd /home/pi/Desktop/sniff-probes-master
IFACE=wlan1 OUTPUT=OUT.txt CHANNEL_HOP=1  ./sniff-probes.sh -vv
cp /home/pi/Desktop/sniff-probes-master/panoptique.db mtp://Xiaomi_POCO_X4_Pro_5G_94a4bb52a478
done


