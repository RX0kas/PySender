from PySender import LOGGER
class WrongIPError(Exception):
    """Exception personnalis�e pour signaler une erreur"""

    def __init__(self, message="The value must be an IP"):
        self.message = message
        LOGGER.error(message)
        super().__init__(self.message)


