

class DegitalInput:
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

DegitalInputs = {
    'DIGIN-1': DegitalInput("DIGIN-1"),
    'DIGIN-2': DegitalInput('DIGIN-2'),
    'DIGIN-3': DegitalInput('DIGIN-3'),
    'DIGIN-4': DegitalInput('DIGIN-4'),
    'DIGIN-5': DegitalInput('DIGIN-5'),
    'DIGIN-6': DegitalInput('DIGIN-6'),
    'DIGIN-7': DegitalInput('DIGIN-7'),
    'DIGIN-8': DegitalInput('DIGIN-8'),
    'DIGIN-9': DegitalInput('DIGIN-9'),
    'DIGIN-10': DegitalInput('DIGIN-10')
}
