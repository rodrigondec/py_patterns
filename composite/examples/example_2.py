from composite.client import Client
from composite.composite import Composite
from composite.leaf import Leaf

raiz = Client(
    Composite()
)


raiz.component.add_component(
    Leaf(),
    Leaf(),
    Leaf()
)


raiz.component.add_component(
    Composite(
        [
            Leaf(),
            Leaf()
        ]
    )
)


raiz.print()
