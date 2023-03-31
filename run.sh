#!/bin/bash
cd /home/pi/Desktop/sniff-probes-master
while true; do
IFACE=wlan1 CHANNEL_HOP=1 ./sniff-probes.sh 
cp /home/pi/Desktop/sniff-probes-master/panoptique.db mtp://Xiaomi_POCO_X4_Pro_5G_94a4bb52a478
#Emplacement souhaiter
done


