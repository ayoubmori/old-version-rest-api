
class Relay:
    def __init__(self, id, status="OFF"):
        self.id = id
        self.status = status
        
    def turn_on(self):
        self.status = "ON"
        
    def turn_off(self):
        self.status = "OFF"
        
    def as_dict(self):
        return {
            "id": self.id,
            "status": self.status
        }

relays = {
    'relay1': Relay("relay1"),
    'relay2': Relay("relay2"),
    'relay3': Relay("relay3")
}
