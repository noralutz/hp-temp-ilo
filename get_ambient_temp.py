#!/usr/bin/env python
# -*- coding: utf-8 '*'

import hpilo
import json
import sys

def get_temp(host,ilo_user,ilo_pass):
	ilo = hpilo.Ilo(host,ilo_user,ilo_pass)
	health = ilo.get_embedded_health()
	#get the current Inlet Ambient temp from the sensor, in Celcius
	temp_c = health['temperature']['01-Inlet Ambient']['currentreading'][0]
	#convert to fahrenheit
	temp_f = int(temp_c) * 9/5 + 32
        return temp_f

if len(sys.argv) < 5:
       	print("usage: get_ambient_temp.py admin_user ilo_password inventory_filename warn_temp")
        sys.exit(1)
else:
	inventory = open(str(sys.argv[3]), 'r')
	for line in inventory.readlines():
               	host = line.split()
               	temp = get_temp(host[0],str(sys.argv[1]),str(sys.argv[2]))
               	if temp >= int(sys.argv[4]):
                       	print("WARNING. The temperature is {0} degrees, exceeded {1} degrees.".format(temp,int(sys.argv[4])))
