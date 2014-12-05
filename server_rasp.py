import web

from web.wsgiserver import CherryPyWSGIServer

CherryPyWSGIServer.ssl_certificate = "./localhost.pem"
CherryPyWSGIServer.ssl_private_key = "./localhost.key"

urls = (

        '/start/observation', 'start_obs',
        '/stop/observation', 'stop_obs'
)

# https://localhost/start/observation?id=id_entity&id_type&position
# Questo metodo crea l'entita' observatin su Orion richiamando
# lo script createEntity.py e fa partire lo script per iniziare
# l'osservazione

class start_obs:

        def GET(self):
		tablet_data = web.input()
		id_entity = tablet_data.
                return "observations"

class stop_obs:

        def GET(self):
                return "rest hive server 0.0.1"


if __name__ == "__main__":
        app = web.application(urls, globals())
        app.run()

