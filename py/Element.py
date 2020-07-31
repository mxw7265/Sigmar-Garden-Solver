class Element:
    """docstring"""
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __repr__(self):
        return f"{self.name}()"

    __str__ = __repr__

class Fire(Element):
    def __init__(self):
        super().__init__("Fire")

    def __add__(self, other):
        return isinstance(other, (Fire, Salt))

    __radd__ = __add__

class Earth(Element):
    def __init__(self):
        super().__init__("Earth")

    def __add__(self, other):
        return isinstance(other, (Earth, Salt))

    __radd__ = __add__

class Water(Element):
    def __init__(self):
        super().__init__("Water")

    def __add__(self, other):
        return isinstance(other, (Water, Salt))

    __radd__ = __add__

class Air(Element):
    def __init__(self):
        super().__init__("Air")

    def __add__(self, other):
        return isinstance(other, (Air, Salt))

    __radd__ = __add__

class Salt(Element):
    def __init__(self):
        super().__init__("Salt")

    def __add__(self, other):
        return isinstance(other, (Fire, Earth, Water, Air, Salt))

    __radd__ = __add__

class Vitae(Element):
    def __init__(self):
        super().__init__("Vitae")

    def __add__(self, other):
        return isinstance(other, Mors)

    __radd__ = __add__

class Mors(Element):
    def __init__(self):
        super().__init__("Mors")

    def __add__(self, other):
        return isinstance(other, Vitae)

    __radd__ = __add__

class Metal(Element):
    def __init__(self, name):
        super().__init__(name)

    def __add__(self, other):
        return isinstance(other, Quicksilver)

    __radd__ = __add__

class Quicksilver(Element):
    def __init__(self):
        super().__init__("Quicksilver")

    def __add__(self, other):
        return issubclass(other, Metal)

    __radd__ = __add__

class Lead(Metal):
    def __init__(self):
        super().__init__("Lead")

class Tin(Metal):
    def __init__(self):
        super().__init__("Tin")

class Iron(Metal):
    def __init__(self):
        super().__init__("Iron")

class Copper(Metal):
    def __init__(self):
        super().__init__("Copper")

class Silver(Metal):
    def __init__(self):
        super().__init__("Silver")

class Gold(Element):
    def __init__(self):
        super().__init__("Gold")

    def __add__(self, other):
        return False

    __radd__ = __add__
