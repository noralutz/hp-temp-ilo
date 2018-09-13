This is a simple python script designed to access the HP ILO API to gather ambient temperature data as measured by the inlet temperature sensor from HP servers defined in an inventory. It will return a warning if the temperature measured is in excess of the threshold set by "warn_temp"

Usage: get_ambient_temp.py admin_user ilo_password inventory_filename warn_temp

Example inventory file: 
---
somehost.example.com
---

Note: All temperatures are in Fahrenheit. 
