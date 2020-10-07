from .component import Component


class Composite(Component):
    def __init__(self, components=None):
        if components is None:
            components = []
        self.components = components

    def print(self):
        print(f'Inicio Composite: {self}')
        for component in self.components:
            component.print()
        print(f'Fim Composite: {self}')

    def add_component(self, *args):
        for arg in args:
            self.components.append(arg)

    def remove_component(self, component):
        self.components.remove(component)
