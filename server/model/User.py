__all__ = ['BasicUser', 'AuthenticatedUser', 'Student', 'Company']

class BasicUser(object):
    """
    Attributes:
        wechat_id: user's wechat id
        profile_photo: how to load the profile photo?
        nickname: user's nickname, the default value is wechat nickname
        phone_number: user's phone number
        sexual: man or female
        intro: introduction
        create_date: date when this user was created
    """
    __slots__ = ['wechat_id', 'profile_photo', 'nickname', 'phone_number', 'gender', 'intro', 'create_date']
    def __init__(self, wechat_id, profile_photo, nickname, phone_number, gender, intro, create_date):
        self.wechat_id = wechat_id
        self.profile_photo = profile_photo
        self.nickname = nickname
        self.phone_number = phone_number
        self.gender = gender
        self.intro = intro
        self.create_date = create_date


class AuthenticatedUser(BasicUser):
    """
    Attributes:
        identification: the authentification that had been certified by the administrator
    """
    __slots__ = ['identification']
    def __init__(self):
        super(AuthenticatedUser, self).__init__()
        pass

class Student(AuthenticatedUser):

    __slots__ = ['college', 'std_id', 'school', 'major']
    def __init__(self):
        super(Student, self).__init__()
        pass

class Company(AuthenticatedUser):
    __slots__ = ['company']
    def __init__(self):
        super(Company, self).__init__()
        pass






if __name__ == '__main__':
    b = BasicUser()

