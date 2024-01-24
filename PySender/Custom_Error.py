from PySender import LOGGER
class WrongIPError(Exception):
    """Exception personnalisée pour signaler une erreur"""

    def __init__(self, message="The value must be an IP"):
        self.message = message
        LOGGER.error(message)
        super().__init__(self.message)


