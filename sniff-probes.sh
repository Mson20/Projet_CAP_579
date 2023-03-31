#!/bin/bash

counter=0
condition=10
DB_NAME="panoptique.db"
DATE=$(date +%Y-%m-%d)
CHANNEL_HOP="${CHANNEL_HOP:-0}"

sqlite3 $DB_NAME "CREATE TABLE IF NOT EXISTS '$DATE'(id INTEGER PRIMARY KEY AUTOINCREMENT,date_time TEXT,signal_strength TEXT,mac_address TEXT,ssid TEXT);"

# channel hop every 2 seconds
channel_hop() {
    #Different standard
    IEEE80211bg="1 2 3 4 5 6 7 8 9 10 11"
    IEEE80211bg_intl="$IEEE80211bg 12 13 14"
    IEEE80211a="36 40 44 48 52 56 60 64 149 153 157 161"
    IEEE80211bga="$IEEE80211bg $IEEE80211a"
    IEEE80211bga_intl="$IEEE80211bg_intl $IEEE80211a"
    
    while true ; do
        for CHAN in $IEEE80211bg ; do
            # echo "switching $IFACE to channel $CHAN"
            sudo iwconfig $IFACE channel $CHAN
            sleep 2
        done
    done
}
	#Condition nécessaire
    	if ! [ -x "$(command -v gawk)" ]; then
		echo 'gawk (GNU awk) is not installed. Please install gawk.' >&2
		exit 1
    	fi

    	if [ -z "$IFACE" ] ; then
        	echo "IFACE env variable must be set. Type "ifconfig" to view network interaces."
        	exit 1
    	fi
	if [ "$CHANNEL_HOP" -eq 1 ] ; then
        	# channel hop in the background
        	channel_hop &
	fi

# filter with awk, then use sed to convert tabs to spaces and remove front and back quotes around SSID
sudo tcpdump -l -I -i "$IFACE" -e -s 256 type mgt subtype probe-req | awk -f parse-tcpdump.awk | while read -r line; do

#Ligne vers variable pour DB
stringarray=($line)
var1=( ${stringarray[0]})
var2=( ${stringarray[1]})
var3=( ${stringarray[2]})
var4=( ${stringarray[3]})

# Insert data into database
sqlite3 $DB_NAME "INSERT INTO '$DATE'(date_time, signal_strength, mac_address, ssid) VALUES ('$var1', '$var2', '$var3', '$var4') ;"

##Condition d'arret
((counter=counter+1))
if [ "$counter" == "$condition" ] ;then
	exit 1
fi

done
