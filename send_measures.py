import os
import io
import time

OBD_TEMP_PATH = "obd_temperature"
OBD_PRES_PATH = "obd_pressure"
SHINYEI_PM10_PATH = "shinyei_PM10"

lastModifyTemp = 0
lastModifyPres = 0
lastModifyPM10 = 0

cont = 1

coords = ["'38.173079, 15.543566'", "'38.188192, 15.556098'", "'38.206404, 15.557471'"]

while 1:
	#prova = os.path.getmtime("/home/Gioak/Codice-Sensori-Broker/obd_temperature")
	if lastModifyTemp != os.path.getmtime(OBD_TEMP_PATH):
		lastModifyTemp = os.path.getmtime(OBD_TEMP_PATH)
		print "Il file ", OBD_TEMP_PATH, " e' cambiato, invio il nuovo dato"
		temp_file = open(OBD_TEMP_PATH, "r")
		value = temp_file.readline()
		parameters = "python2.7 UpdateEntityAttribute.py Taxi1 Taxi temperature centigrade " + str(value)
		os.system(str(parameters))
	if lastModifyPres != os.path.getmtime(OBD_PRES_PATH):
		lastModifyPres = os.path.getmtime(OBD_PRES_PATH)
		print "Il file ", OBD_PRES_PATH, " e' cambiato, invio il nuovo dato"
		temp_file = open(OBD_PRES_PATH, "r")
		value = temp_file.readline()
		parameters = "python2.7 UpdateEntityAttribute.py Taxi1 Taxi pressure mmHg " + str(value)
		os.system(str(parameters))
	if lastModifyPM10 != os.path.getmtime(SHINYEI_PM10_PATH):
		lastModifyPM10 = os.path.getmtime(SHINYEI_PM10_PATH)
		print "Il file ", SHINYEI_PM10_PATH, " e' cambiato, invio il nuovo dato"
		temp_file = open(SHINYEI_PM10_PATH, "r")
		value = temp_file.readline()
		parameters = "python2.7 UpdateEntityAttribute.py Taxi1 Taxi PM10 concentration " + str(value)
		os.system(str(parameters))
	indice = cont % 3
	value = coords[indice]
	#value = "/"+value+/""
	parameters = "python2.7 UpdateEntityAttribute.py Taxi1 Taxi taxiPosition coords " + str(value)
	os.system(str(parameters))
	cont = cont + 1
	time.sleep(30)
