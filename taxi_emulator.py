import time
import threading
import requests
import random

coords = ["'38.173079, 15.543566'", "'38.188192, 15.556098'", "'38.206404, 15.557471'", "'38.216404, 15.567471'", "'38.226404, 15.577471'", "'38.236404, 15.587471'", "'38.246404, 15.597471'", "'38.256404, 15.607471'"]

taxi_id = "Taxi1"


rand_index = random.randint(0,len(coords))	# Calcolo random dell'indice della coordinata iniziale
current_point = coords[rand_index]
old_point = current_point
move = True					# Stato del TAXI (true --> in movimento, false --> fermo)


# Thread che simula il cambio delle coordinate del TAXI
def change_coords():
	global rand_index
	global current_point
	while 1:
		time_to_move = random.randint(1,200) 		#tempo di cambio della coordinata
		time.sleep(time_to_move)			
		rand_index = (rand_index + 1) % len(coords)	
		current_point = coords[rand_index]		#nuova coordinata corrente
		print "Cambio Coordinata: " + current_point + "\nTempo passato per il cambio della coordinata: "+ str(time_to_move) + "\n"

# Thread che controlla lo stato del TAXI e il cambio della coordinata per calcolare il nuovo stato del TAXI	
def check_state():
	global move
	global current_point
	global old_point

	cont = 0
	while 1:
		if old_point != current_point:
			if move == False:
				move = True
				old_point = current_point
				cont = 0
				#stop sensoristica
				#r = requests.get('http://192.168.1.239:1234/stop/observation')
				print "Sto partendo: invio lo stop per la sensoristica\n" 
			else:
				old_point = current_point
				cont = 0
				print "Sono in movimento\n"
		
		else:
			if move == False:
				print "Sono fermo\n"
			else:
				cont = cont + 1	
				print "Ero in movimento e sono fermo da " + str(15*cont) + " secondi\n"
				if cont >= 6:
					move = False
					#start sensoristica
					ts = str(time.time())
					#r = requests.get('http://192.168.1.239:1234/start/observation?id='+ ts +'&type=observation&position='+current_point)
					print "Sono fermo da piu' di 90 secondi: invio lo start per la sensoristica\n"+ "id_observation=" + ts + "\ncurrent_position="+ current_point +"\n" 

			
		time.sleep(15)					#ogni 15 secondi controllo se sono cambiate le coordinate
		print "CONTROLLO STATO:\n"
			
		

t1 = threading.Thread(target=change_coords)
t2 = threading.Thread(target=check_state)
t1.start()
t2.start()

