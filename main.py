# -*- coding: utf-8 -*-
from server import create_app

app = create_app()

app.run(host='localhost', port=8080)
