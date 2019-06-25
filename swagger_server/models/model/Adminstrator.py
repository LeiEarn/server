# -*- coding: utf-8 -*-
from ...utils.db import Database

class Adminstrator(object):

    @staticmethod
    def get_admin():
        sql = 'SELECT * FROM audit_administrator;'
        return Database.execute(sql)