class Client:
    def __init__(self, component):
        self.component = component

    def print(self):
        print(f'Client: {Client}')
        self.component.print()

