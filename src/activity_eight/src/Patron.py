class Patron:

    def __init__(self, name: str = ""):
        self.name = name
        self.checked_out = []
    
    def __str__(self):
        return self.__dict__