
if __name__ == '__main__':
    from certificationServer.routers import prove
    prove.app.run(host='0.0.0.0', port=8001, threaded=True)
