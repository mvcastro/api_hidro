class CredentialsNotFoundError(Exception):
    def __init__(self, message):
        self.message = message


class TokenNotFoundError(Exception):
    def __init__(self, message):
        self.message = message


class ArgsNotGiven(Exception):
    def __init__(self, message):
        self.message = message
