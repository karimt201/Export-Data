class RequiredInputError(Exception):
    def __init__(self, message="Missing field", attribute_name=None):
        super().__init__(message)
        self.message = message
        self.attribute_name = attribute_name

    @property
    def data(self):
        return {"attributeName": self.attribute_name}


class InvalidInputError(Exception):
    def __init__(self, message="Invalid field", attribute_name=None):
        super().__init__(message)
        self.message = message
        self.attribute_name = attribute_name

    @property
    def data(self):
        return {"attributeName": self.attribute_name}


class NotFoundError(Exception):
    def __init__(self, message="User Not Found", attribute_name=None):
        super().__init__(message)
        self.message = message
        self.attribute_name = attribute_name

    @property
    def data(self):
        return {"attributeName": self.attribute_name}
    
class InvalidFieldError(Exception):
    def __init__(self, message="Invalid field", attribute_name=None):
        super().__init__(message)
        self.message = message
        self.attribute_name = attribute_name

    @property
    def data(self):
        return {"attributeName": self.attribute_name}

class NotImplementError(Exception):
    def __init__(self, message="Invalid field", attribute_name=None):
        super().__init__(message)
        self.message = message
        self.attribute_name = attribute_name

    @property
    def data(self):
        return {"attributeName": self.attribute_name}

