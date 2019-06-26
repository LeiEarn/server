from certificationServer.routers import prove
prove.app.run(host='0.0.0.0', port=60006, threaded=True)

# from server.model.User import User
#if __name__ == '__main__':
#    from swagger_server.modules.userManagementSystem import User
#    print(User.table.load_detail_user_id(user_id=1, identity='C'))
