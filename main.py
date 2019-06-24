# -*- coding: utf-8 -*-
from server import create_app
from certificationServer.routers import prove

app = create_app()

app.run(host='0.0.0.0', port=9000)

prove.app.run(host='0.0.0.0', port=60006, threaded=True)
