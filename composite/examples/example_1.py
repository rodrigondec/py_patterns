from composite.client import Client
from composite.leaf import Leaf


primeiro_componente = Leaf()
raiz = Client(primeiro_componente)


raiz.print()
