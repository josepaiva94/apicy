
class ModelNotFoundException(Exception):
    def __init__(self, identifier: str):
        self.identifier = identifier
