class User(object):
    def __init__(self):
        pass


class BasicUser(User):

    def __init__(self):
        super(User, self).__init__()
        pass

class AuthenticatedUser(BasicUser):
    def __init__(self):
        super(AuthenticatedUser, self).__init__()
        pass






if __name__ == '__main__':
    class Base:
        def __init__(self):
            print('e Base')
            print('l Base')
    class A(Base):
        def __init__(self):
            print('e A')
            super(A, self).__init__()
            print('l A')
    class B(Base):
        def __init__(self):
            print('e B')
            super(B, self).__init__()
            print('l B')


    class C(A, B):
        def __init__(self):
            print('e C')
            super(C, self).__init__()
            print('l C')
    C()
    print(C.mro())