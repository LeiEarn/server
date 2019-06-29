# -*- coding: utf-8 -*-
from ..models.model.User import User as User
from flask import g
from ..utils.utils import code2session

from .loginPersistentSystem import PersistentSystem as persistentSystem

"""
   小程序登录过程
       1. 登录时用户端调用login，从微信服务器获取到jscode，
       2. 用户端将jscode发送给小程序服务器
       3. 小程序服务器用jscode 从微信服务器处获取到union等标识信息
       4. 小程序服务器用union唯一认知用户是否存在
       5. 当用户存在则登录成功，服务器生成uuid, 临时存储并返回uuid给用户端，
               用户端用uuid发起其他请求标志处于session期间
               
       6. 用户不存在则转向注册界面
   登录备注：
       1. 是否处于session期间，需要重新登录由小程序服务器根据uuid判断，
               正常情况下小程序不发起登录请求，直接用本地存储的uuid进行其他操作
               在收到服务器端登录过期或者uuid错误的情况下才发起登录
       2. 账号只能与一个小程序id绑定，即不可在第二个微信上登录
"""


class ManagementSystem:
    def __init__(self):
        pass

    def login(self, js_code, app_id, app_secret):
        """
            登录模块， 小程序启动即刻调用
            数据库获取【用户简单信息】，并返回
            session保存登录状态
            不存在则注册
        
        Parameters:
            js_code: 小程序端发来的token,用于从微信服务器获取unionid
        
        Returns:
            用户信息 or None
            :param app_secret:

        """

        wechatresult = code2session(
            js_code=js_code, app_id=app_id, app_secret=app_secret
        )

        # wechatresult = {
        #   'unionid':'ofAUV5mo9AjSRLiowX6i4PPVhTzw'
        # }
        print(wechatresult)
        if "error" in wechatresult:
            return None

        unionid = wechatresult.get("unionid")
        print(unionid)
        if unionid is None:
            return None
        else:
            user = User.table.query_user(unionid_=unionid)
            if isinstance(user, User.BasicUser):
                """
                persistent_info
                openid, unionid, session_key, user
                """
                persistentSystem.save(
                    wechat_server_reply=wechatresult, user=user
                )
                return user
            else:
                user = self.register(union_id=unionid)
                persistentSystem.save(
                    wechat_server_reply=wechatresult, user=user
                )
                return user

    @staticmethod
    def register(union_id=None):
        """
            注册模块,小程序启动时，在用户不存在时使用
            先数据库查询用户【用户简单信息】，存在则返回错误
            数据库添加用户id

        Parameters:
            id: unionid登录时获得
            :param union_id:

        """
        if union_id is None:
            return None
        user = User.table.query_user(unionid_=union_id)
        if user is None:
            User.table.create_new_user(unionid=union_id)
            user = User.table.query_user(unionid_=union_id)
            return user
        else:
            return user

    @staticmethod
    def prove(identity_info):
        """
            用户发起认证请求
        """
        user_id = g.get("persistent").get("user_id")
        user = User.table.query_user(user_id=user_id)
        unionid = g.get("persistent").get("unionid")
        if user is None:
            return "error", "no such user"
        elif user.isprove is "P":
            return "error", "hasproved"
        elif user.isprove is "W":
            return "error", "in auditing"
        elif user.isprove is "F" and user.identity is not identity_info.iden_type:
            return "error", "identity type error, please certificaate another type "

        print(user_id)
        print(identity_info.iden_type)
        if identity_info.iden_type is "S":
            result = User.table.prove(
                user_id=user_id,
                name=identity_info.name,
                gender=identity_info.sex,
                identity=identity_info.iden_type,
                phone_number=identity_info.tel,
                school=identity_info.school,
                id=identity_info.id,
                prove=identity_info.cert,
            )
            if isinstance(result, Exception):
                return "error", "fail"
            result = User.table.update_info(unionid=unionid, identity="S", isprove="W")
            if not isinstance(result, Exception):
                return "success", "changed"
            else:
                return "error", "fail"
        elif identity_info.iden_type is "C":
            result = User.table.prove(
                user_id=user_id,
                name=identity_info.name,
                gender=identity_info.sex,
                identity=identity_info.iden_type,
                phone_number=identity_info.tel,
                company=identity_info.company,
                id=identity_info.id,
                prove=identity_info.cert,
            )
            if isinstance(result, Exception):
                return "error", "fail"
            result = User.table.update_info(unionid=unionid, identity="C", isprove="W")
            if not isinstance(result, Exception):
                return "success", "changed"
            else:
                return "error", "fail"
        else:
            return "error", "no such user"

    @staticmethod
    def modify(nick_name, avatar_url):
        union_id = g.get("persistent").get("unionid")
        # user_id = g.get("persistent").get("user_id")
        User.table.update_info(unionid=union_id, nickname=nick_name, photo=avatar_url)
        user_info = User.table.query_user(unionid_=union_id)
        return user_info

    @staticmethod
    def get_user_count(user_type="all"):
        return User.table.user_count(user_type)

    @staticmethod
    def specific_user_count(gender="all", identity="U"):
        return User.table.specific_user_count(gender, identity)

    @staticmethod
    def get_company_count(type_="company"):
        if type_ == "company":
            return User.table.get_company_count()
        else:
            return User.table.get_school_count()

    @staticmethod
    def low_credit_count(credit):
        return User.table.low_credit_count(credit)

    @staticmethod
    def get_users(user_type="all", page=0):
        return User.table.get_users(
            user_type=user_type, begin=page * 100, end=(page + 1) * 100
        )

    @staticmethod
    def get_user_info(user_id):
        """
        获取信息模块
        """
        user = User.table.query_user(user_id=user_id)
        if isinstance(user, User.BasicUser):
            return user
        else:
            return None

    @staticmethod
    def get_indentity_info(user_id, identity):
        """

        :param identity:
        :param user_id:
        :param identity: S or C, count be U
        :return:
        """
        if identity in ["S", "C"]:
            return User.table.load_detail_user_id(user_id, identity)
        else:
            raise KeyError("Wrong identity %s" % identity)

    @staticmethod
    def get_user_detail(user_id):
        """
        获取认证信息模块
        """
        print(g.get("persistent").get("user_type"))
        detail = User.table.load_detail_user_id(
            user_id=user_id,
            identity=g.get("persistent").get("user_type").get("identity"),
        )
        if detail is None:
            detail = {}
        detail["identity"] = g.get("persistent").get("user_type").get("identity")
        if detail["identity"] is "S":
            detail["id"] = detail.get("student_num")
        elif detail["identity"] is "C":
            detail["id"] = detail.get("job_num")
        return detail

    @staticmethod
    def audit_user(user_id, identity, audit):
        return User.table.audit(user_id, identity, audit)
