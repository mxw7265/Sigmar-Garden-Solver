class Element:
    """
    Class to represent an element (marbles) for a Sigmar's Garden game.
    This class is used as an abstract class. Any subclasses will handle
    how elements interact with each other.
    """

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __repr__(self):
        return f"{self.name}()"

    __str__ = __repr__

class Fire(Element):
    """
    Class to represent Fire element
    """

    def __init__(self):
        super().__init__("Fire")

    def __add__(self, other):
        return isinstance(other, (Fire, Salt))

    __radd__ = __add__

class Earth(Element):
    """
    Class to represent Earth element
    """

    def __init__(self):
        super().__init__("Earth")

    def __add__(self, other):
        return isinstance(other, (Earth, Salt))

    __radd__ = __add__

class Water(Element):
    """
    Class to represent Water element
    """

    def __init__(self):
        super().__init__("Water")

    def __add__(self, other):
        return isinstance(other, (Water, Salt))

    __radd__ = __add__

class Air(Element):
    """
    Class to represent Air element
    """

    def __init__(self):
        super().__init__("Air")

    def __add__(self, other):
        return isinstance(other, (Air, Salt))

    __radd__ = __add__

class Salt(Element):
    """
    Class to represent Salt element
    """

    def __init__(self):
        super().__init__("Salt")

    def __add__(self, other):
        return isinstance(other, (Fire, Earth, Water, Air, Salt))

    __radd__ = __add__

class Vitae(Element):
    """
    Class to represent Vitae element
    """

    def __init__(self):
        super().__init__("Vitae")

    def __add__(self, other):
        return isinstance(other, Mors)

    __radd__ = __add__

class Mors(Element):
    """
    Class to represent Mors element
    """

    def __init__(self):
        super().__init__("Mors")

    def __add__(self, other):
        return isinstance(other, Vitae)

    __radd__ = __add__

class Metal(Element):
    """
    Abstract subclass to represent any metal element except Gold and Quicksilver.

    Created to abide DRY principle, because those metal elements contain
    same way to interact.
    """

    def __init__(self, name):
        super().__init__(name)

    def __add__(self, other):
        return isinstance(other, Quicksilver)

    __radd__ = __add__

class Quicksilver(Element):
    """
    Class to represent Quicksilver element.
    (Also known as Mercury, but "quicksilver" was used in the Opus Magnum.)
    """

    def __init__(self):
        super().__init__("Quicksilver")

    def __add__(self, other):
        return issubclass(other, Metal)

    __radd__ = __add__

class Lead(Metal):
    """
    Class to represent Lead element
    """

    def __init__(self):
        super().__init__("Lead")

class Tin(Metal):
    """
    Class to represent Tin element
    """

    def __init__(self):
        super().__init__("Tin")

class Iron(Metal):
    """
    Class to represent Iron element
    """

    def __init__(self):
        super().__init__("Iron")

class Copper(Metal):
    """
    Class to represent Copper element
    """

    def __init__(self):
        super().__init__("Copper")

class Silver(Metal):
    """
    Class to represent Silver element
    """

    def __init__(self):
        super().__init__("Silver")

class Gold(Element):
    """
    Class to represent Gold element

    NOTE: This element does not interact with each other; it will cancel itself.
          Model classes will need to take that into account.
    """

    def __init__(self):
        super().__init__("Gold")

    def __add__(self, other):
        # Does not interact with any elements.
        return False

    __radd__ = __add__
