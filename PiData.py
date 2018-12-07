

class PiData:
    def __init__(self, id, temperature, location, inDoor, timestamp):
        self.id = id
        self.temperature = temperature
        self.location = location
        self.inDoor = inDoor
        self.timestamp = timestamp


def create_pidata(id, temperature, location, inDoor, timestamp):
    pidata = PiData(id, temperature, location, inDoor, timestamp)
    return pidata


def __str__(self):
    return (f"id : {self.id}, temperature : {self.temperature}, location : {self.location}, inDoor : {self.inDoor}, timestamp : {self.timestamp}")
