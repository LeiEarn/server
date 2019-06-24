# -*- encoding:utf-8 -*-
from flask import session, Flask, jsonify, request, send_from_directory
from server.modules.userManagementSystem import ManagementSystem as UMS
from server.modules.taskManagementSystem import taskManagementSystem as TMS

app = Flask(__name__)
app.secret_key = "nQnk2n8moN=GLNmE.wL6PTZD"


def ok(data=None):
    return jsonify({
        "status": "ok",
        "data": data
    })


def bad(msg=""):
    return jsonify({
        "status": "bad",
        "message": msg
    })

# Login Part:
@app.route("/api/v1/login", methods=['POST'])
def login():
    req = request.get_json()
    password = req['password']
    if password != "this_is_password":
        return bad("密码错误")
    else:
        session['user'] = password
        return ok()


# Query Part:
@app.route('/api/v1/get_all_users', methods=['POST'])
def get_all_users():
    if request.method =='POST':
        # 1 page = 100 record
        page = request.form.get('page')
        record_num = UMS.get_user_count()
        if page > record_num // 100 + 1:
            return bad('out of user size')

        data = UMS.get_users(page=page)
        return ok(data)
    return bad('error')

@app.route('/api/v1/get_wait_user', methods=['POST'])
def get_wait_user():
    if request.method == 'POST':
        # 1 page = 100 record
        page = request.form.get('page')
        record_num = UMS.get_wait_user_count()
        if page > record_num // 100 + 1:
            return bad('out of user size')

        data = UMS.get_wait_users(page=page)
        return ok(data)
    return bad('error')


@app.route('/api/v1/get_all_task', methods=['POST'])
def get_all_task():
    if request.method == 'POST':
        # 1 page = 100 record
        page = request.form.get('page')
        record_num = TMS.get_record_num()
        if page > record_num // 100 + 1:
            return bad('out of user size')

        data = UMS.get_records(page=page)
        return ok(data)
    return bad('error')


@app.route('/api/v1/get_wait_task', methods=['POST'])
def get_wait_task():
    if request.method == 'POST':
        # 1 page = 100 record
        page = request.form.get('page')
        record_num = TMS.get_wait_record_num()
        if page > record_num // 100 + 1:
            return bad('out of user size')

        data = UMS.get_wait_records(page=page)
        return ok(data)
    return bad('error')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=60006, threaded=True)
