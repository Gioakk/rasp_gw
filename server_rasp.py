import web
import os
import psutil
import pdb

#from web.wsgiserver import CherryPyWSGIServer

#CherryPyWSGIServer.ssl_certificate = "./localhost.pem"
#CherryPyWSGIServer.ssl_private_key = "./localhost.key"

urls = (

        '/start/observation', 'start_obs',
        '/stop/observation', 'stop_obs'
)

# https://localhost/start/observation?id=id_entity&type=&position=
# Questo metodo crea l'entita' observatin su Orion richiamando
# lo script createEntity.py e fa partire lo script per iniziare
# l'osservazione

class start_obs:

        def GET(self):
		#pdb.set_trace()
		tablet_data = web.input()
		id_entity = tablet_data.id
		id_type = tablet_data.type
		position = tablet_data.position

		start_obd_sim = "obdsim -g Cycle > obd_sim.out &"
		start_obd = "python2.7 obd.py > obd.out &"
		start_pm10 = "python2.7 Shinyei.py > shinyei.out &" 
		
		start_send_measures = "python2.7 send_measures.py" + " " + id_entity + " " + id_type + " " + position + " &" 

		os.system(str(start_pm10))
		os.system(str(start_obd_sim))
		#inserire una sleep??
		os.system(str(start_obd))
		os.system(str(start_send_measures))

                return "id=" + id_entity + " type=" + id_type + " position=" + position

class stop_obs:

        def GET(self):
		python_process = []
		list_process = psutil.pids()
		i = 0

		#ciclio tutti i processi e inserisco in lista solo i tre da killare
		for pid in list_process:
			p = psutil.Process(pid)
			command = p.cmdline()
			if len(command) == 0:
				continue
			#command[0]=python2.7 command[1]=obd.py
			if command[0] == 'python2.7' and len(command) > 1:
				if command[1] == "obd.py" or command[1] == "Shinyei.py" or command[1] == "send_measures.py":
					print "killed process " + command[1]
					p.kill()
					python_process[i] = command[1]
					i = i + 1	
                return "stop onservation"


if __name__ == "__main__":
        app = web.application(urls, globals())
        app.run()

