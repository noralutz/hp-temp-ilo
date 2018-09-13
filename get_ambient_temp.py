#!/usr/bin/env python
# -*- coding: utf-8 '*'

import hpilo
import json
import sys

def get_temp(host,ilo_user,ilo_pass):
	ilo = hpilo.Ilo(host,ilo_user,ilo_pass)
#	health_str = json.dumps(ilo.get_embedded_health())
	health_dict = json.loads(json.dumps(ilo.get_embedded_health()))
	#get the current Inlet Ambient temp from the sensor, in Celcius
	temp_c = health_dict['temperature']['01-Inlet Ambient']['currentreading'][0]
	#convert to fahrenheit
	temp_f = int(temp_c) * 9/5 + 32
        return temp_f

if len(sys.argv) < 5:
	print("usage: get_ambient_temp.py admin_user ilo_password inventory_filename warn_temp")
	sys.exit(1)

else:
	ilo_user = str(sys.argv[1])
	ilo_pass = str(sys.argv[2])
	inventory_file = str(sys.argv[3])
	warn_temp = int(sys.argv[4])

	inventory = open(inventory_file, 'r')
	for line in inventory.readlines():
        	host = line.split()
		temp = get_temp(host[0],ilo_user,ilo_pass)
		if temp >= warn_temp:
			print("WARNING. The temperature is {} degrees, exceeded {} degrees.".format(temp,warn_temp))
  			sys.exit(0)
