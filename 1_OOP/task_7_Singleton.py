

class Logger:
    instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


    def __init__(self):
        if not Logger._initialized:
            self.lst = []
            Logger._initialized = True

    def log(self, message):
        self.lst.append(message)

    def get_logs(self):
        return self.lst

logger_1 = Logger()
logger_1.log("сообщение 1")
print(logger_1.get_logs())

logger_2 = Logger()
logger_2.log("сообщение 2")
print(logger_2.get_logs())

