class CredentialsNotFoundError(Exception):
    def __init__(self, message):
        self.message = message


class TokenNotFoundError(Exception):
    def __init__(self, message):
        self.message = message


class ArgsNotGivenError(Exception):
    def __init__(self, message):
        self.message = message


class InventoryNotFoundError(Exception):
    def __init__(self, message):
        self.message = message
        
        
class TimeSerieNotFoundError(Exception):
    def __init__(self, message):
        self.message = message
