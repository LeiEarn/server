# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import sys,os
print(sys.path)   # 查看当前路径
from os import path
#d = path.dirname(__file__)  # 获取当前路径
#parent_path = os.path.dirname(d)  # 获取上一级路径
#sys.path.append(parent_path)    # 如果要导入到包在上一级
import connexion

from swagger_server import encoder

from swagger_server import init_app


def main():
    app = connexion.App(__name__, specification_dir="./swagger/")

    app.app.json_encoder = encoder.JSONEncoder
    api = app.add_api(
        "swagger.yaml", arguments={"title": "Sample Application Flow OAuth2 Project"}
    )

    print(app.app.before_request)

    init_app(app=app)
    app.run(host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()
