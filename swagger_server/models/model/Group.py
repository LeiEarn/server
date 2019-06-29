# -*- coding: utf-8 -*-
__all__ = ["Group"]


class Group(object):
    """
    Attributes:
        group_photo:
        intro:
        members:
    """

    __slots__ = [
        "creater_date",
        "creater",
        "group_photo",
        "members",
        "intro",
        "managers",
    ]

    def __init__(self):
        pass
        self.creater_date = ""
        self.creater = None
        self.group_photo = None
        self.members = []
        self.intro = ""
        self.managers = []
