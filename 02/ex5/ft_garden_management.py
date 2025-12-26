class GardenError(Exception):
    '''
        Class for garden relative errors.
    '''
    def __init__(self, message="An undefined GardenError occured."):
        super().__init__(message)


class InvalidName(GardenError):
    '''
        Exception raised for invalid plant names.
    '''
    def __init__(self, message="plant_name cannot be empty."):
        super().__init__(message)


class Planr:
    def __init__(self, name):
        self.set_name(name)

    def set_name(self, name):
        if name is None or name == "":
            raise InvalidName
        self.__name = name.capitalize()

    def get_name(self):
        return (self.__name)
