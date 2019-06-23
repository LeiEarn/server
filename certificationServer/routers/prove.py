from flask import request

def login():
    account = request.args.get('account')
    password = request.args.get('password')
    if account is not 'admin':
        return 'error'

def 