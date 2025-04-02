class Home:

    def __int__(self, appliance, room, device):  # Corrected __int__ to __init__
        self.appliance = appliance
        self.room = room
        self.device = device

    def __str__(self):  # Optional: To print a friendly string representation of the object
        return f'Home(appliance={self.appliance}, room={self.room}, device={self.device})'

home_1 = Home('sofa', 'bathroom', 'cell')

print(home_1)







