# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas

from ....modules import loginPersistentSystem, userManagementSystem,accessControlSystem
controller = userManagementSystem.ManagementSystem()
persistent = loginPersistentSystem.PersistentSystem()
control = accessControlSystem.AccessControlSystem()
class Login(Resource):

    @control.login_required(redirect_to_login='login')
    def post(self):
        print(g.args)
        js_code = g.args['js_code']
        result = controller.login(js_code)
        if result is None:
            return {'login'}, 200, None
        return {}, 200, None