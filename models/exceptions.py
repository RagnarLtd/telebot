class ZeroHotels(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return str(self.message)


class TimeOut(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return str(self.message)