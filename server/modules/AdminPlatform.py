__all__ = ['AdminPlatform']
import threading

class AdminPlatform():
    _instance_lock = threading.Lock()

    __slots__ = ['Task_wait_list']

    def __new__(cls, *args, **kwargs):
        if not hasattr(AdminPlatform, "_instance"):
            with AdminPlatform._instance_lock:
                if not hasattr(AdminPlatform, "_instance"):
                    AdminPlatform._instance = object.__new__(cls)
                    AdminPlatform.Task_wait_list = []
        return AdminPlatform._instance

    def commit_new_task(self, task):
        pass